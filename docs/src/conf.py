# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))

import spectrum_utils


# -- Project information -----------------------------------------------------

project = "spectrum_utils"
copyright = "2019–2022, Wout Bittremieux"
author = "Wout Bittremieux"

# The short X.Y version
version = spectrum_utils.__version__
# The full version, including alpha/beta/rc tags
release = spectrum_utils.__version__


# -- General configuration ---------------------------------------------------
os.environ["SPHINX_BUILD"] = "1"

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = "1.0"
# conf.py

# ... other configuration options ...

# Global setup for doctests: this code is executed before any doctest example.
doctest_global_setup = """
from spectrum_utils import spectrum, proforma
import matplotlib
"""


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",  # Use Markdown instead of reStructuredText.
    "sphinx_markdown_tables",  # Support tables in Markdown.
    "sphinx.ext.autodoc",  # Include documentation from docstrings.
    # "sphinx.ext.autosummary",  # Generate documentation summary one-liners.
    "sphinx.ext.doctest",  # Test code in the documentation.
    # "sphinx.ext.coverage",  # Collect documentation coverage statistics.
    "sphinx.ext.napoleon",  # Support NumPy and Google style docstrings.
    "sphinx.ext.viewcode",  # Add links to the source code.
    "sphinx_rtd_theme",  # Read-the-docs theme.
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

# Generate documentation from all docstrings.
autodoc_default_options = {
    "member-order": "bysource",  # Sort by order in the source.
    "special-members": "__init__",  # Include __init__ methods.
    "undoc-members": True,  # Include methods without a docstring.
}
# Prevent import errors from these modules.
# autodoc_mock_imports = []
# Scan all found documents for autosummary directives and generate stub pages
# for each.
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``["localtoc.html", "relations.html", "sourcelink.html",
# "searchbox.html"]``.
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "spectrum_utilsdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ("letterpaper" or "a4paper").
    # "papersize": "letterpaper",
    # The font size ("10pt", "11pt" or "12pt").
    # "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    # "preamble": "",
    # Latex figure (float) alignment
    # "figure_align": "htbp",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "spectrum_utils.tex",
        "spectrum\\_utils Documentation",
        "Wout Bittremieux",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "spectrum_utils", "spectrum_utils Documentation", [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "spectrum_utils",
        "spectrum_utils Documentation",
        author,
        "spectrum_utils",
        " Python package for efficient MS/MS spectrum processing and "
        "visualization.",
        "Miscellaneous",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ""

# A unique identification for the text.
# epub_uid = ""

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------

autodoc_mock_imports = [
    "fastobo",
    "lark",
    "matplotlib",
    "numba",
    "numpy",
    "pandas",
    "pyteomics",
]
