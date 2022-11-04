# ProxySQL 1.4.6 and proxysql-admin (2018-03-12)

* **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

*ProxySQL* release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving
complex replication topology issues.

The *ProxySQL* 1.4.6 source and binary packages available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/).

## Usability improvements

* [PSQLADM-32](https://jira.percona.com/browse/PSQLADM-32): Now, proxysql-admin script can configure
multiple clusters in *ProxySQL*, when there are unique cluster names specified
by the wsrep_cluster_name option, and the /etc/proxysql-admin.cnf
configuration contains different *ProxySQL* READ/WRITE hostgroup and different
application user for each cluster. Currently multiple clusters support is not
compatible with host priority feature, which works only with a single cluster.

* [PSQLADM-81](https://jira.percona.com/browse/PSQLADM-81): The new version substantially increases the number of test cases
in the ProxySQL Admin test-suite.

## Bug fixes

* [PSQLADM-35](https://jira.percona.com/browse/PSQLADM-35): proxysql_galera_checker monitoring script was
unable to discover new writer nodes.

* [PSQLADM-36](https://jira.percona.com/browse/PSQLADM-36): upgrade to *ProxySQL* 1.4.6 from the previous version
was broken.

* [PSQLADM-79](https://jira.percona.com/browse/PSQLADM-79): Fixed by properly quoting the MONITOR_USERNAME environment
variable in the admin script query.

*ProxySQL* is available under Open Source license GPLv3.
