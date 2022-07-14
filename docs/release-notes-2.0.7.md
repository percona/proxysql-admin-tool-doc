# ProxySQL 2.0.7 and proxysql-admin (2019-10-23)

* **Installation**

    [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* 2.0.7, released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of Percona’s proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from
GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.7 [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

This version includes *ProxySQL* release. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* release [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

The proxysql-admin tool now supports MariaDB 10.4.

### New Features

* [PSQLADM-204](https://jira.percona.com/browse/PSQLADM-204): Add support of MariaDB 10.4

### Improvements

* [PSQLADM-195](https://jira.percona.com/browse/PSQLADM-195): A new option `–with-stats-reset` has been added to the proxysql_status script to display the \*_reset tables from the stats database. If this option is not specified, these tables are not displayed by default.

### Bugs fixed

* [PSQLADM-157](https://jira.percona.com/browse/PSQLADM-157): In some cases, the proxysql_status script used the cat command to display a file without checking if the file existed and was readable.

* [PSQLADM-181](https://jira.percona.com/browse/PSQLADM-181): When run with `–update-cluster`, `–write-node` set to <node_name>, `proxysql-admin` now verifies that the writer nodes are not read-only.

*ProxySQL* is available under Open Source license GPLv3.