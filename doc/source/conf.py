# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Eccles'
copyright = '2023, Paul Hewlett'
author = 'Paul Hewlett'
release = '0.1.0'

import sphinx_rtd_theme

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxcontrib.spelling",
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",

]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.md': 'restructuredtext',
    '.rst': 'restructuredtext',
}

# myst markdown parser
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
}
html_static_path = ['_static']

# -- Spelling -------------------------------------------------
spelling_lang = 'en_UK'
spelling_word_list_filename ='spelling_wordlist.txt'
spelling_show_suggestions = True
spelling_verbose = True
