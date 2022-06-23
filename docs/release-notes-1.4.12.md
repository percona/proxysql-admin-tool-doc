# ProxySQL 1.4.12 and proxysql-admin (2018-11-13)

* **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

*ProxySQL* release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* 1.4.12 source and binary packages are available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include **ProxySQL Admin** – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/).

## Improvements

* [PSQLADM-68](https://jira.percona.com/browse/PSQLADM-68): Scripts are now compatible with *Percona XtraDB Cluster (PXC)* hosts using IPv6

* [PSQLADM-107](https://jira.percona.com/browse/PSQLADM-107): In include-slaves, a slave would always be moved into the write hostgroup even if the whole cluster went down. A new option –use-slave-as-writer specifies whether or not the slave is added to the write hostgroup.

## Bugs Fixed

* [PSQLADM-110](https://jira.percona.com/browse/PSQLADM-110): In some cases, pattern cluster hostname did not work with proxysql-admin.

* [PSQLADM-104](https://jira.percona.com/browse/PSQLADM-104): proxysql-admin testsuite bug fixes.

* [PSQLADM-113](https://jira.percona.com/browse/PSQLADM-113): `proxysql_galera_checker` assumed that parameters were given in the long format.

* [PSQLADM-114](https://jira.percona.com/browse/PSQLADM-114): In some cases, *ProxySQL* could not be started

* [PSQLADM-115](https://jira.percona.com/browse/PSQLADM-115): `proxysql_node_monitor` could fail with more than one command in the ProxySQL scheduler.

* [PSQLADM-116](https://jira.percona.com/browse/PSQLADM-116): In some cases, the ProxySQL scheduler was reloading servers on every run

* [PSQLADM-117](https://jira.percona.com/browse/PSQLADM-117): The `–syncusers` option did not work when enabling cluster

* [PSQLADM-125](https://jira.percona.com/browse/PSQLADM-125): The check-is-galera-checker-running function was not preventing multiple instances of the script from running.

Other bugs fixed: [PSQLADM-112](https://jira.percona.com/browse/PSQLADM-112), [PSQLADM-120](https://jira.percona.com/browse/PSQLADM-120)

*ProxySQL* is available under Open Source license GPLv3.
