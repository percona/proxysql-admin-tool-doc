# 2.0.3 and {#proxysql-release-notes-2.0.3}

Date

:   May 7, 2019

Installation

:   

2.0.3, released by [ProxySQL](), is now available for download in the
[Percona repository]() along with an updated version of 's tool.

is a high-performance proxy, currently for , and database servers in the
ecosystem (like and ). It acts as an intermediary for client requests
seeking resources from the database. created for DBAs as a means of
solving complex replication topology issues.

The 2.0.3 source and binary packages available from the [Percona
download page for ProxySQL 2.0]() include -- a tool developed by to
configure nodes into . images for release 2.0.3 are available as well.
You can [download the original ProxySQL from GitHub](). offers the
[ProxySQL documentation in the wiki format]().

With 2.0.3, now uses the native support for and does not require custom
bash scripts to keep track of status. As a result, and have been
removed.

**Improvements**

-   The tool is 8.0 compatible

**New features**

-   New option to use for connections between and the backend database
    servers New option to determine the maximum number of writesets that
    can be queued before the node is *SHUNNED* to avoid stale reads. The
    default value is *100*.
-   New operation to update the cluster membership by adding server
    nodes as found. (Note that nodes are added but not removed). The
    option may be used to specify which galera hostgroup to update. The
    option instructs to remove all servers from the table before
    updating the cluster. Hostgroups can now be specified on the
    command-line: , , , and . Previously, these host groups were only
    read from the configuration file.
-   The and options used simultaneously have special meaning. If the
    cluster has not been enabled, then is run. If the cluster has
    already been enabled, then is run.
-   New command to see if a cluster has been enabled. This command
    checks for the existence of a row in the table. may be used to
    specify the writer hostgroup used to search the table.
-   New command to display galera hostgroup information. This command
    lists all rows in the current table as well as all servers that
    belong to these hostgroups. With the option, only the information
    for the galera hostgroup with that writer hostgroup is displayed.

**Changed features**

-   Setting now changes the global variable Note that this is a global
    variable, not a per-cluster variable.
-   The option now takes only a single address as a parameter. In the
    singlewrite mode we only set the weight if specifies address:port. A
    priority list of addresses is no longer accepted.
-   The option option now accepts a different set of values. Due to
    changes in the behavior of between version 1.4 and version 2.0
    related to support, the values of have been changed. This option now
    accepts the following values: yes, no, and backup.

    yes:

    :   writers, backup-writers, and read-only nodes can act as readers.

    no:

    :   only read-only nodes can act as readers.

    backup:

    :   only backup-writers can act as readers.
-   The commands , , , and can now use the option.
-   The command removes all users associated with the galera cluster
    hostgroups. Previously, this command only removed the users with the
    .
-   The command now accepts the option to disable the cluster associated
    with that hostgroup overriding the value specified in the
    configuration file.

**Removed features**

-   Asynchronous slave reader support has been removed: the option is
    not supported.
-   A list of nodes in the priority order is no longer supported. Only a
    single node is supported at this time.
-   Since the and scripts are no longer run in , automatic cluster
    membership updates are not supported.
-   Checking the variable is no longer supported
-   Using desynced nodes if no other nodes are available is no longer
    supported.
-   The server status is no longer maintained in the table.

**Limitations**

-   With set to *backup*, read-only nodes are not allowed. This a
    limitation of 2.0. Note that *backup* is the default value of when
    equals to *singlewrite*

is available under .
