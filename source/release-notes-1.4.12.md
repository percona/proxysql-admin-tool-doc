# 1.4.12 and {#proxysql-release-notes-1.4.12}

Date

:   November 13, 2018

Installation

:   

1.4.12, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 1.4.12 source and binary packages available from the [Percona
download page for ProxySQL]() include -- a tool developed by to
configure nodes into . images for release 1.4.12 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

**Improvements**

-   `PSQLADM-68`{.interpreted-text role="jira"}: Scripts are now
    compatible with hosts using IPv6
-   `PSQLADM-107`{.interpreted-text role="jira"}: In include-slaves, a
    slave would always be moved into the write hostgroup even if the
    whole cluster went down. A new option specifies whether or not the
    slave is added to the write hostgroup.

**Bugs Fixed**

-   `PSQLADM-110`{.interpreted-text role="jira"}: In some cases, pattern
    cluster hostname did not work with .
-   `PSQLADM-104`{.interpreted-text role="jira"}: testsuite bug fixes.
-   `PSQLADM-113`{.interpreted-text role="jira"}: assumed that
    parameters were given in the long format.
-   `PSQLADM-114`{.interpreted-text role="jira"}: In some cases, could
    not be started
-   `PSQLADM-115`{.interpreted-text role="jira"}: could fail with more
    than one command in the .
-   `PSQLADM-116`{.interpreted-text role="jira"}: In some cases, the was
    reloading servers on every run
-   `PSQLADM-117`{.interpreted-text role="jira"}: The option did not
    work when enabling cluster
-   `PSQLADM-125`{.interpreted-text role="jira"}: The function was not
    preventing multiple instances of the script from running.

Other bugs fixed: `PSQLADM-112`{.interpreted-text role="jira"},
`PSQLADM-120`{.interpreted-text role="jira"}

is available under .
