# ProxySQL 1.4.4 and **proxysql-admin**

Date:   January 18, 2018

Installation: [Install ProxySQL 1.x.x](https://docs.percona.com/proxysql/proxysql-v1.html#installing-proxysql-v1)

*ProxySQL* 1.4.4, released by [ProxySQL](www.proxysql.com), is now available for download in the
[Percona repository](https://www.percona.com/downloads/proxysql/) along with an updated version of Percona's **proxysql-admin** tool.

ProxySQL is a high-performance proxy, currently for *MySQL*, and database servers in the *MySQL*
ecosystem (like *Percona Server for MySQL* and *MariaDB*). It acts as an intermediary for client requests
seeking resources from the database. René Cannaò created *ProxySQL* for DBAs as a means of
solving complex replication topology issues.

The *ProxySQL* 1.4.4 source and binary packages available from the [Percona
download page for ProxySQL](https://percona.com/downloads/proxysql) include **ProxySQL Admin** -- a tool developed by Percona to configure *Percona XtraDB Cluster* nodes into ProxySQL. *Docker* images for release 1.4.4 are available as well.
You can [download the original ProxySQL from GitHub](https://github.com/sysown/proxysql/releases/tag/v1.4.4). ProxySQL offers the
[ProxySQL documentation](https://proxysql.com/documentation/).

## **This release fixes the following bugs in ProxySQL Admin**

- [PXC-892](https://jira.percona.com/browse/PXC-892): ProxySQL Admin was unable to recognize IP
    address of localhost.
- [PXC-893](https://jira.percona.com/browse/PXC-893): ProxySQL Admin couldn't interpret
    passwords with special characters correctly, such as '\$'
- [PSQLADM-3](https://jira.percona.com/browse/PSQLADM-3): proxysql_node_monitor
    script had writer/reader hostgroup conflict issue.
- [PQA-155](https://jira.percona.com/browse/PQA-155): Runtime table was not
    updated in case of any changes in Percona XtraDB Cluster membership.
- [BLD-853](https://jira.percona.com/browse/BLD-853): The ProxySQL logrotate script did not
    work properly, producing empty proxysql-log after logrotate.

ProxySQL is available under Open Source license GPLv3.
