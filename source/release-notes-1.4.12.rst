.. _proxysql-release-notes-1.4.12:

|proxysql| |release| and |command.proxysql-admin|
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Improvements

- :jira:`PSQLADM-68`: Scripts are now compatible with |abbr.pxc| hosts using
  IPv6
- :jira:`PSQLADM-107`: In include-slaves, a slave would always be moved into
  the write hostgroup even if the whole cluster went down. A new option
  |opt.use-slave-as-writer| specifies whether or not the slave is added to the
  write hostgroup.

.. rubric:: Bugs Fixed

- :jira:`PSQLADM-110`: In some cases, pattern cluster hostname did not work
  with |command.proxysql-admin|.
- :jira:`PSQLADM-104`: |command.proxysql-admin| testsuite bug fixes.
- :jira:`PSQLADM-113`: |command.proxysql-galera-checker| assumed that parameters
  were given in the long format.
- :jira:`PSQLADM-114`: In some cases, |proxysql| could not be started
- :jira:`PSQLADM-115`: |command.proxysql-node-monitor| could fail with more
  than one command in the |proxysql-scheduler|.
- :jira:`PSQLADM-116`: In some cases, the |proxysql-scheduler| was reloading
  servers on every run
- :jira:`PSQLADM-117`: The |opt.syncusers| option did not work when enabling
  cluster
- :jira:`PSQLADM-125`: The function |command.check-is-galera-checker-running|
  was not preventing multiple instances of the script from running.

Other bugs fixed: :jira:`PSQLADM-112`, :jira:`PSQLADM-120`

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.12
.. |date| replace:: November 13, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
