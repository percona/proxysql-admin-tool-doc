.. _1.4.4:

*ProxySQL* |release| and `proxysql-admin`
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: This release fixes the following bugs in `ProxySQL Admin`

- :jira:`PXC-892`: `proxysql-admin` was unable to recognize IP
  address of localhost.
- :jira:`PXC-893`: `proxysql-admin` couldn’t interpret passwords with
  special characters correctly, such as ‘$’
- :jira:`PSQLADM-3`: proxysql_node_monitor script had writer/reader hostgroup
  conflict issue.
- :jira:`PQA-155`: Runtime table was not updated in case of any changes in
  Percona XtraDB Cluster membership.
- :jira:`BLD-853`: *ProxySQL* logrotate script did not work properly,
  producing empty `/etc/proxysql.log` after logrotate.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.4
.. |date| replace:: January 18, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
