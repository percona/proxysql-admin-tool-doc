# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup ----------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Custom modules ------------------------------------------------------------

from project_info import ProjectInfo

# -- Project information -------------------------------------------------------

p_info = ProjectInfo()
project = ' '.join([p_info.product, 'Documentation'])
htmlhelp_basename = ''.join(p_info.product.split()) + 'Doc'
author = p_info.author
product = p_info.product
license = p_info.license
version = p_info.version
release = p_info.release
copyright = p_info.copyright
rst_prolog = """
.. |copyright| replace:: {}
.. |product| replace:: {}
.. |version| replace:: {}
.. |license| replace:: {}
""".format(copyright, product, version, license)

# -- General configuration -----------------------------------------------------

master_doc = 'index'
extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.todo', 
              'sphinx.ext.coverage',
              'sphinx.ext.ifconfig', 
              'sphinx.ext.extlinks'
]
pygments_style = 'sphinx'
templates_path = ['_templates']
source_suffix = '.rst'
exclude_patterns = []
#primary_domain = 'psdom'

extlinks = {
    'jira': ('https://jira.percona.com/browse/%s', '')
}

# -- Options for HTML output ---------------------------------------------------

#html_theme = 'percona-theme'
#html_theme_path = ['.', './percona-theme']
html_title = project
html_static_path = ['_static']

# -- Options for LaTeX output --------------------------------------------------

target_name = ''.join(product.split())
latex_documents = [('index',              # source start file
                    f'{target_name}.tex', # target_name
                    f'{project}',         # title
                    f'{author}',          # author
                    'manual')             # documentclass [howto/manual]
]

latex_logo = 'percona-logo.jpg'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False
latex_toplevel_sectioning = 'chapter'

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
man_page_name = ''.join(product.split()).lower()
# (source start file, name, description, authors, manual section).
man_pages = [('index',       # source start file
              man_page_name, # name
              project,       # description
              [author],      # authors
              1)             # manual sections
]
