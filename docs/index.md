

# ProxySQL and ProxySQL Admin documentation

[ProxySQL](https://www.proxysql.com/) is a high-performance SQL proxy. ProxySQL runs as a daemon watched
by a monitoring process. This process monitors the daemon and restarts
it in case of a crash to minimize downtime.

The daemon accepts incoming traffic from clients and forwards it to
backend servers.

ProxySQL is designed to run continuously without needing to be restarted. Most
configuration can be done at runtime using queries similar to SQL
statements. These include runtime parameters, server grouping, and
traffic-related settings.


>See also: 
>
>[ProxySQL documentation](https://proxysql.com/documentation/)



ProxySQL is available from the software repositories in two versions:

* **ProxySQL v1** does not
natively support Percona XtraDB Cluster and requires custom bash scripts to keep track of the
status of Percona XtraDB Cluster nodes using the ProxySQL scheduler.
* **ProxySQL v2** supports Percona XtraDB Cluster natively. With this version, the tool does not require custom
scripts to keep track of Percona XtraDB Cluster status.

To learn more about other changes in ProxySQL v2, see the [Changes in the ProxySQL-admin tool with PrxoySQL version 2](changes.md).

Both versions are bundled with the `proxysql-admin` tool. It is dedicated to automate and simplify the setup of ProxySQL with Percona XtraDB Cluster. 

## Setting up

* Install ProxySQL. The choices are:

    * [using a package manager](install-proxysql2.md). Find the information about supported operating system distributions in the [ProxySQl documentation](https://proxysql.com/documentation/installing-proxysql/).
    * [from a binary tarball](installing-tarball.md)

* Configure ProxySQL. For initial configuration, we recommend the [automatic configuration](configuring-v2.md) using the `proxysql-admin` tool. For manual configuration, refer to the [Configuring ProxySQL](configuring.md) tutorial.
* [Use ProxySQL](running.md)

## Read more

* [ProxySQL options](options.md)
* [How to upgrade](upgrading.md)
* [How to uninstall](uninstalling.md)

## Release notes

* [Release notes](release-notes.md)
