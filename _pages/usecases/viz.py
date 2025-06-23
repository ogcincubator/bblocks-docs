import graphviz

# Create a diagram of use case relationships
dot = graphviz.Digraph(comment="OGC Building Block Use Case Relationships", format='png')

# Use case nodes
dot.node('U0', 'Publish FAIR Standards\n(Standard Editors,Standards Organisations)')
dot.node('U1', '1. Reuse Requirements\n(Standard Editors)')
dot.node('U2', '2. Schema Compatibility QC\n(Standards Devs)')
dot.node('U3', '3. Example Validation\n(Tool Vendors)')
dot.node('U4', '4. Rule Testing\n(Conformance Devs)')
dot.node('U5', '5. Enhanced Resources\n(SWGs, Educators)')
dot.node('U6', '6. Profiling Standards\n(Profile Designers)')
dot.node('U7', '7. Infrastructure Design\n(Platform Providers)')
dot.node('U8', '8. Application Design\n(App Developers)')
dot.node('U9', '9. Discover Standards\n(New Users, AI)')
dot.node('U01', 'Quality Control\n(Standards Organisations)')

# Connections (simplified relationships)
dot.edges([
    ('U0', 'U1'),
    ('U0', 'U6'),
    ('U0', 'U01'),
    ('U01', 'U2'),
    ('U9', 'U1'),
    ('U9', 'U6'),
    ('U9', 'U7'),
    ('U1', 'U2'),
    ('U01', 'U3'),
    ('U2', 'U3'),
    ('U4', 'U3'),
    ('U01', 'U4'),
    ('U0', 'U5'),
    ('U6', 'U7'),
    ('U6', 'U4'),
    ('U8', 'U6'),
    ('U5', 'U8'),
    ('U5', 'U3'),
    ('U9', 'U8')
])

# Save the diagram
diagram_path = "ogc_use_case_flow.png"
dot.render(filename=diagram_path, cleanup=True)

