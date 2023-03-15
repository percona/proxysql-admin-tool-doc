# ProxySQL, proxysql-admin, and percona-scheduler-admin documentation

!!! note ""

    This documentation is for the latest release: Percona ProxySQL admin tools {{release}} ([Release notes]({{release}}.md)).

[ProxySQL](https://www.proxysql.com/) is a tool that performs like a proxy between *Percona XtraDB Cluster* and your client application. *ProxySQL* manages a connection pool, which caches your connections and keeps the connections open for future requests. *ProxySQL* is designed to run continuously without being restarted.

Without a connection pool, each SQL request opens a connections to the remote node. When the SQL request is complete, the connection is closed. A new one is opened on the next SQL request.

ProxySQL maintains the connection pool. The pool allows a certain number of connections to remain open. A connection is reused or closed if not reused within a specific time. You connect to the proxy and the tool forwards your requests to the cluster.

*ProxySQL* runs as a daemon watched by a monitoring process which can restart *ProxySQL* in case of an unexpected exit to minimize downtime. The daemon accepts incoming traffic from *MySQL* clients and forwards the traffic to backend *MySQL* servers.

The configuration options include runtime parameters, server grouping, and traffic-related parameters. Many of the settings can be done at runtime using queries that are similar to SQL statements.

The [ProxySQL documentation](https://proxysql.com/documentation/) provides information on installing and running ProxySQL and the ProxySQL admin tools.


ProxySQL is available from the Percona software repositories with the following:

* ProxySQL 1.x.x downloads include:

    * [ProxySQL Admin 1.x.x](proxysql-v1.md) does not natively support *Percona XtraDB Cluster* and requires custom `Bash` scripts to track the status of a *Percona XtraDB Cluster*.
  
* ProxySQL 2.x.x downloads include:

    * [ProxySQL Admin (proxysql-admin)](proxysql-admin-tool-v2-config.md) simplifies the configuration of *Percona XtraDB Cluster* nodes with ProxySQL.

    * [pxc_scheduler_handler](build-psh.md) can automatically perform a failover due to node failures, service degradation, or maintenance. This utility is available from [ProxySQL 2.3.2-1.2](./release-notes-2.3.2-1.md) and higher.

