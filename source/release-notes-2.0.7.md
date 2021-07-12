# 2.0.7 and {#proxysql-release-notes-2.0.7}

Date

:   October 23, 2019

Installation

:   

2.0.7, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 2.0.7 source and binary packages available from the [Percona
download page for ProxySQL 2.0]() include -- a tool developed by to
configure nodes into . images for release 2.0.7 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

This release includes 2.0.7 which fixes many bugs and introduces a
number of features and enhancements. For more information see:

The tool now supports 10.4.

**New Features**

-   `PSQLADM-204`{.interpreted-text role="jira"}: Add support of 10.4

**Improvements**

-   `PSQLADM-195`{.interpreted-text role="jira"}: A new option has been
    added to the script to display the [\*\_reset]{.title-ref} tables
    from the [stats]{.title-ref} database. If this option is not
    specified, these tables are not displayed by default.

**Bugs fixed**

-   `PSQLADM-157`{.interpreted-text role="jira"}: In some cases, the
    script used the cat command to display a file without checking if
    the file existed and was readable.
-   `PSQLADM-181`{.interpreted-text role="jira"}: When run with set to
    [\<node_name\>]{.title-ref}, now verifies that the writer nodes are
    not read-only.

is available under .
