:orphan:

.. _proxysql-admin-interface.installing-tarball:

Installing from a tarball
================================================================================

Installing |proxysql| from a tarball is an alternative method if the recommended
approaches, using either apt or yum package managers are not applicable in your
environment. With this method, you download a |tar-file| file from the `ProxySQL
v1 downloads page`_ or from `ProxySQL v2 downloads page`_ and then install to a
custom directory.

1. Visit one of the downloads pages, select **Linux - Generic** in the
   *Software* field and download the package appropriate for your platform.
   
   .. note::
   
       As of ProxySQL 2.0.15 and later, the multiple tarball files are
       combined into the following files:

         .. tabularcolumns:: |p{5cm}|p{11cm}|
       
       .. list-table::
          :header-rows: 1

          * - Name
            - Description
          * - proxysql-2.0.XX-Linux-x86_64.glibc2.12.tar.gz
            - For every supported operating system but ``xenial``

              For CentOS 7, install OpenSSL 1.1.1, if needed. 
          * - proxysql-2.0.XX-Linux-x86_64.glibc2.23.xenial.tar.gz
            - For Ubuntu 16.04 ``xenial`` only

              The password-based file encryption requires OpenSSL 1.1.1, but Ubuntu 16.04 does not support this OpenSSL version. A special statically linked OpenSSL 1.1.1 binary is packaged with the executable. This packaged binary avoids conflicts with the system OpenSSL and any shared libraries. Each new release rebuilds the binary.
                          
#. For versions 2.0.13 or lower, extract the files from the archive and change to the directory that contains
   the extracted files (for version 2.0.14 and higher, review the note):

   .. code-block:: bash
      
      $ # Extract the files (assuming you have changed to the download destination directory)
      $ tar xzf proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE*.tar.gz
      $ # Change to the directory that contains the extracted files
      $ cd proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE
      
  .. note::
  
       For version 2.0.14 and higher, the step is the same except the extraction
       command is:
       
       .. code-block:: bash
       
           tar xzf proxysql-2.0.XX-<PLATFORM-ARCHITECTURE*>.tar.gz
       
#. Create a directory to store the |proxysql| data:

   .. code-block:: bash

      $ mkdir /home/user/data
	 
#. Update the value of the ``datadir`` in the configuration file to point
   to the data directory you have created.

   .. code-block:: text

      datadir="/home/user/data"

#. Set the other options, as needed.

Start |proxysql| with the ``-c`` option to pass the configuration
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
