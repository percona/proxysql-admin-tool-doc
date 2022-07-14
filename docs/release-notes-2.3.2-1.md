# ProxySQL 2.3.2-1.2, proxysql-admin, and percona-scheduler-admin (2022-06-15)

ProxySQL is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like Percona Server for MySQL and MariaDB). It acts as an intermediary for client requests seeking resources from the database. ProxySQL was created for DBAs as a means of solving complex replication topology issues. The [ProxySQL documentation](https://proxysql.com/documentation/) provides information on installing and running ProxySQL.

The ProxySQL Admin (proxysql-admin) tool is used to simplify configurations of Percona XtraDB Cluster nodes with ProxySQL.

The Percona Scheduler Admin (percona-scheduler-admin) tool is used to simplify configurations of Percona XtraDB Cluster nodes into ProxySQL. This tool can automatically perform a failover due to node failures, service degradation, or maintenance.

## Release Highlights

Percona adds support for the [Percona Scheduler Admin tool](https://docs.percona.com/proxysql/psa-scheduler.html).

This tool manages the integration between ProxySQL and Galera/Percona XtraDB Cluster. The tool maintains the ProxySQL mysql_server table during maintenance or if negative scenarios occur, such as failures or service degradation. The tool replaces the Replication Manager, simplifying the cluster’s architecture.

## New Features

* [PSQLADM-330](https://jira.percona.com/browse/PSQLADM-330): Adds support for the Percona Scheduler Admin tool.

## Improvements

The ProxySQL Admin tool adds support for Percona XtraDB Cluster 5.5 and MariaDB Server 10.6.

## Useful links

* The [ProxySQL and proxysql-admin installation instructions](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

* The [Percona Software downloads](https://www.percona.com/downloads/)

* The [ProxySQL and proxysql-admin GitHub location](https://github.com/percona/proxysql-admin-tool)

* To contribute to the documentation, review the [Documentation Contribution Guide](https://github.com/percona/proxysql-admin-tool-doc/blob/main/source/contributing.md)
