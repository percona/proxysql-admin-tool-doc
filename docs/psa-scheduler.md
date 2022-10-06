# ProxySQL 2.x.x and Percona Scheduler Admin tool

Implemented in *ProxySQL* 2.3.2-1.2, the Percona Scheduler Admin
(percona-scheduler-admin) tool configures **Percona XtraDB Cluster** nodes into
*ProxySQL*.

!!! note

    The Percona Scheduler Admin tool has been tested with ProxySQL 2.3.0, 2.3.2-1.2, and later versions.

This tool has a segment-aware failover mechanism and can automatically perform a failover due to node failures,
service degradation, or maintenance requirements. The external
scheduler has the following qualities:

* Capable of parallel query execution on nodes which results in faster failover or fallback

* Supports fallback

* Supports promoting a reader to primary with the following conditions are met:

  * wsrep_on=OFF

  * wsrep_sst_donor_rejects_queries is set when, for example, connections are rejected due to an ongoing state transfer

* Supports a retry of operations in case of network glitches

If you find a bug in the the Percona Scheduler Admin tool, add a bug report in the [PSQLADM project](https://jira.percona.com/projects/PSQLADM).

**NOTE**: The Percona Scheduler Admin tool has different features than
the [proxy-admin](v2-config.md) tool. You cannot use the options from one tool in the other tool. Mixing the options may cause unintended results.

## Version changes

* When ``pxc_scheduler_handler`` launches, a lock file is created to prevent the running of multiple instances of ``pxc_scheduler_handler``. Prior to **ProxySQL 2.4.2**, the lock file remained in the file system and prevented the handler script from running. 

  Starting with **ProxySQL 2.4.2**, on startup, ``pxc_scheduler_handler`` does the following:

   * Reads the Process identifier (PID)

   * Reads the timestamp from the lock file
   
   * Checks if PID is running on startup
 
  If PID is still running, the newly launched ``pxc_scheduler_handler`` exits. If the PID is not running, ``pxc_scheduler_handler`` checks whether the timeout specified in `lockFileTimeout` exceeds. If the timeout exceeds, ``pxc_scheduler_handler`` removes the lock file and performs the operations.

## Prerequisites

The following are the prerequisites for using the Percona Scheduler Admin:

* The mysql client and my_print_defaults tool must be installed on the system.

* The ProxySQL and Percona XtraDB Cluster should be up and running.

For information on the Percona Scheduler Admin tool installation, see [Installing ProxySQL 2.x.x and the admin utilities](/install-v2.md) or [Build the Percona Scheduler admin tool](psa-build.md).
