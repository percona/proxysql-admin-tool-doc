

## Automatic Configuration

The `proxysql2.x` package from includes
the `proxysql-admin` tool for configuring nodes with ProxySQL.

Before using the ProxySQL-Admin tool, ensure that ProxySQL and Percona XtraDB Cluster nodes you want to add are
running. For security purposes, change the default user settings in the ProxySQL configuration file.

>Important
>The ProxySQL-Admin tool can only be used for the *initial* configuration.

Percona specifically develops the ProxySQL-Admin tool to automate this configuration.
Bug reports and feature proposals are welcome in the [issue tracking
system](https://jira.percona.com/projects/PSQLADM).

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
These options are the possible operations for proxysql-admin.
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

## Preparing the configuration file

It is recommended to provide the connection and authentication
information in `proxysql-admin-cnf` file. Do not specify this
information on the command line.

By default, the configuration file contains the following:

```text
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
export MONITOR_USERNAME="monitor"
export MONITOR_PASSWORD="monit0r"

# Application user to connect to pxc-node through proxysql
export CLUSTER_APP_USERNAME="proxysql_user"
export CLUSTER_APP_PASSWORD="passw0rd"

# ProxySQL hostgroup IDs
export WRITER_HOSTGROUP_ID='10'
export READER_HOSTGROUP_ID='11'
export BACKUP_WRITER_HOSTGROUP_ID='12'
export OFFLINE_HOSTGROUP_ID='13'

# ProxySQL read/write configuration mode.
export MODE="singlewrite"

# max_connections default (used only when INSERTing a new mysql_servers entry)
export MAX_CONNECTIONS="1000"

# Determines the maximum number of writesets a node can have queued
# before the node is SHUNNED to avoid stale reads.
export MAX_TRANSACTIONS_BEHIND=100

# Connections to the backend servers (from ProxySQL) will use SSL
export USE_SSL="no"

# Determines if a node should be added to the reader hostgroup if it has
# been promoted to the writer hostgroup.
# If set to 'yes', then all writers (including backup-writers) are added to
# the read hostgroup.
# If set to 'no', then none of the writers (including backup-writers) are added.
# If set to 'backup', then only the backup-writers will be added to
# the read hostgroup.
export WRITERS_ARE_READERS="backup"
```

## Configuring the ProxySQL Admin Login

Use `--config-file` to run the proxysql-admin script. The login file
contains the information needed by proxysql-admin in an encrypted
format.

If no credentials are specified, either on the command line or in the
login-file, then the following credentials are used:

-   The default MySQL client credentials found in my.cnf, if they
    connect to a ProxySQL instance.
-   If the default MySQL client credentials do not exist or do not
    connect to a ProxySQL instance, then the credentials in
    `etc/proxysql-admin.cnf` are used.


**Example of the ProxySQL Admin File**

The following is an example of the unencrypted data:

```text
# --------------------------------
# This file is constructed as a set of "name=value" pairs.
# Notes:
# (1) Comment lines start with '#' and must be on separate lines
# (2) the name part
#   - The only acceptable values are shown below in this example.
#     Other values will be ignored.
# (3) The value part:
#   - This does NOT use quotes, so any quote character will be part of the value
#   - The entire line will be used (be careful with spaces)
#
# If a value is not specified here, than the default value from the
# configuration file will be used.
# --------------------------------

# --------------------------------
# proxysql admin interface credentials.
# --------------------------------
proxysql.user=admin
proxysql.password=admin
proxysql.host=localhost
proxysql.port=6032

# --------------------------------
# PXC admin credentials for connecting to pxc-cluster-node.
# --------------------------------
cluster.user=admin
cluster.password=admin
cluster.host=localhost
cluster.port=4110

# --------------------------------
# proxysql monitoring user. proxysql admin script will create
# this user in pxc to monitor pxc-nodes.
# --------------------------------
monitor.user=monitor
monitor.password=monitor

# --------------------------------
# Application user to connect to pxc-node through proxysql
# --------------------------------
cluster-app.user=cluster_one
cluster-app.password=passw0rd
```

**Creating the login file**

The following steps encrypt the login:

1.  Create the unencrypted data
2.  Encrypt the data with the proxysql-login-file script
3.  Use the login-file with proxysql-admin

```text
# create the file as shown above
 $ echo "monitor.user=monitor" > data.cnf
 $ echo "monitor.password=password" >> data.cnf

 # Choose a secret password
 $ passwd="secret"


 # Method (1) : Encrypt this data with --password
 $ proxysql-login-file --in data.cnf --out login-file.cnf --password=${passwd}

 # Method (2) : Encrypt the data with --password-file
 #              Sending the password via the command-line is insecure,
 #              it's better to use --password-file so that the
 #              password doesn't show up in the command-line
 $ proxysql-login-file --in data.cnf --out login-file.cnf \
    --password-file=<(echo "${passwd}")

 # Method (3) : The script will prompt for the password
 #              if no password is provided via the command-line options.
 $ proxysql-login-file --in data.cnf --out login-file.cnf

 # Remove the unencrypted data file
 $ rm data.cnf


 # Call the proxysql-admin script with the login-file
 $ proxysql-admin --enable --login-file=login-file.cnf \
    --login-password-file=<(echo "${passwd}")

 # Call proxysql-status with the login-file
 $ proxysql-status --login-file=login-file.cnf \
    --login-password-file=<(echo "${passwd}")
```

**Verifying the login-file**

You can decrypt the login-file with the proxysql-login-file-script

```text
# Decrypt the login-file with the --decrypt option
# If --in is not used, the input data will be read from stdin
# If --out is not used, the unencrypted data will be written to stdout
$ proxysql-login-file --in login-file.cnf --password=secret --decrypt
monitor.user=monitor
monitor.password=password
```
