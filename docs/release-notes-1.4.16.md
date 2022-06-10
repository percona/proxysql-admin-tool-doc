# 1.4.16 and {#proxysql-release-notes-1.4.16}

Date

:   February 11, 2020

Installation

:   

1.4.16, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 1.4.16 source and binary packages available from the [Percona
download page for ProxySQL]() include -- a tool developed by to
configure nodes into . images for release 1.4.16 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

**Bugs Fixed**

-   `PSQLADM-219`{.interpreted-text role="jira"}: The [ProxySQL
    scheduler]() was handling the variable incorrectly. As a result,
    open connections were closed immediately. This bug has been fixed
    and now the only sets the node status to . This prevents opening new
    connections and lets the already established connections finish
    their work. It is up to the user to decide when it is safe to start
    the node maintenance.

is available under .
