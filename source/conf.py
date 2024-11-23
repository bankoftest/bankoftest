# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bank Of Test'
copyright = '2024, bankoftest'
author = 'bankoftest'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []

language = 'zh'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

# Add extensions
extensions = [
    "sphinx_design",
]

# Use pydata-sphinx-theme
html_theme = "pydata_sphinx_theme"

# Configure theme options
html_theme_options = {
    "navbar_align": "content",  # Center navigation
    "show_nav_level": 0,       # Sidebar navigation depth
    "navigation_depth": 1,     
    "secondary_sidebar_items": {
        "driver_test/ca/bc": [],
    },
    "primary_sidebar_items": {
        "driver_test/ca/bc": [],
    },
    "collapse_navigation": True,
}

html_sidebars = {
  "driver_test/ca/bc": [],
}

# Set paths for custom static files
html_static_path = ["_static"]
html_css_files = ["quiz.css"]
html_js_files = ["quiz.js"]

# Enable gettext translations
locale_dirs = ['../locales/']
gettext_compact = False
