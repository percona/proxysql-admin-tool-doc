# The proxysql-admin functions

The script has the following functions.

## --enable

This option creates the entry for the Galera hostgroups and adds the **Percona XtraDB Cluster** nodes to ProxySQL.

It adds two new users into the Percona XtraDB Cluster with the USAGE
privilege; one monitors the cluster nodes through ProxySQL, and the other connects to the PXC Cluster node through the ProxySQL console.

```bash
$ sudo proxysql-admin --config-file=/etc/proxysql-admin.cnf --enable
```

### Output

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

      Percona XtraDB Cluster application user 'proxysql_user'@'127.%' has been added with ALL privileges, 
      this user is created for testing purposes
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

You can use the following login credentials to connect your application through
ProxySQL:

```sql
$ mysql --user=proxysql_user -p --host=127.0.0.1 --port=6033 --protocol=tcp
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

The `--enable` command can be used with `--update-cluster`.  If the
cluster has not been setup, then the enable function is run.  If the
cluster has been setup, then the update cluster function runs.

## --disable

This option removes **Percona XtraDB Cluster** nodes from *ProxySQL* and stop
the *ProxySQL* monitoring daemon.

```bash
$ proxysql-admin --config-file=/etc/proxysql-admin.cnf --disable
Removing cluster application users from the ProxySQL database.
Removing cluster nodes from the ProxySQL database.
Removing query rules from the ProxySQL database if any.
Removing the cluster from the ProxySQL database.
ProxySQL configuration removed!
```

A specific Galera cluster can be disabled by using the –writer-hg option with
`--disable`.

## --adduser

This option will aid with adding the Cluster application user to the ProxySQL
database for you

```bash
$ proxysql-admin --config-file=/etc/proxysql-admin.cnf --adduser
Adding Percona XtraDB Cluster application user to ProxySQL database
Enter Percona XtraDB Cluster application user name: root
Enter Percona XtraDB Cluster application user password:
Added Percona XtraDB Cluster application user to ProxySQL database!
```

## --syncusers

This option will sync user accounts currently configured in Percona XtraDB Cluster with the ProxySQL database except for password-less users and admin users. It also deletes ProxySQL users not in Percona XtraDB Cluster from the ProxySQL database.

```bash
$ /usr/bin/proxysql-admin --syncusers
Syncing user accounts from Percona XtraDB Cluster to ProxySQL
Synced Percona XtraDB Cluster users to the ProxySQL database!
```

## From ProxySQL DB

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

### From PXC

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

## –-sync-multi-cluster-users

This option works in the same way as –syncusers but does not delete ProxySQL
users that are not present in the Percona XtraDB Cluster. Used this option when
syncing proxysql instances that manage multiple clusters.

## –-add-query-rule

Create query rules for synced mysql user. This is applicable only for
singlewrite mode and works only with `--syncusers`
and `–-sync-multi-cluster-users` options.

```bash
Syncing user accounts from PXC to ProxySQL

Note : 'admin' is in proxysql admin user list, this user cannot be added to ProxySQL
-- (For more info, see https://github.com/sysown/proxysql/issues/709)
Adding user to ProxySQL: test_query_rule
Added query rule for user: test_query_rule

Synced PXC users to the ProxySQL database!
```

## –-quick-demo

This option configures a dummy proxysql configuration.

```bash
$ sudo  proxysql-admin --quick-demo
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

## --update-cluster

This option will check the Percona XtraDB Cluster to see if any new nodes have
joined the cluster.  If so, the new nodes are added to ProxySQL.  Any offline
nodes are not removed from the cluster by default.

If used with `--remove-all-servers`, then the server list for this configuration
will be removed before running the update cluster function.

A specific Galera cluster can be updated by using the `--writer-hg` option
with `--update-cluster`.  Otherwise, the cluster specified in the config file
will be updated.

If `--write-node` is used with `--update-cluster`, then that node will
be made the writer node (by giving it a larger weight), if the node is in
the server list and is ONLINE.  This should only be used if the mode is *singlewrite*.

```bash
$ sudo proxysql-admin --update-cluster --writer-hg=10 --remove-all-servers
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

## –-is-enabled

This option checks if a Galera cluster (specified by the writer hostgroup,
either from `--writer-hg` or from the config file) has any active entries
in the `mysql_galera_hostgroups` table in ProxySQL.

|Value|Returned Value|
|--- |--- |
|0|An entry corresponding to the writer hostgroup and is set to active in ProxySQL.|
|1|No entry corresponding to the writer hostgroup.|
|2|An entry corresponding to the writer hostgroup but is not active.|

```bash
$ sudo proxysql-admin --is-enabled --writer-hg=10
The current configuration has been enabled and is active

$ sudo proxysql-admin --is-enabled --writer-hg=20
ERROR (line:2925) : The current configuration has not been enabled
```

## --status

Displays information about all Galera hostgroups and their servers being
supported by this ProxySQL instance, unless it is used with the `--writer-hg` option, which displays information about the
given Galera cluster which uses that writer hostgroup.

```bash
$ sudo proxysql-admin --status --writer-hg=10
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

## --force

Skips the existing configuration checks with the `--enable` option in
mysql_servers, mysql_users, and mysql_galera_hostgroups tables.

## –-update-mysql-version

This option updates the mysql server version (specified by the writer
hostgroup, either from `--writer-hg` or the config file) in proxysql db-based
on the online writer node.

```bash
$  sudo proxysql-admin --update-mysql-version --writer-hg=10
ProxySQL MySQL version changed to 5.7.26
```

### Extra options

## –-mode

This option allows you to set up the read/write mode for PXC cluster nodes in
the ProxySQL database based on the hostgroup. For now, the only supported modes
are singlewrite and loadbal. The singlewrite option is the default mode, and configures Percona XtraDB Cluster to only accept writes on a single node.
Depending on the `--writers-are-readers` value, the write node may
accept read requests. All other remaining nodes are read-only and only receive read statements.

With the `--write-node` option we control which node ProxySQL uses as
the writer node. The writer node is specified as the address:port -
**10.0.0.51:3306** If `--write-node` is used, the writer node is given a weight of
**1000000** (the default weight is **1000**).

The loadbal mode is a load balanced set of evenly weighted read/write nodes.

### singlewrite mode setup

```bash
$ sudo grep "MODE" /etc/proxysql-admin.cnf
$ export MODE="singlewrite"
$ sudo proxysql-admin --config-file=/etc/proxysql-admin.cnf --write-node=127.0.0.1:25000 --enable
ProxySQL read/write configuration mode is singlewrite
[..]
ProxySQL configuration completed!
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

### loadbal mode setup

```bash
$ sudo proxysql-admin --config-file=/etc/proxysql-admin.cnf --mode=loadbal --enable
This script assists with configuring ProxySQL (currently only Percona XtraDB Cluster in combination with ProxySQL is supported)

ProxySQL read/write configuration mode is loadbal
[..]
ProxySQL has been successfully configured to use with Percona XtraDB Cluster

You can use the following login credentials to connect your application through ProxySQL.

$ mysql --user=proxysql_user --password=*****  --host=127.0.0.1 --port=6033 --protocol=tcp

mysql> select hostgroup_id,hostname,port,status from runtime_mysql_servers;
+--------------+-----------+-------+--------+
| hostgroup_id | hostname  | port  | status |
+--------------+-----------+-------+--------+
| 10           | 127.0.0.1 | 25000 | ONLINE |
| 10           | 127.0.0.1 | 25100 | ONLINE |
| 10           | 127.0.0.1 | 25200 | ONLINE |
+--------------+-----------+-------+--------+
3 rows in set (0.01 sec)
```

## –-node-check-interval

This option configures the interval for the cluster node health monitoring by
ProxySQL (in milliseconds). This is a global variable and is used by all
clusters that are being served by this ProxySQL instance. This can only be
used with `--enable`.

```bash
$ proxysql-admin --config-file=/etc/proxysql-admin.cnf --node-check-interval=5000 --enable
```

## –-write-node

This option is used to choose which node will be the writer node when the mode
is singlewrite. This option can be used with –enable and –update-cluster.

A single IP address and port combination is expected. For example,
“–write-node=127.0.0.1:3306”

### The proxysql-status script

The *proxysql-status* is a simple script to dump the ProxySQL configuration
and statistics.

```{.bash data-prompt="$"}
$ proxysql-status admin admin 127.0.0.1 6032
```

The default behavior is to display all tables and files. By using the following options, you can retrieve more specific information:

|Option|Use to display|
|--- |--- |
|–files|The contents of proxysql-admin related files|
|–main|Main tables (both on-disk and runtime)|
|–monitor|Monitor tables|
|–runtime|Runtime-related data (implies –main)|
|–stats|Stats tables|
|–table=<table_name>|Only tables that contain the table name (a case-sensitive match)|
|–with-stats-reset|_reset tables, by default _reset tables will not be queried.|

!!! note

    If no credentials are specified, the credentials in
    `/etc/proxysql-admin.cnf` are used.
