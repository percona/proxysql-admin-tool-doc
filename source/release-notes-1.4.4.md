# 1.4.4 and {#proxysql-release-notes-1.4.4}

Date

:   January 18, 2018

Installation

:   

1.4.4, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 1.4.4 source and binary packages available from the [Percona
download page for ProxySQL]() include -- a tool developed by to
configure nodes into . images for release 1.4.4 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

**This release fixes the following bugs in**

-   `PXC-892`{.interpreted-text role="jira"}: was unable to recognize IP
    address of localhost.
-   `PXC-893`{.interpreted-text role="jira"}: couldn't interpret
    passwords with special characters correctly, such as '\$'
-   `PSQLADM-3`{.interpreted-text role="jira"}: proxysql_node_monitor
    script had writer/reader hostgroup conflict issue.
-   `PQA-155`{.interpreted-text role="jira"}: Runtime table was not
    updated in case of any changes in Percona XtraDB Cluster membership.
-   `BLD-853`{.interpreted-text role="jira"}: logrotate script did not
    work properly, producing empty after logrotate.

is available under .
