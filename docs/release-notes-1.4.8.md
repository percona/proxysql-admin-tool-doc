# 1.4.8 and {#proxysql-release-notes-1.4.8}

Date

:   May 22, 2018

Installation

:   

1.4.8, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 1.4.8 source and binary packages available from the [Percona
download page for ProxySQL]() include -- a tool developed by to
configure nodes into . images for release 1.4.8 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

**Usability improvement**

-   `PSQLADM-84`{.interpreted-text role="jira"}: Now tool dumps
    [host_priority]{.title-ref} and . Also output format was changed.

**Other improvements and bug fixes**

-   `PSQLADM-66`{.interpreted-text role="jira"}: The option now makes to
    update the user's password in database if there is any password
    difference between user and user.
-   `PSQLADM-45`{.interpreted-text role="jira"}: it was unclear from the
    help screen, that option requires an argument.
-   `PSQLADM-48`{.interpreted-text role="jira"}:
    [\${PROXYSQL_DATADIR}/\${CLUSTER_NAME}\_mode]{.title-ref} file was
    not created at upgrade (1.4.5 or before to 1.4.6 onwards).
-   `PSQLADM-52`{.interpreted-text role="jira"}: The script was not
    checking empty query rules.
-   `PSQLADM-54`{.interpreted-text role="jira"}: did not change status
    properly for the coming back online nodes.

is available under .
