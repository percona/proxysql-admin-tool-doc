.. _proxysql-configuring:

Configuring |proxysql|
================================================================================

This tutorial describes how to configure |proxysql| with three |abbr.pxc| nodes.

.. _table.proxysql-pxc:

.. include:: _res/tables/proxysql-pxc.txt

|proxysql| can be configured either using |file.etc-proxysql-cnf| or through the
admin interface.  Using the admin interface is preferable, because it allows
changing the configuration dynamically (no need to restart the proxy).

To connect to the |proxysql-admin-interface|, use the ``mysql`` client.  You
can either connect to the admin interface from a |pxc| node that already has the
``mysql`` client installed (*Node 1*, *Node 2*, *Node 3*) or install the client on
*Node 4* and connect locally.  For this tutorial, install |pxc| on Node 4:

* On Debian or Ubuntu:

  .. code-block:: bash

     [root@proxysql ~]# apt-get install percona-xtradb-cluster-client

* On Red Hat Enterprise Linux or CentOS:

  .. code-block:: bash

     [root@proxysql ~]# yum install percona-xtradb-cluster-client

To connect to the admin interface, use the credentials, host name, and port
specified in the `ProxySQL global variables`_.

.. warning::

   Do not use default credentials in production!

The following example shows how to connect to the |proxysql-admin-interface|
with default credentials:

.. include:: _res/code-blocks/mysql-hpu.txt

To see the |proxysql| databases and tables use the following commands:

.. code-block:: text

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
 
.. code-block:: text
 
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

.. seealso::

   |ProxySQL| Documentation: Admin Tables
      https://github.com/sysown/proxysql/blob/master/doc/admin_tables.md

.. note::

  ProxySQL has 3 areas where the configuration can reside:

  * MEMORY (your current working place)
  * RUNTIME (the production settings)
  * DISK (durable configuration, saved inside an SQLITE database)

  When you change a parameter, you change it in MEMORY area.  That is done by
  design to allow you to test the changes before pushing to production
  (RUNTIME), or save them to disk.

Adding cluster nodes to |proxysql|
--------------------------------------------------------------------------------

To configure the backend |pxc| nodes in |proxysql|, insert corresponding records
into the ``mysql_servers`` table.

.. note::

   |proxysql| uses the concept of *hostgroups* to group cluster nodes. This
   approach enables balancing the load in a cluster by routing different types
   of traffic to different groups.

   There are many ways you can configure hostgroups (for
   example master and slaves, read and write load, etc.)  and every node can
   be a member of multiple hostgroups.

This example adds three |pxc| nodes to the default hostgroup (``0``),
which receives both write and read traffic:

.. code-block:: text

   mysql@proxysql> INSERT INTO mysql_servers(hostgroup_id, hostname, port) VALUES (0,'192.168.70.61',3306);
   mysql@proxysql> INSERT INTO mysql_servers(hostgroup_id, hostname, port) VALUES (0,'192.168.70.62',3306);
   mysql@proxysql> INSERT INTO mysql_servers(hostgroup_id, hostname, port) VALUES (0,'192.168.70.63',3306);

To see the nodes:

.. include:: _res/code-blocks/select-from-mysql-servers.txt

Creating a |proxysql| Monitoring User
--------------------------------------------------------------------------------

To enable monitoring of |pxc| nodes in |proxysql|,
create a user with the ``USAGE`` privilege on any node in the cluster
and configure the user in ProxySQL.

The following example shows how to add a monitoring user on Node 2:

.. code-block:: text

  mysql@pxc2> CREATE USER 'proxysql'@'%' IDENTIFIED BY 'ProxySQLPa55';
  mysql@pxc2> GRANT USAGE ON *.* TO 'proxysql'@'%';

The following example shows how to configure this user on the ProxySQL node:

.. code-block:: text

  mysql@proxysql> UPDATE global_variables SET variable_value='proxysql'
                WHERE variable_name='mysql-monitor_username';
  mysql@proxysql> UPDATE global_variables SET variable_value='ProxySQLPa55'
                WHERE variable_name='mysql-monitor_password';

To load this configuration at runtime, issue a ``LOAD`` command.
To save these changes to disk
(ensuring that they persist after ProxySQL shuts down),
issue a ``SAVE`` command.

.. code-block:: text

  mysql@proxysql> LOAD MYSQL VARIABLES TO RUNTIME;
  mysql@proxysql> SAVE MYSQL VARIABLES TO DISK;

To ensure that monitoring is enabled,
check the monitoring logs:

.. code-block:: text

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

.. code-block:: text

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

The previous examples show that |proxysql| is able to connect
and ping the nodes you added.

To enable monitoring of these nodes, load them at runtime:

.. code-block:: text

   mysql@proxysql> LOAD MYSQL SERVERS TO RUNTIME;

.. _proxysql-client-user:

Creating a |proxysql| client user
--------------------------------------------------------------------------------

|proxysql| must have users that can access backend nodes
to manage connections.

To add a user, insert credentials into ``mysql_users`` table:

.. code-block:: text

   mysql@proxysql> INSERT INTO mysql_users (username,password) VALUES ('sbuser','sbpass');
   Query OK, 1 row affected (0.00 sec)

.. note::

   |proxysql| currently doesn't encrypt passwords.

Load the user into runtime space and save these changes to disk
(ensuring that they persist after ProxySQL shuts down):

.. code-block:: text

   mysql@proxysql> LOAD MYSQL USERS TO RUNTIME;
   mysql@proxysql> SAVE MYSQL USERS TO DISK;

To confirm that the user has been set up correctly, you can try to log in:

.. code-block:: bash

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

To provide read/write access to the cluster for ProxySQL, add this user on one
of the |pxc| nodes:

.. code-block:: text

   mysql@pxc3> CREATE USER 'sbuser'@'192.168.70.64' IDENTIFIED BY 'sbpass';
   Query OK, 0 rows affected (0.01 sec)

   mysql@pxc3> GRANT ALL ON *.* TO 'sbuser'@'192.168.70.64';
   Query OK, 0 rows affected (0.00 sec)

Adding Galera support in |proxysql-v1|
--------------------------------------------------------------------------------

|proxysql-v2| supports monitoring the status |pxc| nodes. |proxysql-v1| cannot
detect a node which is not in ``Synced`` state.  To monitor the status of |pxc|
nodes in |proxysql-v1|, use the script |command.proxysql-galera-checker|.

To use this script, load it into `ProxySQL scheduler`_.

The following example shows how you can load the script for default
|proxysql-v1| configuration:

.. code-block:: text

   INSERT INTO scheduler (active,interval_ms,filename,arg1,comment)
   VALUES (1,10000,'/usr/bin/proxysql_galera_checker','--config-file=/etc/proxysql-admin.cnf
   --write-hg=10 --read-hg=11 --writer-count=1 --mode=singlewrite 
   --priority=192.168.100.20:3306,192.168.100.40:3306,192.168.100.10:3306,192.168.100.30:3306 
   --log=/var/lib/proxysql/cluster_one_proxysql_galera_check.log','cluster_one');

This scheduler script accepts the following options in the ``arg1`` argument:

.. include:: _res/tables/options.proxysql-scheduler.txt

.. note:: Specify cluster name in `comment` column.

To load the scheduler changes into the runtime space:

.. code-block:: text

   mysql@proxysql> LOAD SCHEDULER TO RUNTIME;

To make sure that the script has been loaded,
check the |table.runtime-scheduler| table:

.. code-block:: text

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

To check the status of available nodes, run the following command:

.. code-block:: text

   mysql@proxysql> SELECT hostgroup_id,hostname,port,status FROM mysql_servers;
   +--------------+---------------+------+--------+
   | hostgroup_id | hostname      | port | status |
   +--------------+---------------+------+--------+
   | 0            | 192.168.70.61 | 3306 | ONLINE |
   | 0            | 192.168.70.62 | 3306 | ONLINE |
   | 0            | 192.168.70.63 | 3306 | ONLINE |
   +--------------+---------------+------+--------+
   3 rows in set (0.00 sec)

Each node can have the following status:

.. include:: _res/lists/node-statuses.txt

Testing Cluster with sysbench
-----------------------------

You can install ``sysbench`` from Percona software repositories:

* For Debian or Ubuntu:

  .. code-block:: bash

     root@proxysql:~# apt-get install sysbench

* For Red Hat Enterprise Linux or CentOS

  .. code-block:: bash

     [root@proxysql ~]# yum install sysbench

.. note:: ``sysbench`` requires ProxySQL client user credentials
   that you creted in :ref:`proxysql-client-user`.

1. Create the database that will be used for testing on one of the |PXC| nodes:

   .. code-block:: text

      mysql@pxc1> CREATE DATABASE sbtest;

#. Populate the table with data for the benchmark on the ProxySQL node:

   .. code-block:: bash

      root@proxysql:~# sysbench --report-interval=5 --num-threads=4 \
      --num-requests=0 --max-time=20 \
      --test=/usr/share/doc/sysbench/tests/db/oltp.lua \
      --mysql-user='sbuser' --mysql-password='sbpass' \
      --oltp-table-size=10000 --mysql-host=127.0.0.1 --mysql-port=6033 \
      prepare

#. Run the benchmark on the ProxySQL node:

   .. code-block:: bash

      root@proxysql:~# sysbench --report-interval=5 --num-threads=4 \
        --num-requests=0 --max-time=20 \
        --test=/usr/share/doc/sysbench/tests/db/oltp.lua \
        --mysql-user='sbuser' --mysql-password='sbpass' \
        --oltp-table-size=10000 --mysql-host=127.0.0.1 --mysql-port=6033 \
        run

ProxySQL stores collected data in the ``stats`` schema:

.. code-block:: text

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

For example, to see the number of commands that run on the cluster:


Automatic Fail-over
-------------------

|proxysql| will automatically detect if a node is not available
or not synced with the cluster.

You can check the status of all available nodes by running:

.. code-block:: text

   mysql@proxysql> SELECT hostgroup_id,hostname,port,status FROM mysql_servers;
   +--------------+---------------+------+--------+
   | hostgroup_id | hostname      | port | status |
   +--------------+---------------+------+--------+
   | 0            | 192.168.70.61 | 3306 | ONLINE |
   | 0            | 192.168.70.62 | 3306 | ONLINE |
   | 0            | 192.168.70.63 | 3306 | ONLINE |
   +--------------+---------------+------+--------+
   3 rows in set (0.00 sec)

To test problem detection and fail-over mechanism, shut down Node 3:

.. code-block:: bash

   root@pxc3:~# service mysql stop

|proxysql| will detect that the node is down and update its status to
``OFFLINE_SOFT``:

.. code-block:: text

   mysql@proxysql> SELECT hostgroup_id,hostname,port,status FROM mysql_servers;
   +--------------+---------------+------+--------------+
   | hostgroup_id | hostname      | port | status       |
   +--------------+---------------+------+--------------+
   | 0            | 192.168.70.61 | 3306 | ONLINE       |
   | 0            | 192.168.70.62 | 3306 | ONLINE       |
   | 0            | 192.168.70.63 | 3306 | OFFLINE_SOFT |
   +--------------+---------------+------+--------------+
   3 rows in set (0.00 sec)

Now start Node 3 again:

.. code-block:: bash

   root@pxc3:~# service mysql start

The script will detect the change and mark the node as
``ONLINE``:

.. code-block:: text

   mysql@proxysql> SELECT hostgroup_id,hostname,port,status FROM mysql_servers;
   +--------------+---------------+------+--------+
   | hostgroup_id | hostname      | port | status |
   +--------------+---------------+------+--------+
   | 0            | 192.168.70.61 | 3306 | ONLINE |
   | 0            | 192.168.70.62 | 3306 | ONLINE |
   | 0            | 192.168.70.63 | 3306 | ONLINE |
   +--------------+---------------+------+--------+
   3 rows in set (0.00 sec)

.. _index.proxysql-admin-interface.pxc-maint-mode:

Assisted Maintenance Mode
================================================================================

Usually, to take a node down for maintenance, you need to identify that node,
update its status in ProxySQL to ``OFFLINE_SOFT``, wait for ProxySQL to divert
traffic from this node, and then initiate the shutdown or perform maintenance
tasks.  |pxc| includes a special *maintenance mode* for nodes that enables you
to take a node down without adjusting |proxysql| manually.  This mode is
controlled via `pxc_maint_mode variable`_, which is monitored by
|proxysql| and can be set to one of the following values:

.. include:: _res/links.txt
.. include:: _res/replace.txt
