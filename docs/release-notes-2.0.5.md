# 2.0.5 and {#proxysql-release-notes-2.0.5}

Date

:   October 23, 2019

Installation

:   

2.0.5, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 2.0.5 source and binary packages available from the [Percona
download page for ProxySQL 2.0]() include -- a tool developed by to
configure nodes into . images for release 2.0.5 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

This release includes 2.0.5 which fixes many bugs and introduces a
number of features and enhancements. For more information see:

The tool has been enhanced to support the following new options and
commands:

  Option      Description
  ----------- ----------------------------------------------------------------------------------------------------------------------------------------
              Creates query rules for synced users. This option is only applicable for the singlewrite mode and works together with the and options.
              
  (command)   Updates the variable in with the version from a node in .

**Improvements**

-   `PSQLADM-49`{.interpreted-text role="jira"}: Create rules for . When
    running with or , the option can now be specified to add the
    singlewriter query rules for the new users.
-   `PSQLADM-51`{.interpreted-text role="jira"}: Update variable. The
    command has been added to set the global variable in ProxySQL. This
    will take the version from a node in the cluster and set it in .

**Bugs fixed**

-   `PSQLADM-190`{.interpreted-text role="jira"}: The option did not
    work on enable. When running with proxysql-cluster, the galera
    hostgroups information was not replicated, which could result in
    failing to run on a different node. The option was added for to be
    able to ignore any errors and always configure the cluster.
-   `PSQLADM-199`{.interpreted-text role="jira"}: query-rules removed
    during proxysql-cluster creation with operator. When using the
    operator for and creating a proxysql-cluster, the query rules could
    be removed. The code was modified to merge the query rules (rather
    than deleting and recreating). If the option was specified, then a
    warning was issued in case any existing rules were found; otherwise
    an error was issued. The option was added to ensure that cluster
    updates did not interfere with the current command.
-   `PSQLADM-200`{.interpreted-text role="jira"}: users were not created
    for with operator. When using the operator for , the command was run
    but the table was not updated. The fix for
    `PSQLADM-199`{.interpreted-text role="jira"} that suggested to use
    also applies here.

is available under .
