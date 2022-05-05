.. _index.proxysql-admin-interface:

.. ProxySQL Admin Documentation documentation master file, created by
   sphinx-quickstart on Fri Apr 17 21:29:13 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

|proxysql| and |proxysql-admin| documentation
********************************************************************************

ProxySQL_ is a high-performance SQL proxy.  |proxysql| runs as a daemon watched by
a monitoring process. This process monitors the daemon and restarts it in case
of a crash to minimize downtime.

The daemon accepts incoming traffic from |mysql| clients and forwards it to
backend |mysql| servers.

|proxysql| is designed to run continuously without needing to be restarted.  Most
configuration can be done at runtime using queries similar to SQL statements.
These include runtime parameters, server grouping, and traffic-related settings.

# Reference

   |proxysql| documentation
      https://github.com/sysown/proxysql/tree/master/doc

|proxysql| is available from the |percona| software repositories in two
versions. |proxysql-v1| does not natively support |pxc| and requires
custom bash scripts to keep track of the status of |pxc| nodes using the
|proxysql| scheduler.

|proxysql-v2| natively supports |pxc|. With this version,
the |command.proxysql-admin| tool does not require custom scripts to keep track of |pxc| status.

.. toctree::
   :maxdepth: 1

   configuring
   proxysql-v2
   proxysql-v1
   Release notes <release-notes>

2022, Percona LLC and/or its affiliates 2009-2022

.. rubric:: Indices and tables

* :ref:`genindex`
* :ref:`modindex`

.. include:: _res/replace.txt
.. include:: _res/links.txt
