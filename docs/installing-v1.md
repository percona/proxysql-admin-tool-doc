# Install ProxySQL 1.x.x

If that is what you used to [install PXC](https://www.percona.com/doc/percona-xtradb-cluster/5.7/install/index.html) or
any other **Percona** software, run the corresponding command:

On Debian or Ubuntu:

```sh
$ sudo apt install proxysql
```

On Red Hat Enterprise Linux or CentOS:

```sh
$ sudo yum install proxysql
```

To start *ProxySQL*, run the following command:

```sh
$ sudo service proxysql start
```

## Do not use the default credentials

!!! warning

    Do not run ProxySQL with default credentials in production. 
     
Before starting the proxysql service, you can change the defaults in `/etc/proxysql.cnf` by changing the `admin_credentials` variable.  For more information, see [ProxySQL global variables](https://github.com/sysown/proxysql/blob/master/doc/global_variables.md).
