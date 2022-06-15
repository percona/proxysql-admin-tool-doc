.. _psa-scheduler:

==========================================================
ProxySQL 2.x.x and Percona Scheduler Admin tool
==========================================================

Implemented in *ProxySQL* 2.3.2-1, the `Percona Scheduler Admin`
(percona-scheduler-admin) tool configures **Percona XtraDB Cluster** nodes into
*ProxySQL*.

.. important::

  The Percona Scheduler Admin has been tested with ProxySQL 2.3.0 and ProxySQL 2.3.2-1.

This tool has a segment-aware failover mechanism and can automatically perform a failover due to node failures,
service degradation, or maintenance requirements. The external
scheduler has the following qualities:

* Capable of parallel query execution on nodes which results in faster failover
  or fallback

* Supports fallback

* Supports promoting a reader to primary with the following conditions are met:

  * wsrep_on=OFF

  * wsrep_sst_donor_rejects_queries is set when, for example, connections are rejected due to an ongoing state transfer

* Supports a retry of operations in case of network glitches

If you find a bug in the the Percona Scheduler Admin tool, add a bug report in the `PSQLADM project <https://jira.percona.com/projects/PSQLADM>`__.

.. note::

    The Percona Scheduler Admin tool has different features than
    :ref:`the proxy-admin tool <v2-config>`. You cannot use the options from one tool in the other tool. Mixing the options may cause unintended results.

.. _prerequisites

Prerequisites
-----------------------

The following are the prerequisites for using the Percona Scheduler Admin:

* The mysql client and my_print_defaults tool must be installed on the system.
    
* The ProxySQL and Percona XtraDB Cluster should be up and running.

.. _psa-usage:


