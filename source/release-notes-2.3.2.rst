.. _2.3.2:

===============================================================================
ProxySQL 2.3.2 and `proxysql-admin`
===============================================================================

:Date: November 3, 2021
:Installation: https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2

ProxySQL 2.3.2, released by ProxySQL_, is now available for download in
the `Percona repository`_ along with an updated version of Percona's
**proxysql-admin** tool.

ProxySQL is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like Percona Server for MySQL and MariaDB). It acts as an intermediary for client requests seeking resources from the
database. ProxySQL was created for DBAs as a means of solving
complex replication topology issues.

The ProxySQL 2.3.2 source and binary packages available from the `Percona download page for ProxySQL 2`_ includes *proxysql-admin* - a tool developed by Percona to configure Percona XtraDB Clusters nodes into ProxySQL. Docker images are also available.

You can `download the original ProxySQL from
GitHub`_. ProxySQL provides the `ProxySQL documentation`_.

The ProxySQL 2.3.2 and *proxysql-admin* release includes all the features and bug fixes available in the following versions. Select the version number to see the individual release notes:

* `ProxySQL 2.2.1 <https://github.com/sysown/proxysql/releases/tag/v2.2.1>`__
* `ProxySQL 2.2.2 <https://github.com/sysown/proxysql/releases/tag/v2.2.2>`_
* `ProxySQL 2.3.0 <https://github.com/sysown/proxysql/releases/tag/v2.3.0>`_
* `ProxySQL 2.3.1 <https://github.com/sysown/proxysql/releases/tag/v2.3.1>`_
* `ProxySQL 2.3.2 <https://github.com/sysown/proxysql/releases/tag/v2.3.2>`_

Release Highlights
-------------------------------

The following list are some of the bug fixes provided by ProxySQL from versions 2.2.1 to 2.3.2:

- Supports the use of grave accent or backtick (`) symbol for SET statements. `#3479 <https://github.com/sysown/proxysql/issues/3479>`__
- Reimplements how comments are handled in ``USE`` statements. `#3610 <https://github.com/sysown/proxysql/pull/3610>`__
- Implements the ``PROXYSQL TLS RELOAD`` command which allows reloading TLS files at runtime. This command lets ProxySQL change its certifications and key files used for client connections. `#3552 <https://github.com/sysown/proxysql/pull/3552>`__
- Improves for group replication monitoring and replication lag actions. `#3533 <https://github.com/sysown/proxysql/pull/3533>`__
- Fixes issues found with the ``client error limit`` implementation. `#3627 <https://github.com/sysown/proxysql/pull/3627>`__

Improvements
--------------------------------

- :jira:`psqladm-320`: Performs a ``SAVE`` operation for the users table only if the users table has changed.
- :jira:`psqladm-339`: Provides a method when a cluster read-only state has changed to update proxysql-admin without requiring a cluster restart.
- :jira:`psqladm-327`: Adds the ``--server`` option to skip the check for cluster membership. This option is specified with either the ``--syncusers`` command or the ``--sync-multi-cluster-users`` command and allows standalone nodes to be synced.

.. warning::

    An upgrade from ProxySQL v1.x to ProxySQL v2.x requires the user to manually remove the ProxySQL v1.x packages. After that operation, the user can install ProxySQL v2.x.



.. include:: _res/text/license.txt

.. include:: _res/replace.txt
.. include:: _res/links.txt
