In an MySQL 8.4 or Percona Server for MySQL 8.4 environment, you may have the following issues:

* ProxySQL contains counters that have not been updated to use the new terminology. Unexpected results may occur
* The binlog reader errors out during initialization due to the use of the old terminology, such as SHOW MASTER STATUS command.