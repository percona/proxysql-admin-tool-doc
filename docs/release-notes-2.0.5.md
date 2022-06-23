# ProxySQL 2.0.5 and proxysql-admin (2019-11-23)

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

## Improvements

* [PSQLADM-49](https://jira.percona.com/browse/PSQLADM-49): Create rules for `–syncusers`. When running with `–syncusers` or `–sync-multi-cluster-users`, the `–add-query-rule` option can now be specified to add the `singlewriter` query rules for the new users.

* [PSQLADM-51](https://jira.percona.com/browse/PSQLADM-51): Update `mysql-server_version` variable. The `–update-mysql-version` command has been added to set the `mysql-server_version` global variable in ProxySQL. This will take the version from a node in the cluster and set it in *ProxySQL*.

## Bugs fixed

* [PSQLADM-190](https://jira.percona.com/browse/PSQLADM-190): The `–remove-all-servers` option did not work on enable. When running with `proxysql-cluster`, the galera hostgroups information was not replicated, which could result in failing to run `–enable` on a different *ProxySQL* node.  The –force option was added for `–enable` to be able to ignore any errors and always configure the cluster.

* [PSQLADM-199](https://jira.percona.com/browse/PSQLADM-199): query-rules removed during proxysql-cluster creation with *Percona XtraDB Cluster (PXC)* operator. When using the *Percona XtraDB Cluster (PXC)* operator for Kubernetes and creating a proxysql-cluster, the query rules could be removed. The code was modified to merge the query rules (rather than deleting and recreating).  If the `–force` option was specified, then a warning was issued in case any existing rules were found; otherwise an error was issued. The `–disable-updates` option was added to ensure that *ProxySQL* cluster updates did not interfere with the current command.

* [PSQLADM-200](https://jira.percona.com/browse/PSQLADM-200): users were not created for `–syncusers` with *Percona XtraDB Cluster (PXC)* operator. When using the *Percona XtraDB Cluster (PXC)* operator for Kubernetes, the `–syncusers` command was run but the mysql_users table was not updated. The fix for [PSQLADM-199](https://jira.percona.com/browse/PSQLADM-199) that suggested to use `–disable-updates` also applies here.

*ProxySQL* is available under Open Source license GPLv3.
