.. _index.proxysql-admin-interface:


*ProxySQL*, *proxysql-admin*, and *percona-scheduler-admin* documentation
********************************************************************************

ProxySQL_ is a tool that performs like a proxy between **Percona XtraDB Cluster** and your client application. *ProxySQL* manages a connection pool, which caches your connections and keeps the connections open for future requests. *ProxySQL* is designed to run continuously without being restarted. 

Without a connection pool, each SQL request opens a connections to the remote node. When the SQL request is complete, the connection is closed. A new one is opened on the next SQL request.

ProxySQL maintains the connection pool. The pool allows a certain number of connections to remain open. A connection is reused or closed if not reused within a certain time period. You connect to the proxy and the tool forwards your requests to the cluster. 

*ProxySQL* runs as a daemon watched by a monitoring process which can restart *ProxySQL* in case of an unexpected exit to minimize downtime. The daemon accepts incoming traffic from *MySQL* clients and forwards the traffic to backend *MySQL* servers.

The configuration options include runtime parameters, server grouping, and traffic-related parameters. Many of the settings can be done at runtime using queries that are similar to SQL statements.

THe `ProxySQL documentation <https://proxysql.com/documentation/>`__ provides information on installing and running ProxySQL.

*ProxySQL* is available from the **Percona** software repositories in the following versions:

ProxySQL 1.x.x and the proxysql-admin tool
------------------------------------------------

*ProxySQL* 1.x.x does not natively support **Percona XtraDB Cluster**. This
version requires custom bash scripts to track the status of **Percona XtraDB Cluster** nodes using the *ProxySQL* scheduler.

.. toctree::
   :maxdepth: 1

   
   proxysql-v1
   tarball-v1
   configuring


Install ProxySQL 2.x.x and admin tools
------------------------------------------------------

Installation procedures for *ProxySQL* 2.x.x, proxysql-admin tool, and Percona
Scheduler admin.

.. toctree::
   :maxdepth: 2


   install-v2
   installing-tarball
   psa-build

Start, Stop, Upgrade, and Uninstall ProxySQL 2.x.x
----------------------------------------------------

.. toctree::
   :maxdepth: 2

   psql-process
   upgrade-psql
   uninstall-psql


Use the ProxySQL 2.x.x and proxysql-admin tool
-----------------------------------------------------------------

The **proxysql-admin** tool in version 2.X natively supports **Percona XtraDB Cluster**. This version does not need custom scripts to track the cluster status.

.. toctree::
   :maxdepth: 2

   proxysql-changes
   v2-config
   psql-functions


Use the ProxySQL 2.x.x and Percona Scheduler Admin tool
---------------------------------------------------------------------

Implemented in version 2.3.2-1, the Percona Scheduler Admin tool can be used to automatically perform a failover due to node failures, service degradation, or maintenance.

.. toctree::
   :maxdepth: 2
   
   psa-scheduler
   psa-config
   psa-ref
   psa-options
   psa-known-limitations


   

Release notes for ProxySQL v2.x and ProxySQL v1.4.x
---------------------------------------------------------------
.. toctree::
   :maxdepth: 1

   release-notes


2022, Percona LLC and/or its affiliates 2009-2022

.. rubric:: Indices and tables

* :ref:`genindex`
* :ref:`modindex`

.. include:: _res/replace.txt
.. include:: _res/links.txt
