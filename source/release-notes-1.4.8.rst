.. _1.4.8:

|proxysql| |release| and |command.proxysql-admin|
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Usability improvement

- :jira:`PSQLADM-84`: Now |command.proxysql-status| tool dumps `host_priority`
  and |file.proxysql-admin-cnf|. Also output format was changed.

.. rubric:: Other improvements and bug fixes

- :jira:`PSQLADM-66`: The |opt.syncusers| option now makes |proxysql-admin| to
  update the user’s password in |proxysql| database if there is any password
  difference between |proxysql| user and |mysql| user.
- :jira:`PSQLADM-45`: it was unclear from the help screen, that
  |opt.config-file| option requires an argument.
- :jira:`PSQLADM-48`: `${PROXYSQL_DATADIR}/${CLUSTER_NAME}_mode` file was not
  created at |proxysql-admin| upgrade (1.4.5 or before to 1.4.6 onwards).
- :jira:`PSQLADM-52`: The |command.proxysql-galera-checker| script was not
  checking empty query rules.
- :jira:`PSQLADM-54`: |command.proxysql-node-monitor| did not change
  |const.offline-hard| status properly for the coming back online nodes.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.8
.. |date| replace:: May 22, 2018

.. include:: _res/replace.txt
.. include:: _res/links.txt
