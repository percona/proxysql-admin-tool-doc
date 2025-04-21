[Download](https://www.percona.com/download-proxysql)<br>
[Install](install-v2.md)<br>
[View the GitHub repository](https://github.com/percona/proxysql-admin-tool)

[ProxySQL](https://proxysql.com/) is a high-performance proxy for MySQL and MySQL-compatible database servers such as Percona Server for MySQL and MariaDB. It acts as an intermediary for client requests seeking resources from the database. ProxySQL was created for the database administrator to solve complex replication topology issues.

You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). The [ProxySQL documentation](https://proxysql.com/documentation/) provides information on installing and running ProxySQL.

The [ProxySQL Admin (proxysql-admin)](proxysql-admin-tool-v2-config.md) tool simplifies the configuration of Percona XtraDB Cluster nodes with ProxySQL.  [ProxySQL Admin 2](proxysql-admin-tool-functions.md) supports Percona XtraDB Cluster without custom scripts.

The [pxc_scheduler_handler](psh-overview.md) tool can automatically perform a failover due to node failures, service degradation, or maintenance. This tool has features and capabilities that differ from the ProxySQL admin tool, so you should not use options from one tool in the other, as that may cause unintended results.
