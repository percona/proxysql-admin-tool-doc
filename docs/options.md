# ProxySQL Admin options


## \--mode

This option allows you to set up the read/write mode for PXC cluster
nodes in the ProxySQL database based on the hostgroup. The only
supported modes are`singlewrite` and `loadbal`.

The `singlewrite` option is the default mode. Percona XtraDB Cluster only accepts writes on a single node. The write node may accept read requests, depending on the `--writers-are-readers` value. The other nodes are read-only and accept only read statements.

The `--write-node` option controls which node ProxySQL uses as
the writer node. The writer node is specified as the address:port - `10.0.0.51:3306`.  If `--write-node` is used, the writer node has a weight of **1000000**, which is greater than the default weight of **1000**, and the node has the assigned address:port of -**10.0.0.51:3306**.

The `loadbal` mode is a load balanced set of evenly weighted
read/write nodes.

The following example is a `singlewrite` mode setup:**

```bash
$ sudo grep "MODE" /etc/proxysql-admin.cnf
$ export MODE="singlewrite"
$ sudo proxysql-admin --config-file=/etc/proxysql-admin.cnf --write-node=127.0.0.1:25000 --enable
ProxySQL read/write configuration mode is singlewrite
[..]
ProxySQL configuration completed!
```
The result of a MySQL query:

```sql
mysql> SELECT hostgroup_id,hostname,port,status FROM runtime_mysql_servers;
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

The following example is a `loadbal` mode setup**

```bash
$ sudo proxysql-admin --config-file=/etc/proxysql-admin.cnf --mode=loadbal --enable
This script assists with configuring ProxySQL (currently only Percona XtraDB Cluster in combination with ProxySQL is supported)

ProxySQL read/write configuration mode is loadbal
[..]
ProxySQL has been successfully configured to use with Percona XtraDB Cluster

You can use the following login credentials to connect your application through ProxySQL.
```
The following are the results of a MySQL query:

```sql
$ mysql --user=proxysql_user --password=*****  --host=127.0.0.1 --port=6033 --protocol=tcp

mysql> SELECT hostgroup_id,hostname,port,status FROM runtime_mysql_servers;
+--------------+-----------+-------+--------+
| hostgroup_id | hostname  | port  | status |
+--------------+-----------+-------+--------+
| 10           | 127.0.0.1 | 25000 | ONLINE |
| 10           | 127.0.0.1 | 25100 | ONLINE |
| 10           | 127.0.0.1 | 25200 | ONLINE |
+--------------+-----------+-------+--------+
3 rows in set (0.01 sec)
```

### \--node-check-interval 

This option configures the interval for the cluster node health
monitoring by ProxySQL in milliseconds. This is a global variable for this ProxySQL instance and all clusters served by this instance use the variable.
This can only be used with `--enable`.

```bash
$ proxysql-admin --config-file=/etc/proxysql-admin.cnf --node-check-interval=5000 --enable
```

### \--write-node

This option is used to choose which node will be the writer node when
the mode is `singlewrite`. This option can be used with
`--enable` and `--update-cluster`.

A single IP address and port combination is expected. The following combination is an example: `--write-node=127.0.0.1:3306` 

## The `proxysql-staus` script

The proxysql-status script dumps configuration and statistics.

```bash
   proxysql-status admin admin 127.0.0.1 6032
```

Displaying all tables and files is the default behavior. By using the
following options, you can retrieve more specific information:

| Option               | Result                                                                          |
| -------------------- | --------------------------------------------------------------------------------- |
| --files              | The contents of the proxysql-admin-related files                                  |
| --main               | The main tables - both on-disk and runtime                                        |
| --monitor            | Monitor tables                                                                    |
| --runtime            | Runtime-related data - implies --main                                             |
| --stats              | Stats tables                                                                      |
| --table=(table name) | Return only the tables that contain the table name - this match is case-sensitive |
| --with-stats-reset   | --reset tables, by default _reset tables are not queried                          |                       |

> Note:
> 
> If no credentials are specified, the credentials in `/etc/proxysql-admin.cnf` are used.


