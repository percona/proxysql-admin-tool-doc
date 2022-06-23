# ProxySQL, proxysql-admin, and percona-scheduler-admin documentation

[ProxySQL](https://www.proxysql.com/) is a tool that performs like a proxy between **Percona XtraDB Cluster** and your client application. *ProxySQL* manages a connection pool, which caches your connections and keeps the connections open for future requests. *ProxySQL* is designed to run continuously without being restarted.

Without a connection pool, each SQL request opens a connections to the remote node. When the SQL request is complete, the connection is closed. A new one is opened on the next SQL request.

ProxySQL maintains the connection pool. The pool allows a certain number of connections to remain open. A connection is reused or closed if not reused within a certain time period. You connect to the proxy and the tool forwards your requests to the cluster.

*ProxySQL* runs as a daemon watched by a monitoring process which can restart *ProxySQL* in case of an unexpected exit to minimize downtime. The daemon accepts incoming traffic from *MySQL* clients and forwards the traffic to backend *MySQL* servers.

The configuration options include runtime parameters, server grouping, and traffic-related parameters. Many of the settings can be done at runtime using queries that are similar to SQL statements.

THe [ProxySQL documentation](https://proxysql.com/documentation/) provides information on installing and running ProxySQL.

*ProxySQL* is available from the **Percona** software repositories in the following versions:

## ProxySQL 1.x.x and the proxysql-admin tool

*ProxySQL* 1.x.x does not natively support **Percona XtraDB Cluster**. This
version requires custom bash scripts to track the status of **Percona XtraDB Cluster** nodes using the *ProxySQL* scheduler.

* [Using ProxySQL 1.x.x with ProxySQL Admin](proxysql-v1.md)

* [Installing ProxySQL 1.x.x](proxysql-v1.md#installing-proxysql-1-x-x)

* [Automatic Configuration](proxysql-v1.md#automatic-configuration)

* [Install *ProxySQL* 1.X from a binary tarball](tarball-v1.md)

* [Configuring *ProxySQL*](configuring.md)

* [Assisted Maintenance Mode](configuring.md#assisted-maintenance-mode)

## Install ProxySQL 2.x.x and admin tools

Installation procedures for *ProxySQL* 2.x.x, proxysql-admin tool, and Percona
Scheduler admin.

* [Install ProxySQL 2.x.x and admin tools](install-v2.md)


    * [Using a package manager](install-v2.md#using-a-package-manager)

* [Install *ProxySQL* 2.x.x from a binary tarball](installing-tarball.md)


    * [Available tar files for ProxySQL 2.3.2-1.2 and higher](installing-tarball.md#available-tar-files-for-proxysql-2-3-2-1-2-and-higher)

    * [Available tar files from ProxySQL 2.0.15 to ProxySQL 2.3.2](installing-tarball.md#available-tar-files-from-proxysql-2-0-15-to-proxysql-2-3-2)

    * [ProxySQL 2.0.14 or higher extraction commands](installing-tarball.md#proxysql-2-0-14-or-higher-extraction-commands)

    * [ProxySQL 2.0.13 or lower extraction commands](installing-tarball.md#proxysql-2-0-13-or-lower-extraction-commands)


    * [Starting ProxySQL](installing-tarball.md#starting-proxysql)

* [Build the Percona Scheduler admin tool](psa-build.md)

## Start, Stop, Upgrade, and Uninstall ProxySQL 2.x.x

* [Starting and Stopping ProxySQL](psql-process.md)

    * [Starting ProxySQL 2.x.x](psql-process.md#starting-proxysql-2-x-x)

    * [Stopping ProxySQL 2.x.x](psql-process.md#stopping-proxysql-2-x-x)

* [Upgrading from an earlier version](upgrade-psql.md)

* [Uninstalling ProxySQL 2.x.x](uninstall-psql.md)

## Use the ProxySQL 2.x.x and proxysql-admin tool

The **proxysql-admin** tool in version 2.X natively supports **Percona XtraDB Cluster**. This version does not need custom scripts to track the cluster status.

* [Summary of ProxySQL 2.x changes in the **proxysql-admin** tool](proxysql-changes.md)

    * [Added Features](proxysql-changes.md#added-features)

    * [Changed Features](proxysql-changes.md#changed-features)

    * [Removed Features](proxysql-changes.md#removed-features)

    * [Limitations](proxysql-changes.md#limitations)

* [*ProxySQL* 2.x and proxysql-admin utility](v2-config.md)

    * [The proxysql-admin options](v2-config.md#the-proxysql-admin-options)

    * [Preparing the configuration file](v2-config.md#preparing-the-configuration-file)

    * [Configuring the proxysql-admin login](v2-config.md#configuring-the-proxysql-admin-login)

    * [Example of the proxysql-admin file](v2-config.md#example-of-the-proxysql-admin-file)

    * [Create the login file](v2-config.md#create-the-login-file)

    * [Verifying the login file](v2-config.md#verifying-the-login-file)

* [The proxysql-admin functions](psql-functions.md)

    * [–sync-multi-cluster-users](psql-functions.md#sync-multi-cluster-users)

    * [–add-query-rule](psql-functions.md#add-query-rule)

    * [–quick-demo](psql-functions.md#quick-demo)

    * [–is-enabled](psql-functions.md#is-enabled)

    * [–update-mysql-version](psql-functions.md#update-mysql-version)

    * [–mode](psql-functions.md#mode)

    * [–node-check-interval](psql-functions.md#node-check-interval)

    * [–write-node](psql-functions.md#write-node)

## Use the ProxySQL 2.x.x and Percona Scheduler Admin tool

Implemented in version 2.3.2-1, the Percona Scheduler Admin tool can be used to automatically perform a failover due to node failures, service degradation, or maintenance.

* [ProxySQL 2.x.x and Percona Scheduler Admin tool](psa-scheduler.md)

    * [Prerequisites](psa-scheduler.md#prerequisites)

* [Percona Scheduler Admin configuration file](psa-config.md)

    * [Example of a configuration file](psa-config.md#example-of-a-configuration-file)

* [Percona Scheduler Admin Statements and Options](psa-ref.md)

    * [Statement reference](psa-ref.md#statement-reference)

    * [Option Reference](psa-ref.md#option-reference)

* [Option Details](psa-options.md)

    * [–add-query-rule](psa-options.md#add-query-rule)

    * [–adduser](psa-options.md#adduser)

    * [–auto-assign-weights](psa-options.md#auto-assign-weights)

    * [–disable / -d](psa-options.md#disable-d)

    * [–enable / -e](psa-options.md#enable-e)

    * [–force](psa-options.md#force)

    * [–is-enabled](psa-options.md#is-enabled)

    * [–server](psa-options.md#server)

    * [–status](psa-options.md#status)

    * [–sync-multi-cluster-users](psa-options.md#sync-multi-cluster-users)

    * [–syncusers](psa-options.md#syncusers)

    * [–update-cluster](psa-options.md#update-cluster)

    * [–update-mysql-version](psa-options.md#update-mysql-version)

    * [–update-read-weight](psa-options.md#update-read-weight)

    * [–update-write-weight](psa-options.md#update-write-weight)

    * [–write-node](psa-options.md#write-node)

* [Percona Scheduler Admin tool known limitations](psa-known-limitations.md)

    * [Do not combine the following options](psa-known-limitations.md#do-not-combine-the-following-options)

    * [Log file or lock file locations](psa-known-limitations.md#log-file-or-lock-file-locations)

## Release notes for ProxySQL v2.x and ProxySQL v1.4.x

* [Release notes of ProxySQL, proxysql-admin, and percona-scheduler-admin](release-notes.md)

2022, Percona LLC and/or its affiliates 2009-2022

<!-- `Docker` replace:: Docker -->
<!-- `MariaDB` replace:: MariaDB -->
<!-- `MySQL` replace:: MySQL -->
<!-- `--disable` replace:: `--disable` -->
<!-- **Percona** replace:: Percona -->
<!-- `ProxySQL Admin` replace:: **ProxySQL Admin** -->
<!-- `ProxySQL scheduler` replace:: ProxySQL scheduler -->
<!-- *ProxySQL* replace:: *ProxySQL* -->
<!-- **Percona Server for MySQL** replace:: Percona Server for MySQL -->
<!-- **Percona XtraDB Cluster** replace:: Percona XtraDB Cluster -->
