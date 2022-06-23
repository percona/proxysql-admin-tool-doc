# ProxySQL 2.0.3 and proxysql-admin  (2019-05-07)

* **Installation**

    [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v2.html#installing-proxysql-v2)

*ProxySQL* 2.0.3, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of Percona’s proxysql-admin tool.

*ProxySQL* is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created *ProxySQL* for DBAs as a means of solving complex replication topology issues.

The *ProxySQL* release source and binary packages available from the [Percona download page for ProxySQL 2](https://www.percona.com/downloads/proxysql2/) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into *ProxySQL*. Docker images are available as well.

You can [download the original ProxySQL from
GitHub](https://github.com/sysown/proxysql/releases). *ProxySQL* offers the [ProxySQL documentation](https://proxysql.com/documentation/). For more information on the issues fixed, features, or enhancements, see the *ProxySQL* 2.0.3 [release notes](https://github.com/sysown/proxysql/releases/tag/v2.0.17)

With *ProxySQL* 2.0.3, ProxySQL Admin now uses the native *ProxySQL* support for **Percona XtraDB Cluster** and does not require custom bash scripts to keep track of *Percona XtraDB Cluster (PXC)* status.  As a result, `proxysql_galera_checker` and `proxysql_node_monitor` have been removed.

## Improvements

* The proxysql-admin tool is MySQL 8.0 compatible

## New features

* New option –`use-ssl` to use SSL (Secure Sockets Layer) for connections between *ProxySQL* and the backend database servers

* New option - `–max-transactions-behind` to determine the maximum number of writesets that can be queued before the node is *SHUNNED* to avoid stale reads. The default value is *100*.

* New operation –update-cluster to update the cluster membership by adding server nodes as found. (Note that nodes are added but not removed).  The `–writer-hg` option may be used to specify which galera hostgroup to update. The `–remove-all-servers` option instructs to remove all servers fromthe mysql_servers table before updating the cluster.  Hostgroups can now be specified on the command-line: `–writer-hg`, `–reader-hg`, `–backup-writer-hg`, and `–offline-hg`.  Previously, these host groups were only read from the configuration file.

* The –enable and –update-cluster options used simultaneously have special meaning. If the cluster has not been enabled, then `–enable` is run.  If the cluster has already been enabled, then `–update-cluster` is run.

* New command –is-enabled to see if a cluster has been enabled. This command checks for the existence of a row in the `mysql_galera_hostgroups` table. `–writer-hg` may be used to specify the writer hostgroup used to search the `mysql_galera_hostgroups` table.

* New command –status to display galera hostgroup information. This commandlists all rows in the current `mysql_galera_hostgroups` table as well as all servers that belong to these hostgroups.  With the `–writer-hg` option, only the information for the galera hostgroup with that writer hostgroup is displayed.

## Changed features

* Setting `–node-check-interval` now changes the *ProxySQL* global variable `mysql-monitor_galera_healthcheck_interval`. Note that this is a global variable, not a per-cluster variable.

* The option –write-node now takes only a single address as a parameter. In the singlewrite mode we only set the weight if `–write-node` specifies address:port. A priority list of addresses is no longer accepted.

* The option `–writers-as-readers` option now accepts a different set of values. Due to changes in the behavior of *ProxySQL* between version 1.4 and version 2.0 related to Galera support, the values of `–writers-as-readers` have been changed. This option now accepts the following values: yes, no, and backup.

yes:

    writers, backup-writers, and read-only nodes can act as readers.

no:

    only read-only nodes can act as readers.

backup:

    only backup-writers can act as readers.

* The commands `–syncusers`, `–sync-multi-cluster-users`, `–adduser`, and `–disable` can now use the `–writer-hg` option.

* The command `–disable` removes all users associated with the galera cluster hostgroups. Previously, this command only removed the users with the `CLUSTER_APP_USERNAME`.

* The command `–disable` now accepts the `–writer-hg` option to disable the Galera cluster associated with that hostgroup overriding the value specified in the configuration file.

### Removed features

* Asynchronous slave reader support has been removed: the `–include-slaves` option is not supported.

* A list of nodes in the priority order is no longer supported. Only a single node is supported at this time.

* Since the proxysql_galera_checker and proxysql_node_monitor scripts are no longer run in ProxySQL scheduler, automatic cluster membership updates are not supported.

* Checking the `pxc_maint_mode` variable is no longer supported

* Using desynced nodes if no other nodes are available is no longer supported.

* The server status is no longer maintained in the mysql_servers table.

### Limitations

* With –writers-as-readers set to *backup*, read-only nodes are not allowed. This a limitation of *ProxySQL* 2.0.  Note that *backup* is the default value of `–writers-as-readers` when `–mode` equals to *singlewrite*

*ProxySQL* is available under Open Source license GPLv3.
