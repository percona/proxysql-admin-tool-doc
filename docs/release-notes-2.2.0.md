# ProxySQL 2.2.0 and proxysql-admin (2021-08-10)

[Installation](install-v2.md)

*ProxySQL* 2.2.0, released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/downloads/proxysql2/) along with an updated version of the Percona proxysql-admin tool.

ProxySQL is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like Percona Server for MySQL and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The ProxySQL 2.2.0 source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin - a tool developed by Percona to configure Percona XtraDB Cluster nodes into ProxySQL. Docker images for 2.2.0 are available as well.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). ProxySQL offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* [2.2.0 release notes](https://github.com/sysown/proxysql/releases/tag/v2.2.0)

!!! note

    An upgrade from ProxySQL v1.x to ProxySQL v2.x requires the user to manually remove the ProxySQL v1.x packages. After that operation, the user can install ProxySQL v2.x.

**ProxySQL Admin** has not changed since the previous release.

*ProxySQL* is available under Open Source license GPLv3.

