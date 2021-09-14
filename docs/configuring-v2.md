# Automatic Configuration with ProxySQL   Admin

The `proxysql2.x` package from includes
the `proxysql-admin` tool for configuring nodes with ProxySQL.

Percona specifically develops the ProxySQL-Admin tool to automate this configuration.
Bug reports and feature proposals are welcome in the [issue tracking
system](https://jira.percona.com/projects/PSQLADM).

!!! note

    Before using the `proxysql-admin` tool, ensure that ProxySQL and Percona XtraDB Cluster nodes you want to add are running. For security purposes, change the default user settings in the [ProxySQL configuration file](https://proxysql.com/Documentation/configuration-file/). Refer to the [Global Variables](https://github.com/sysown/proxysql/blob/master/doc/global_variables.md) chapter in ProxySQL documentation for details and guidelines.

!!! Important

    The ProxySQL Admin tool can only be used for the *initial* configuration.

## Preparing the configuration file

It is recommended to provide the connection and authentication
information in the `proxysql-admin-cnf` file. Do not specify this
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

Use the `--config-file` option to run the `proxysql-admin` script. The login file
contains the information needed by `proxysql-admin` in an encrypted
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
