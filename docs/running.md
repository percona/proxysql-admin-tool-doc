# Running ProxySQL Admin

It is recommended to change default ProxySQL credentials before running
ProxySQL in production. Make sure that you provide location and
credentials in the configuration file.

Provide superuser credentials for one of the nodes. The script will
detect other nodes in the cluster automatically.

To view the usage information, run `proxysql-admin` without any options:

```text
Usage: proxysql-admin [ options ]
Options:

--config-file=<config-file>       Read login credentials from a configuration file
                                   (command line options override any configuration file values)
--login-file=<login-file-path>    Read login credentials from an encrypted
                                   file. If the `--login-password`
                                   or `--login-password-file` options are
                                   not specified, the user is prompted for
                                   the password. Command line options
                                   override any login login file values.
--login-password=<password>       The key used to decrypt the encrypted
                                   login-file. This option cannot be
                                   used with `--login-password-file`.
--login-password-file=<path>       Reads the key from a file using the
                                   <path>. This option cannot be
                                   used with `--login-password`.
--writer-hg=<number>               The hostgroup that all traffic will be sent to
                                   by default. Nodes that have 'read-only=0' in MySQL
                                   will be assigned to this hostgroup.
--backup-writer-hg=<number>        If the cluster has multiple nodes with 'read-only=0'
                                   and max_writers set, then additional nodes (in excess
                                   of max_writers), will be assigned to this hostgroup.
--reader-hg=<number>               The hostgroup that read traffic should be sent to.
                                   Nodes with 'read-only=0' in MySQL will be assigned
                                   to this hostgroup.
--offline-hg=<number>              Nodes that are determined to be OFFLINE will
                                   assigned to this hostgroup.

--proxysql-datadir=<datadir>       Specify the proxysql data directory location
--proxysql-username=<user_name>    ProxySQL service username
--proxysql-password[=<password>]   ProxySQL service password
--proxysql-port=<port_num>         ProxySQL service port number
--proxysql-hostname=<host_name>    ProxySQL service hostname

--cluster-username=<user_name>     Percona XtraDB Cluster node username
--cluster-password[=<password>]    Percona XtraDB Cluster node password
--cluster-port=<port_num>          Percona XtraDB Cluster node port number
--cluster-hostname=<host_name>     Percona XtraDB Cluster node hostname

--cluster-app-username=<user_name> Percona XtraDB Cluster node application username
--cluster-app-password[=<password>] Percona XtraDB Cluster node application passwrod
--without-cluster-app-user         Configure Percona XtraDB Cluster without application user

--monitor-username=<user_name>     Username for monitoring Percona XtraDB Cluster nodes through ProxySQL
--monitor-password[=<password>]    Password for monitoring Percona XtraDB Cluster nodes through ProxySQL
--use-existing-monitor-password    Do not prompt for a new monitor password if one is provided.

--node-check-interval=<NUMBER>     The interval at which the proxy should connect
                                   to the backend servers in order to monitor the
                                   Galera staus of a node (in milliseconds).
                                   (default: 5000)
--mode=[loadbal|singlewrite]       ProxySQL read/write configuration mode
                                   currently supporting: 'loadbal' and 'singlewrite'
                                   (default: 'singlewrite')
--write-node=<IPADDRESS>:<PORT>    Specifies the node that is to be used for
                                   writes for singlewrite mode.  If left unspecified,
                                   the cluster node is then used as the write node.
                                   This only applies when 'mode=singlewrite' is used.
--max-connections=<NUMBER>         Value for max_connections in the mysql_servers table.
                                   This is the maximum number of connections that
                                   ProxySQL will open to the backend servers.
                                   (default: 1000)
--max-transactions-behind=<NUMBER> Determines the maximum number of writesets a node
                                   can have queued before the node is SHUNNED to avoid
                                   stale reads.
                                   (default: 100)
--use-ssl=[yes|no]                 If set to 'yes', then connections between ProxySQL
                                   and the backend servers will use SSL.
                                   (default: no)
--writers-are-readers=[yes|no|backup]
                                   If set to 'yes', then all writers (backup-writers also)
                                   are added to the reader hostgroup.
                                   If set to 'no', then none of the writers (backup-writers also)
                                   will be added to the reader hostgroup.
                                   If set to 'backup', then only the backup-writers
                                   will be added to the reader hostgroup.
                                   (default: backup)
--remove-all-servers               When used with --update-cluster, this will remove all
                                   servers belonging to the current cluster before
                                   updating the list.
--debug                            Enables additional debug logging.
--help                             Displays this help text.
```


The following options are the possible operations for `proxysql-admin`.
Provide one of the following options:

```text
--adduser                          Adds the Percona XtraDB Cluster application user to the ProxySQL database
--disable, -d                      Remove any Percona XtraDB Cluster configurations from ProxySQL
--enable, -e                       Auto-configure Percona XtraDB Cluster nodes into ProxySQL
--update-cluster                   Updates the cluster membership, adds new cluster nodes
                                   to the configuration.
--update-mysql-version             Updates the `mysql-server_version` variable in ProxySQL with the version
                                   from a node in the cluster.
--quick-demo                       Setup a quick demo with no authentication
--syncusers                        Sync user accounts currently configured in MySQL to ProxySQL
                                   May be used with --enable.
                                   (deletes ProxySQL users not in MySQL)
--sync-multi-cluster-users         Sync user accounts currently configured in MySQL to ProxySQL
                                   May be used with --enable.
                                   (doesn't delete ProxySQL users not in MySQL)
--add-query-rule                   Create query rules for synced mysql user. This is applicable only
                                   for singlewrite mode and works only with --syncusers
                                   and --sync-multi-cluster-users options
--is-enabled                       Checks if the current configuration is enabled in ProxySQL.
--status                           Returns a status report on the current configuration.
                                   If "--writer-hg=<NUM>" is specified, than the
                                   data corresponding to the Galera cluster with that
                                   writer hostgroup is displayed. Otherwise, information
                                   for all clusters will be displayed.
--force                            This option will skip existing configuration checks in mysql_servers,
                                   mysql_users and mysql_galera_hostgroups tables. This option will only
                   work with ``proxysql-admin --enable``.
--disable-updates                  Disable admin updates for ProxySQL cluster for the
                                   current operation. The default is to not change the
                                   admin variable settings.  If this option is specified,
                                   these options will be set to false.
                                   (default: updates are not disabled)
--version, -v                      Prints the version info
```

For details about using these options see [Running ProxySQL Admin](running.md)


`--enable`


This option creates the entry for the Galera hostgroups and adds the
nodes to ProxySQL.

It will also add two new users into the Percona XtraDB Cluster with the
USAGE privilege; one is for monitoring the cluster nodes through
ProxySQL, and another is for connecting to the PXC Cluster node via the
ProxySQL console.

```bash
 sudo proxysql-admin --config-file=/etc/proxysql-admin.cnf --enable
```

Output

```text
This script will assist with configuring ProxySQL for use with
Percona XtraDB Cluster (currently only PXC in combination
with ProxySQL is supported)

ProxySQL read/write configuration mode is singlewrite

Configuring the ProxySQL monitoring user.
ProxySQL monitor user name as per command line/config-file is monitor

User 'monitor'@'127.%' has been added with USAGE privileges

Configuring the Percona XtraDB Cluster application user to connect through ProxySQL
Percona XtraDB Cluster application user name as per command line/config-file is proxysql_user

Percona XtraDB Cluster application user 'proxysql_user'@'127.%' has been added with ALL privileges, this user is created for testing purposes
Adding the Percona XtraDB Cluster server nodes to ProxySQL

Write node info
+-----------+--------------+-------+--------+
| hostname  | hostgroup_id | port  | weight |
+-----------+--------------+-------+--------+
| 127.0.0.1 | 10           | 26100 | 1000   |
+-----------+--------------+-------+--------+

ProxySQL configuration completed!

ProxySQL has been successfully configured to use with Percona XtraDB Cluster

You can use the following login credentials to connect your application through ProxySQL

mysql --user=proxysql_user -p --host=localhost --port=6033 --protocol=tcp
```
You can use the following login credentials to connect your application
through ProxySQL:

```bash
mysql --user=proxysql_user -p --host=127.0.0.1 --port=6033 --protocol=tcp
mysql> select hostgroup_id,hostname,port,status from runtime_mysql_servers;
+--------------+-----------+-------+--------+
| hostgroup_id | hostname  | port  | status |
+--------------+-----------+-------+--------+
| 10           | 127.0.0.1 | 25000 | ONLINE |
| 11           | 127.0.0.1 | 25100 | ONLINE |
| 11           | 127.0.0.1 | 25200 | ONLINE |
| 12           | 127.0.0.1 | 25100 | ONLINE |
| 12           | 127.0.0.1 | 25200 | ONLINE |
+--------------+-----------+-------+--------+
5 rows in set (0.00 sec)

```
```sql
    mysql> select * from mysql_galera_hostgroups\G
    writer_hostgroup: 10
    backup_writer_hostgroup: 12
    reader_hostgroup: 11
    offline_hostgroup: 13
    active: 1
    max_writers: 1
    writer_is_also_reader: 2
    max_transactions_behind: 100
    comment: NULL
    1 row in set (0.00 sec)
```

The `--enable` command can be combined with `--update-cluster`. If
the cluster has not been configured, the `--enable` function is run or the `--update-cluster` function is run on a configured cluster.

`--disable`


This option removes Percona XtraDB Cluster nodes from ProxySQL and stops the ProxySQL monitoring daemon.

```bash
proxysql-admin --config-file=/etc/proxysql-admin.cnf --disable
Removing cluster application users from the ProxySQL database.
Removing cluster nodes from the ProxySQL database.
Removing query rules from the ProxySQL database if any.
Removing the cluster from the ProxySQL database.
ProxySQL configuration removed!
```

A specific Galera cluster can be disabled by using the `--writer-hg`
option with `--disable`.


`--adduser`

This option adds the Cluster application user to the
ProxySQL database for you.

```bash
proxysql-admin --config-file=/etc/proxysql-admin.cnf --adduser
Adding Percona XtraDB Cluster application user to ProxySQL database
Enter Percona XtraDB Cluster application user name: root
Enter Percona XtraDB Cluster application user password:
Added Percona XtraDB Cluster application user to ProxySQL database!
```


`--syncusers`


This option syncs the user accounts that are currently configured in Percona
XtraDB Cluster with the ProxySQL database except for user accounts without password and admin users. The option also deletes ProxySQL users not in Percona XtraDB Cluster from the ProxySQL database.

```bash
/usr/bin/proxysql-admin --syncusers
Syncing user accounts from Percona XtraDB Cluster to ProxySQL
Synced Percona XtraDB Cluster users to the ProxySQL database!
```

**From ProxySQL DB**

```sql
mysql> select username from mysql_users;
+---------------+
| username      |
+---------------+
| monitor       |
| one           |
| proxysql_user |
| two           |
+---------------+
4 rows in set (0.00 sec)
```

**From PXC**

```sql
mysql> select user,host from mysql.user where authentication_string!='' and user not in ('admin','mysql.sys');
+---------------+-------+
| user          | host  |
+---------------+-------+
| monitor       | 192.% |
| proxysql_user | 192.% |
| two           | %     |
| one           | %     |
+---------------+-------+
4 rows in set (0.00 sec)
```

--sync-multi-cluster-users

This option works in the same way as `--syncusers` but does not delete
ProxySQL users that are not present in the Percona XtraDB Cluster. Use this option when syncing ProxySQL instances that manage multiple
clusters.

--add-query-rule

Create query rules for synced mysql user. This is applicable only for
`--singlewrite` mode and works only with the `--syncusers` and the
`--sync-multi-cluster-users` options.

```text
Syncing user accounts from PXC to ProxySQL

Note : 'admin' is in proxysql admin user list, this user cannot be added to ProxySQL
-- (For more info, see https://github.com/sysown/proxysql/issues/709)
Adding user to ProxySQL: test_query_rule
Added query rule for user: test_query_rule

Synced PXC users to the ProxySQL database!
```

--quick-demo

This option creates a dummy proxysql configuration.

```bash
sudo  proxysql-admin --quick-demo
You have selected the dry test run mode. WARNING: This will create a test user (with all privileges) in the Percona XtraDB Cluster & ProxySQL installations.
You may want to delete this user after you complete your testing!
Would you like to proceed with '--quick-demo' [y/n] ? y
Setting up proxysql test configuration!

Do you want to use the default ProxySQL credentials (admin:admin:6032:127.0.0.1) [y/n] ? y
Do you want to use the default Percona XtraDB Cluster credentials (root::3306:127.0.0.1) [y/n] ? n

Enter the Percona XtraDB Cluster username (super user): root
Enter the Percona XtraDB Cluster user password:
Enter the Percona XtraDB Cluster port: 25100
Enter the Percona XtraDB Cluster hostname: localhost

ProxySQL read/write configuration mode is singlewrite

Configuring ProxySQL monitoring user..

User 'monitor'@'127.%' has been added with USAGE privilege
Configuring the Percona XtraDB Cluster application user to connect through ProxySQL
Percona XtraDB Cluster application user 'pxc_test_user'@'127.%' has been added with ALL privileges, this user is created for testing purposes
Adding the Percona XtraDB Cluster server nodes to ProxySQL

ProxySQL configuration completed!

ProxySQL has been successfully configured to use with Percona XtraDB Cluster

You can use the following login credentials to connect your application through ProxySQL

mysql --user=pxc_test_user  --host=127.0.0.1 --port=6033 --protocol=tcp
```

```sql
mysql> select hostgroup_id,hostname,port,status from runtime_mysql_servers;
+--------------+-----------+-------+--------+
| hostgroup_id | hostname  | port  | status |
+--------------+-----------+-------+--------+
| 10           | 127.0.0.1 | 25000 | ONLINE |
| 11           | 127.0.0.1 | 25100 | ONLINE |
| 11           | 127.0.0.1 | 25200 | ONLINE |
| 12           | 127.0.0.1 | 25100 | ONLINE |
| 12           | 127.0.0.1 | 25200 | ONLINE |
+--------------+-----------+-------+--------+
5 rows in set (0.00 sec)
```

`--update-cluster`


This option checks the Percona XtraDB Cluster for new
nodes in the cluster and add the nodes to
ProxySQL. Offline nodes are not removed from the cluster by default.

If used with `--remove-all-servers`, then the server list for this
configuration is removed before running the update cluster
function.

A specific Galera cluster can be updated by using the `--writer-hg`
option with `--update-cluster`. Otherwise, the cluster specified in the
config file is updated.

If `--write-node` is used with `--update-cluster`, then that node is made the writer node, if the node is in the server list and is online, giving this node a larger weight. This should only be used if the mode
is `singlewrite`.

```bash
sudo proxysql-admin --update-cluster --writer-hg=10 --remove-all-servers
Removing all servers from ProxySQL
Cluster node (127.0.0.1:25000) does not exist in ProxySQL, adding to the writer hostgroup(10)
Cluster node (127.0.0.1:25100) does not exist in ProxySQL, adding to the writer hostgroup(10)
Cluster node (127.0.0.1:25200) does not exist in ProxySQL, adding to the writer hostgroup(10)
Waiting for ProxySQL to process the new nodes...

Cluster node info
+---------------+-------+-----------+-------+-----------+
| hostgroup     | hg_id | hostname  | port  | weight    |
+---------------+-------+-----------+-------+-----------+
| writer        | 10    | 127.0.0.1 | 25000 | 1000      |
| reader        | 11    | 127.0.0.1 | 25100 | 1000      |
| reader        | 11    | 127.0.0.1 | 25200 | 1000      |
| backup-writer | 12    | 127.0.0.1 | 25100 | 1000      |
| backup-writer | 12    | 127.0.0.1 | 25200 | 1000      |
+---------------+-------+-----------+------+------------+

Cluster membership updated in the ProxySQL database!
```

--is-enabled

This option checks if a Galera cluster specified by the writer
hostgroup, either from `--writer-hg` or from the config file has any
active entries in the `mysql_galera_hostgroups` table in ProxySQL.

|Value   | Returned Value  |
|---|---|
| 0 | An entry corresponding to the writer hostgroup and is set to *active* in ProxySQL.  |
| 1 |  No entry corresponding to the writer hostgroup.  |
| 2 |  An entry corresponding to the writer hostgroup but is not active. |
  Value   Returned Value


```bash
 sudo proxysql-admin --is-enabled --writer-hg=10
The current configuration has been enabled and is active

 sudo proxysql-admin --is-enabled --writer-hg=20
ERROR (line:2925) : The current configuration has not been enabled
```


--status


Displays information about all Galera hostgroups and their servers that are
supported by this ProxySQL instance, unless it is used with the
`--writer-hg` option, which displays information about the given Galera
cluster which uses that writer hostgroup. .

```bash
 sudo proxysql-admin --status --writer-hg=10
mysql_galera_hostgroups row for writer-hostgroup: 10
+--------+--------+---------------+---------+--------+-------------+-----------------------+------------------+
| writer | reader | backup-writer | offline | active | max_writers | writer_is_also_reader | max_trans_behind |
+--------+--------+---------------+---------+--------+-------------+-----------------------+------------------+
| 10     | 11     | 12            | 13      | 1      | 1           | 2                     | 100              |
+--------+--------+---------------+---------+--------+-------------+-----------------------+------------------+

mysql_servers rows for this configuration
+---------------+-------+-----------+-------+--------+-----------+----------+---------+-----------+
| hostgroup     | hg_id | hostname  | port  | status | weight    | max_conn | use_ssl | gtid_port |
+---------------+-------+-----------+-------+--------+-----------+----------+---------+-----------+
| writer        | 10    | 127.0.0.1 | 25000 | ONLINE | 1000000   | 1000     | 0       | 0         |
| reader        | 11    | 127.0.0.1 | 25100 | ONLINE | 1000      | 1000     | 0       | 0         |
| reader        | 11    | 127.0.0.1 | 25200 | ONLINE | 1000      | 1000     | 0       | 0         |
| backup-writer | 12    | 127.0.0.1 | 25100 | ONLINE | 1000      | 1000     | 0       | 0         |
| backup-writer | 12    | 127.0.0.1 | 25200 | ONLINE | 1000      | 1000     | 0       | 0         |
+---------------+-------+-----------+-------+--------+-----------+----------+---------+-----------+
```

--force


Skips the existing configuration checks with the `--enable` option in
mysql\_servers table, mysql\_users table, and mysql\_galera\_hostgroups table.

--update-mysql-version

This option updates the mysql server version specified by the writer
hostgroup, either from `--writer-hg` or the config file in proxysql
db-based on the online writer node.

```bash
  sudo proxysql-admin --update-mysql-version --writer-hg=10
ProxySQL MySQL version changed to 5.7.26
```
