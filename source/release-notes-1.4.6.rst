.. _1.4.6:

*ProxySQL* |release| and `proxysql-admin`
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Usability improvements

- :jira:`PSQLADM-32`: Now, `proxysql-admin` script can configure
  multiple clusters in *ProxySQL*, when there are unique cluster names specified
  by the wsrep_cluster_name option, and the `/etc/proxysql-admin.cnf`
  configuration contains different *ProxySQL* READ/WRITE hostgroup and different
  application user for each cluster. Currently multiple clusters support is not
  compatible with host priority feature, which works only with a single cluster.
- :jira:`81`: The new version substantially increases the number of test cases
  in the `ProxySQL Admin` test-suite.

.. rubric:: Bug fixes

- :jira:`PSQLADM-35`: `proxysql_galera_checker` monitoring script was
  unable to discover new writer nodes.
- :jira:`PSQLADM-36`: upgrade to *ProxySQL* |release| from the previous version
  was broken.
- :jira:`PSQLADM-79`: Fixed by properly quoting the MONITOR_USERNAME environment
  variable in the admin script query.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.6
.. |date| replace:: March 12, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
