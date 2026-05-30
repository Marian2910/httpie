# Rules for <https://github.com/markdownlint/markdownlint>

# Load all rules by default
all

#
# Tweak rules
#

# MD002 First header should be a top level header
# Because we use HTML to hide them on the website.
exclude_rule 'MD002'

# MD007 Allow unordered list indentation
exclude_rule 'MD007'

# MD013 Line length
exclude_rule 'MD013'

# MD014 Dollar signs used before commands without showing output
exclude_rule 'MD014'

# MD028 Blank line inside blockquote
exclude_rule 'MD028'

# MD012 Multiple consecutive blank lines
exclude_rule 'MD012'

# Tell the linter to use ordered lists:
#   1. Foo
#   2. Bar
#   3. Baz
#
# Instead of:
#   1. Foo
#   1. Bar
#   1. Baz
rule 'MD029', :style => :ordered

# MD033 Inline HTML
# Keep this disabled until markdownlint supports the HTML fragments used in our docs.
exclude_rule 'MD033'

# MD034 Bare URL used
# Keep this disabled while upstream still flags URLs we intentionally render as plain text.
exclude_rule 'MD034'

# MD041 First line in file should be a top level header
# Because we use HTML to hide them on the website.
exclude_rule 'MD041'
