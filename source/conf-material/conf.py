#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath("../"))
from conf import *
extensions.append('sphinx_gitstamp')
extensions.append('sphinx_copybutton')
html_theme = 'sphinx_material'
html_sidebars['**']=['globaltoc.html', 'searchbox.html', 'localtoc.html', 'logo-text.html']
html_theme_options = {
    'base_url': 'http://bashtage.github.io/sphinx-material/',
    'repo_url': 'https://github.com/percona/proxysql-admin-tool-doc',
    'repo_name': 'percona/proxysql-admin-tool-doc',
    'color_accent': 'grey',
    'color_primary': 'orange'
}
html_logo = '../_images/percona-logo.svg'
html_favicon = '../_images/percona_favicon.ico'
pygments_style = 'emacs'
gitstamp_fmt = "%b %d, %Y"
# Specify the text pattern that won't be copied with the code block contents
copybutton_prompt_text = '$'
# Add any paths that contain templates here, relative to this directory.
templates_path = ['../_templates/theme']
#html_last_updated_fmt = ''
plantuml = 'java -jar ../../bin/plantuml.jar'

