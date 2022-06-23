# ProxySQL 1.4.5 and proxysql-admin (2018-02-15)

* **Installation**:[https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

*ProxySQL* 1.4.5, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the *MySQL* ecosystem (like **Percona Server for MySQL** and *MariaDB*). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* 1.4.5 source and binary packages are available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/).

* [PSQLADM-6](https://jira.percona.com/browse/PSQLADM-6): If the cluster node goes offline, the proxysql_node_monitor
script now sets the node status as OFFLINE_HARD, and does not remove it from the *ProxySQL* database. Also, logging is consistent regardless of the cluster node online status.

* [PSQLADM-30](https://jira.percona.com/browse/PSQLADM-30): Validation was added for the host priority file.

* [PSQLADM-33](https://jira.percona.com/browse/PSQLADM-33): Added –proxysql-datadir option to run the proxysql-admin script with a custom *ProxySQL* data directory.

* Also, BATS test suite was added for the proxysql-admin testing.

## Bug fixes

* [PSQLADM-5](https://jira.percona.com/browse/PSQLADM-5): *Percona XtraDB Cluster (PXC)* mode specified with proxysql-admin with use of `–mode` parameter was not persistent.

* [PSQLADM-8](https://jira.percona.com/browse/PSQLADM-8): *ProxySQL* High CPU load took place when mysqld was hanging.

*ProxySQL* is available under Open Source license GPLv3.
