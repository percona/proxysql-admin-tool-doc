.. _1.4.7:

*ProxySQL* |release| and `proxysql-admin`
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Usability improvements

- Added `proxysql_status` tool to dump *ProxySQL* configuration and
  statistics.

.. rubric:: Bug fixes

- :jira:`PSQLADM-2`: `proxysql_galera_checker` script didn’t check if
  another instance of itself is already running. While running more then one
  copy of `proxysql_galera_checker` in the same runtime environment at
  the same time is still not supported, the introduced fix is able to prevent
  duplicate script execution in most cases.
- :jira:`PSQLADM-40`: `ProxySQL scheduler` generated a lot of
  `proxysql_galera_checker` and `proxysql_node_monitor`
  processes in case of wrong ProxySQL credentials in `/etc/proxysql-admin.cnf`
  file.
- :jira:`PSQLADM-41`: Timeout error handling was improved with clear messages.
- :jira:`PSQLADM-42`: An inconsistency of the date format in *ProxySQL* and scripts was
  fixed.
- :jira:`PSQLADM-43`: `proxysql_galera_checker` didn’t take into account
  the possibility of special characters presence in
  `mysql-monitor_password`.
- :jira:`PSQLADM-44`: `proxysql_galera_checker` generated unclear errors
  in the `/etc/proxysql.log` file if wrong credentials where passed.
- :jira:`PSQLADM-46`: `proxysql_node_monitor` script incorrectly split
  the hostname and the port number in URLs containing hyphen character.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.7
.. |date| replace:: April 16, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
