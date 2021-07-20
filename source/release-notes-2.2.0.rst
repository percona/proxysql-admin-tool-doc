.. proxysql-release-notes-2.2.0:

===============================================================================
|proxysql| |release| and |command.proxysql-admin|
===============================================================================

:Date: |date|
:Installation: |url.proxysql-install-v2|

|proxysql| |release|, released by ProxySQL_, is now available for download in
the `Percona repository`_ along with an updated version of |percona|’s
|command.proxysql-admin| tool.

|proxysql| is a high-performance proxy, currently for |mysql|, and database
servers in the |mysql| ecosystem (like |ps| and |mariadb|). It acts as an
intermediary for client requests seeking resources from the
database. |proxysql-author| created |proxysql| for DBAs as a means of solving
complex replication topology issues.

The |proxysql| |release| source and binary packages available from the `Percona download page for ProxySQL 2`_ include |proxysql-admin| – a tool developed by
|percona| to configure |pxc| nodes into |proxysql|. |docker| images for
|release| are available as well.

You can `download the original ProxySQL from
GitHub`_. |proxysql| offers the `ProxySQL documentation`_. For more information on the issues fixed, features, or enhancements, see the |proxysql| `2.2.0 release notes <https://github.com/sysown/proxysql/releases/tag/v2.2.0>`__

.. note::

    An upgrade from ProxySQL v1.x to ProxySQL v2.x requires the user to manually remove the ProxySQL v1.x packages. After that operation, the user can install ProxySQL v2.x.

|proxysql-admin| has not changed since the previous release.

.. include:: _res/text/license.txt

.. |date| replace:: July 28, 2021
.. |release| replace:: 2.2.0

.. include:: _res/replace.txt
.. include:: _res/links.txt
