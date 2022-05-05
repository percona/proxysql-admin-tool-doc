.. _1.4.7:

|proxysql| |release| and |command.proxysql-admin|
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Usability improvements

- Added |command.proxysql-status| tool to dump |proxysql| configuration and
  statistics.

.. rubric:: Bug fixes

- :jira:`PSQLADM-2`: |command.proxysql-galera-checker| script didn’t check if
  another instance of itself is already running. While running more then one
  copy of |command.proxysql-galera-checker| in the same runtime environment at
  the same time is still not supported, the introduced fix is able to prevent
  duplicate script execution in most cases.
- :jira:`PSQLADM-40`: |proxysql-scheduler| generated a lot of
  |command.proxysql-galera-checker| and |command.proxysql-node-monitor|
  processes in case of wrong ProxySQL credentials in |file.proxysql-admin-cnf|
  file.
- :jira:`PSQLADM-41`: Timeout error handling was improved with clear messages.
- :jira:`PSQLADM-42`: An inconsistency of the date format in |proxysql| and scripts was
  fixed.
- :jira:`PSQLADM-43`: |command.proxysql-galera-checker| didn’t take into account
  the possibility of special characters presence in
  |table.mysql-monitor-password|.
- :jira:`PSQLADM-44`: |command.proxysql-galera-checker| generated unclear errors
  in the |file.proxysql-log| file if wrong credentials where passed.
- :jira:`PSQLADM-46`: |command.proxysql-node-monitor| script incorrectly split
  the hostname and the port number in URLs containing hyphen character.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.7
.. |date| replace:: April 16, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
