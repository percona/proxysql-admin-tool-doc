# ProxySQL 2.0.14 and proxysql-admin (2020-09-24)

* **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* release , released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of the Percona proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by Percona to configure Percona XtraDB Cluster nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.14[release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.14)

This version includes *ProxySQL* release. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* release [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17). This is the [ProxySQL release tag](https://github.com/sysown/proxysql/releases/tag/v2.0.14) 

## Improvements

* [PSQLADM-256](https://jira.percona.com/browse/PSQLADM-256): Wrong password with % character

*ProxySQL* is available under Open Source license GPLv3.
