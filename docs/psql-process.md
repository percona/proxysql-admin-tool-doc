# Starting and Stopping ProxySQL

## Starting ProxySQL 2.x.x

To start ProxySQL 2.x, run the following command:

```bash
$> sudo service proxysql2 start
```

**WARNING**: **Do not run ProxySQL with default credentials in production.** Before starting the `proxysql` service, you can change the defaults in the `/etc/proxysql.cnf` file by changing the `admin_credentials` variable.  For more information, see [Global Variables](https://github.com/sysown/proxysql/blob/master/doc/global_variables.md).

For more information on starting ProxySQL, see [Getting Started](https://proxysql.com/documentation/getting-started/).

## Stopping ProxySQL 2.x.x

To stop ProxySQL 2.x, run either  of the following commands:

```bash
$> sudo service proxysql stop
```

or

```bash
$> sudo service proxysql2 stop
```
