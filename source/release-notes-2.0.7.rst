.. _2.0.7:

*ProxySQL* |release| and `proxysql-admin`
================================================================================

.. include:: _res/text/release-notes/attr-v2.txt
.. include:: _res/text/release-notes/description-v2.txt
.. include:: _res/text/release-notes/upstream.txt

The `proxysql-admin` tool now supports `MariaDB` 10.4.

.. rubric:: New Features

- :jira:`PSQLADM-204`: Add support of `MariaDB` 10.4

.. rubric:: Improvements

- :jira:`PSQLADM-195`: A new option `--with-stats-reset` has been added to
  the `proxysql_status` script to display the `\*_reset` tables from the
  `stats` database. If this option is not specified, these tables are not
  displayed by default.

.. rubric:: Bugs fixed

- :jira:`PSQLADM-157`: In some cases, the `proxysql_status` script
  used the cat command to display a file without checking if the file existed
  and was readable.
- :jira:`PSQLADM-181`: When run with `--update-cluster`
  `--write-node` set to `<node_name>`, `proxysql-admin` now verifies that the
  writer nodes are not read-only.

.. include:: _res/text/license.txt

.. |date| replace:: October 23, 2019
.. |release| replace:: 2.0.7

.. include:: _res/replace.txt
.. include:: _res/links.txt
