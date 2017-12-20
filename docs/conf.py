# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# auto-generated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from __future__ import print_function

import datetime
import os
import re
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from conflib.constants import *

# Pre-Build Manipulation Code

target_dirs = ['dynamic']

# Allow this to be built up over time
epilog = []

# Just for convenience
#
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents
#

# The full version, X.Y.Z-R, where
# - X.Y.Z is the version in which X, Y, and Z must be numbers
# - R is the release, which can be alpha-numeric, e.g. '0', 'Beta', 'RC1'
full_version = project_config['ABOUT']['Version']

epilog.append('.. |project_version| replace:: %s' % full_version)

def setup(app):
    app.add_config_value('project_version', full_version, 'env') # The third value must always be 'env'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    # To use this, you need to make the necessary variable available in setup
    # using the 'add_config_value' function.
    #
    # Example:
    #   def setup(app):
    #     app.add_config_value('releaselevel', '', 'env') # The third value must always be 'env'
    #
    # Usage:
    #   .. ifconfig:: releaselevel in ('alpha', 'beta', 'rc')
    'sphinx.ext.ifconfig',
    'rst2pdf.pdfbuilder'
]

todo_include_todos = False

if project_config['CONFIG']['Show_Todo'] == 'True':
    todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = project_config['ABOUT']['Name']
copyright = str(datetime.datetime.now().year) + u',' + project_config['ABOUT']['Author']
author = project_config['ABOUT']['Author']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['*.no_rst', '_build', '**/*.inc']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# Need this to be > 1 for Travis
linkcheck_retries = 3

# This causes issues with our documentation
linkcheck_anchors = False

# A regex of links that the linkcheck builder should ignore
linkcheck_ignore = [
    # ignore rpms
    r'^http[s]?:\/\/.*\.(src\.)?rpm$',
    # ignore pdfs
    r'^http[s]?:\/\/.*\.pdf$',
    # ignore doc
    r'^http[s]?:\/\/.*\.doc(x)?$',
    # ignore isos
    r'^http[s]?:\/\/.*\.iso$',
    # ignore tarballs
    r'^http[s]?:\/\/.*\.tar(\..{2,3})?$',
    # links that the resolver has trouble with
    r'^http[s]?:\/\/groups\.google\.com\/forum\/.+',
    r'^http[s]?:\/\/travis-ci\.org(/.*|$)',
    r'^http[s]?:\/\/bundler\.io/rationale\.html',
    # NIST redirects everything everywhere
    r'^http[s]?:\/\/.*\.nist.gov(/.*|$)',
    # Microsoft redirects everything everywhere
    r'^http[s]?:\/\/.*\.microsoft.com(/.*|$)',
 ]

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme_path = ["_themes"]
html_theme      = "sphinx_rtd_theme"

# adds a file for overwriting the default css. We use this for fixing tables
html_context = {
        'css_files': [
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/css_overrides.css',
        ],
    }

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "%s %s documentation" % (project, full_version )

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "images/Your_Logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'SSPdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'SSP.tex', project_config['ABOUT']['Name'],
   project_config['ABOUT']['Author'], 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'SSP', project_config['ABOUT']['Author'],
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'SSP', project_config['ABOUT']['Name'],
   author, 'SSP', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'https://docs.python.org/': None}

# PDF
pdf_documents = [
    (master_doc, project_config['ABOUT']['Name'], project_config['ABOUT']['Name'], u'SSP'),
]

pdf_language = "en_US"
pdf_fit_background_mode = "scale"
pdf_compressed = True
pdf_stylesheets = ['sphinx','kerning','letter']
pdf_use_toc = True
pdf_use_index = False
pdf_toc_depth = 3

# tag
tags.add('ssp_%s' % full_version.split('.')[0])
tags.add('fips_199_%s' %  project_config['CONFIG']['FIPS_199_Level'].lower())
tags.add('system_type_%s' %  re.sub(r'\s+', '_', project_config['CONFIG']['System_Type'].lower()))
tags.add('operational_status_%s' %  re.sub(r'\s+', '_', project_config['CONFIG']['Operational_Status'].lower()))

rst_epilog = "\n".join(epilog)
