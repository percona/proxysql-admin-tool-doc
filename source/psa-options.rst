.. _psa-options:

===============================================
Option Details
===============================================

The Percona Scheduler Admin script lists the available options in :ref:`psa-config`. The following options are described in more detail:

.. list-table::
   :header-rows: 1
   
   * - Option Name
   * - :ref:`psa-add-query`
   * - :ref:`psa-adduser`
   * - :ref:`psa-auto-assign-weights`
   * - :ref:`psa-disable`
   * - :ref:`psa-enable`
   * - :ref:`psa-force`
   * - :ref:`psa-is-enabled`
   * - :ref:`psa-server`
   * - :ref:`psa-status`
   * - :ref:`psa-sync-multi`
   * - :ref:`psa-syncusers`
   * - :ref:`psa-update-cluster`
   * - :ref:`psa-update-mysql-v`
   * - :ref:`psa-update-read-weight`
   * - :ref:`psa-update-write-weight`
   * - :ref:`psa-write-node`
   
  
.. _psa-add-query:

--add-query-rule
^^^^^^^^^^^^^^^^^^

This option creates query rules for a synced mysql user and applies only to the
``singlewrite`` mode.


.. rubric:: Requires

Either the :ref:`psa-syncusers` or :ref:`psa-sync-multi` options.

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --syncusers
    --add-query-rule

    Syncing user accounts from PXC to ProxySQL

    Note : 'admin' is in proxysql admin user list, this user cannot be added to ProxySQL
    -- (For more info, see https://github.com/sysown/proxysql/issues/709)
    Adding user to ProxySQL: test_query_rule
    Added query rule for user: test_query_rule
    Adding user to ProxySQL: test_query_rule
      Added query rule for user: test_query_rule

    Synced PXC users to the ProxySQL database!
    $>



.. _psa-adduser:

--adduser
^^^^^^^^^^^^

This option adds the cluster application user account to the ProxySQL database.

.. code-block:: bash

    $> percona-scheduler-admin --config-file=config.toml --adduser

    Adding PXC application user to the ProxySQL database
    Enter the PXC application user name: cluster_one
    Enter the PXC application user password:


    The application user 'cluster_one' does not exist in PXC. Would you like to proceed [y/n] ? y

    Please create the user cluster_one in PXC to access the application through ProxySQL

    Added PXC application user to the ProxySQL database!


.. _psa-auto-assign-weights:

--auto-assign-weights
^^^^^^^^^^^^^^^^^^^^^^

ProxySQL uses weights for defining the failover procedure in singlewrite mode
and handling load balancing loadbal mode.

For the failover procedure, this option with the
``--update-cluster`` option assigns weights to the PXC nodes when the cluster is
in singlewrite mode.

As a best practice, ensure that the writer node election operation returns the
same result each time. For example, assign the value of ``1000`` to node one,
``999`` to node two, and ``998`` to the node three. This method sets a clear
priority for the election.

For load balancing you want to reduce the reads on the writer node and, also,
split the reads across all the reader nodes equally.

For example, in a three-node cluster, assign a ``900`` to the writer node and
``1000`` and ``1000`` to the reader nodes.

This option does these operations automatically without any manual intervention.

.. warning::

    See :ref:`do-not-combine` for information on options that should not be
    in the same statement.

The following example is a default configuration when the
``percona-scheduler-admin`` sets up proxysql.

.. sourcecode:: mysql

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

    $> percona-scheduler-admin --config-file=config.toml --update-cluster --auto-assign-weights
    No new nodes detected.

.. sourcecode:: mysql

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

.. _psa-disable:

--disable / -d
^^^^^^^^^^^^^^^^^

This option removes Percona XtraDB Cluster nodes from ProxySQL and stops the
ProxySQL monitoring daemon.

.. sourcecode:: bash
    
    $> percona-scheduler-admin --config-file=config.toml --disable
    Removing cluster application users from the ProxySQL database.
    Removing cluster nodes from the ProxySQL database.
    Removing query rules from the ProxySQL database if any.


.. _psa-enable:

--enable / -e
^^^^^^^^^^^^^^^^^

This option creates entries for the Galera hostgroups and adds the Percona XtraDB Cluster nodes into ProxySQL's `mysql_servers` table.

The option adds two users into the Percona XtraDB Cluster with the ``USAGE``
privilege. The users have the following tasks:

* First user monitors the cluster nodes through ProxySQL.

* Second user connects to the PXC Cluster node through the ProxySQL console.

.. note:: You must have ``super`` user credentials from Percona XtraDB Cluster
   to setup the default users.

.. sourcecode:: bash
  
    $> percona-scheduler-admin --config-file=config.toml --enable
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

    Observe below that
    mysql> select * from runtime_mysql_servers;
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


    mysql> select * from scheduler\G
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

.. _psa-force:

--force
^^^^^^^^^^^^^^^^
This option must be combined with either :ref:`psa-enable` or :ref:`psa-update-cluster`. This option skips any `mysql_servers table`, `mysql_users table`, and `mysql_galera_hostgroups` table configuration checks. Certain checks issue warnings instead of errors.

.. _psa-is-enabled:

--is-enabled
^^^^^^^^^^^^^^^

This option checks if the hostgroups in ProxySQL have been configured by ``percona-scheduler-admin``.

Returns a zero (0) if an entry corresponds to the writer hostgroup
and is set to active in ProxySQL.

Returns a one (1) if an entry does not correspond to the writer hostgroup.

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --is-enabled
    The current configuration has been enabled and is active

    $> echo $?
    0


    #> When the cluster config is disabled, then -- is-enabled option shall throw an error
    $ percona-scheduler-admin --config-file=config.toml --disable
    Removing cluster application users from the ProxySQL database.
    Removing cluster nodes from the ProxySQL database.
    Removing query rules from the ProxySQL database if any.
    ProxySQL configuration removed!

    $> percona-scheduler-admin --config-file=config.toml --is-enabled
    ERROR (line:2450) : The current configuration has not been enabled

.. _psa-server:

--server
^^^^^^^^^^^^^

Selects a server by the IP address and port. This option can be combined with :ref:`_psa-syncusers` or :ref:`psa-sync-multi` to sync a single non-cluster server node.


Usage:

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --server=192.168.56.32:3306


.. _psa-status:

--status
^^^^^^^^^^

This option displays information about all Galera hostgroups and their servers supported by this ProxySQL instance.

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --status
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

.. _psa-sync-multi:

--sync-multi-cluster-users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use this option to sync proxysql instances that manage multiple
clusters.

This option does the following:

* Syncs the currently configured *Percona XtraDB Cluster* user accounts with the ProxySQL database except for user accounts without a password and admin user accounts.

* Keeps ProxySQL users that are not present in the Percona XtraDB Cluster

To sync a specific server combine this option with the ``--server`` option.

.. _psa-syncusers:

--syncusers
^^^^^^^^^^^^

This option does the following:

* Syncs the currently configured *Percona XtraDB Cluster* user accounts with the ProxySQL database except for user accounts without a password and admin user accounts. 

* Deletes ProxySQL user accounts that are not also in Percona XtraDB Cluster from the ProxySQL database.

To sync a specific server combine this option with the ``--server`` option.

Review the user accounts in the ProxySQL database as root.

.. sourcecode:: bash

    #> From ProxySQL DB
    proxysql admin> SELECT DISTINCT username FROM mysql_users;
    +----------+
    | username |
    +----------+
    | monitor  |
    +----------+
    1 row in set (0.00 sec)

On a Percona XtraDB Cluster node, verify if a user account is already added.

.. sourcecode:: mysql

      mysql> SELECT user FROM mysql.user WHERE user LIKE 'test%';
    Empty set (0.00 sec)

On the node, add a new user.

.. sourcecode:: mysql

    mysql> CREATE USER 'test_user'@'localhost' IDENTIFIED WITH 'mysql_native_password' by 'passw0Rd';
    Query OK, 0 rows affected (0.04 sec)

Run `percona-scheduler-admin` with the ``--syncusers`` option

.. sourcecode:: bash

    ./percona-scheduler-admin --config-file=config.toml --syncusers

    Syncing user accounts from PXC(192.168.56.32:3306) to ProxySQL

    Adding user to ProxySQL: test_user

    Synced PXC users to the ProxySQL database!

Verify, in the ProxySQL database, that the user account has been added.

.. sourcecode:: bash

    proxysql admin> SELECT DISTINCT username FROM mysql_users;

    +-----------+
    | username  |
    +-----------+
    | monitor   |
    | test_user |
    +-----------+
    2 rows in set (0.00 sec)

.. _psa-update-cluster:

--update-cluster
^^^^^^^^^^^^^^^^^^^

This option checks the *Percona XtraDB Cluster* for new nodes. If nodes are
found, they are added to ProxySQL. Offline nodes are not removed from the
cluster, by default.

Combining ``--remove-all-servers`` with this option removes the server list
for the configuration before the update runs.

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --write-node=127.0.0.1:4130 --update-cluster
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

.. _psa-update-mysql-v:

--update-mysql-version
^^^^^^^^^^^^^^^^^^^^^^^^^

This option updates the mysql server version in the proxysql db based on
the online writer node.

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --update-mysql-version
    ProxySQL MySQL version changed to 8.0.27


.. _psa-update-read-weight:

--update-read-weight
^^^^^^^^^^^^^^^^^^^^^^^

Combining :ref:`psa-update-cluster` with this option assigns the specified read
weight to a node.

Usage:

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --update-cluster --update-read-weight="<IP_ADDRESS:PORT>, <New Weight>"

The syntax for the arguments are: <IP_ADDRESS:PORT> and <New Weight>. The
<IP_ADDRESS> format can be either Internet Protocol version 4 (IPv4)
or Internet Protocol version 6 (IPv6).

The ``percona-scheduler-admin`` default configuration for *ProxySQL*.


.. sourcecode:: bash

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
    

The following command assigns the weight value of ``1111`` to the
``192.168.56.32:3306`` node in the reader and reader-config hostgroups.

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --update-cluster --update-read-weight="192.168.56.32:3306,1111"
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



.. _psa-update-write-weight:

--update-write-weight
^^^^^^^^^^^^^^^^^^^^^^^

Combining this option with :ref:`psa-update-cluster` assigns the
specified write weight to a node.

Usage:

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --update-cluster --update-write-weight="<IP_ADDRESS:PORT>, <New Weight>"

The syntax for the arguments are: <IP_ADDRESS:PORT> and <New Weight>. The
<IP_ADDRESS> format can be either Internet Protocol version 4 (IPv4)
or Internet Protocol version 6 (IPv6).

The ``percona-scheduler-admin`` default configuration for *ProxySQL*.

.. sourcecode:: bash

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


The following command assigns the weight value of ``1111`` to the
``192.168.56.33:3306`` node in the writer and writer-config hostgroups.

.. sourcecode:: bash

    $ percona-scheduler-admin --config-file=config.toml --update-cluster --update-write-weight="192.168.56.33:3306,1111"
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

.. _psa-write-node:

--write-node
^^^^^^^^^^^^^^^^^^^

This option chooses which Percona XtraDB Cluster node is the writer node when the mode is ``singlewrite``. You can combine this option with :ref:`psa-enable` and :ref:`psa-update-cluster`.

Assigning a node with ``--write-node`` gives the writer node a weight of 1000000. The default weight is 1000.

Usage:

.. sourcecode:: bash

    $> percona-scheduler-admin --config-file=config.toml --write-node=192.168.56.32:3306


The argument syntax is a single IP address and port combination.


