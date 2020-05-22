.. _proxysql-release-notes-1.4.16:

|proxysql| |release| and |command.proxysql-admin| tool
================================================================================

.. include:: _res/text/release-notes/attr-v1.txt
.. include:: _res/text/release-notes/description.txt

.. rubric:: Bugs Fixed

- :jira:`PSQLADM-219`: The `ProxySQL scheduler`_ was handling the
  |opt.pxc-maint-mode| variable incorrectly. As a result, open connections were
  closed immediately. This bug has been fixed and now the |scheduler| only sets
  the node status to |const.offline-soft|. This prevents opening new connections
  and lets the already established connections finish their work. It is up to
  the user to decide when it is safe to start the node maintenance.

.. include:: _res/text/license.txt

.. |release| replace:: 1.4.16
.. |date| replace:: February 11, 2020

.. include:: _res/replace.txt
.. include:: _res/links.txt
