.. _1.4.5:

*ProxySQL* |release| and `proxysql-admin` (2018-02-15)
================================================================================

:Installation: https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1

*ProxySQL* 1.4.5, released by ProxySQL_, is now available for download in
the `Percona repository`_ along with an updated version of **Percona**’s
**proxysql-admin** tool.

*ProxySQL* is a high-performance proxy, currently for `MySQL`, and database
servers in the `MySQL` ecosystem (like **Percona Server for MySQL** and `MariaDB`). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* 1.4.5 source and binary packages are available from the `Percona
download page for ProxySQL`_ include `ProxySQL Admin` – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. `Docker` images are available as well. You can `download the original ProxySQL from GitHub`_. *ProxySQL* offers the `ProxySQL documentation`_.

 Usability improvements
 -----------------------------

- :jira:`PSQLADM-6`: If the cluster node goes offline, the `proxysql_node_monitor`
  script now sets the node status as `OFFLINE_HARD`, and does not remove it from
  the *ProxySQL* database. Also, logging is consistent regardless of the cluster
  node online status.
- :jira:`PSQLADM-30`: Validation was added for the host priority file.
- :jira:`PSQLADM-33`: Added `--proxysql-datadir` option to run the `proxysql-admin`
  script with a custom *ProxySQL* data directory.
- Also, BATS test suite was added for the `proxysql-admin` testing.

Bug fixes
----------------

- :jira:`PSQLADM-5`: *Percona XtraDB Cluster (PXC)* mode specified with `proxysql-admin`
  with use of `--mode` parameter was not persistent.
- :jira:`PSQLADM-8`: *ProxySQL* High CPU load took place when `mysqld` was hanging.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.5
.. |date| replace:: February 15, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
