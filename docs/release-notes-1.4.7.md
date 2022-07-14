# ProxySQL 1.4.7 and proxysql-admin (2018-04-16)

- **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

*ProxySQL* release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* 1.4.7 source and binary packages available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/).

## Usability improvements

- Added `proxysql_status` tool to dump *ProxySQL* configuration and statistics.

## Bug fixes

- [PSQLADM-2](https://jira.percona.com/browse/PSQLADM-2): `proxysql_galera_checker` script didn’t check if
another instance of itself is already running. While running more then one
copy of `proxysql_galera_checker` in the same runtime environment at
the same time is still not supported, the introduced fix is able to prevent
duplicate script execution in most cases.

- [PSQLADM-40](https://jira.percona.com/browse/PSQLADM-40): ProxySQL scheduler generated a lot of
`proxysql_galera_checker` and `proxysql_node_monitor` processes in case of wrong ProxySQL credentials in `/etc/proxysql-admin.cnf` file.

- [PSQLADM-41](https://jira.percona.com/browse/PSQLADM-41): Timeout error handling was improved with clear messages.

- [PSQLADM-42](https://jira.percona.com/browse/PSQLADM-42): An inconsistency of the date format in *ProxySQL* and scripts was fixed.

- [PSQLADM-43](https://jira.percona.com/browse/PSQLADM-43): `proxysql_galera_checker` didn’t take into account
the possibility of special characters presence in mysql-monitor_password.

- [PSQLADM-44](https://jira.percona.com/browse/PSQLADM-44): `proxysql_galera_checker` generated unclear errors
in the `/etc/proxysql.log` file if wrong credentials where passed.

- [PSQLADM-46](https://jira.percona.com/browse/PSQLADM-46): `proxysql_node_monitor` script incorrectly split
the hostname and the port number in URLs containing hyphen character.

*ProxySQL* is available under Open Source license GPLv3.
