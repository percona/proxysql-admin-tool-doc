.. _1.4.4:

================================================================================
*ProxySQL* 1.4.4 and `proxysql-admin` (2018-01-18)
================================================================================

:Installation: https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1

*ProxySQL* 1.4.4, released by ProxySQL_, is now available for download in
the `Percona repository`_ along with an updated version of **Percona**’s
**proxysql-admin** tool.

*ProxySQL* is a high-performance proxy, currently for `MySQL`, and database
servers in the `MySQL` ecosystem (like **Percona Server for MySQL** and `MariaDB`). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* 1.4.4 source and binary packages are available from the `Percona
download page for ProxySQL`_ include `ProxySQL Admin` – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. `Docker` images are available as well. You can `download the original ProxySQL from GitHub`_. *ProxySQL* offers the `ProxySQL documentation`_.


This release fixes the following bugs in `ProxySQL Admin`
===========================================================

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



.. include:: _res/replace.txt
.. include:: _res/links.txt
