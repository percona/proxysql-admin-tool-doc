.. _1.4.8:

*ProxySQL* |release| and `proxysql-admin`
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Usability improvement

- :jira:`PSQLADM-84`: Now `proxysql_status` tool dumps `host_priority`
  and `/etc/proxysql-admin.cnf`. Also output format was changed.

.. rubric:: Other improvements and bug fixes

- :jira:`PSQLADM-66`: The `--syncusers` option now makes `ProxySQL Admin` to
  update the user’s password in *ProxySQL* database if there is any password
  difference between *ProxySQL* user and `MySQL` user.
- :jira:`PSQLADM-45`: it was unclear from the help screen, that
  `--config-file` option requires an argument.
- :jira:`PSQLADM-48`: `${PROXYSQL_DATADIR}/${CLUSTER_NAME}_mode` file was not
  created at `ProxySQL Admin` upgrade (1.4.5 or before to 1.4.6 onwards).
- :jira:`PSQLADM-52`: The `proxysql_galera_checker` script was not
  checking empty query rules.
- :jira:`PSQLADM-54`: `proxysql_node_monitor` did not change
  `OFFLINE_HARD` status properly for the coming back online nodes.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.8
.. |date| replace:: May 22, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
