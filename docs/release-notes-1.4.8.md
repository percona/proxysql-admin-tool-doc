# ProxySQL 1.4.8 and proxysql-admin (2018-05-22)

- **Installation**

    [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

*ProxySQL* release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* 1.4.8 source and binary packages are available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/).

## Usability improvement

- [PSQLADM-84](https://jira.percona.com/browse/PSQLADM-84): Now proxysql_status tool dumps host_priority
and /etc/proxysql-admin.cnf. Also output format was changed.

## Other improvements and bug fixes

- [PSQLADM-66](https://jira.percona.com/browse/PSQLADM-66): The `–syncusers` option now makes ProxySQL Admin to
update the user’s password in *ProxySQL* database if there is any password difference between *ProxySQL* user and MySQL user.

- [PSQLADM-45](https://jira.percona.com/browse/PSQLADM-45): it was unclear from the help screen, that
`–config-file` option requires an argument.

- [PSQLADM-48](https://jira.percona.com/browse/PSQLADM-48): `${PROXYSQL_DATADIR}/${CLUSTER_NAME}`_mode file was not
created at ProxySQL Admin upgrade (1.4.5 or before to 1.4.6 onwards).

- [PSQLADM-52](https://jira.percona.com/browse/PSQLADM-52): The *proxysql_galera_checker* script was not
checking empty query rules.

- [PSQLADM-54](https://jira.percona.com/browse/PSQLADM-54): `proxysql_node_monitor` did not change
OFFLINE_HARD status properly for the coming back online nodes.

*ProxySQL* is available under Open Source license GPLv3.
