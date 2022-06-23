# ProxySQL 2.3.2 and proxysql-admin (2021-11-03)

**Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

ProxySQL 2.3.2, released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of Percona’s **proxysql-admin** tool.

ProxySQL is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like Percona Server for MySQL and MariaDB). It acts as an intermediary for client requests seeking resources from the database. ProxySQL was created for DBAs as a means of solving complex replication topology issues.

The ProxySQL 2.3.2 source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) includes *proxysql-admin* - a tool developed by Percona to configure Percona XtraDB Clusters nodes into ProxySQL. Docker images are also available.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). ProxySQL provides the [ProxySQL documentation](https://proxysql.com/documentation/).

The ProxySQL 2.3.2 and *proxysql-admin* release includes all the features and bug fixes available in the following versions. Select the version number to see the individual release notes:

* [ProxySQL 2.2.1](https://github.com/sysown/proxysql/releases/tag/v2.2.1)

* [ProxySQL 2.2.2](https://github.com/sysown/proxysql/releases/tag/v2.2.2)

* [ProxySQL 2.3.0](https://github.com/sysown/proxysql/releases/tag/v2.3.0)

* [ProxySQL 2.3.1](https://github.com/sysown/proxysql/releases/tag/v2.3.1)

* [ProxySQL 2.3.2](https://github.com/sysown/proxysql/releases/tag/v2.3.2)

## Release Highlights

The following list are some of the bug fixes provided by ProxySQL from versions 2.2.1 to 2.3.2:

* Supports the use of grave accent or backtick (\`) symbol for SET statements. [#3479](https://github.com/sysown/proxysql/issues/3479)

* Re-implements how comments are handled in `USE` statements. [#3610](https://github.com/sysown/proxysql/pull/3610)

* Implements the `PROXYSQL TLS RELOAD` command which allows reloading TLS files at runtime. This command lets ProxySQL change its certifications and key files used for client connections. [#3552](https://github.com/sysown/proxysql/pull/3552)

* Improves for group replication monitoring and replication lag actions. [#3533](https://github.com/sysown/proxysql/pull/3533)

* Fixes issues found with the `client error limit` implementation. [#3627](https://github.com/sysown/proxysql/pull/3627)

## Improvements

* [psqladm-320](https://jira.percona.com/browse/psqladm-320): Performs a `SAVE` operation for the users table only if the users table has changed.

* [psqladm-339](https://jira.percona.com/browse/psqladm-339): Provides a method when a cluster read-only state has changed to update proxysql-admin without requiring a cluster restart.

* [psqladm-327](https://jira.percona.com/browse/psqladm-327): Adds the `--server` option to skip the check for cluster membership. This option is specified with either the `--syncusers` command or the `--sync-multi-cluster-users` command and allows standalone nodes to be synced.

**WARNING**: An upgrade from ProxySQL v1.x to ProxySQL v2.x requires the user to manually remove the ProxySQL v1.x packages. After that operation, the user can install ProxySQL v2.x.

*ProxySQL* is available under Open Source license GPLv3.
