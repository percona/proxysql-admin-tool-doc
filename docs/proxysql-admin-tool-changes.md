# ProxySQL Admin tool changes

## Added Features

* New option `--use-ssl` to use SSL for connections between ProxySQL and the backend database servers

* New option `--max-transactions-behind` to determine the maximum number of writesets 
  that can be queued before the node is SHUNNED to avoid stale reads. The default value is 100

* New operation `--update-cluster` to update the cluster membership by adding
  server nodes as found. (Note that nodes are added but not removed).  The
  `--writer-hg` option may be used to specify which Galera hostgroup to
  update. The `--remove-all-servers` option instructs to remove all servers
  from the mysql_servers table before updating the cluster.

* Hostgroups can be specified on the command-line: `--writer-hg`,
  `--reader-hg`, `--backup-writer-hg`, and `--offline-hg`.  Previously,
  these host groups were only read from the configuration file.

* The `--enable` and `--update-cluster` options used simultaneously have
  special meaning. If the cluster has not been enabled, then `--enable` is
  run. If the cluster has already been enabled, then `--update-cluster` is run.

* New command `--is-enabled` to see if a cluster has been enabled. This
  command checks for the existence of a row in the mysql_Galera_hostgroups
  table. The `--writer-hg` option may be used to specify the writer hostgroup
  used to search the mysql_galera_hostgroups table.

* New command `--status` to display Galera hostgroup information. This command
  lists all rows in the current `mysql_galera_hostgroups` table as well as all
  servers that belong to these hostgroups.  With the `--writer-hg` option,
  only the information for the Galera hostgroup with that writer hostgroup is
  displayed.

* New option `--login-file` reads login credentials from an encrypted file.
  If the `--login-password` or `login-password-file` options are not
  specified, the user is prompted for the password.

* New option `--login-password` is the key used to decrypt the encrypted
  login-file. You cannot use the option with the `--login-password-file`.

* New option `--login-password-file` reads the key from a file using the
  specified path. You cannot use the option with `login-password`.

## Changed Features

* Setting `--node-check-interval` changes the ProxySQL global variable
  `mysql-monitor_galera_healthcheck_interval`. Note that this is a global
  variable, not a per-cluster variable.

* The option `--write-node` takes only a single address as a parameter. In the
  singlewrite mode we only set the weight if `--write-node` specifies
  *address:port*. A priority list of addresses is no longer accepted.

* The option `--writers-as-readers` option accepts a different set of values. The values of `--writers-as-readers`
  have been changed, due to changes in the behavior of ProxySQL between version 1.4 and version 2.0 related to Galera support. This option accepts the following values:

    | Option | Description                                                                        |
    | ------ | ---------------------------------------------------------------------------------- |
    | yes    | Writers, backup-writers, and read-only nodes can act as readers.                   |
    | no     |  Only read-only nodes can act as readers. Only read-only nodes can act as readers. |
    | backup | Only backup-writers can act as readers.                                            |

* The commands `--syncusers`, `--sync-multi-cluster-users`, `--adduser`,
  and `--disable` can use the `--writer-hg` option.

* The command `--disable` removes all users associated with the Galera cluster
  hostgroups. Previously, this command only removed the users with the
  **CLUSTER_APP_USERNAME**.

* The command `--disable` accepts the `--writer-hg` option to disable the
    Galera cluster associated with that hostgroup overriding the value specified
    in the configuration file.

## Removed Features

* Asynchronous slave reader support has been removed: the `--include-slaves`
    option is not supported.

* A list of nodes in the priority order is not supported in *ProxySQL* v2. Only
    a single node is supported at this time.

* Since the galera_proxysql_checker and galera_node_monitor scripts are no
    longer run in the scheduler, automatic cluster membership updates are not
    supported.

* Checking the pxc_maint_mode variable is no longer supported

* Using desynced nodes if no other nodes are available is no longer supported.

* The server status is no longer maintained in the mysql_servers table.

## Limitations

* With `--writers-as-readers=backup` read-only nodes are not allowed. This is a limitation of ProxySQL 2.x. Note that backup is the default value of
    `--writers-as-readers` when `--mode=singlewrite`
