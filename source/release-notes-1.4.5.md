# 1.4.5 and {#proxysql-release-notes-1.4.5}

Date

:   February 15, 2018

Installation

:   

1.4.5, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 1.4.5 source and binary packages available from the [Percona
download page for ProxySQL]() include -- a tool developed by to
configure nodes into . images for release 1.4.5 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

**Usability improvements**

-   `PSQLADM-6`{.interpreted-text role="jira"}: If the cluster node goes
    offline, the script now sets the node status as , and does not
    remove it from the database. Also, logging is consistent regardless
    of the cluster node online status.
-   `PSQLADM-30`{.interpreted-text role="jira"}: Validation was added
    for the host priority file.
-   `PSQLADM-33`{.interpreted-text role="jira"}: Added option to run the
    script with a custom data directory.
-   Also, BATS test suite was added for the testing.

**Bug fixes**

-   `PSQLADM-5`{.interpreted-text role="jira"}: mode specified with with
    use of parameter was not persistent.
-   `PSQLADM-8`{.interpreted-text role="jira"}: High CPU load took place
    when was hanging.

is available under .
