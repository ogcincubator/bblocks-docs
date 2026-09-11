/**
 * Docs search widget: queries the build-time FTS5 index
 * (assets/search/search-index.<hash>.sqlite, built by
 * tools/build_search_index.py) client-side via the official SQLite Wasm
 * build (@sqlite.org/sqlite-wasm). Not sql.js -- sql.js's published build
 * omits FTS5 entirely (only FTS3 is compiled in; confirmed against their
 * Makefile), so queries against our FTS5 index fail there with "no such
 * module: fts5". The official sqlite.org build does include FTS5 (verified
 * against the actual .wasm binary's exported symbols).
 *
 * The library and the index db are both loaded lazily, on first
 * focus/keystroke in the search box, not on page load.
 */
(function () {
  "use strict";

  var SQLITE_WASM_VERSION = "3.53.4-build1";
  var SQLITE_WASM_MODULE_URL =
    "https://cdn.jsdelivr.net/npm/@sqlite.org/sqlite-wasm@" + SQLITE_WASM_VERSION + "/dist/index.mjs";
  // In-memory VFS path the fetched db bytes are written to before opening
  // (see loadDatabase()) -- not a real filesystem path, just a label.
  var DB_VFS_PATH = "/docs-search-index.sqlite";
  var DEBOUNCE_MS = 300;
  var MAX_RESULTS = 8;
  // A query matching a word from some page's own title pulls in *every*
  // section-row of that page (page_title is duplicated per section), which
  // can flood the result list with one page's sections and crowd out other,
  // equally-relevant pages. Fetch a larger candidate pool ordered by score,
  // then keep at most MAX_PER_PAGE of any one page's rows when building the
  // final (still score-ordered) list -- see .claude/search-plan.md ("why
  // does 'find' return ...") for the tuning that led here; weight-tuning
  // alone couldn't fix this, since it's a result-shaping problem, not a
  // per-row scoring one.
  var MAX_PER_PAGE = 2;
  var CANDIDATE_LIMIT = MAX_RESULTS * 4;
  var SNIPPET_TOKENS = 12;
  // Two FTS5 tables, queried in sequence (see loadDatabase()/runQuery()):
  // search_titles (page_title, section_title, url) is tried first, and
  // search_body (page_title, section_title, body, url) only fills in
  // remaining slots if the title tier comes up short. See
  // .claude/search-plan.md for why titles get their own table -- in short,
  // bm25()'s length normalization is computed over a row's *whole* token
  // count across all columns, so a title match on a row with a long body
  // always loses to the same match on a short-bodied row, and no column
  // weight fixes that; splitting them into separate tables sidesteps it.
  // Column weights below: section_title > page_title for the title tier;
  // body is the only indexed column in the body tier, so it needs no
  // weighting at all.
  var TITLE_BM25_WEIGHTS = "4.0, 8.0";
  var MOBILE_BREAKPOINT = "(max-width: 600px)";
  // Sentinel characters wrapping matched terms in snippet() output, swapped
  // for real <mark> tags only after the surrounding text has been
  // HTML-escaped -- so a match can't inject markup, and real page text
  // can't collide with the markers (non-printable control chars, never
  // part of real content).
  var MARK_START = "\x01";
  var MARK_END = "\x02";

  var container = document.getElementById("docs-search");
  if (!container) {
    return;
  }

  var dbUrl = container.getAttribute("data-db-url");
  var baseUrlPrefix = container.getAttribute("data-baseurl") || "";
  var toggle = container.querySelector(".docs-search__toggle");
  var panel = container.querySelector(".docs-search__panel");
  var input = container.querySelector(".docs-search__input");
  var resultsEl = container.querySelector(".docs-search__results");

  var dbPromise = null;
  var debounceTimer = null;
  var activeIndex = -1;

  function loadDatabase() {
    if (dbPromise) {
      return dbPromise;
    }
    if (!dbUrl) {
      return Promise.reject(new Error(
        "docs-search: no search index configured " +
        "(missing _data/search_index.yml -- run tools/build_search_index.py)"
      ));
    }
    dbPromise = import(SQLITE_WASM_MODULE_URL)
      .then(function (mod) {
        return mod.default(); // sqlite3InitModule()
      })
      .then(function (sqlite3) {
        return fetch(dbUrl).then(function (res) {
          if (!res.ok) {
            throw new Error("failed to fetch search index: " + res.status);
          }
          return res.arrayBuffer();
        }).then(function (buf) {
          // oo1.DB has no "load from bytes" constructor -- write the bytes
          // to sqlite3's in-memory (Emscripten MEMFS) filesystem first, then
          // open that path read-only. See
          // https://sqlite.org/wasm/doc/trunk/api-c-style.md#sqlite3_js_posix_create_file
          sqlite3.capi.sqlite3_js_posix_create_file(DB_VFS_PATH, new Uint8Array(buf));
          return new sqlite3.oo1.DB(DB_VFS_PATH, "r");
        });
      });
    return dbPromise;
  }

  function toMatchQuery(term) {
    // Quote each token and mark it a prefix query ("foo"*) so FTS5 syntax
    // characters in the user's input (colons, parens, hyphens, ...) can't
    // be misread as query operators, while still matching as-you-type.
    return term
      .trim()
      .split(/\s+/)
      .filter(Boolean)
      .map(function (tok) {
        return '"' + tok.replace(/"/g, '""') + '"*';
      })
      .join(" ");
  }

  // Title tier first, body tier only to fill remaining slots -- see
  // .claude/search-plan.md. The title tier alone answers most queries
  // ("find", "imports", ...); the body tier is a fallback for queries that
  // only appear in prose, not in any page/section title.
  function runQuery(db, term) {
    var matchQuery = toMatchQuery(term);
    if (!matchQuery) {
      return [];
    }

    var titleCandidates = db.selectObjects(
      "SELECT page_title, section_title, url, " +
      "bm25(search_titles, " + TITLE_BM25_WEIGHTS + ") AS score " +
      "FROM search_titles WHERE search_titles MATCH ? ORDER BY score LIMIT ?",
      [matchQuery, CANDIDATE_LIMIT]
    );
    var perPageCount = {};
    var kept = [];
    capPerPage(titleCandidates, kept, perPageCount);
    // No body text to draw a snippet from for a title-only match -- the
    // title itself (already rendered) is why it matched.
    kept.forEach(function (row) {
      row.snip = "";
    });

    if (kept.length < MAX_RESULTS) {
      var seenUrls = {};
      kept.forEach(function (row) {
        seenUrls[row.url] = true;
      });
      // char(1)/char(2) generate the same bytes as MARK_START/MARK_END
      // inline in SQL, so there's no need to bind them as parameters too.
      // body is the only indexed (matchable) column in search_body, so no
      // bm25() weight arguments are needed.
      var bodyCandidates = db.selectObjects(
        "SELECT page_title, section_title, url, " +
        "snippet(search_body, 2, char(1), char(2), '…', ?) AS snip, " +
        "bm25(search_body) AS score " +
        "FROM search_body WHERE search_body MATCH ? ORDER BY score LIMIT ?",
        [SNIPPET_TOKENS, matchQuery, CANDIDATE_LIMIT]
      );
      var freshBodyCandidates = bodyCandidates.filter(function (row) {
        return !seenUrls[row.url];
      });
      capPerPage(freshBodyCandidates, kept, perPageCount);
    }

    return kept;
  }

  // rows is already score-ordered (best first) within its own tier; appends
  // to `kept` (in place) up to MAX_RESULTS, skipping rows past MAX_PER_PAGE
  // for any one page. `perPageCount` is shared across both tiers' calls, so
  // a page already showing MAX_PER_PAGE title-tier rows won't also crowd in
  // body-tier ones. The grouping key is the row's own page (the URL without
  // its #anchor), not page_title (just display text) and not any single
  // matched row's identity.
  function capPerPage(rows, kept, perPageCount) {
    for (var i = 0; i < rows.length && kept.length < MAX_RESULTS; i++) {
      var row = rows[i];
      var pageKey = row.url.split("#")[0];
      var count = perPageCount[pageKey] || 0;
      if (count >= MAX_PER_PAGE) {
        continue;
      }
      perPageCount[pageKey] = count + 1;
      kept.push(row);
    }
  }

  function escapeHtml(str) {
    var div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  function renderSnippet(raw) {
    var parts = raw.split(MARK_START);
    var html = escapeHtml(parts[0]);
    for (var i = 1; i < parts.length; i++) {
      var bits = parts[i].split(MARK_END);
      html += "<mark>" + escapeHtml(bits[0]) + "</mark>" + escapeHtml(bits.slice(1).join(MARK_END));
    }
    return html;
  }

  function resultHref(url) {
    return baseUrlPrefix + url;
  }

  function closePanel() {
    resultsEl.hidden = true;
    activeIndex = -1;
  }

  function render(rows, term) {
    resultsEl.innerHTML = "";
    activeIndex = -1;
    if (!term.trim()) {
      closePanel();
      return;
    }
    if (!rows.length) {
      var empty = document.createElement("p");
      empty.className = "docs-search__empty";
      empty.textContent = "No results for “" + term.trim() + "”.";
      resultsEl.appendChild(empty);
      resultsEl.hidden = false;
      return;
    }
    var list = document.createElement("ul");
    list.className = "docs-search__list";
    rows.forEach(function (row) {
      var li = document.createElement("li");
      li.className = "docs-search__item";
      var a = document.createElement("a");
      a.href = resultHref(row.url);
      var showSection = row.section_title && row.section_title !== row.page_title;
      var titleHtml = escapeHtml(row.page_title) +
        (showSection
          ? ' <span class="docs-search__item-section">› ' + escapeHtml(row.section_title) + "</span>"
          : "");
      a.innerHTML =
        '<span class="docs-search__item-title">' + titleHtml + "</span>" +
        '<span class="docs-search__item-snippet">' + renderSnippet(row.snip) + "</span>";
      li.appendChild(a);
      list.appendChild(li);
    });
    resultsEl.appendChild(list);
    resultsEl.hidden = false;
  }

  function moveActive(delta) {
    var items = resultsEl.querySelectorAll(".docs-search__item a");
    if (!items.length) {
      return;
    }
    activeIndex = (activeIndex + delta + items.length) % items.length;
    items.forEach(function (el, i) {
      el.classList.toggle("is--active", i === activeIndex);
    });
    items[activeIndex].scrollIntoView({ block: "nearest" });
  }

  function onInput() {
    var term = input.value;
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function () {
      loadDatabase()
        .then(function (db) {
          render(runQuery(db, term), term);
        })
        .catch(function (err) {
          // eslint-disable-next-line no-console
          console.error("docs-search:", err);
        });
    }, DEBOUNCE_MS);
  }

  input.addEventListener("input", onInput);
  input.addEventListener("focus", function () {
    loadDatabase().catch(function () { /* surfaced on next query */ });
  });

  input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") {
      e.preventDefault();
      moveActive(1);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      moveActive(-1);
    } else if (e.key === "Enter" && activeIndex >= 0) {
      e.preventDefault();
      var items = resultsEl.querySelectorAll(".docs-search__item a");
      if (items[activeIndex]) {
        window.location.href = items[activeIndex].href;
      }
    } else if (e.key === "Escape") {
      closePanel();
      input.blur();
    }
  });

  if (toggle) {
    toggle.addEventListener("click", function () {
      var isOpen = panel.classList.toggle("is--visible");
      toggle.setAttribute("aria-expanded", String(isOpen));
      if (isOpen) {
        input.focus();
      } else {
        closePanel();
      }
    });
  }

  document.addEventListener("click", function (e) {
    if (container.contains(e.target)) {
      return;
    }
    closePanel();
    if (toggle && window.matchMedia(MOBILE_BREAKPOINT).matches) {
      panel.classList.remove("is--visible");
      toggle.setAttribute("aria-expanded", "false");
    }
  });

  // "/" focuses the search box from anywhere on the page, like most docs
  // sites -- unless the user is already typing into some other field.
  document.addEventListener("keydown", function (e) {
    if (e.key !== "/" || e.metaKey || e.ctrlKey || e.altKey) {
      return;
    }
    var active = document.activeElement;
    var isTyping = active && /^(input|textarea|select)$/i.test(active.tagName);
    if (isTyping) {
      return;
    }
    e.preventDefault();
    if (toggle && getComputedStyle(toggle).display !== "none" && !panel.classList.contains("is--visible")) {
      toggle.click();
      return;
    }
    input.focus();
  });
})();
