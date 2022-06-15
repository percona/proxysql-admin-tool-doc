.. _1.4.5:

|proxysql| |release| and |command.proxysql-admin|
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Usability improvements

- :jira:`PSQLADM-6`: If the cluster node goes offline, the |command.proxysql-node-monitor|
  script now sets the node status as |const.offline-hard|, and does not remove it from
  the |proxysql| database. Also, logging is consistent regardless of the cluster
  node online status.
- :jira:`PSQLADM-30`: Validation was added for the host priority file.
- :jira:`PSQLADM-33`: Added |opt.proxysql-datadir| option to run the |command.proxysql-admin|
  script with a custom |proxysql| data directory.
- Also, BATS test suite was added for the |command.proxysql-admin| testing.

.. rubric:: Bug fixes

- :jira:`PSQLADM-5`: |abbr.pxc| mode specified with |command.proxysql-admin|
  with use of |opt.mode| parameter was not persistent.
- :jira:`PSQLADM-8`: |proxysql| High CPU load took place when |command.mysqld| was hanging.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.5
.. |date| replace:: February 15, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
