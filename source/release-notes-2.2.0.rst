.. _2.2.0:

===============================================================================
*ProxySQL* |release| and `proxysql-admin`
===============================================================================

:Date: |date|
:Installation: https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2

*ProxySQL* |release|, released by ProxySQL_, is now available for download in
the `Percona repository`_ along with an updated version of **Percona**'s
`proxysql-admin` tool.

*ProxySQL* is a high-performance proxy, currently for `MySQL`, and database
servers in the `MySQL` ecosystem (like **Percona Server for MySQL** and `MariaDB`). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* |release| source and binary packages available from the `Percona download page for ProxySQL 2`_ include `ProxySQL Admin` - a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. `Docker` images for
|release| are available as well.

You can `download the original ProxySQL from
GitHub`_. *ProxySQL* offers the `ProxySQL documentation`_. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* `2.2.0 release notes <https://github.com/sysown/proxysql/releases/tag/v2.2.0>`__

.. note::

    An upgrade from ProxySQL v1.x to ProxySQL v2.x requires the user to manually remove the ProxySQL v1.x packages. After that operation, the user can install ProxySQL v2.x.

`ProxySQL Admin` has not changed since the previous release.

.. include:: _res/text/license.txt

.. |date| replace:: August 10, 2021
.. |release| replace:: 2.2.0

.. include:: _res/replace.txt
.. include:: _res/links.txt
