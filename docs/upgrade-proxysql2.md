# Upgrade ProxySQL 



In an MySQL 8.4 or Percona Server for MySQL 8.4 environment, you may have the following issues:

* ProxySQL contains counters that have not been updated to use the new terminology. Unexpected results may occur
* The binlog reader errors out during initialization due to the use of the old terminology, such as SHOW MASTER STATUS command.

You can upgrade ProxySQL from version 1 to the latest version 2 or you can upgrade minor versions with ProxySQL 2.

=== "Upgrade between major versions"

    Remove any *ProxySQL 1.x.x* packages before installing *ProxySQL 2.x.x* to upgrade ProxySQL. 

=== "Upgrade between minor ProxySQL 2 versions"

    Installing a later version automatically upgrades an earlier version *ProxySQL 2.x.x*.

!!! admonition "See also" 

    [Install ProxySQL 2.x.x and the admin utilities](install-v2.md)
