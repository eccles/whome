# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'whome'
copyright = '2023, Paul Hewlett'
author = 'Paul Hewlett'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.spelling",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",

]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = [ '.md', '.rst']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Spelling -------------------------------------------------
spelling_lang = 'en_UK'
spelling_word_list_filename ='spelling_wordlist.txt'
spelling_show_suggestions = True
spelling_verbose = True
