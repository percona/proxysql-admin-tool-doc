# Using ProxySQL v1 with ProxySQLAdmin

ProxySQL version 1.4 does not natively support Percona XtraDB Cluster and **proxysql-admin** . It requires custom bash
scripts to keep track of status: *proxysql_galera_checker* and **proxysql_node_monitor**.


# Installing ProxySQL v1

If that is what you used to [install
PXC](https://www.percona.com/doc/percona-xtradb-cluster/5.7/install/index.html)
or any other software, run the corresponding command:

On Debian or Ubuntu:

   ``` bash
    $ sudo apt-get install proxysql
   ```

On Red Hat Enterprise Linux or CentOS:

  ```bash
    $ sudo yum install proxysql
  ```

> seealso:
> 
> [installing from tarball](#tarball)

To start ProxySQL, run the following command:

``` bash
$ sudo service proxysql start
```


>Warning
>
>**Do not run ProxySQL with the default credentials in production.**
>
>Before starting the service, you can change the defaults in by changing
the `admin_credentials` variable. For more information, see [ProxySQL
global variables]().


# Automatic Configuration

The `proxysql` package from includes the **proxysql-admin** tool for configuring nodes with ProxySQL.


>Note
>
>**proxysql-admin** is specially developed by Percona to automate the ProxySQL configuration. Bug reports and
feature proposals are welcome in the **proxysql-admin**[issue tracking
system](https://jira.percona.com/projects/PSQLADM).

The **proxysql-admin** tool can only be used for the *initial* ProxySQL configuration.


To view usage information, run `proxysql-admin` without any options:

```bash
Usage: [ options ]
Options:
--config-file=<config-file>        Read login credentials from a configuration file
                                   (command line options override any configuration file login credentials)
--proxysql-datadir=<datadir>       Specify the proxysql data directory location
--proxysql-username=user_name      ProxySQL service username
--proxysql-password[=password]     ProxySQL service password
--proxysql-port=port_num           ProxySQL service port number
--proxysql-hostname=host_name      ProxySQL service hostname
--cluster-username=user_name       Percona XtraDB Cluster node username
--cluster-password[=password]      Percona XtraDB Cluster node password
--cluster-port=port_num            Percona XtraDB Cluster node port number
--cluster-hostname=host_name       Percona XtraDB Cluster node hostname
--cluster-app-username=user_name   Percona XtraDB Cluster node application username
--cluster-app-password[=password]  Percona XtraDB Cluster node application passwrod
--without-cluster-app-user         Configure Percona XtraDB Cluster without application user
--monitor-username=user_name       Username for monitoring Percona XtraDB Cluster nodes through ProxySQL
--monitor-password[=password]      Password for monitoring Percona XtraDB Cluster nodes through ProxySQL
--use-existing-monitor-password    Do not prompt for a new monitor password if one is provided.
--node-check-interval=3000         Interval for monitoring node checker script (in milliseconds)
                                   (default: 3000)
--mode=[loadbal|singlewrite]       ProxySQL read/write configuration mode
                                   currently supporting: 'loadbal' and 'singlewrite'
                                   (default: 'singlewrite')
--write-node=host_name:port        Writer node to accept write statments.
                                   This option is supported only when using --mode=singlewrite
                                   Can accept comma delimited list with the first listed being
                                   the highest priority.
--include-slaves=host_name:port    Add specified slave node(s) to ProxySQL, these nodes will go
                                   into the reader hostgroup and will only be put into
                                   the writer hostgroup if all cluster nodes are down (this
                                   depends on the value of --use-slave-as-writer).
                                   Slaves must be read only.  Can accept a comma delimited list.
                                   If this is used make sure 'read_only=1' is in the "slave's" my.cnf
--use-slave-as-writer=<yes/no>     If this value is 'yes', then a slave may be used as a writer
                                   if the entire cluster is down. If 'no', then a slave
                                   will not be used as a writer. This option is required
                                   if '--include-slaves' is used.
--writer-is-reader=<value>         Defines if the writer node also accepts writes.
                                   Possible values are 'always', 'never', and 'ondemand'.
                                   'ondemand' means that the writer node only accepts reads
                                   if there are no other readers.
                                   (default: 'ondemand')
--max-connections=<NUMBER>         Value for max_connections in the mysql_servers table.
                                   This is the maximum number of connections that
                                   ProxySQL will open to the backend servers.
                                   (default: 1000)
--debug                            Enables additional debug logging.
--help                             Dispalys this help text.

These options are the possible operations for proxysql-admin.
One of the options below must be provided.
--adduser                          Adds the Percona XtraDB Cluster application user to the ProxySQL database
--disable, -d                      Remove any Percona XtraDB Cluster configurations from ProxySQL
--enable, -e                       Auto-configure Percona XtraDB Cluster nodes into ProxySQL
--quick-demo                       Setup a quick demo with no authentication
--syncusers                        Sync user accounts currently configured in MySQL to ProxySQL
                                   May be used with --enable.
                                   (deletes ProxySQL users not in MySQL)
--sync-multi-cluster-users         Sync user accounts currently configured in MySQL to ProxySQL
                                   May be used with --enable.
                                   (doesn't delete ProxySQL users not in MySQL)
--version, -v                      Print version info   
```


>Note
>
>Before using the **proxysql-admin**, ensure that ProxySQL and the Percona XtraDB Cluster nodes you want to add are running.
For security purposes, do not use the default user settings in the configuration file.


## Preparing the Configuration File

A best practice is to define connection and authentication information
in the ProxySQL configuration file (**/etc/proxysql-admin.cnf**), instead of specifying this information on the command
line.

By default, the configuration file contains the following settings:

```bash
# proxysql admin interface credentials.
export PROXYSQL_DATADIR='/var/lib/proxysql'
export PROXYSQL_USERNAME='admin'
export PROXYSQL_PASSWORD='admin'
export PROXYSQL_HOSTNAME='localhost'
export PROXYSQL_PORT='6032'

# PXC admin credentials for connecting to pxc-cluster-node.
export CLUSTER_USERNAME='admin'
export CLUSTER_PASSWORD='admin'
export CLUSTER_HOSTNAME='localhost'
export CLUSTER_PORT='3306'

# proxysql monitoring user. proxysql admin script will create this user in pxc to monitor pxc-nodes.
export MONITOR_USERNAME='monitor'
export MONITOR_PASSWORD='monit0r'

# Application user to connect to pxc-node through proxysql
export CLUSTER_APP_USERNAME='proxysql_user'
export CLUSTER_APP_PASSWORD='passw0rd'

# |proxysql| read/write hostgroup 
export WRITE_HOSTGROUP_ID='10'
export READ_HOSTGROUP_ID='11'

# |proxysql| read/write configuration mode.
export MODE="singlewrite"

# Writer-is-reader configuration
export WRITER_IS_READER="ondemand"

# max_connections default (used only when INSERTing a new mysql_servers entry)
export MAX_CONNECTIONS="1000"
```


>Note

>You should change the [default ProxySQL credentials]
(https://proxysql.com/documentation/global-variables/admin-variables/#admin-admin_credentials) before running ProxySQL in
production. Make sure that you provide the ProxySQL location and the credentials in the
configuration file.

>Provide superuser credentials for one of the Percona XtraDB Cluster nodes. The `proxysql-admin`
script detects the other nodes in the cluster automatically.


## Enabling ProxySQL

Use the `--enable` option to automatically configure a Percona XtraDB Cluster node into ProxySQL. The
`proxysql-admin` tool does the following:

-   Adds a Percona XtraDB Cluster node into the ProxySQL database
-   Adds the `proxysql_galera_checker` monitoring script into the
    [ProxySQL scheduler](https://proxysql.com/documentation/scheduler/) table if it is not available. This script
    checks for the desynced nodes and temporarily deactivates them. It also
    calls the `proxysql_node_monitor` script, which checks the cluster node
    membership and reconfigures if the membership changes.
-   Create two new Percona XtraDB Cluster users with the `USAGE` privilege on the node and add
    them to the ProxySQL configuration, if they are not already configured. ProxySQL uses one
    user for monitoring the cluster nodes, and the other user
    communicates with the cluster. Make sure to use the super user
    credentials from the Cluster to set up the default users.


>Warning
>
>Running multiple copies the of `proxysql_galera_check` in the same
runtime environment simultaneously is not supported and may lead to
undefined behavior.

>To avoid this problem, Galera process identification prevents a
duplicate script execution in most cases. However, in some rare cases,
it may be possible to circumvent this check if you run more then one
copy of `proxysql_galera_check`.


The following example shows how to add a Percona XtraDB Cluster node using the ProxySQL configuration
file with all necessary connection and authentication information:

``` bash
$ proxysql-admin --config-file=/etc/proxysql-admin.cnf --enable
```


Output

``` bash
This script will assist with configuring ProxySQL for use with
Percona XtraDB Cluster (currently only PXC in combination with ProxySQL is supported)

ProxySQL read/write configuration mode is singlewrite

Configuring the ProxySQL monitoring user.  ProxySQL monitor user name as per
command line/config-file is monitor

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

$ mysql --user=proxysql_user -p --host=localhost --port=6033 --protocol=tcp
```


``` sql
mysql> select hostgroup_id,hostname,port,status,comment from mysql_servers;
```


Output

``` bash
+--------------+-----------+-------+--------+---------+
| hostgroup_id | hostname  | port  | status | comment |
+--------------+-----------+-------+--------+---------+
| 11           | 127.0.0.1 | 25400 | ONLINE | READ    |
| 10           | 127.0.0.1 | 25000 | ONLINE | WRITE   |
| 11           | 127.0.0.1 | 25100 | ONLINE | READ    |
| 11           | 127.0.0.1 | 25200 | ONLINE | READ    |
| 11           | 127.0.0.1 | 25300 | ONLINE | READ    |
+--------------+-----------+-------+--------+---------+
5 rows in set (0.00 sec)
```


## Disabling ProxySQL

Use the `--disable` option to remove a Percona XtraDB Cluster node's configuration from ProxySQL. The
`proxysql-admin` tool does the following:

-   Removes a Percona XtraDB Cluster node from the ProxySQL database
-   Stops the ProxySQL monitoring daemon for this node
-   Removes the application user for this cluster
-   Removes any query rules set up for this cluster

The following example shows how to disable and remove the node:

``` bash
$ proxysql-admin --config-file=/etc/proxysql-admin.cnf --disable
ProxySQL configuration removed!
```

## Additional Options

The following extra options are available:

-   `--adduser`

    Add Percona XtraDB Cluster application user to the ProxySQL database.

    ``` bash
    $ proxysql-admin --config-file=/etc/proxysql-admin.cnf --adduser

    Adding Percona XtraDB Cluster application user to |proxysql| database
    Enter Percona XtraDB Cluster application user name: cluster_user
    Enter Percona XtraDB Cluster application user password: cluster_passw0Rd
    Added Percona XtraDB Cluster application user to |proxysql| database!
    ```

-   `--syncusers`

    Syncs user accounts currently configured in the Percona XtraDB Cluster to the ProxySQL database except users
    with no password and the `admin` user.


>Note
 
>This option also deletes any user account which is not in the Percona XtraDB Cluster from the ProxySQL database.


-   `--sync-multi-cluster-users`

    This option works in the same way as `--syncusers` but does not
    delete the user accounts that are not present in  Percona XtraDB Cluster. Use this option when syncing proxysql instances that manage multiple
    clusters.

-   `--node-check-interval`

    This option configures the interval for monitoring with the
    `proxysql_galera_checker` script (in milliseconds).

    ``` bash
    $ proxysql-admin --config-file=/etc/proxysql-admin.cnf \
       --node-check-interval=5000 --enable
    ```

-   `--mode`

    Set the read/write mode for the Percona XtraDB Cluster nodes in the ProxySQL database, based on the
    hostgroup. Supported modes are `loadbal` and `singlewrite`.

    -   `singlewrite` is the default mode. This mode accepts writes only on
        one single node (based on the information you provide in
        `--write-node`). The remaining nodes accept only read
        statements.

        Servers can be separated by commas, for example:

            10.0.0.51:3306,10.0.0.52:3306

        In the previous example, `10.0.0.51:3306` is in the writer
        hostgroup if it is ONLINE. If it is OFFLINE, then
        `10.0.0.52:3306` is added to the writer hostgroup. And if that
        node also goes down, then one of the remaining nodes is
        randomly chosen for the writer hostgroup. 
        
   		The configuration file
        is deleted when `--disable` is used.

    -   `singlewrite` mode setup:

        ``` bash
        $ sudo grep "MODE" /etc/proxysql-admin.cnf
        export MODE="singlewrite"
        $ sudo proxysql-admin --config-file=/etc/proxysql-admin.cnf --write-node=127.0.0.1:25000 --enable
        |proxysql| read/write configuration mode is singlewrite
        [..]
        |proxysql| configuration completed!
        ```

        To check the configuration you can run:

        ``` sql
        mysql> SELECT hostgroup_id,hostname,port,status,comment FROM mysql_servers;
        +--------------+-----------+-------+--------+---------+
        | hostgroup_id | hostname  | port  | status | comment |
        +--------------+-----------+-------+--------+---------+
        | 11           | 127.0.0.1 | 25400 | ONLINE | READ    |
        | 10           | 127.0.0.1 | 25000 | ONLINE | WRITE   |
        | 11           | 127.0.0.1 | 25100 | ONLINE | READ    |
        | 11           | 127.0.0.1 | 25200 | ONLINE | READ    |
        | 11           | 127.0.0.1 | 25300 | ONLINE | READ    |
        +--------------+-----------+-------+--------+---------+
        5 rows in set (0.00 sec)
        ```

    -   The `loadbal` mode uses a set of evenly weighed read/write
        nodes.

        `loadbal` mode setup:

        ``` bash
        $ sudo proxysql-admin --config-file=/etc/proxysql-admin.cnf --mode=loadbal --enable

        This script will assist with configuring |proxysql| (currently only Percona XtraDB cluster in combination with |proxysql| is supported)

        |proxysql| read/write configuration mode is loadbal
        [..]
        |proxysql| has been successfully configured to use with Percona XtraDB Cluster

        You can use the following login credentials to connect your application through |proxysql|

        mysql --user=proxysql_user --password=*****  --host=127.0.0.1 --port=6033 --protocol=tcp 
        ```

        ``` sql
        mysql> SELECT hostgroup_id,hostname,port,status,comment FROM mysql_servers;
        +--------------+-----------+-------+--------+-----------+
        | hostgroup_id | hostname  | port  | status | comment   |
        +--------------+-----------+-------+--------+-----------+
        | 10           | 127.0.0.1 | 25400 | ONLINE | READWRITE |
        | 10           | 127.0.0.1 | 25000 | ONLINE | READWRITE |
        | 10           | 127.0.0.1 | 25100 | ONLINE | READWRITE |
        | 10           | 127.0.0.1 | 25200 | ONLINE | READWRITE |
        | 10           | 127.0.0.1 | 25300 | ONLINE | READWRITE |
        +--------------+-----------+-------+--------+-----------+
        5 rows in set (0.01 sec)
        ```

-   `--quick-demo`

    This option is used to setup a dummy configuration.

    ``` bash
    $ sudo  proxysql-admin  --enable --quick-demo

    You have selected the dry test run mode. WARNING: This will create a test user (with all privileges) in the Percona XtraDB Cluster & |proxysql| installations.

    You may want to delete this user after you complete your testing!

    Would you like to proceed with '--quick-demo' [y/n] ? y

    Setting up proxysql test configuration!

    Do you want to use the default |proxysql| credentials (admin:admin:6032:127.0.0.1) [y/n] ? y
    Do you want to use the default Percona XtraDB Cluster credentials (root::3306:127.0.0.1) [y/n] ? n

    Enter the Percona XtraDB Cluster username (super user): root
    Enter the Percona XtraDB Cluster user password: 
    Enter the Percona XtraDB Cluster port: 25100
    Enter the Percona XtraDB Cluster hostname: localhost


    |proxysql| read/write configuration mode is singlewrite

    Configuring |proxysql| monitoring user..

    User 'monitor'@'127.%' has been added with USAGE privilege

    Configuring the Percona XtraDB Cluster application user to connect through |proxysql|

    Percona XtraDB Cluster application user 'pxc_test_user'@'127.%' has been added with ALL privileges, this user is created for testing purposes

    Adding the Percona XtraDB Cluster server nodes to |proxysql|

    |proxysql| configuration completed!

    |proxysql| has been successfully configured to use with Percona XtraDB Cluster

    You can use the following login credentials to connect your application through |proxysql|

    mysql --user=pxc_test_user  --host=127.0.0.1 --port=6033 --protocol=tcp 
    ```

-   `--include-slaves=host_name:port`

    This option includes the specified replica node(s) to the ProxySQL database.
    These nodes are added to the reader hostgroup and will only be put
    into the writer hostgroup if all cluster nodes are down. Replicas must
    be read-only. This option can accept comma-delimited list. If a list is used, make
    sure `read_only=1` is included into the replica's `my.cnf`
    configuration file.


  >  Note


   > With `loadbal` mode, replica hosts only accept read/write requests when
    all cluster nodes are down.


## script

There is a simple script to dump the configuration and statistics:

``` text
Usage:

proxysql-status admin admin 127.0.0.1 6032
```
