# ProxySQL 2.x.x and Percona Scheduler Admin tool

[*ProxySQL* 2.3.2-1.2](release-notes-2.3.2-1.md) adds the Percona Scheduler Admin (percona-scheduler-admin) tool. This tool has a segment-aware failover mechanism and can automatically perform a failover due to node failures, service degradation, or maintenance requirements. The external scheduler has the following qualities:

* Capable of parallel query execution on nodes which results in faster failover or fallback

* Supports fallback

* Supports promoting a reader to primary with the following conditions are met:

  * wsrep_on=OFF

  * wsrep_sst_donor_rejects_queries is set when, for example, connections are rejected due to an ongoing state transfer

* Supports a retry of operations in case of network glitches

!!! important

    Percona Scheduler Admin was built for a different purpose and has different features than [proxy-admin](proxysql-admin-tool-v2-config.md). You cannot use the options from one admin tool in the other admin tool. Combining the options causes unintended results.

## Version changes

The Percona Scheduler Admin tool has been tested with ProxySQL 2.3.0, 2.3.2-1.2, and later versions.

[*ProxySQL* 2.4.2](2.4.2.md) add the following checks:

  When `pxc_scheduler_handler` launches, the application creates a lock file to prevent the running of multiple instances. Prior to *ProxySQL* 2.4.2, the lock file remained in the file system and prevented the handler script from running. 

  Starting with *ProxySQL 2.4.2*, on startup, `pxc_scheduler_handler` does the following:

    * Reads the Process identifier (PID)

    * Reads the timestamp from the lock file

    * Checks if the PID is running on startup

  If the PID is running, the newly launched `pxc_scheduler_handler` exits.

  If the PID is not running, the `pxc_scheduler_handler` checks the `lockFileTimeout` timeout value. If the timeout value has been exceeded, the ``pxc_scheduler_handler`` removes the lock file and launches `pxc_scheduler_handler`.

## Prerequisites

The following are the prerequisites for using the Percona Scheduler Admin:

* The [mysql command-line client](https://dev.mysql.com/doc/refman/8.0/en/mysql.html) and [my_print_defaults](https://dev.mysql.com/doc/refman/8.0/en/my-print-defaults.html) must be installed on the system.

* *ProxySQL* and *Percona XtraDB Cluster* are running.

For information on the Percona Scheduler Admin tool installation, see [Install ProxySQL 2.x.x and the admin utilities](install-v2.md) or [Build the Percona Scheduler admin tool](build-percona-scheduler-admin.md).

## Add an issue

If you find a Percona Scheduler Admin bug, add a bug report in the [PSQLADM project](https://jira.percona.com/projects/PSQLADM).

