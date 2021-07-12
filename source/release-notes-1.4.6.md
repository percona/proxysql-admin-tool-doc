# 1.4.6 and {#proxysql-release-notes-1.4.6}

Date

:   March 12, 2018

Installation

:   

1.4.6, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 1.4.6 source and binary packages available from the [Percona
download page for ProxySQL]() include -- a tool developed by to
configure nodes into . images for release 1.4.6 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

**Usability improvements**

-   `PSQLADM-32`{.interpreted-text role="jira"}: Now, script can
    configure multiple clusters in , when there are unique cluster names
    specified by the wsrep_cluster_name option, and the configuration
    contains different READ/WRITE hostgroup and different application
    user for each cluster. Currently multiple clusters support is not
    compatible with host priority feature, which works only with a
    single cluster.
-   `81`{.interpreted-text role="jira"}: The new version substantially
    increases the number of test cases in the test-suite.

**Bug fixes**

-   `PSQLADM-35`{.interpreted-text role="jira"}: monitoring script was
    unable to discover new writer nodes.
-   `PSQLADM-36`{.interpreted-text role="jira"}: upgrade to 1.4.6 from
    the previous version was broken.
-   `PSQLADM-79`{.interpreted-text role="jira"}: Fixed by properly
    quoting the MONITOR_USERNAME environment variable in the admin
    script query.

is available under .
