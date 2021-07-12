.. _install-proxysql:

Installing ProxySQL v2 using a Package Manager
------------------------------------------------

If you used a package manager to [install
Percona XtraDB Cluster](https://www.percona.com/doc/percona-xtradb-cluster/8.0/install/index.html)
or any other Percona software, run the corresponding command based on the supported platform:

Installing ProxySQL 2.0.x and ProxySQL Admin on Debian or the supported derivatives:

```bash
sudo apt-get install proxysql2
```
Installing ProxySQL 2.0.x and ProxySQL Admin on Red Hat Enterprise Linux or the supported derivatives:

```bash
    sudo yum install proxysql2
```



To start ProxySQL 2.0.x or ProxySQL 2.1.x, run the following command: 

.. sourcecode:: bash

     sudo service proxysql2 start


Warning


**Do not run ProxySQL with default credentials in production.**

Before starting the `proxysql` service, you can change the defaults in
the `/etc/proxysql.cnf`{.interpreted-text role="file"} file by changing
the `admin_credentials` variable. For more information, see [Global
Variables](https://github.com/sysown/proxysql/blob/master/doc/global_variables.md).
