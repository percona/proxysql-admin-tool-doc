import sys, os
sys.path.append(os.path.abspath('ext'))
extensions = ['sphinx.ext.intersphinx',
                'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.ifconfig',
              'sphinx.ext.extlinks'
              ]
templates_path = ['_templates'
                    ]
source_suffix = '.rst'
master_doc = 'index'
version = '2.3'
release = '.'.join([version, '2-1.2'])
#project = u'ProxySQL and proxysql-admin'
product_name = 'ProxySQL and proxySQL-admin'
project = ' '.join([product_name, release, 'Documentation'])
copyright = u'Percona LLC and/or its affiliates 2015-2022'
exclude_patterns = []
pygments_style = 'default'

rst_prolog = '''

.. role:: dir(file)

.. role:: bash(code)
   :language: bash

.. |license| replace:: Open Source license GPLv3

'''

extlinks = {
    'jira': ('https://jira.percona.com/browse/%s', ''),
    'jirabug': ('https://jira.percona.com/browse/%s', '')
}

html_theme = 'percona-theme'
html_theme_path = ['.', './percona-theme']
# Redirect info for Edit on Github link
html_context = {
    'repo_name': '/percona/proxysql-admin-tool-doc',
    'repo_url': 'https://github.com/percona/proxysql-admin-tool-doc',
    'edit_uri': 'blob/main/source'
}
html_title = project
html_static_path = ['_static']
html_sidebars = {
        '**': ['localtoc.html', 'sourcelink.html', 'edit.html', 'relations.html'],
        'using/windows': ['windowssidebar.html'],
}
