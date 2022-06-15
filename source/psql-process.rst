.. _functions:


Starting and Stopping ProxySQL
====================================


.. _start:

Starting ProxySQL 2.x.x
-------------------------------------------

To start ProxySQL 2.x, run the following command: ::

   $> sudo service proxysql2 start


.. warning::

   **Do not run ProxySQL with default credentials in production.**

   Before starting the ``proxysql`` service, you can change the
   defaults in the :file:`/etc/proxysql.cnf` file by changing the
   ``admin_credentials`` variable.  For more information, see `Global
   Variables
   <https://github.com/sysown/proxysql/blob/master/doc/global_variables.md>`_.

.. seealso::

   `ProxySQL Getting Started <https://proxysql.com/documentation/getting-started/>`__


.. _stop:

Stopping ProxySQL 2.x.x
-------------------------------

To stop ProxySQL 2.x, run either  of the following commands: ::

   $> sudo service proxysql stop

or ::

   $> sudo service proxysql2 stop




