#!/usr/bin/env ruby
# frozen_string_literal: true

# Renders page bodies to HTML using the same kramdown settings Jekyll applies
# by default (input: GFM, auto_ids: true) -- see Jekyll::Configuration::DEFAULTS
# -- so the heading ids this produces match the anchors the built site actually
# uses. Called from tools/build_search_index.py; not run standalone.
#
# stdin:  JSON array of {"path": "...", "body": "..."}
# stdout: JSON array of {"path": "...", "html": "..."}

require 'kramdown'
require 'kramdown-parser-gfm'
require 'json'

KRAMDOWN_OPTIONS = {
  input: 'GFM',
  auto_ids: true,
  entity_output: :as_char,
  smart_quotes: 'lsquo,rsquo,ldquo,rdquo',
  hard_wrap: false,
  syntax_highlighter: nil
}.freeze

pages = JSON.parse($stdin.read)
result = pages.map do |page|
  html = Kramdown::Document.new(page['body'], **KRAMDOWN_OPTIONS).to_html
  { 'path' => page['path'], 'html' => html }
end

puts JSON.generate(result)
