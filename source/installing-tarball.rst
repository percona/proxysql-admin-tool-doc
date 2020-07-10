:orphan:

.. _proxysql-admin-interface.installing-tarball:

Installing from a tarball
================================================================================

Installing |proxysql| from a tarball is an alterative method if recommended
approaches, using apt or yum package managers, are not applicable in your
environment. With this method, you download a |tar-file| file from the `ProxySQL
v1 downloads page`_ or from `ProxySQL v2 downloads page`_ and then install to a
custom directory.

1. Visit one of the downloads pages, select **Linux - Generic** in the
   *Software* field and download the package appropriate for your platform.

#. Extract the files from the archive and change to the directory that contains
   the extracted files:

   .. code-block:: bash
      
      $ # Extract the files (assuming you have changed to the download destination directory)
      $ tar xzf proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE.tar.gz
      $ # Change to the directory that contains the extracted files
      $ cd proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE
   
#. Create a directory to store |proxysql| data:

   .. code-block:: bash

      $ mkdir /home/user/data
	 
#. Update the value of the |param.datadir| in the configuration file to point
   to the data directory you have created.

   .. code-block:: text

      datadir="/home/user/data"

#. Set other options as needed.

Now, you can start |proxysql|. Use the |opt.c| option to pass the configuration
file you have updated:

.. code-block:: bash

   $ /home/user/path-to-extracted-dir/usr/bin/proxysql \
   -c /home/user/path-to-extracted-dir/etc/proxysql.cnf
      
   ... [INFO] Using config file proxysql.cnf

-----

.. rubric:: Related information: other installation methods

- :ref:`proxysql-v1.installing`
- :ref:`proxysql-v2.installing`

.. include:: _res/replace.txt
.. include:: _res/links.txt
