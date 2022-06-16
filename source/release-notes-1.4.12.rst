.. _1.4.12:

*ProxySQL* |release| and `proxysql-admin`
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Improvements

- :jira:`PSQLADM-68`: Scripts are now compatible with *Percona XtraDB Cluster (PXC)* hosts using
  IPv6
- :jira:`PSQLADM-107`: In include-slaves, a slave would always be moved into
  the write hostgroup even if the whole cluster went down. A new option
  `--use-slave-as-writer` specifies whether or not the slave is added to the
  write hostgroup.

.. rubric:: Bugs Fixed

- :jira:`PSQLADM-110`: In some cases, pattern cluster hostname did not work
  with `proxysql-admin`.
- :jira:`PSQLADM-104`: `proxysql-admin` testsuite bug fixes.
- :jira:`PSQLADM-113`: `proxysql_galera_checker` assumed that parameters
  were given in the long format.
- :jira:`PSQLADM-114`: In some cases, *ProxySQL* could not be started
- :jira:`PSQLADM-115`: `proxysql_node_monitor` could fail with more
  than one command in the `ProxySQL scheduler`.
- :jira:`PSQLADM-116`: In some cases, the `ProxySQL scheduler` was reloading
  servers on every run
- :jira:`PSQLADM-117`: The `--syncusers` option did not work when enabling
  cluster
- :jira:`PSQLADM-125`: The `check-is-galera-checker-running` function 
  was not preventing multiple instances of the script from running.

Other bugs fixed: :jira:`PSQLADM-112`, :jira:`PSQLADM-120`

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.12
.. |date| replace:: November 13, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
