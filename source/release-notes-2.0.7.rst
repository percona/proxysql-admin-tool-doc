.. _proxysql-release-notes-2.0.7:

|proxysql| |release| and |command.proxysql-admin|
================================================================================

.. include:: _res/text/release-notes/attr-v2.txt
.. include:: _res/text/release-notes/description.txt
.. include:: _res/text/release-notes/upstream.txt

The |command.proxysql-admin| tool now supports |mariadb| 10.4.

.. rubric:: New Features

- :jira:`PSQLADM-204`: Add support of |mariadb| 10.4

.. rubric:: Improvements

- :jira:`PSQLADM-195`: A new option |opt.with-stats-reset| has been added to
  the |command.proxysql-status| script to display the `\*_reset` tables from the
  `stats` database. If this option is not specified, these tables are not
  displayed by default.

.. rubric:: Bugs fixed

- :jira:`PSQLADM-157`: In some cases, the |command.proxysql-status| script
  used the cat command to display a file without checking if the file existed
  and was readable.
- :jira:`PSQLADM-181`: When run with |opt.update-cluster|
  |opt.write-node| set to `<node_name>`, |command.proxysql-admin| now verifies that the
  writer nodes are not read-only.

.. include:: _res/text/license.txt

.. |date| replace:: October 23, 2019
.. |release| replace:: 2.0.7

.. include:: _res/replace.txt
.. include:: _res/links.txt
