# 1.4.7 and {#proxysql-release-notes-1.4.7}

Date

:   April 16, 2018

Installation

:   

1.4.7, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 1.4.7 source and binary packages available from the [Percona
download page for ProxySQL]() include -- a tool developed by to
configure nodes into . images for release 1.4.7 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

**Usability improvements**

-   Added tool to dump configuration and statistics.

**Bug fixes**

-   `PSQLADM-2`{.interpreted-text role="jira"}: script didn't check if
    another instance of itself is already running. While running more
    then one copy of in the same runtime environment at the same time is
    still not supported, the introduced fix is able to prevent duplicate
    script execution in most cases.
-   `PSQLADM-40`{.interpreted-text role="jira"}: generated a lot of and
    processes in case of wrong ProxySQL credentials in file.
-   `PSQLADM-41`{.interpreted-text role="jira"}: Timeout error handling
    was improved with clear messages.
-   `PSQLADM-42`{.interpreted-text role="jira"}: An inconsistency of the
    date format in and scripts was fixed.
-   `PSQLADM-43`{.interpreted-text role="jira"}: didn't take into
    account the possibility of special characters presence in .
-   `PSQLADM-44`{.interpreted-text role="jira"}: generated unclear
    errors in the file if wrong credentials where passed.
-   `PSQLADM-46`{.interpreted-text role="jira"}: script incorrectly
    split the hostname and the port number in URLs containing hyphen
    character.

is available under .
