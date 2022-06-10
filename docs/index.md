::: {#index.proxysql-admin-interface}
:::

# and documentation

[ProxySQL](https://www.proxysql.com/), an high-performance SQL proxy, runs as a daemon watched by a monitoring process. This process monitors the daemon and restarts
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



ProxySQL is available from the software repositories in two versions. ProxySQL 1.x.x does not
natively support the **Percona XtraDB Cluster** and requires custom bash scripts to keep track of the
status of Percona XtraDB Cluster nodes using the ProxySQL scheduler.

* [Configuring ProxySQL](configuring.md)
* [Assisted Maintenance Mode](#assisted-maintenance)
* 
* 
configuring proxysql-v2 proxysql-v1 Release notes \<release-notes\>
:::

**Indices and tables**

-   `genindex`{.interpreted-text role="ref"}
-   `modindex`{.interpreted-text role="ref"}
-   `search`{.interpreted-text role="ref"}
