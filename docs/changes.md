.. _changes:

Changes in the ProxySQL-admin tool with PrxoySQL version 2
-----------------------------------------------------------

Starting with ProxySQL 2.0.3, the ProxySQL-admin tool uses the native ProxySQL support for Percona XtraDB Cluster and no longer
requires a set of custom bash scripts to keep track of the PXC status. As a result,
`proxysql_galera_checker` and `proxysql_node_monitor` are removed.

## Summary of Changes in Tool with ProxySQL v2


### Added Features

The following features are added:

-   New command `--is-enabled` verifies a cluster is enabled.
    This command checks for the existence of a row in the `mysql_galera_hostgroups` table. Add the `--writer-hg` option to specify the writer hostgroup used to search the `mysql_galera_hostgroups` table.
-   New command `--status` displays the Galera hostgroup information. This command lists all rows in the current `mysql_galera_hostgroups` table as well as all servers that belong to these hostgroups. With the `--writer-hg` option, only the information for the Galera hostgroup with that writer hostgroup is displayed.
-   New option `--use-ssl` uses SSL for connections between ProxySQL and the backend database servers
-   New option `--max-transactions-behind` determines the maximum number of writesets that can be queued before the node is shunned to avoid stale reads. The default value is 100.
-   New option `--login-file` reads login credentials from an encrypted
    file. If the `--login-password` or `login-password-file` options are
    not specified, the user is prompted for the password.
-   New option `--login-password` is the key used to decrypt the
    encrypted login-file. You cannot use the option with the
    `--login-password-file`.
-   New option `--login-password-file` reads the key from a file using
    the specified path. You cannot use the option with `login-password`.
-   New operation `--update-cluster` updates the cluster membership by
    adding server nodes as found. (Note that nodes are added but not
    removed). The `--writer-hg` option may be used to specify which
    Galera hostgroup to update. The `--remove-all-servers` option
    instructs ProxySQL to remove all servers from the `mysql_servers` table before
    updating the cluster.
-   Hostgroups can be specified on the command-line: `--writer-hg`,
    `--reader-hg`, `--backup-writer-hg`, and `--offline-hg`. Previously,
    these host groups were only read from the configuration file.
-   The `--enable` and `--update-cluster` options used simultaneously
    have special meaning. If the cluster has not been enabled, then
    `--enable` is run. If the cluster has already been enabled, then
    `--update-cluster` is run.



### Changed Features

The following features are changed:

-   Setting `--node-check-interval` changes the ProxySQL global variable `mysql-monitor_galera_healthcheck_interval`. This is a
    global variable not a per-cluster variable.
-   The option `--write-node` takes only a single address as a
    parameter. In the singlewrite mode, we set the weight only if the
    `--write-node` specifies *address:port*. A priority list of
    addresses is no longer accepted.
-   The option `--writers-as-readers` accepts a different set of
    values. The `--writers-as-readers` values have been changed due
    to changes in the ProxySQL behavior related to Galera support between version 1.4 and
    version 2.0. This option accepts the
    following values:

	*   yes - `writers`, `backup-writers`, and `read-only` nodes can act as readers

	*   no - only `read-only` nodes can act as readers

	*   backup - only `backup-writers` can act as readers

-   The commands `--syncusers`, `--sync-multi-cluster-users`,
    `--adduser`, and `--disable` can use the `--writer-hg` option.
-   The command `--disable` removes all users associated with the Galera
    cluster hostgroups. Previously, this command only removed the users
    with the **CLUSTER_APP_USERNAME**.
-   The command `--disable` accepts the `--writer-hg` option. The option disables the Galera cluster associated with that hostgroup and overrides the
    configuration file value.

### Removed Features

The following features are removed:

-   Asynchronous slave reader support has been removed: the
    `--include-slaves` option is not supported.
-   A list of nodes in the priority order is not supported in v2. Only a
    single node is supported at this time.
-   Since the `galera_proxysql_checker` and `galera_node_monitor` scripts
    are no longer run in the scheduler, automatic cluster membership
    updates are not supported.
-   Checking the `pxc_maint_mode` variable is no longer supported
-   Using desynced nodes when other nodes are unavailable is no longer
    supported.
-   The server status is no longer maintained in the mysql_servers
    table.

### Limitations

The following limitations are defined:

-   With `--writers-as-readers=backup` read-only nodes are not allowed.
    This a limitation of ProxySQL 2.0. Note that backup is the default
    value of `--writers-as-readers` when `--mode=singlewrite`
