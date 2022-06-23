# Configuring ProxySQL

This tutorial describes how to configure *ProxySQL* with three *Percona XtraDB Cluster* nodes.

| Node   | Host name | IP address    |
| ------ | --------- | ------------- |
| Node 1 | pxc1      | 192.168.70.61 |
| Node 2 | pxc2      | 192.168.70.62 |
| Node 3 | pxc3      | 192.168.70.63 |
| Node 4 | proxysql  | 192.168.70.64 |

*ProxySQL* can be configured either using *etc/proxysql-admin.cnf* or using the
admin interface. The admin interface can change the configuration dynamically (no need to restart the proxy).

To connect to the ProxySQL admin interface, use the `mysql` client.  You
can either connect to the admin interface from a *Percona XtraDB Cluster* node that already has the
`mysql` client installed (*Node 1*, *Node 2*, *Node 3*) or install the client on
*Node 4* and connect locally.  For this tutorial, install *Percona XtraDB Cluster* on Node 4:

* On Debian or Ubuntu:

```bash
    [root@proxysql ~]# apt-get install percona-xtradb-cluster-client
```

* On Red Hat Enterprise Linux or CentOS:

```bash
    [root@proxysql ~]# yum install percona-xtradb-cluster-client
```

To connect to the admin interface, use the credentials, host name, and port
specified in the [ProxySQL global variables](https://github.com/sysown/proxysql/blob/master/doc/global_variables.md).

**WARNING**: Do not use default credentials in production!

The following example shows how to connect to the ProxySQL admin interface
with default credentials:

```bash
root@proxysql:~# mysql -u admin -padmin -h 127.0.0.1 -P 6032

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.1.30 (ProxySQL Admin Module)

Copyright (c) 2009-2016 Percona LLC and/or its affiliates
Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql@proxysql>
```

To see the *ProxySQL* databases and tables use the following commands:

```mysql
mysql@proxysql> SHOW DATABASES;
+-----+---------+-------------------------------+
| seq | name    | file                          |
+-----+---------+-------------------------------+
| 0   | main    |                               |
| 2   | disk    | /var/lib/proxysql/proxysql.db |
| 3   | stats   |                               |
| 4   | monitor |                               |
+-----+---------+-------------------------------+
4 rows in set (0.00 sec)
```

```mysql
mysql@proxysql> SHOW TABLES;
+--------------------------------------+
| tables                               |
+--------------------------------------+
| global_variables                     |
| mysql_collations                     |
| mysql_query_rules                    |
| mysql_replication_hostgroups         |
| mysql_servers                        |
| mysql_users                          |
| runtime_global_variables             |
| runtime_mysql_query_rules            |
| runtime_mysql_replication_hostgroups |
| runtime_mysql_servers                |
| runtime_scheduler                    |
| scheduler                            |
+--------------------------------------+
12 rows in set (0.00 sec)
```

**NOTE**: ProxySQL has three areas where the configuration can reside:

* MEMORY (your current working place)

* RUNTIME (the production settings)

* DISK (durable configuration saved in a [SQLite](https://sqlite.org/index.html) database)

When you change a parameter, you change it in the MEMORY area. This method
allows you to test the changes before pushing the change to production
(RUNTIME) or to disk.

## Adding cluster nodes to *ProxySQL*

To configure the backend *Percona XtraDB Cluster* nodes in *ProxySQL*, insert the corresponding records
into the `mysql_servers` table.

**NOTE**: *ProxySQL* uses the concept of *hostgroups* to group cluster nodes. This
approach enables balancing the load in a cluster by routing different types
of traffic to different groups.

There are many ways you can configure hostgroups (for
example, master and slaves, read and write load, etc.) and a node can
be a member of multiple hostgroups.

This example adds three *Percona XtraDB Cluster* nodes to the default hostgroup (`0`),
which receives both write and read traffic:

```mysql
mysql@proxysql> INSERT INTO mysql_servers(hostgroup_id, hostname, port) VALUES (0,'192.168.70.61',3306);
mysql@proxysql> INSERT INTO mysql_servers(hostgroup_id, hostname, port) VALUES (0,'192.168.70.62',3306);
mysql@proxysql> INSERT INTO mysql_servers(hostgroup_id, hostname, port) VALUES (0,'192.168.70.63',3306);
```

To see the nodes:

```text
mysql@proxysql> SELECT * FROM mysql_servers;

+--------------+---------------+------+--------+--------+-------------+-----------------+---------------------+---------+----------------+---------+
| hostgroup_id | hostname      | port | status | weight | compression | max_connections | max_replication_lag | use_ssl | max_latency_ms | comment |
+--------------+---------------+------+--------+--------+-------------+-----------------+---------------------+---------+----------------+---------+
| 0            | 192.168.70.61 | 3306 | ONLINE | 1      | 0           | 1000            | 0                   | 0       | 0              |         |
| 0            | 192.168.70.62 | 3306 | ONLINE | 1      | 0           | 1000            | 0                   | 0       | 0              |         |
| 0            | 192.168.70.63 | 3306 | ONLINE | 1      | 0           | 1000            | 0                   | 0       | 0              |         |
+--------------+---------------+------+--------+--------+-------------+-----------------+---------------------+---------+----------------+---------+
3 rows in set (0.00 sec)
```

## Creating a *ProxySQL* Monitoring User

To enable monitoring of *Percona XtraDB Cluster* nodes in *ProxySQL*,
create a user with the `USAGE` privilege on any node in the cluster
and configure the user in ProxySQL.

The following example shows how to add a monitoring user on Node 2:

```text
mysql@pxc2> CREATE USER 'proxysql'@'%' IDENTIFIED BY 'ProxySQLPa55';
mysql@pxc2> GRANT USAGE ON *.* TO 'proxysql'@'%';
```

The following example shows how to configure this user on the ProxySQL node:

```text
mysql@proxysql> UPDATE global_variables SET variable_value='proxysql'
              WHERE variable_name='mysql-monitor_username';
mysql@proxysql> UPDATE global_variables SET variable_value='ProxySQLPa55'
              WHERE variable_name='mysql-monitor_password';
```

To load this configuration at runtime, issue a `LOAD` command.
Issue a `SAVE` command to save these changes to disk, this operation ensures that the changes persist after ProxySQL shuts down.

```mysql
mysql@proxysql> LOAD MYSQL VARIABLES TO RUNTIME;
mysql@proxysql> SAVE MYSQL VARIABLES TO DISK;
```

Check the monitoring logs to ensure that monitoring is enabled:

```mysql
mysql@proxysql> SELECT * FROM monitor.mysql_server_connect_log ORDER BY time_start_us DESC LIMIT 6;
+---------------+------+------------------+----------------------+---------------+
| hostname      | port | time_start_us    | connect_success_time | connect_error |
+---------------+------+------------------+----------------------+---------------+
| 192.168.70.61 | 3306 | 1469635762434625 | 1695                 | NULL          |
| 192.168.70.62 | 3306 | 1469635762434625 | 1779                 | NULL          |
| 192.168.70.63 | 3306 | 1469635762434625 | 1627                 | NULL          |
| 192.168.70.61 | 3306 | 1469635642434517 | 1557                 | NULL          |
| 192.168.70.62 | 3306 | 1469635642434517 | 2737                 | NULL          |
| 192.168.70.63 | 3306 | 1469635642434517 | 1447                 | NULL          |
+---------------+------+------------------+----------------------+---------------+
6 rows in set (0.00 sec)
```

```mysql
mysql> SELECT * FROM monitor.mysql_server_ping_log ORDER BY time_start_us DESC LIMIT 6;
+---------------+------+------------------+-------------------+------------+
| hostname      | port | time_start_us    | ping_success_time | ping_error |
+---------------+------+------------------+-------------------+------------+
| 192.168.70.61 | 3306 | 1469635762416190 | 948               | NULL       |
| 192.168.70.62 | 3306 | 1469635762416190 | 803               | NULL       |
| 192.168.70.63 | 3306 | 1469635762416190 | 711               | NULL       |
| 192.168.70.61 | 3306 | 1469635702416062 | 783               | NULL       |
| 192.168.70.62 | 3306 | 1469635702416062 | 631               | NULL       |
| 192.168.70.63 | 3306 | 1469635702416062 | 542               | NULL       |
+---------------+------+------------------+-------------------+------------+
6 rows in set (0.00 sec)
```

The previous examples show that *ProxySQL* is able to connect
and ping the nodes you added.

To enable monitoring of these nodes, load them at runtime:

```mysql
mysql@proxysql> LOAD MYSQL SERVERS TO RUNTIME;
```

## Creating a *ProxySQL* client user

*ProxySQL* must have users that can access backend nodes
to manage connections.

To add a user, insert credentials into `mysql_users` table:

```
mysql@proxysql> INSERT INTO mysql_users (username,password) VALUES ('sbuser','sbpass');
Query OK, 1 row affected (0.00 sec)
```

**NOTE**: *ProxySQL* currently doesn’t encrypt passwords.

Load the user into runtime space and save these changes to disk to ensure that the user account persists after ProxySQL shuts down:

```mysql
mysql@proxysql> LOAD MYSQL USERS TO RUNTIME;
mysql@proxysql> SAVE MYSQL USERS TO DISK;
```

To confirm that the user has been set up correctly, you can try to log in:

```mysql
root@proxysql:~# mysql -u sbuser -psbpass -h 127.0.0.1 -P 6033

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1491
Server version: 5.1.30 (ProxySQL)

Copyright (c) 2009-2016 Percona LLC and/or its affiliates
Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```

To provide read/write access to the cluster for ProxySQL, add this user on one
of the *Percona XtraDB Cluster* nodes:

```mysql
mysql@pxc3> CREATE USER 'sbuser'@'192.168.70.64' IDENTIFIED BY 'sbpass';
Query OK, 0 rows affected (0.01 sec)

mysql@pxc3> GRANT ALL ON *.* TO 'sbuser'@'192.168.70.64';
Query OK, 0 rows affected (0.00 sec)
```

## Adding Galera support in ProxySQL 1.x.x

ProxySQL 2.x.x supports monitoring the status *Percona XtraDB Cluster* nodes. ProxySQL 1.x.x cannot
detect a node which is not in `Synced` state.  To monitor the status of *Percona XtraDB Cluster*
nodes in ProxySQL 1.x.x, use the script proxysql_galera_checker.

To use this script, load it into [ProxySQL scheduler](https://github.com/sysown/proxysql/blob/master/doc/scheduler.md).

The following example shows how you can load the script for default
ProxySQL 1.x.x configuration:

```mysql
mysql> INSERT INTO scheduler (active,interval_ms,filename,arg1,comment)
VALUES (1,10000,'/usr/bin/proxysql_galera_checker','--config-file=/etc/proxysql-admin.cnf
--write-hg=10 --read-hg=11 --writer-count=1 --mode=singlewrite
--priority=192.168.100.20:3306,192.168.100.40:3306,192.168.100.10:3306,192.168.100.30:3306
--log=/var/lib/proxysql/cluster_one_proxysql_galera_check.log','cluster_one');
```

This scheduler script accepts the following options in the `arg1` argument:

| Option         | Name               | Required | Description                                                                                         |
| -------------- | ------------------ | -------- | --------------------------------------------------------------------------------------------------- |
| `--config-file`  | Configuration file | Yes      | Specify `proxysql-admin` conifiguration file                                                        |
| `--write-hg`     | HOSTGROUP WRITERS  | No       | Specify ProxySQL write hostgroup                                                                    |
| `--read-hg`      | HOSTGROUP READERS  | No       | Specify ProxySQL read hostgroup                                                                     |
| `--writer-count` | NUMBER WRITERS     | No       | Specify the write node count. The options are: 0 for `loadbal` mode and `1` for `singlewrite` mode. |
| `--mode`         | MODE               | No       | Specify ProxySQL read/write configuration mode                                                      |
| `--priority`     | WRITER PRIORITY    | No       | Specify write notes priority                                                                        |
| `--log`          | LOG FILE           | No       | Specify `proxysql_galera_checker` log file                                                          |

**NOTE**: Specify cluster name in comment column.

To load the scheduler changes into the runtime space:

```mysql
mysql@proxysql> LOAD SCHEDULER TO RUNTIME;
```

To make sure that the script has been loaded,
check the runtime_scheduler table:

```mysql
mysql@proxysql> SELECT * FROM scheduler\G
*************************** 1. row ***************************
         id: 1
     active: 1
interval_ms: 10000
   filename: /bin/proxysql_galera_checker
       arg1: --config-file=/etc/proxysql-admin.cnf --write-hg=10 --read-hg=11
             --writer-count=1 --mode=singlewrite
             --priority=192.168.100.20:3306,192.168.100.40:3306,192.168.100.10:3306,192.168.100.30:3306
             --log=/var/lib/proxysql/cluster_one_proxysql_galera_check.log
       arg2: NULL
       arg3: NULL
       arg4: NULL
       arg5: NULL
    comment: cluster_one
1 row in set (0.00 sec)
```

To check the status of available nodes, run the following command:

```mysql
mysql@proxysql> SELECT hostgroup_id,hostname,port,status FROM mysql_servers;
+--------------+---------------+------+--------+
| hostgroup_id | hostname      | port | status |
+--------------+---------------+------+--------+
| 0            | 192.168.70.61 | 3306 | ONLINE |
| 0            | 192.168.70.62 | 3306 | ONLINE |
| 0            | 192.168.70.63 | 3306 | ONLINE |
+--------------+---------------+------+--------+
3 rows in set (0.00 sec)
```

Each node can have the following status:

ONLINE

    Backend node is fully operational.

SHUNNED

    backend node is temporarily taken out of use, because either too many
    connection errors happened in a short time, or replication lag exceeded the
    allowed threshold.

OFFLINE_SOFT

    New incoming connections aren’t accepted, while existing connections are kept
    until they become inactive. In other words, connections are kept in use until
    the current transaction is completed.  This allows to gracefully detach a
    backend node.

OFFLINE_HARD

    Existing connections are dropped, and new incoming connections aren’t
    accepted.  This is equivalent to deleting the node from a hostgroup, or
    temporarily taking it out of the hostgroup for maintenance.

## Testing Cluster with sysbench

You can install `sysbench` from Percona software repositories:

* For Debian or Ubuntu:

```mysql
root@proxysql:~#> apt-get install sysbench
```

* For Red Hat Enterprise Linux or CentOS

```bash
[root@proxysql ~]#> yum install sysbench
```

**NOTE**: `sysbench` requires ProxySQL client user credentials
that you creted in Creating a ProxySQL client user.


1. Create the database that will be used for testing on one of the *Percona XtraDB Cluster* nodes:

```mysql
mysql@pxc1> CREATE DATABASE sbtest;
```


2. Populate the table with data for the benchmark on the ProxySQL node:

```bash
root@proxysql:~#> sysbench --report-interval=5 --num-threads=4 \
--num-requests=0 --max-time=20 \
--test=/usr/share/doc/sysbench/tests/db/oltp.lua \
--mysql-user='sbuser' --mysql-password='sbpass' \
--oltp-table-size=10000 --mysql-host=127.0.0.1 --mysql-port=6033 \
prepare
```


3. Run the benchmark on the ProxySQL node:

```bash
root@proxysql:~#> sysbench --report-interval=5 --num-threads=4 \
  --num-requests=0 --max-time=20 \
  --test=/usr/share/doc/sysbench/tests/db/oltp.lua \
  --mysql-user='sbuser' --mysql-password='sbpass' \
  --oltp-table-size=10000 --mysql-host=127.0.0.1 --mysql-port=6033 \
  run
```

ProxySQL stores collected data in the `stats` schema:

```mysql
mysql@proxysql> SHOW TABLES FROM stats;
+--------------------------------+
| tables                         |
+--------------------------------+
| stats_mysql_query_rules        |
| stats_mysql_commands_counters  |
| stats_mysql_processlist        |
| stats_mysql_connection_pool    |
| stats_mysql_query_digest       |
| stats_mysql_query_digest_reset |
| stats_mysql_global             |
+--------------------------------+
```

For example, to see the number of commands that run on the cluster:

## Automatic Fail-over

*ProxySQL* will automatically detect if a node is not available
or not synced with the cluster.

You can check the status of all available nodes by running:

```mysql
mysql@proxysql> SELECT hostgroup_id,hostname,port,status FROM mysql_servers;
+--------------+---------------+------+--------+
| hostgroup_id | hostname      | port | status |
+--------------+---------------+------+--------+
| 0            | 192.168.70.61 | 3306 | ONLINE |
| 0            | 192.168.70.62 | 3306 | ONLINE |
| 0            | 192.168.70.63 | 3306 | ONLINE |
+--------------+---------------+------+--------+
3 rows in set (0.00 sec)
```

To test problem detection and fail-over mechanism, shut down Node 3:

```bash
root@pxc3:~# service mysql stop
```

*ProxySQL* will detect that the node is down and update its status to
`OFFLINE_SOFT`:

```mysql
mysql@proxysql> SELECT hostgroup_id,hostname,port,status FROM mysql_servers;
+--------------+---------------+------+--------------+
| hostgroup_id | hostname      | port | status       |
+--------------+---------------+------+--------------+
| 0            | 192.168.70.61 | 3306 | ONLINE       |
| 0            | 192.168.70.62 | 3306 | ONLINE       |
| 0            | 192.168.70.63 | 3306 | OFFLINE_SOFT |
+--------------+---------------+------+--------------+
3 rows in set (0.00 sec)
```

Now start Node 3 again:

```bash
root@pxc3:~#> service mysql start
```

The script will detect the change and mark the node as
`ONLINE`:

```mysql
mysql@proxysql> SELECT hostgroup_id,hostname,port,status FROM mysql_servers;
+--------------+---------------+------+--------+
| hostgroup_id | hostname      | port | status |
+--------------+---------------+------+--------+
| 0            | 192.168.70.61 | 3306 | ONLINE |
| 0            | 192.168.70.62 | 3306 | ONLINE |
| 0            | 192.168.70.63 | 3306 | ONLINE |
+--------------+---------------+------+--------+
3 rows in set (0.00 sec)
```

# Assisted Maintenance Mode

Usually, to take a node down for maintenance, you need to identify that node,
update its status in ProxySQL to `OFFLINE_SOFT`, wait for ProxySQL to divert
traffic from this node, and then initiate the shutdown or perform maintenance
tasks.  *Percona XtraDB Cluster* includes a special *maintenance mode* for nodes that enables you
to take a node down without adjusting *ProxySQL* manually. This mode is
controlled via pxc_maint_mode_ variable, which is monitored by
*ProxySQL* and can be set to one of the following values:

* `DISABLED`: This is the default state
that tells ProxySQL to route traffic to the node as usual.

* `SHUTDOWN`: This state is set automatically
when you initiate node shutdown.

* `MAINTENANCE`: You can manually change to this state
if you need to perform maintenance on a node without shutting it down.


