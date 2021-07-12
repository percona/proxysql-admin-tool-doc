# 2.0.14 and {#proxysql-release-notes-2.0.14}

Date

:   September 24, 2020

Installation

:   

2.0.14, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 2.0.14 source and binary packages available from the [Percona
download page for ProxySQL 2.0]() include -- a tool developed by to
configure nodes into . images for release 2.0.14 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

This release includes 2.0.14 which fixes many bugs and introduces a
number of features and enhancements. For more information see:

<https://github.com/sysown/proxysql/releases/tag/v2.0.14>

**Improvements**

-   `PSQLADM-256`{.interpreted-text role="jira"}: Wrong password with %
    character

is available under .
