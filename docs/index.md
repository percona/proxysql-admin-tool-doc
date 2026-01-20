# Percona build of ProxySQL, proxysql-admin, and percona-scheduler-handler documentation

!!! note ""

    This documentation is for the latest release: Percona ProxySQL admin tools {{release}} ([Release notes]({{release}}.md)).

Percona distributes [ProxySQL](https://www.proxysql.com/) from the upstream project without code changes and provides additional tools like proxysql-admin for easier integration with Percona XtraDB Cluster. ProxySQL is a high-performance proxy that sits between client applications and Percona XtraDB Cluster. The proxy manages a connection pool by caching database connections and keeping those connections open for future use. This behavior reduces the overhead of repeatedly establishing and tearing down connections for each SQL request.

Without a connection pool, every SQL query would require a new connection to a cluster node, which would be closed after the query completed. ProxySQL maintains selected connections and reuses them as needed or closes unused connections after a defined idle time. Client applications connect to ProxySQL, which forwards database traffic to the XtraDB Cluster.

The ProxySQL service runs as a daemon and is monitored by a watchdog process capable of restarting it in case of unexpected termination, which helps minimize downtime. The daemon receives traffic from MySQL clients and forwards it to backend MySQL-compatible servers.

Configuration is handled using SQL-like statements, including runtime options, server grouping, and query routing rules. Most settings can be changed dynamically without restarting the proxy.

!!! note

    [ProxySQL 3.0 contains a PostgreSQL module in beta.](https://github.com/sysown/proxysql/releases) The Percona build of ProxySQL is only tested with Percona Server for MySQL.

The [ProxySQL documentation](https://proxysql.com/documentation/) includes detailed guidance on installation, operation, and the use of supporting tools. The maintained releases are listed on 
[ProxySQL Installation](https://proxysql.com/documentation/installing-proxysql/).

[You can download Percona build of ProxySQL](https://www.percona.com/download-proxysql). Note that 
Version 1 is no longer actively maintained. The ProxySQL downloads may include:

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

<div data-grid markdown><div data-banner markdown>

### :material-progress-download: Installation guide { .title }

Find the best installation solution with our step-by-step installation instructions.

[Installation instructions](install-v2.md){ .md-button }

</div><div data-banner markdown>

## :material-progress-download: pxc_scheduler_handler tool { .title }

Learn about the pxc_scheduler_handler tool.

[pxc_scheduler_handler tool](psh-overview.md){ .md-button }

</div><div data-banner markdown>

### :material-backup-restore: proxysql-admin utility { .title }

Learn about the proxysql-admin utility.

[proxysql-admin utility](proxysql-admin-tool-v2-config.md){ .md-button }

</div><div data-banner markdown>

## :fontawesome-solid-gears: Start and stop ProxySQL { .title }

Learn about how to start and stop ProxySQL.

[Start and stop ProxySQL](start-or-stop-proxysql2.md){ .md-button}

</div>
</div>
