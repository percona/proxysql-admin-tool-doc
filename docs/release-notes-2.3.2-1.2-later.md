# Release notes from ProxySQL 2.0.3 to ProxySQL 2.3.2

## ProxySQL 2.3.2 and proxysql-admin (2021-11-03)

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

### Release Highlights

The following list are some of the bug fixes provided by ProxySQL from versions 2.2.1 to 2.3.2:

* Supports the use of grave accent or backtick (\`) symbol for SET statements. [#3479](https://github.com/sysown/proxysql/issues/3479)

* Re-implements how comments are handled in `USE` statements. [#3610](https://github.com/sysown/proxysql/pull/3610)

* Implements the `PROXYSQL TLS RELOAD` command which allows reloading TLS files at runtime. This command lets ProxySQL change its certifications and key files used for client connections. [#3552](https://github.com/sysown/proxysql/pull/3552)

* Improves for group replication monitoring and replication lag actions. [#3533](https://github.com/sysown/proxysql/pull/3533)

* Fixes issues found with the `client error limit` implementation. [#3627](https://github.com/sysown/proxysql/pull/3627)

### Improvements

* [psqladm-320](https://jira.percona.com/browse/psqladm-320): Performs a `SAVE` operation for the users table only if the users table has changed.

* [psqladm-339](https://jira.percona.com/browse/psqladm-339): Provides a method when a cluster read-only state has changed to update proxysql-admin without requiring a cluster restart.

* [psqladm-327](https://jira.percona.com/browse/psqladm-327): Adds the `--server` option to skip the check for cluster membership. This option is specified with either the `--syncusers` command or the `--sync-multi-cluster-users` command and allows standalone nodes to be synced.

**WARNING**: An upgrade from ProxySQL v1.x to ProxySQL v2.x requires the user to manually remove the ProxySQL v1.x packages. After that operation, the user can install ProxySQL v2.x.

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.2.0 and proxysql-admin (2021-08-10)

[Installation](install-v2.md)

*ProxySQL* 2.2.0, released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/downloads/proxysql2/) along with an updated version of the Percona proxysql-admin tool.

ProxySQL is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like Percona Server for MySQL and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The ProxySQL 2.2.0 source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin - a tool developed by Percona to configure Percona XtraDB Cluster nodes into ProxySQL. Docker images for 2.2.0 are available as well.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). ProxySQL offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* [2.2.0 release notes](https://github.com/sysown/proxysql/releases/tag/v2.2.0)

!!! note

    An upgrade from ProxySQL v1.x to ProxySQL v2.x requires the user to manually remove the ProxySQL v1.x packages. After that operation, the user can install ProxySQL v2.x.

**ProxySQL Admin** has not changed since the previous release.

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.1.1 and proxysql-admin (2021-07-09)

**Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)


*ProxySQL* 2.1.1, released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* 2.1.1 source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by **Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images for 2.1.1 are available as well.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* [2.1.0 release notes](https://github.com/sysown/proxysql/releases/tag/v2.1.0) and [2.1.1 release notes](https://github.com/sysown/proxysql/releases/tag/v2.1.1)

**NOTE**: An upgrade from ProxySQL v1.x to ProxySQL v2.x requires the user to manually remove the ProxySQL v1.x packages. After that operation, the user can install ProxySQL v2.x.

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.0.18 and proxysql-admin (2021-04-19)

* **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)


ProxySQL 2.0.18, released by [ProxySQL](https://www.proxysql.com/), is now available for [download in the Percona repository](https://www.percona.com/downloads/proxysql2/) along with an updated version of Percona’s proxysql-admin tool.

ProxySQL is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like Percona Server for MySQL and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created ProxySQL for database administrators as a means of solving complex replication topology issues.

The ProxySQL 2.0.18 source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by Percona to configure Percona XtraDB Cluster nodes into ProxySQL. [Docker images for 2.0.18](https://hub.docker.com/r/percona/proxysql2) are available as well.

You can download the original ProxySQL from GitHub. ProxySQL offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the [ProxySQL 2.0.18 release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.18) This is the [ProxySQL release tag](https://github.com/sysown/proxysql/releases/tag/v2.0.18).

ProxySQL Admin has not changed since the previous release.

ProxySQL is available under Open Source license GPLv3.

## ProxySQL 2.0.17 and proxysql-admin (2021-04-06)

* **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* release , released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of the Percona proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by **Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.17[release notes]. This is the [ProxySQL release tag](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

### Bug Fixes

* [PSQLADM-282](https://jira.percona.com/browse/PSQLADM-282): Fix proxysql-admin zombie processes issue

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.0.15 and proxysql-admin (2020-11-17)

* **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* release , released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of the Percona proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by **Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.15 [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

This version includes *ProxySQL* release. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* release [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.15)

This is the [ProxySQL release tag](https://github.com/sysown/proxysql/releases/tag/v2.0.15).

## Improvements

* [PSQLADM-92](https://jira.percona.com/browse/PSQLADM-92): Allow the use of an encrypted password in proxysql-admin

*ProxySQL* is available under Open Source license GPLv3.

<!-- `Docker` replace:: Docker -->
<!-- `MariaDB` replace:: MariaDB -->
<!-- `MySQL` replace:: MySQL -->
<!-- `--disable` replace:: `--disable` -->
<!-- **Percona** replace:: Percona -->
<!-- `ProxySQL Admin` replace:: **ProxySQL Admin** -->
<!-- `ProxySQL scheduler` replace:: ProxySQL scheduler -->
<!-- *ProxySQL* replace:: *ProxySQL* -->
<!-- **Percona Server for MySQL** replace:: Percona Server for MySQL -->
<!-- **Percona XtraDB Cluster** replace:: Percona XtraDB Cluster -->

## ProxySQL 2.0.14 and proxysql-admin (2020-09-24)

* **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* release , released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of the Percona proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by Percona to configure Percona XtraDB Cluster nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.14[release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.14)

This version includes *ProxySQL* release. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* release [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17). This is the [ProxySQL release tag](https://github.com/sysown/proxysql/releases/tag/v2.0.14) 

### Improvements

* [PSQLADM-256](https://jira.percona.com/browse/PSQLADM-256): Wrong password with % character

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.0.13 and proxysql-admin (2020-08-05)

* [Installation](install-v2.md)

*ProxySQL* 2.0.13, released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of the Percona proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by **Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.13 [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

This version includes *ProxySQL* release. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.13)

### Bugs Fixed

* [PSQLADM-209](https://jira.percona.com/browse/PSQLADM-209): No installation documentation for ProxySQL tarball packages

* [PSQLADM-254](https://jira.percona.com/browse/PSQLADM-254): proxysql-admin script did not print write node info from runtime_mysql_servers table when using singlewrite mode

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.0.12 and proxysql-admin (2020-06-11)

* **Installation**

    [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* 2.0.12, released by [ProxySQL](https://www.proxysql.com/), is now available for download in the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of Percona’s proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an intermediary for client requests seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by **Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from
GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.12 [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

This version includes *ProxySQL* release. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* release [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.12)

[https://github.com/sysown/proxysql/releases/tag/v2.0.12](https://github.com/sysown/proxysql/releases/tag/v2.0.12)

ProxySQL Admin has not changed since the previous release.

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.0.7 and proxysql-admin (2019-10-23)

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

## ProxySQL 2.0.6 and proxysql-admin (2019-08-21)

**Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* 2.0.6, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of Percona’s
proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from
GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.6 [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

This version includes *ProxySQL* release. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* release [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

[https://github.com/sysown/proxysql/releases/tag/v2.0.6](https://github.com/sysown/proxysql/releases/tag/v2.0.6)

ProxySQL Admin has not changed since the previous release.

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.0.5 and proxysql-admin (2019-11-23)

* **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* 2.0.5, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of Percona’s proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from
GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.5 [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

This version includes *ProxySQL* release. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* release [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

The proxysql-admin tool has been enhanced to support the following new options and commands:

|Option|Description|
|--- |--- |
|`–add-query-rule`|Creates query rules for synced MySQL users. This option is only applicable for the singlewrite mode and works together with the `–syncusers` and `–sync-multi-cluster-users` options.|
|`–force`|Skips existing configuration checks in `mysql_servers`, `mysql_users` and `mysql_galera_hostgroups` tables. This option will only work together with the `–enable` option: `$ proxysql-admin --enable --force`|
|`–update-mysql-version` (command)|Updates the `mysql-server_version` variable in ProxySQL with the version from a node in Percona XtraDB Cluster.|

### Improvements

* [PSQLADM-49](https://jira.percona.com/browse/PSQLADM-49): Create rules for `–syncusers`. When running with `–syncusers` or `–sync-multi-cluster-users`, the `–add-query-rule` option can now be specified to add the `singlewriter` query rules for the new users.

* [PSQLADM-51](https://jira.percona.com/browse/PSQLADM-51): Update `mysql-server_version` variable. The `–update-mysql-version` command has been added to set the `mysql-server_version` global variable in ProxySQL. This will take the version from a node in the cluster and set it in *ProxySQL*.

### Bugs fixed

* [PSQLADM-190](https://jira.percona.com/browse/PSQLADM-190): The `–remove-all-servers` option did not work on enable. When running with `proxysql-cluster`, the galera hostgroups information was not replicated, which could result in failing to run `–enable` on a different *ProxySQL* node.  The –force option was added for `–enable` to be able to ignore any errors and always configure the cluster.

* [PSQLADM-199](https://jira.percona.com/browse/PSQLADM-199): query-rules removed during proxysql-cluster creation with *Percona XtraDB Cluster (PXC)* operator. When using the *Percona XtraDB Cluster (PXC)* operator for Kubernetes and creating a proxysql-cluster, the query rules could be removed. The code was modified to merge the query rules (rather than deleting and recreating).  If the `–force` option was specified, then a warning was issued in case any existing rules were found; otherwise an error was issued. The `–disable-updates` option was added to ensure that *ProxySQL* cluster updates did not interfere with the current command.

* [PSQLADM-200](https://jira.percona.com/browse/PSQLADM-200): users were not created for `–syncusers` with *Percona XtraDB Cluster (PXC)* operator. When using the *Percona XtraDB Cluster (PXC)* operator for Kubernetes, the `–syncusers` command was run but the mysql_users table was not updated. The fix for [PSQLADM-199](https://jira.percona.com/browse/PSQLADM-199) that suggested to use `–disable-updates` also applies here.

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.0.4 and proxysql-admin (2019-05-28)

**Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* 2.0.4, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of Percona’s **proxysql-admin** tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from
GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.4 [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

This version includes *ProxySQL* release. For more information on the issues fixed, features, or enhancements, see the *ProxySQL* release [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

[https://github.com/sysown/proxysql/releases/tag/v2.0.4](https://github.com/sysown/proxysql/releases/tag/v2.0.4)

ProxySQL Admin has not changed since the previous release.

*ProxySQL* is available under Open Source license GPLv3.

## ProxySQL 2.0.3 and proxysql-admin  (2019-05-07)

* **Installation**

    [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* 2.0.3, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of Percona’s proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from
GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.3 [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

With *ProxySQL* 2.0.3, ProxySQL Admin now uses the native *ProxySQL* support for **Percona XtraDB Cluster** and does not require custom bash scripts to keep track of *Percona XtraDB Cluster (PXC)* status.  As a result, `proxysql_galera_checker` and `proxysql_node_monitor` have been removed.

### Improvements

* The proxysql-admin tool is MySQL 8.0 compatible

### New features

* New option –`use-ssl` to use SSL (Secure Sockets Layer) for connections between *ProxySQL* and the backend database servers

* New option - `–max-transactions-behind` to determine the maximum number of writesets that can be queued before the node is *SHUNNED* to avoid stale reads. The default value is *100*.

* New operation –update-cluster to update the cluster membership by adding server nodes as found. (Note that nodes are added but not removed).  The `–writer-hg` option may be used to specify which galera hostgroup to update. The `–remove-all-servers` option instructs to remove all servers fromthe mysql_servers table before updating the cluster.  Hostgroups can now be specified on the command-line: `–writer-hg`, `–reader-hg`, `–backup-writer-hg`, and `–offline-hg`.  Previously, these host groups were only read from the configuration file.

* The –enable and –update-cluster options used simultaneously have special meaning. If the cluster has not been enabled, then `–enable` is run.  If the cluster has already been enabled, then `–update-cluster` is run.

* New command –is-enabled to see if a cluster has been enabled. This command checks for the existence of a row in the `mysql_galera_hostgroups` table. `–writer-hg` may be used to specify the writer hostgroup used to search the `mysql_galera_hostgroups` table.

* New command –status to display galera hostgroup information. This commandlists all rows in the current `mysql_galera_hostgroups` table as well as all servers that belong to these hostgroups.  With the `–writer-hg` option, only the information for the galera hostgroup with that writer hostgroup is displayed.

### Changed features

* Setting `–node-check-interval` now changes the *ProxySQL* global variable `mysql-monitor_galera_healthcheck_interval`. Note that this is a global variable, not a per-cluster variable.

* The option –write-node now takes only a single address as a parameter. In the singlewrite mode we only set the weight if `–write-node` specifies address:port. A priority list of addresses is no longer accepted.

* The option `–writers-as-readers` option now accepts a different set of values. Due to changes in the behavior of *ProxySQL* between version 1.4 and version 2.0 related to Galera support, the values of `–writers-as-readers` have been changed. This option now accepts the following values: yes, no, and backup.

yes:

    writers, backup-writers, and read-only nodes can act as readers.

no:

    only read-only nodes can act as readers.

backup:

    only backup-writers can act as readers.

* The commands `–syncusers`, `–sync-multi-cluster-users`, `–adduser`, and `–disable` can now use the `–writer-hg` option.

* The command `–disable` removes all users associated with the galera cluster hostgroups. Previously, this command only removed the users with the `CLUSTER_APP_USERNAME`.

* The command `–disable` now accepts the `–writer-hg` option to disable the Galera cluster associated with that hostgroup overriding the value specified in the configuration file.

### Removed features

* Asynchronous slave reader support has been removed: the `–include-slaves` option is not supported.

* A list of nodes in the priority order is no longer supported. Only a single node is supported at this time.

* Since the proxysql_galera_checker and proxysql_node_monitor scripts are no longer run in ProxySQL scheduler, automatic cluster membership updates are not supported.

* Checking the `pxc_maint_mode` variable is no longer supported

* Using desynced nodes if no other nodes are available is no longer supported.

* The server status is no longer maintained in the mysql_servers table.

### Limitations

* With –writers-as-readers set to *backup*, read-only nodes are not allowed. This a limitation of *ProxySQL* 2.0.  Note that *backup* is the default value of `–writers-as-readers` when `–mode` equals to *singlewrite*

*ProxySQL* is available under Open Source license GPLv3.