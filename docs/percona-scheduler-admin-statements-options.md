# Percona Scheduler Admin statements and options

## Statement reference

The standard percona-scheduler-admin statement includes
`percona-scheduler-admin --config-file=<configuration file name and
extension>`. A Percona Scheduler Admin example statement has the following syntax:

```{.text .no-copy}
percona-scheduler-admin --config-file=config.toml [option] [option]
```

If you do not include the configuration file in the command, the result is an error and nothing happens.

```{.text .no-copy}
$ percona-scheduler-admin --debug
ERROR : The --config-file option is required but is missing from the command.
```

The options determine what the statement does. The percona-scheduler-admin statement must include at least one option. A command without an option returns an error and nothing happens.

For most options, two hyphens (–) precede an option name. The [disable](percona-scheduler-admin-options-detail.md#disable-d) and [enable](percona-scheduler-admin-options-detail.md#enable-e) option can be selected with one hyphen (-) and the appropriate abbreviation.

For example, the following commands return the same result:

```{.bash data-prompt="$"}
$ percona-scheduler-admin --config-file=config.toml -e

$ percona-scheduler-admin --config-file=config.toml --enable
```

You can combine some options with other, optional options to modify the statement’s behavior. Multiple options are separated by a space. You can combine the options in any order.

An example of combining options in one statement:

```{.bash data-prompt="$"}
$ percona-scheduler-admin --config-file=config.toml --write-node=127.0.0.1:4130 --update-cluster
```

For some options, they must be combined with a required option to return a result.

An example of an option combined with a required option:

```{.bash data-prompt="$"}
$ percona-scheduler-admin --config-file=config.toml --force -e
```

If you do not combine the option with the required option, the statement does not run and returns an error.

```{.bash data-prompt="$"}
$ percona-scheduler-admin --config-file=tests/testsuite.toml  --update-write-weight="127.0.0.1:33,112"
```

??? example "Expected output"

    ```{.text .no-copy}
    ERROR : --update-write-weight requires --update-cluster.
    ```

Specific options, such as -–write-node or –-server, require a value.

```{.bash data-prompt="$>"}
$> percona-scheduler-admin --config-file=config.toml --server=192.168.56.32:3306
```

## Option reference

|Option name|Acceptable values|Other options|Mode|Description|
|--- |--- |--- |--- |--- |
|–add-query-rule||Requires either: –syncusers or –sync-multi-cluster-users|Requires:singlewrite|Creates query rules for the synced mysql user. See add-query-rule for details.|
|–adduser||||Adds the Percona XtraDB Cluster application user to the ProxySQL database. See adduser for more details.`|
|–auto-assign-weights||Requires: –update-cluster|Requires: singlewrite|Auto-assigns weights. See auto-assign-weights for details.|
|--config-file|<config.toml>|||Reads login credentials from a configuration file. Command-line options override configuration file values. For more information, see Percona Scheduler Admin configuration file.|
|--debug||||Enables additional debug logging.|
|–disable or -d||||Removes any Percona XtraDB Cluster configurations from ProxySQL. See disable for more details.|
|--disable-updates||||Disables admin updates for ProxySQL cluster for the current operation by setting the values to false. The default setting does not change the admin variable settings.|
|–enable or -e||||Configures, without manual intervention, the Percona XtraDB Cluster nodes into ProxySQL. See enable for more details.|
|--force||Requires at least one of the following options: –enable, –disable, –update-cluster, –is-enabled, –adduser, –syncusers, –sync-multi-cluster-users, or –update-mysql-version||Skips any mysql_servers table, mysql_users table, and mysql_galera_hostgroups table configuration checks. Certain checks issue warnings instead of errors.|
|--help||||Displays the help text.|
|is-enabled||||Checks if the current configuration is enabled in ProxySQL. See is-enabled for more details.|
|--remove-all-servers||Requires:–update-cluster||Removes all servers belonging to the current cluster before updating the list.|
|–status||||Returns a status report on the current configuration. See status for more details.|
|–server|IPADDRESS:PORT|Optional: –syncusers or –sync-multi-cluster-users||Specifies the IP address and port for a single server. This option can be combined with –syncusers or –sync-multi-cluster-users to sync a single non-cluster server node.|
|sync-multi-cluster-users||Optional: –enable, –server||Syncs the user accounts currently configured in MySQL to ProxySQL. Combine with the –server option to a sync to a single server. Does not delete ProxySQL users not in MySQL. See sync-multi-cluster-users for more details.|
|–syncusers||Optional: –enable, –server||Syncs the user accounts currently configured in MySQL to ProxySQL. Use with the –server option to specify a single server to sync. Deletes ProxySQL users not in MySQL. See –syncusers for more details.|
|--trace||||Enables shell-level tracing for this shell script.|
|–update-cluster||||Updates the cluster membership, adds new cluster nodes to the configuration. See update-cluster for more details.|
|update-mysql-version||||Updates the mysql server version variable in ProxySQL based on the node version. See :ref:`update-mysql-version <psa-update-mysql-v>`for more details.|
|update-read-weight|IP:PORT,WEIGHT|Requires:update-cluster||Assigns the specified read weight to the given node. See update-read-weight for more details.|
|update-write-weight|IP:PORT,WEIGHT|Requires:update-cluster||Assigns the specified write weight to the given node. See update-write-weight for more details.|
|--use-stdin-for-credentials||||Uses stdin to send credentials to the MySQL client instead of process substitution. The default setting disables the option and uses process substitution.|
|--version or  -v||||Prints the version information.|
|–write-node|IPADDRESS:PORT||Requires:singlewrite|Specifies the node to be used for writes for singlewrite mode. If left unspecified, the cluster node is the write node.|
