# Percona build of ProxySQL Admin tool changes

## Added features

### `--use-ssl`

Enables SSL connections between ProxySQL and the backend database servers

### `--max-transactions-behind` 

Specifies the maximum number of writesets that can be queued before the node is SHUNNED to avoid stale reads. The default value is `100`.

### `--update-cluster` 

Updates the cluster membership by adding newly discoveredserver nodes. Note: This operation adds nodes but does not remove them. Use [`--writer-hg`] option may be used to specify which Galera hostgroup to update. The `--remove-all-servers` option instructs to remove all servers from the mysql_servers table before updating the cluster.

### Hostgroup options on the command-line

Hostgroups can now be set with command-line options:

* `--writer-hg`


* `--reader-hg`

* `--backup-writer-hg`

* `--offline-hg`.  

These options were previously only available through the configuration file.

### Combined use of  `--enable` and `--update-cluster`

When used together:

* If the cluster is not yet enabled, then `--enable` is
  executed. 
  
* If the cluster is already enabled, then `--update-cluster` is executed.

### `--is-enabled` 

Checks whether a cluster has been enabled by querying the `mysql_galera_hostgroups` table. Optionally, use the `--writer-hg` option to specify the writer hostgroup for the lookup.


### `--status` 

Displays the current Galera hostgroup configuration. This option lists all rows in the current `mysql_galera_hostgroups` table, along with the servers assigned to each hostgroup.  

Use the `--writer-hg` option to limit the result to a specific hostgroup.

### `--login-file`

Reads login credentials from an encrypted file.  
If neither `--login-password` nor `--login-password-file` is specified, the user is prompted to enter the decryption password interactively.

### `--login-password`

Specifies the decryption key used to unlock the credentials stored in the `--login-file`.  
This option is mutually exclusive with `--login-password-file`.

### `--login-password-file`

Reads the decryption key from a file located at the specified path.  
This option is mutually exclusive with `--login-password`.

## Changed features

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

### Asynchronous slave reader support

The `--include-slaves` option is no longer supported. Asynchronous slave reader support has been removed.

### Node priority lists

ProxySQL v2 no longer supports specifying a list of nodes in priority order. Only a single node is supported.

### Automatic cluster membership updates

Cluster membership is no longer updated automatically. The `galera_proxysql_checker` and `galera_node_monitor` scripts are no longer run in the scheduler.

### `pxc_maint_mode` check

The check for the `pxc_maint_mode` variable has been removed and is no longer supported.

### Desynced node fallback

Falling back to desynced nodes when no synced nodes are available is no longer supported.

### Server status tracking in `mysql_servers`

The `mysql_servers` table no longer maintains server status information.

## Limitations

* With `--writers-as-readers=backup` read-only nodes are not allowed. This is a limitation of ProxySQL. Note that backup is the default value of `--writers-as-readers` when `--mode=singlewrite`
