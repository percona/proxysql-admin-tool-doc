# ProxySQL 1.4.16 and proxysql-admin (2020-02-11)

* **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

*ProxySQL* release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* 1.4.16 source and binary packages are available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include **ProxySQL Admin** – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/).

## Bugs Fixed

* [PSQLADM-219](https://jira.percona.com/browse/PSQLADM-219): The [ProxySQL scheduler](https://github.com/sysown/proxysql/blob/master/doc/scheduler.md) was handling the `pxc_maint_mode` variable incorrectly. As a result, open connections were closed immediately. This bug has been fixed and now the ProxySQL scheduler only sets the node status to `OFFLINE_SOFT`. This prevents opening new connections and lets the already established connections finish their work. It is up to the user to decide when it is safe to start the node maintenance.

*ProxySQL* is available under Open Source license GPLv3.
