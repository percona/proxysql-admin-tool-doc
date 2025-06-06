# ProxySQL and proxysql-admin utility

The Percona build of ProxySQL from Percona includes the `proxysql-admin` tool for configuring Percona XtraDB Cluster nodes with ProxySQL.

Before using the `proxysql-admin` tool, ensure that ProxySQL and Percona XtraDB Cluster nodes you want to add are running. For security purposes, change the default user settings in the Proxysql configuration file.

Implemented in ProxySQL 2.3.2-1, the psqladm-scheduler tool configures Percona XtraDB cluster nodes into ProxySQL.

!!! note

    The pxc_scheduler_handler tool has different options than the proxysql-admin tool. Do not use the options from one tool in the other tool. Mixing the options may cause unintended results.

Command line options override configuration file options.

The `proxysql-admin.cnf` file is only read when proxysql-admin is invoked. After that process, changing the configuration file does not update settings. For example, you cannot change the `--mode` option dynamically. 

If you must change this option, you can run the following commands. 

!!! warning

    These commands may also remove all `proxysql-admin` entries from the proxysql tables.

1. `proxysql --disable`

2. Modify the `proxysql-admin.cnf` file with the desired changes.

2. `proxysql --enable`


## The proxysql-admin options

To view the usage information, run `proxysql-admin` without any options:

```{.text .no-copy}
Usage: proxysql-admin [ options ]
Options:

--config-file=<config-file>        Read login credentials from a configuration file.

--login-file=<login-file-path>     Read login credentials from an encrypted
                                   file. The user is prompted for
                                   the password if the --login-password
                                   or --login-password-file options are
                                   specified.

--login-password=<password>        The key used to decrypt the encrypted
                                   login-file. This option cannot be
                                   used with --login-password-file.

--login-password-file=<path>       Reads the key from a file using the
                                   <path>. This option cannot be
                                   used with --login-password.

--writer-hg=<number>               Traffic is sent to this hostgroup by default.
                                   Nodes that have 'read-only=0' in MySQL
                                   are assigned to this hostgroup.

--backup-writer-hg=<number>        If the cluster has multiple nodes with 'read-only=0'
                                   and the max_writers value is set, any nodes in excess
                                   of the max_writers value are assigned to this hostgroup.

--reader-hg=<number>               The hostgroup that read traffic should be sent to.
                                   Nodes with 'read-only=1' in MySQL will be assigned
                                   to this hostgroup.

--offline-hg=<number>              Nodes that are determined to be OFFLINE are
                                   assigned to this hostgroup.

--proxysql-datadir=<datadir>       Specify the ProxySQL data directory location

--proxysql-username=<user_name>    ProxySQL service username

--proxysql-password[=<password>]   ProxySQL service password

--proxysql-port=<port_num>         ProxySQL service port number

--proxysql-hostname=<host_name>    ProxySQL service hostname

--cluster-username=<user_name>     Percona XtraDB Cluster node username

--cluster-password[=<password>]    Percona XtraDB Cluster node password

--cluster-port=<port_num>          Percona XtraDB Cluster node port number

--cluster-hostname=<host_name>     Percona XtraDB Cluster node hostname

--cluster-app-username=<user_name> Percona XtraDB Cluster node application username

--cluster-app-password[=<password>] Percona XtraDB Cluster node application password

--without-cluster-app-user         Configure Percona XtraDB Cluster without application user

--monitor-username=<user_name>     Username for monitoring Percona XtraDB Cluster nodes through ProxySQL

--monitor-password[=<password>]    Password for monitoring Percona XtraDB Cluster nodes through ProxySQL

--use-existing-monitor-password    Do not prompt for a new monitor password if one is provided.

--node-check-interval=<NUMBER>     The interval at which the proxy should connect
                                   to the backend servers in order to monitor the
                                   Galera status of a node (in milliseconds).
                                   (default: 5000)

--mode=[loadbal|singlewrite]       ProxySQL read/write configuration mode
                                   currently supports: 'loadbal' and 'singlewrite'
                                   (default: 'singlewrite')

--write-node=<IPADDRESS>:<PORT>    Specifies the node used for
                                   writes when `mode=singlewrite` is used. The cluster node is used if left unspecified.

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

--remove-all-servers               When used with --update-cluster, this removes all
                                   servers belonging to the current cluster before
                                   updating the list.

--debug                            Enables additional debug logging.

--help                             Displays this help text.

These options are the possible operations for proxysql-admin.
Provide one of the following options:

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

It is recommended to provide the connection and authentication information in
the ProxySQL configuration file (proxysql-admin-cnf). Do not
specify this information on the command line.

By default, the configuration file contains the following:

```{.text .no-copy}
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

# ProxySQL hostgroup IDs
export WRITER_HOSTGROUP_ID='10'
export READER_HOSTGROUP_ID='11'
export BACKUP_WRITER_HOSTGROUP_ID='12'
export OFFLINE_HOSTGROUP_ID='13'

# ProxySQL read/write configuration mode.
export MODE="singlewrite"

# max_connections default (used only when INSERTing a new mysql_servers entry)
export MAX_CONNECTIONS='1000'

# Determines the maximum number of writesets a node can have queued
# before the node is SHUNNED to avoid stale reads.
export MAX_TRANSACTIONS_BEHIND=100

# Connections to the backend servers (from ProxySQL) will use SSL
export USE_SSL='no'

# Determines if a node should be added to the reader hostgroup if it has
# been promoted to the writer hostgroup.
# If set to 'yes', then all writers (including backup-writers) are added to
# the read hostgroup.
# If set to 'no', then none of the writers (including backup-writers) are added.
# If set to 'backup', then only the backup-writers will be added to
# the read hostgroup.
export WRITERS_ARE_READERS='backup'
```

## Configuring the proxysql-admin login

Use `--config-file` to run the proxysql-admin script. The login file contains the information needed by proxysql-admin in an encrypted format.

If no credentials are specified, either on the command line or in the login-file, then the following credentials are used:

* The default MySQL client credentials are found in my.cnf they connect to a ProxySQL instance.

* If the default MySQL client credentials do not exist or do not connect to a ProxySQL instance, then the credentials in `etc/proxysql-admin.cnf` are used.

## Example of the proxysql-admin file

The following is an example of the unencrypted data:

```{.text .no-copy}
# --------------------------------
# This file is constructed as a set of 'name=value' pairs.
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

## Create the login file

The following steps encrypt the login:

1. Create the unencrypted data

2. Encrypt the data with the proxysql-login-file script

3. Use the login-file with proxysql-admin

```{.text .no-copy}
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

## Verifying the login file

You can decrypt the login-file with the proxysql-login-file-script

```{.text .no-copy}
# Decrypt the login-file with the --decrypt option
# If --in is not used, the input data will be read from stdin
# If --out is not used, the unencrypted data will be written to stdout
$ proxysql-login-file --in login-file.cnf --password=secret --decrypt
monitor.user=monitor
monitor.password=password
```
