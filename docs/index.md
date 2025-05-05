# Percona build of ProxySQL, proxysql-admin, and percona-scheduler-handler documentation

!!! note ""

    This documentation is for the latest release: Percona ProxySQL admin tools {{release}} ([Release notes]({{release}}.md)).

[ProxySQL](https://www.proxysql.com/) acts as a proxy between Percona XtraDB Cluster 
and your client application. It manages a connection pool, caching connections and 
keeping them open for future requests. ProxySQL runs continuously without needing a 
restart.

Without a connection pool, each SQL request opens a new connection to the remote 
node and closes it after completion. ProxySQL keeps certain connections open and 
reuses them or closes them if not reused within a specific time. You connect to the 
proxy, and it forwards your requests to the cluster.

ProxySQL operates as a daemon monitored by a process that can restart it in case of 
an unexpected exit, minimizing downtime. The daemon accepts traffic from MySQL 
clients and forwards it to backend MySQL servers.

Configuration options include runtime parameters, server grouping, and 
traffic-related parameters, many of which can be set at runtime using SQL-like 
queries.

The [ProxySQL 2 documentation](https://proxysql.com/documentation/) provides details 
on installation, running ProxySQL, and using the ProxySQL admin tools. The maintained releases are listed on 
[ProxySQL Installation](https://proxysql.com/documentation/installing-proxysql/).

You can [download ProxySQL 2.x.x](https://www.percona.com/download-proxysql). Note that 
version 1 is no longer actively maintained.

ProxySQL 2.x.x downloads include:

- [ProxySQL Admin (proxysql-admin)](proxysql-admin-tool-v2-config.md) simplifies 
  the configuration of Percona XtraDB Cluster nodes with ProxySQL.

- [pxc_scheduler_handler](build-psh.md) automatically performs failovers due to 
  node failures, service degradation, or maintenance. Available from 
  [ProxySQL 2.3.2-1.2](./release-notes-2.3.2-1.md) and higher.

In a MySQL 8.4 or Percona Server for MySQL 8.4 environment, you may face these 
issues:

- ProxySQL contains counters that have not been updated to use the new terminology, 
  leading to unexpected results.

- The binlog reader errors out during initialization due to the use of old 
  terminology, such as the the `SHOW MASTER STATUS` command
