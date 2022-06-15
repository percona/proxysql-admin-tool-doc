.. _tarball:

Install *ProxySQL* 2.x.x from a binary tarball
================================================================================

Installing *ProxySQL* version 2.x from a tarball is an alternative method if the recommended method, using either the apt or the yum package manager (see :ref:`install-v2`), is not available in your environment.

The tar file extraction procedure is the same for all versions. The difference
between versions is the available tar files or the command to extract the file.

Follow these steps:

#. In `Download ProxySQL2 <https://www.percona.com/downloads/proxysql2/>`__,
   select the version.
#. In the *Software* field, select **Linux - Generic**.
#. Select the tar file.

   See :ref:`2.3.2-1`.

   See :ref:`2.0.15`

#. Navigate to the downloaded tar file.
#. Extract the files with the following commands:

   See :ref:`2.0.14`.

   See :ref:`2.0.13`.

#. Create a directory to store the *ProxySQL* data.

   .. code-block:: bash

      $> mkdir /home/user/data

#. In the configuration file, update the ``datadir`` value to point
   to the created data directory.

   .. code-block:: text

      datadir="/home/user/data"

#. Set the other options, as needed.

.. _2.3.2-1:


Available tar files for ProxySQL 2.3.2-1 and higher
---------------------------------------------------------------------

Starting with **ProxySQL 2.3.2-1**, Percona no longer provides a tarball for
CentOS 6.

.. note:: For more information, see `Spring Cleaning: Discontinuing RHEL
   6/CentOS 6 (glibc2.12) and 32-bit Binary Builds of Percona Software
   <https://www.percona.com/blog/spring-cleaning-discontinuing-rhel-6-centos-6-glibc-2-12-and-32-bit-binary-builds-of-percona-software/>`__

The following tar files are available:

.. tabularcolumns:: |p{5cm}|p{11cm}|

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - proxysql-2-version-Linux-x86_64.glibc2.17.tar.gz
     - For every supported operating system.

       For CentOS 7, install OpenSSL 1.1.1, if needed.



.. _2.0.15:


Available tar files from ProxySQL 2.0.15 to ProxySQL 2.3.2
-------------------------------------------------------------------------------

1. In `Download ProxySQL2 <https://www.percona.com/downloads/proxysql2/>`__,
select the version and in the *Software* field select **Linux - Generic**.
Download the package appropriate for your platform.

The tarball files are combined into the following files:

.. tabularcolumns:: |p{5cm}|p{11cm}|

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - proxysql-2.0.XX-Linux-x86_64.glibc2.12.tar.gz
     - For every supported operating system but ``xenial``

       For CentOS 7, install OpenSSL 1.1.1, if needed.
   * - proxysql-2.x.xx-Linux-x86_64.glibc2.17.tar.gz
     - For every supported operating system
   * - proxysql-2.0.XX-Linux-x86_64.glibc2.23.xenial.tar.gz
     - For Ubuntu 16.04 ``xenial`` only

       The password-based file encryption requires OpenSSL 1.1.1, but Ubuntu 16.04 does not support this OpenSSL version. A special statically linked OpenSSL 1.1.1 binary is packaged with the executable. This packaged binary avoids conflicts with the system OpenSSL and any shared libraries. Each new release rebuilds the binary.

.. _2.0.14:

ProxySQL 2.0.14 or higher extraction commands
----------------------------------------------

The extraction commands for version 2.0.14 and higher:

.. sourcecode:: bash

   $> # Extract the files to the download destination directory
   $> tar xzf proxysql-2.X.X-<PLATFORM-ARCHITECTURE*>.tar.gz
   $> # Change to the directory that contains the extracted files
   $> cd proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE


.. _2.0.13:

ProxySQL 2.0.13 or lower extraction commands
---------------------------------------------


For versions 2.0.13 or lower, the step is the same except the extraction command is:

.. code-block:: bash

   $ # Extract the files (assumes you have changed to the download destination directory)
   $ tar xzf proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE*.tar.gz
   $ # Change to the directory that contains the extracted files
   $ cd proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE


Starting ProxySQL
----------------------------

Start *ProxySQL* with the ``-c`` option to pass the updated configuration
file:

.. code-block:: bash

   $> /home/user/path-to-extracted-dir/usr/bin/proxysql \
   -c /home/user/path-to-extracted-dir/etc/proxysql.cnf
      
.. seealso:: 

      Documentation on the :ref:`v2-config`.

