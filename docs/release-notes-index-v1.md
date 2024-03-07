#

## Release Notes for Version 1

### ProxySQL 1.4.16 and proxysql-admin (2020-02-11)

- **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

_ProxySQL_ release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

_ProxySQL_ is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created _ProxySQL_ for DBAs as a means of solving
complex replication topology issues.

The _ProxySQL_ 1.4.16 source and binary packages are available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include **ProxySQL Admin** – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into _ProxySQL_. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). _ProxySQL_ offers the [ProxySQL documentation](https://proxysql.com/documentation/).

#### Bugs Fixed

- [PSQLADM-219](https://jira.percona.com/browse/PSQLADM-219): The [ProxySQL scheduler](https://github.com/sysown/proxysql/blob/master/doc/scheduler.md) was handling the `pxc_maint_mode` variable incorrectly. As a result, open connections were closed immediately. This bug has been fixed and now the ProxySQL scheduler only sets the node status to `OFFLINE_SOFT`. This prevents opening new connections and lets the already established connections finish their work. It is up to the user to decide when it is safe to start the node maintenance.

_ProxySQL_ is available under Open Source license GPLv3.

### ProxySQL 1.4.12 and proxysql-admin (2018-11-13)

- **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

_ProxySQL_ release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

_ProxySQL_ is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created _ProxySQL_ for DBAs as a means of solving
complex replication topology issues.

The _ProxySQL_ 1.4.12 source and binary packages are available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include **ProxySQL Admin** – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into _ProxySQL_. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). _ProxySQL_ offers the [ProxySQL documentation](https://proxysql.com/documentation/).

#### Improvements

- [PSQLADM-68](https://jira.percona.com/browse/PSQLADM-68): Scripts are now compatible with _Percona XtraDB Cluster (PXC)_ hosts using IPv6

- [PSQLADM-107](https://jira.percona.com/browse/PSQLADM-107): In include-slaves, a slave would always be moved into the write hostgroup even if the whole cluster went down. A new option –use-slave-as-writer specifies whether or not the slave is added to the write hostgroup.

#### Bugs Fixed

- [PSQLADM-110](https://jira.percona.com/browse/PSQLADM-110): In some cases, pattern cluster hostname did not work with proxysql-admin.

- [PSQLADM-104](https://jira.percona.com/browse/PSQLADM-104): proxysql-admin testsuite bug fixes.

- [PSQLADM-113](https://jira.percona.com/browse/PSQLADM-113): `proxysql_galera_checker` assumed that parameters were given in the long format.

- [PSQLADM-114](https://jira.percona.com/browse/PSQLADM-114): In some cases, _ProxySQL_ could not be started

- [PSQLADM-115](https://jira.percona.com/browse/PSQLADM-115): `proxysql_node_monitor` could fail with more than one command in the ProxySQL scheduler.

- [PSQLADM-116](https://jira.percona.com/browse/PSQLADM-116): In some cases, the ProxySQL scheduler was reloading servers on every run

- [PSQLADM-117](https://jira.percona.com/browse/PSQLADM-117): The `–syncusers` option did not work when enabling cluster

- [PSQLADM-125](https://jira.percona.com/browse/PSQLADM-125): The check-is-galera-checker-running function was not preventing multiple instances of the script from running.

Other bugs fixed: [PSQLADM-112](https://jira.percona.com/browse/PSQLADM-112), [PSQLADM-120](https://jira.percona.com/browse/PSQLADM-120)

_ProxySQL_ is available under Open Source license GPLv3.

### ProxySQL 1.4.8 and proxysql-admin (2018-05-22)

- **Installation**

  [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

_ProxySQL_ release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

_ProxySQL_ is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created _ProxySQL_ for DBAs as a means of solving
complex replication topology issues.

The _ProxySQL_ 1.4.8 source and binary packages are available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into _ProxySQL_. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). _ProxySQL_ offers the [ProxySQL documentation](https://proxysql.com/documentation/).

#### Usability improvement

- [PSQLADM-84](https://jira.percona.com/browse/PSQLADM-84): Now proxysql_status tool dumps host_priority
  and /etc/proxysql-admin.cnf. Also output format was changed.

#### Other improvements and bug fixes

- [PSQLADM-66](https://jira.percona.com/browse/PSQLADM-66): The `–syncusers` option now makes ProxySQL Admin to
  update the user’s password in _ProxySQL_ database if there is any password difference between _ProxySQL_ user and MySQL user.

- [PSQLADM-45](https://jira.percona.com/browse/PSQLADM-45): it was unclear from the help screen, that
  `–config-file` option requires an argument.

- [PSQLADM-48](https://jira.percona.com/browse/PSQLADM-48): `${PROXYSQL_DATADIR}/${CLUSTER_NAME}`\_mode file was not
  created at ProxySQL Admin upgrade (1.4.5 or before to 1.4.6 onwards).

- [PSQLADM-52](https://jira.percona.com/browse/PSQLADM-52): The _proxysql_galera_checker_ script was not
  checking empty query rules.

- [PSQLADM-54](https://jira.percona.com/browse/PSQLADM-54): `proxysql_node_monitor` did not change
  OFFLINE_HARD status properly for the coming back online nodes.

_ProxySQL_ is available under Open Source license GPLv3.

### ProxySQL 1.4.7 and proxysql-admin (2018-04-16)

- **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

_ProxySQL_ release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

_ProxySQL_ is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created _ProxySQL_ for DBAs as a means of solving
complex replication topology issues.

The _ProxySQL_ 1.4.7 source and binary packages available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into _ProxySQL_. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). _ProxySQL_ offers the [ProxySQL documentation](https://proxysql.com/documentation/).

#### Usability improvements

- Added `proxysql_status` tool to dump _ProxySQL_ configuration and statistics.

#### Bug fixes

- [PSQLADM-2](https://jira.percona.com/browse/PSQLADM-2): `proxysql_galera_checker` script didn’t check if
  another instance of itself is already running. While running more then one
  copy of `proxysql_galera_checker` in the same runtime environment at
  the same time is still not supported, the introduced fix is able to prevent
  duplicate script execution in most cases.

- [PSQLADM-40](https://jira.percona.com/browse/PSQLADM-40): ProxySQL scheduler generated a lot of
  `proxysql_galera_checker` and `proxysql_node_monitor` processes in case of wrong ProxySQL credentials in `/etc/proxysql-admin.cnf` file.

- [PSQLADM-41](https://jira.percona.com/browse/PSQLADM-41): Timeout error handling was improved with clear messages.

- [PSQLADM-42](https://jira.percona.com/browse/PSQLADM-42): An inconsistency of the date format in _ProxySQL_ and scripts was fixed.

- [PSQLADM-43](https://jira.percona.com/browse/PSQLADM-43): `proxysql_galera_checker` didn’t take into account
  the possibility of special characters presence in mysql-monitor_password.

- [PSQLADM-44](https://jira.percona.com/browse/PSQLADM-44): `proxysql_galera_checker` generated unclear errors
  in the `/etc/proxysql.log` file if wrong credentials where passed.

- [PSQLADM-46](https://jira.percona.com/browse/PSQLADM-46): `proxysql_node_monitor` script incorrectly split
  the hostname and the port number in URLs containing hyphen character.

_ProxySQL_ is available under Open Source license GPLv3.

### ProxySQL 1.4.6 and proxysql-admin (2018-03-12)

- **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

_ProxySQL_ release, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

_ProxySQL_ is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created _ProxySQL_ for DBAs as a means of solving
complex replication topology issues.

The _ProxySQL_ 1.4.6 source and binary packages available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into _ProxySQL_. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). _ProxySQL_ offers the [ProxySQL documentation](https://proxysql.com/documentation/).

#### Usability improvements

- [PSQLADM-32](https://jira.percona.com/browse/PSQLADM-32): Now, proxysql-admin script can configure
  multiple clusters in _ProxySQL_, when there are unique cluster names specified
  by the wsrep*cluster_name option, and the /etc/proxysql-admin.cnf
  configuration contains different \_ProxySQL* READ/WRITE hostgroup and different
  application user for each cluster. Currently multiple clusters support is not
  compatible with host priority feature, which works only with a single cluster.

- [PSQLADM-81](https://jira.percona.com/browse/PSQLADM-81): The new version substantially increases the number of test cases
  in the ProxySQL Admin test-suite.

#### Bug fixes

- [PSQLADM-35](https://jira.percona.com/browse/PSQLADM-35): proxysql_galera_checker monitoring script was
  unable to discover new writer nodes.

- [PSQLADM-36](https://jira.percona.com/browse/PSQLADM-36): upgrade to _ProxySQL_ 1.4.6 from the previous version
  was broken.

- [PSQLADM-79](https://jira.percona.com/browse/PSQLADM-79): Fixed by properly quoting the MONITOR_USERNAME environment
  variable in the admin script query.

_ProxySQL_ is available under Open Source license GPLv3.

### ProxySQL 1.4.5 and proxysql-admin (2018-02-15)

- **Installation**:[https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

_ProxySQL_ 1.4.5, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s
**proxysql-admin** tool.

_ProxySQL_ is a high-performance proxy, currently for MySQL, and database
servers in the _MySQL_ ecosystem (like **Percona Server for MySQL** and _MariaDB_). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created _ProxySQL_ for DBAs as a means of solving
complex replication topology issues.

The _ProxySQL_ 1.4.5 source and binary packages are available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into _ProxySQL_. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). _ProxySQL_ offers the [ProxySQL documentation](https://proxysql.com/documentation/).

- [PSQLADM-6](https://jira.percona.com/browse/PSQLADM-6): If the cluster node goes offline, the proxysql*node_monitor
  script now sets the node status as OFFLINE_HARD, and does not remove it from the \_ProxySQL* database. Also, logging is consistent regardless of the cluster node online status.

- [PSQLADM-30](https://jira.percona.com/browse/PSQLADM-30): Validation was added for the host priority file.

- [PSQLADM-33](https://jira.percona.com/browse/PSQLADM-33): Added –proxysql-datadir option to run the proxysql-admin script with a custom _ProxySQL_ data directory.

- Also, BATS test suite was added for the proxysql-admin testing.

#### Bug fixes

- [PSQLADM-5](https://jira.percona.com/browse/PSQLADM-5): _Percona XtraDB Cluster (PXC)_ mode specified with proxysql-admin with use of `–mode` parameter was not persistent.

- [PSQLADM-8](https://jira.percona.com/browse/PSQLADM-8): _ProxySQL_ High CPU load took place when mysqld was hanging.

_ProxySQL_ is available under Open Source license GPLv3.

### ProxySQL 1.4.4 and proxysql-admin (2018-01-18)

- **Installation**: [https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/proxysql-v1.html#installing-proxysql-v1)

_ProxySQL_ 1.4.4, released by [ProxySQL](https://www.proxysql.com/), is now available for download in
the [Percona repository](https://www.percona.com/software/percona-software-repositories-for-mysql) along with an updated version of **Percona**’s **proxysql-admin** tool.

_ProxySQL_ is a high-performance proxy, currently for MySQL, and database
servers in the MySQL ecosystem (like **Percona Server for MySQL** and MariaDB). It acts as an
intermediary for client requests seeking resources from the
database. René Cannaò created _ProxySQL_ for DBAs as a means of solving
complex replication topology issues.

The _ProxySQL_ 1.4.4 source and binary packages are available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include ProxySQL Admin – a tool developed by
**Percona** to configure **Percona XtraDB Cluster** nodes into _ProxySQL_. Docker images are available as well. You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases). _ProxySQL_ offers the [ProxySQL documentation](https://proxysql.com/documentation/).

#### This release fixes the following bugs in ProxySQL Admin

- [PXC-892](https://jira.percona.com/browse/PXC-892): proxysql-admin was unable to recognize IP
  address of localhost.

- [PXC-893](https://jira.percona.com/browse/PXC-893): proxysql-admin couldn’t interpret passwords with
  special characters correctly, such as ‘$’

- [PSQLADM-3](https://jira.percona.com/browse/PSQLADM-3): proxysql_node_monitor script had writer/reader hostgroup
  conflict issue.

- [PQA-155](https://jira.percona.com/browse/PQA-155): Runtime table was not updated in case of any changes in
  Percona XtraDB Cluster membership.

- [BLD-853](https://jira.percona.com/browse/BLD-853): _ProxySQL_ logrotate script did not work properly,
  producing empty /etc/proxysql.log after logrotate.

_ProxySQL_ is available under Open Source license GPLv3.
