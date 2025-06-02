# Percona build of ProxySQL, proxysql-admin, and percona-scheduler-handler documentation

!!! note ""

    This documentation is for the latest release: Percona ProxySQL admin tools {{release}} ([Release notes]({{release}}.md)).

Percona distributes [ProxySQL](https://www.proxysql.com/) from the upstream project without code changes and provides additional tools like proxysql-admin for easier integration with Percona XtraDB Cluster. ProxySQL is a high-performance proxy that sits between client applications and Percona XtraDB Cluster. The proxy manages a connection pool by caching database connections and keeping those connections open for future use. This behavior reduces the overhead of repeatedly establishing and tearing down connections for each SQL request.

Without a connection pool, every SQL query would require a new connection to a cluster node, which would be closed after the query completed. ProxySQL maintains selected connections and reuses them as needed or closes unused connections after a defined idle time. Client applications connect to ProxySQL, which forwards database traffic to the XtraDB Cluster.

The ProxySQL service runs as a daemon and is monitored by a watchdog process capable of restarting it in case of unexpected termination, which helps minimize downtime. The daemon receives traffic from MySQL clients and forwards it to backend MySQL-compatible servers.

Configuration is handled using SQL-like statements, including runtime options, server grouping, and query routing rules. Most settings can be changed dynamically without restarting the proxy.

The [ProxySQL 2 documentation](https://proxysql.com/documentation/) includes detailed guidance on installation, operation, and the use of supporting tools. The maintained releases are listed on 
[ProxySQL Installation](https://proxysql.com/documentation/installing-proxysql/).

[You can download Percona's build of ProxySQL 2.x.x](https://www.percona.com/download-proxysql). Note that 
Version 1 is no longer actively maintained. The ProxySQL 2. x. x downloads may include:

- [ProxySQL Admin (proxysql-admin)](proxysql-admin-tool-v2-config.md) simplifies the configuration of Percona XtraDB Cluster nodes with ProxySQL.

- [pxc_scheduler_handler](build-psh.md) automatically performs failovers due to 
  node failures, service degradation, or maintenance. Available from 
  [ProxySQL 2.3.2-1.2](./release-notes-2.3.2-1.md) and higher.

In a MySQL 8.4 or Percona Server for MySQL 8.4 environment, you may face these 
issues:

* ProxySQL contains counters that have not been updated to use the new terminology, 
  leading to unexpected results.

* The binlog reader errors out during initialization due to the use of old 
  terminology, such as the `SHOW MASTER STATUS` command

