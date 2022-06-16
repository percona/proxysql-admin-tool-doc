.. _1.4.5:

*ProxySQL* |release| and `proxysql-admin`
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Usability improvements

- :jira:`PSQLADM-6`: If the cluster node goes offline, the `proxysql_node_monitor`
  script now sets the node status as `OFFLINE_HARD`, and does not remove it from
  the *ProxySQL* database. Also, logging is consistent regardless of the cluster
  node online status.
- :jira:`PSQLADM-30`: Validation was added for the host priority file.
- :jira:`PSQLADM-33`: Added `--proxysql-datadir` option to run the `proxysql-admin`
  script with a custom *ProxySQL* data directory.
- Also, BATS test suite was added for the `proxysql-admin` testing.

.. rubric:: Bug fixes

- :jira:`PSQLADM-5`: *Percona XtraDB Cluster (PXC)* mode specified with `proxysql-admin`
  with use of `--mode` parameter was not persistent.
- :jira:`PSQLADM-8`: *ProxySQL* High CPU load took place when `mysqld` was hanging.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.5
.. |date| replace:: February 15, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
