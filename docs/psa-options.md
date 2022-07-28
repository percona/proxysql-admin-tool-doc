# Option Details

The Percona Scheduler Admin script lists the available options in Percona Scheduler Admin configuration file. The following options are described in more detail:

| Option Name                                             |
|---------------------------------------------------------|
| [--add-query-rule](#add-query-rule)                     |
| [--adduser](#adduser)                                   |
| [--auto-assign-weights](#auto-assign-weights)           |
| [--disable/-d](#-disable---d)                           |
| [--enable/-e](#–enable---e)                             |
| [--force](#–force)                                      |
| [--is-enabled](#–is-enabled)                            |
| [--remove-all-servers](#remove-all-servers)             |
| [--server](#server)                                     |
| [--status](#status)                                     |
| [--sync-multi-cluster-users](#sync-multi-cluster-users) |
| [--syncusers](#syncusers)                               |
| [--update-cluster](#update-cluster)                     |
| [--update-mysql-version](#update-mysql-version)         |
| [--update-read-weight](#update-read-weight)             |
| [--update-write-weight](#update-write-weight)           |
| [--write-node](#write-node)                             |

## –add-query-rule

This option creates query rules for a synced mysql user and applies only to the
`singlewrite` mode.

### Requires

Either the –syncusers or –sync-multi-cluster-users options.

```shell
$ percona-scheduler-admin --config-file=config.toml --syncusers
```

The output should be similar to the following:

```text
--add-query-rule

Syncing user accounts from PXC to ProxySQL

Note : 'admin' is in proxysql admin user list, this user cannot be added to ProxySQL
-- (For more info, see https://github.com/sysown/proxysql/issues/709)
Adding user to ProxySQL: test_query_rule
Added query rule for user: test_query_rule
Adding user to ProxySQL: test_query_rule
  Added query rule for user: test_query_rule

Synced PXC users to the ProxySQL database!
```

## –adduser

This option adds the cluster application user account to the ProxySQL database.

```shell
$> percona-scheduler-admin --config-file=config.toml --adduser
```
The output should be similar to the following:

```text 
Adding PXC application user to the ProxySQL database
Enter the PXC application user name: cluster_one
Enter the PXC application user password:


The application user 'cluster_one' does not exist in PXC. Would you like to proceed [y/n] ? y

Please create the user cluster_one in PXC to access the application through ProxySQL

Added PXC application user to the ProxySQL database!
```

## –auto-assign-weights

ProxySQL uses weights for defining the failover procedure in `singlewrite` mode
and handling load balancing loadbal mode.

For the failover procedure, this option with the
[--update-cluster](#update-cluster) option assigns weights to the PXC nodes when the cluster is
in `singlewrite` mode.

As a best practice, ensure that the writer node election operation returns the
same result each time. For example, assign the value of `1000` to node one,
`999` to node two, and `998` to the node three. This method sets a clear
priority for the election.

For load balancing you want to reduce the reads on the writer node and, also,
split the reads across all the reader nodes equally.

For example, in a three-node cluster, assign a `900` to the writer node and
`1000` and `1000` to the reader nodes.

This option does these operations automatically without any manual intervention.

**WARNING**: See Do not combine the following options for information on options that should not be
in the same statement.

The following example is a default configuration when the
`percona-scheduler-admin` sets up proxysql.

```sql
Cluster node info
+---------------+-------+---------------+------+--------+--------+
| hostgroup     | hg_id | hostname      | port | status | weight |
+---------------+-------+---------------+------+--------+--------+
| writer        | 100   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.34 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.34 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.34 | 3306 | ONLINE | 1000   |
+---------------+-------+---------------+------+--------+--------+

Cluster membership updated in the ProxySQL database!
```
An example of the command:

```shell
$> percona-scheduler-admin --config-file=config.toml --update-cluster --auto-assign-weights
```
The output should be similar to the following:
```text
No new nodes detected.
Cluster node info
+---------------+-------+---------------+------+--------+--------+
| hostgroup     | hg_id | hostname      | port | status | weight |
+---------------+-------+---------------+------+--------+--------+
| writer        | 100   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.32 | 3306 | ONLINE | 900    |
| reader        | 101   | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.34 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.34 | 3306 | ONLINE | 998    |
| writer-config | 8100  | 192.168.56.33 | 3306 | ONLINE | 999    |
| writer-config | 8100  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.32 | 3306 | ONLINE | 900    |
| reader-config | 8101  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.34 | 3306 | ONLINE | 1000   |
+---------------+-------+---------------+------+--------+--------+

Cluster membership updated in the ProxySQL database!
```

## –disable / -d

This option removes Percona XtraDB Cluster nodes from ProxySQL and stops the
ProxySQL monitoring daemon.

```shell
$ percona-scheduler-admin --config-file=config.toml --disable
```
The output should be similar to the following:

```text
Removing cluster application users from the ProxySQL database.
Removing cluster nodes from the ProxySQL database.
Removing query rules from the ProxySQL database if any.
```

## –enable / -e

This option creates entries for the Galera hostgroups and adds the Percona XtraDB Cluster nodes into ProxySQL’s mysql_servers table.

The option adds two users into the Percona XtraDB Cluster with the `USAGE`
privilege. The users have the following tasks:

* Monitor the cluster nodes through ProxySQL.

* Connect to the PXC Cluster node through the ProxySQL console.

**NOTE**: You must have `super` user credentials from Percona XtraDB Cluster
to set up the default users.

```shell
$> percona-scheduler-admin --config-file=config.toml --enable
```
The output should be similar to the following:

```text
 Configuring using mode: singlewrite

The ClusterApp User or Password was unspecified and will not be configured.

This script will assist with configuring ProxySQL for use with
 Percona XtraDB Cluster (currently only PXC in combination with ProxySQL is supported)

ProxySQL read/write configuration mode is singlewrite

Configuring the ProxySQL monitoring user.
ProxySQL monitor user name as per command line/config-file is monitor

Monitoring user 'monitor'@'127.%' has been setup in the ProxySQL database.
Adding the Percona XtraDB Cluster nodes to ProxySQL
Using the scheduler binary located at /home/venki/work/proxysql/proxysql-admin-tool/pxc_scheduler_handler

Waiting for scheduler script to process new nodes...
Proxysql status (mysql_servers rows) for this configuration
+---------------+-------+---------------+------+--------+--------+----------+---------+-----------+
| hostgroup     | hg_id | hostname      | port | status | weight | max_conn | use_ssl | gtid_port |
+---------------+-------+---------------+------+--------+--------+----------+---------+-----------+
| writer        | 100   | 192.168.56.32 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader        | 101   | 192.168.56.32 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader        | 101   | 192.168.56.33 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader        | 101   | 192.168.56.34 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| writer-config | 8100  | 192.168.56.32 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| writer-config | 8100  | 192.168.56.33 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| writer-config | 8100  | 192.168.56.34 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader-config | 8101  | 192.168.56.32 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader-config | 8101  | 192.168.56.33 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader-config | 8101  | 192.168.56.34 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
+---------------+-------+---------------+------+--------+--------+----------+---------+-----------+


ProxySQL configuration completed!

ProxySQL has been successfully configured to use with Percona XtraDB Cluster
```

You can verify the success with the following command:

```sql
mysql> select * from runtime_mysql_servers;
```
The output should be similar to the following:

```text
+--------------+---------------+------+-----------+--------+--------+-------------+-----------------+---------------------+---------+----------------+---------+
| hostgroup_id | hostname      | port | gtid_port | status | weight | compression | max_connections | max_replication_lag | use_ssl | max_latency_ms | comment |
+--------------+---------------+------+-----------+--------+--------+-------------+-----------------+---------------------+---------+----------------+---------+
| 100          | 192.168.56.32 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
| 8101         | 192.168.56.33 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
| 8101         | 192.168.56.34 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
| 8101         | 192.168.56.32 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
| 8100         | 192.168.56.33 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
| 8100         | 192.168.56.34 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
| 8100         | 192.168.56.32 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
| 101          | 192.168.56.33 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
| 101          | 192.168.56.34 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
| 101          | 192.168.56.32 | 3306 | 0         | ONLINE | 1000   | 0           | 1000            | 0                   | 0       | 0              |         |
+--------------+---------------+------+-----------+--------+--------+-------------+-----------------+---------------------+---------+----------------+---------+
10 rows in set (0.01 sec)
```
You can also run this command:

```sql
mysql> select * from scheduler\G
```
The output should be similar to the following:


```text
*************************** 1. row ***************************
         id: 6
     active: 1
interval_ms: 5000
   filename: <path/to/pxc_scheduler>/pxc_scheduler_handler
       arg1: --configfile=config.toml
       arg2: --configpath=<path/to/config/dir>
       arg3: NULL
       arg4: NULL
       arg5: NULL
    comment: { hgW:100, hgR:101 }
1 row in set (0.00 sec)
```

## –force

This option must be combined with either [--enable/-e](#–enable---e)  or [--update-cluster](#update-cluster) . This option skips any `mysql_servers`, `mysql_users`, and `mysql_galera_hostgroups` table configuration checks. Certain checks issue warnings instead of errors.

## –is-enabled

This option checks if `percona-scheduler-admin` configured the hostgroups in ProxySQL.

Returns a zero (0) if an entry corresponds to the writer hostgroup and is set to active in ProxySQL.

Returns a one (1) if an entry does not correspond to the writer hostgroup.

```shell
$> percona-scheduler-admin --config-file=config.toml --is-enabled
```
The output should be similar to the following:

```text
The current configuration has been enabled and is active
```
Verify if `percona-scheduler-admin` configured the hostgroups in ProxySQL.

```shell
$> echo $?
```
The output should be similar to the following:

```text
0
```

Disabling the cluster configuration causes the [--is-enabled](#–is-enabled)
option to throw an error.

Disabling the cluster
```shell
$ percona-scheduler-admin --config-file=config.toml --disable
```
The output should be similar to the following:

```text
Removing cluster application users from the ProxySQL database.
Removing cluster nodes from the ProxySQL database.
Removing query rules from the ProxySQL database if any.
ProxySQL configuration removed!
```
Check if the cluster is enabled:
```bash
$> percona-scheduler-admin --config-file=config.toml --is-enabled
```
The output should be similar to the following:

```text
ERROR (line:2450) : The current configuration has not been enabled
```
## –remove-all-servers

When used with [--update-cluster](#update-cluster) this option removes 
all servers belonging to the current cluster before running the 
[--update-cluster](#update-cluster) option.

```shell
$> percona-scheduler-admin --config-file=config.toml 
--remove-all-servers --udpate-cluster
```
## –server

Selects a server by the IP address and port. This option can be combined with [--syncusers](#syncusers)  or [--sync-multi-cluster-users(#sync-multi-cluster-users) to sync a single non-cluster server node.

Usage:

```shell
$> percona-scheduler-admin --config-file=config.toml --server=192.168.56.32:3306
```

## –status

This option displays information about all Galera hostgroups and their servers supported by this ProxySQL instance.

```shell
$> percona-scheduler-admin --config-file=config.toml --status
```
The output should be similar to the following:

```text
mysql_servers rows for this configuration
+---------------+-------+---------------+------+--------+--------+----------+---------+-----------+
| hostgroup     | hg_id | hostname      | port | status | weight | max_conn | use_ssl | gtid_port |
+---------------+-------+---------------+------+--------+--------+----------+---------+-----------+
| writer        | 100   | 192.168.56.32 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader        | 101   | 192.168.56.32 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader        | 101   | 192.168.56.33 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader        | 101   | 192.168.56.34 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| writer-config | 8100  | 192.168.56.32 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| writer-config | 8100  | 192.168.56.33 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| writer-config | 8100  | 192.168.56.34 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader-config | 8101  | 192.168.56.32 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader-config | 8101  | 192.168.56.33 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
| reader-config | 8101  | 192.168.56.34 | 3306 | ONLINE | 1000   | 1000     | 0       | 0         |
+---------------+-------+---------------+------+--------+--------+----------+---------+-----------+
```

## –sync-multi-cluster-users

Use this option to sync proxysql instances that manage multiple
clusters.

This option does the following:


* Syncs the currently configured *Percona XtraDB Cluster* user accounts with the ProxySQL database except for user accounts without a password and admin user accounts.


* Keeps ProxySQL users that are not present in the Percona XtraDB Cluster

To sync a specific server combine this option with the [--server](#server)  option.

## –syncusers

This option does the following:

* Syncs the currently configured *Percona XtraDB Cluster* user accounts with the ProxySQL database except for user accounts without a password and admin user accounts.

* Deletes ProxySQL user accounts that are not also in Percona XtraDB Cluster from the ProxySQL database.

To sync a specific server combine this option with the [--server](#server)  option.

Review the user accounts in the ProxySQL database as root from ProxySQL 
database.

```sql
proxysql admin#> SELECT DISTINCT username FROM mysql_users;
```
The output should be similar to the following:

```text
+----------+
| username |
+----------+
| monitor  |
+----------+
1 row in set (0.00 sec)
```

On a Percona XtraDB Cluster node, verify if a user account is already added.

```sql
mysql> SELECT user FROM mysql.user WHERE user LIKE 'test%';
```

The output should be similar to the following:

```text
Empty set (0.00 sec)
```

On the node, add a new user.

```sql
mysql> CREATE USER 'test_user'@'localhost' IDENTIFIED WITH 'mysql_native_password' by 'passw0Rd';
```
The output should be similar to the following:

```text
Query OK, 0 rows affected (0.04 sec)
```

Run percona-scheduler-admin with the `--syncusers` option

```bash
$ ./percona-scheduler-admin --config-file=config.toml --syncusers
```
The output should be similar to the following:

```text
Syncing user accounts from PXC(192.168.56.32:3306) to ProxySQL

Adding user to ProxySQL: test_user

Synced PXC users to the ProxySQL database!
```

Verify, in the ProxySQL database, that the user account has been added.

```sql
proxysql admin> SELECT DISTINCT username FROM mysql_users;
```

The output should be similar to the following:

```text
+-----------+
| username  |
+-----------+
| monitor   |
| test_user |
+-----------+
2 rows in set (0.00 sec)
```

## –update-cluster

This option checks the *Percona XtraDB Cluster* for new nodes. If nodes are
found, they are added to ProxySQL. Offline nodes are not removed from the
cluster, by default.

Combining `--remove-all-servers` with this option removes the server list
for the configuration before the update runs.

```shell
$> percona-scheduler-admin --config-file=config.toml --write-node=127.0.0.1:4130 --update-cluster
```

The output should be similar to the following:

```text
No new nodes detected.
Waiting for ProxySQL to process the new nodes...

Cluster node info
+---------------+-------+---------------+------+--------+---------+
| hostgroup     | hg_id | hostname      | port | status | weight  |
+---------------+-------+---------------+------+--------+---------+
| writer        | 100   | 192.168.56.34 | 3306 | ONLINE | 1000000 |
| reader        | 101   | 192.168.56.32 | 3306 | ONLINE | 1000    |
| reader        | 101   | 192.168.56.33 | 3306 | ONLINE | 1000    |
| reader        | 101   | 192.168.56.34 | 3306 | ONLINE | 1000    |
| writer-config | 8100  | 192.168.56.32 | 3306 | ONLINE | 1000    |
| writer-config | 8100  | 192.168.56.33 | 3306 | ONLINE | 1000    |
| writer-config | 8100  | 192.168.56.34 | 3306 | ONLINE | 1000000 |
| reader-config | 8101  | 192.168.56.32 | 3306 | ONLINE | 1000    |
| reader-config | 8101  | 192.168.56.33 | 3306 | ONLINE | 1000    |
| reader-config | 8101  | 192.168.56.34 | 3306 | ONLINE | 1000    |
+---------------+-------+---------------+------+--------+---------+

Cluster membership updated in the ProxySQL database!
```

## –update-mysql-version

This option updates the mysql server version in the proxysql db based on the online writer node.

```shell
$> percona-scheduler-admin --config-file=config.toml --update-mysql-version
```

The output should be similar to the following:

```text
ProxySQL MySQL version changed to 8.0.27
```

## –update-read-weight

Combining –update-cluster with this option assigns the specified read
weight to a node.

Usage:

The syntax for the arguments are: <IP_ADDRESS:PORT> and <New Weight>. The
<IP_ADDRESS> format can be either Internet Protocol version 4 (IPv4)
or Internet Protocol version 6 (IPv6).

```shell
$> percona-scheduler-admin --config-file=config.toml --update-cluster --update-read-weight="<IP_ADDRESS:PORT>, <New Weight>"
```


The following is the `percona-scheduler-admin` default configuration for 
*ProxySQL*.

```sql
Cluster node info
+---------------+-------+---------------+------+--------+--------+
| hostgroup     | hg_id | hostname      | port | status | weight |
+---------------+-------+---------------+------+--------+--------+
| writer        | 100   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.34 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.34 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.34 | 3306 | ONLINE | 1000   |
+---------------+-------+---------------+------+--------+--------+

Cluster membership updated in the ProxySQL database!
```

The following command assigns the weight value of `1111` to the
`192.168.56.32:3306` node in the reader and reader-config hostgroups.

```shell
$> percona-scheduler-admin --config-file=config.toml --update-cluster --update-read-weight="192.168.56.32:3306,1111"
```

The output should be similar to the following:

```text
No new nodes detected.
Waiting for scheduler script to process the nodes...

Cluster node info
+---------------+-------+---------------+------+--------+--------+
| hostgroup     | hg_id | hostname      | port | status | weight |
+---------------+-------+---------------+------+--------+--------+
| writer        | 100   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.34 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.32 | 3306 | ONLINE | 1111   |
| writer-config | 8100  | 192.168.56.34 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.34 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.32 | 3306 | ONLINE | 1111   |
+---------------+-------+---------------+------+--------+--------+

Cluster membership updated in the ProxySQL database!
```

## –update-write-weight

Combining this option with [--update-cluster](#update-cluster)  assigns the
specified write weight to a node.

Usage:

The syntax for the arguments are: <IP_ADDRESS:PORT> and <New Weight>. The
<IP_ADDRESS> format can be either Internet Protocol version 4 (IPv4)
or Internet Protocol version 6 (IPv6).

```sql
$> percona-scheduler-admin --config-file=config.toml --update-cluster --update-write-weight="<IP_ADDRESS:PORT>, <New Weight>"
```


The following is the `percona-scheduler-admin` default configuration for 
*ProxySQL*.

```sql
Cluster node info
+---------------+-------+---------------+------+--------+--------+
| hostgroup     | hg_id | hostname      | port | status | weight |
+---------------+-------+---------------+------+--------+--------+
| writer        | 100   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.34 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.34 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.34 | 3306 | ONLINE | 1000   |
+---------------+-------+---------------+------+--------+--------+

Cluster membership updated in the ProxySQL database!
```

The following command assigns the weight value of `1111` to the
`192.168.56.33:3306` node in the writer and writer-config hostgroups.

```sql
$ percona-scheduler-admin --config-file=config.toml --update-cluster --update-write-weight="192.168.56.33:3306,1111"
```

The output should be similar to the following:

```text
No new nodes detected.
Waiting for scheduler script to process the nodes...

Cluster node info
+---------------+-------+---------------+------+--------+--------+
| hostgroup     | hg_id | hostname      | port | status | weight |
+---------------+-------+---------------+------+--------+--------+
| writer        | 100   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader        | 101   | 192.168.56.34 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.34 | 3306 | ONLINE | 1000   |
| writer-config | 8100  | 192.168.56.33 | 3306 | ONLINE | 1111   |
| reader-config | 8101  | 192.168.56.32 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.33 | 3306 | ONLINE | 1000   |
| reader-config | 8101  | 192.168.56.34 | 3306 | ONLINE | 1000   |
+---------------+-------+---------------+------+--------+--------+

Cluster membership updated in the ProxySQL database!
```

## –write-node

This option chooses which Percona XtraDB Cluster node is the writer node when the mode is `singlewrite`. You can combine this option with [--enable/-e](#–enable---e) and [--update-cluster](#update-cluster).

Assigning a node with [--write-node](#write-node) gives the writer node a weight of 1000000. The default weight is 1000.

Usage:

```sql
$> percona-scheduler-admin --config-file=config.toml --write-node=192.168.56.32:3306
```

The argument syntax is a single IP address and port combination.
