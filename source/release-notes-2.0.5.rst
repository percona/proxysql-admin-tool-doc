.. _2.0.5:

*ProxySQL* |release| and `proxysql-admin`
================================================================================

.. include:: _res/text/release-notes/attr-v2.txt
.. include:: _res/text/release-notes/description-v2.txt
.. include:: _res/text/release-notes/upstream.txt

The `proxysql-admin` tool has been enhanced to support the following new options and commands:

.. list-table::
   :header-rows: 1

   * - Option
     - Description
   * - |opt.add-query-rule|
     - Creates query rules for synced `MySQL` users. This option is only
       applicable for the singlewrite mode and works together with the
       `--syncusers` and `--sync-multi-cluster-users` options.
   * - `--force`
     - Skips existing configuration checks in `mysql_servers`,
       `mysql_users` and `mysql_galera_hostgroups` tables. This
       option will only work together with the `--enable` option:

       .. code-block:: bash

	  $ proxysql-admin --enable --force
	  
   * - `--update-mysql-version` (command)
     - Updates the `mysql-server_version` variable in *ProxySQL* with the
       version from a node in **Percona XtraDB Cluster**.

.. rubric:: Improvements

- :jira:`PSQLADM-49`: Create rules for `--syncusers`. When running with
  `--syncusers` or `--sync-multi-cluster-users`, the `--add-query-rule`
  option can now be specified to add the singlewriter query rules for the new
  users.
- :jira:`PSQLADM-51`: Update `mysql-server_version` variable. The
  `--update-mysql-version` command has been added to set the
  `mysql-server_version` global variable in ProxySQL. This will take the
  version from a node in the cluster and set it in *ProxySQL*.

.. rubric:: Bugs fixed

- :jira:`PSQLADM-190`: The `--remove-all-servers` option did not work on
  enable. When running with proxysql-cluster, the galera hostgroups information
  was not replicated, which could result in failing to run `--enable` on a
  different *ProxySQL* node.  The `--force` option was added for `--enable`
  to be able to ignore any errors and always configure the cluster.
- :jira:`PSQLADM-199`: query-rules removed during proxysql-cluster creation with
  *Percona XtraDB Cluster (PXC)* operator. When using the *Percona XtraDB Cluster (PXC)* operator for `Kubernetes` and
  creating a proxysql-cluster, the query rules could be removed. The code was
  modified to merge the query rules (rather than deleting and recreating).  If
  the `--force` option was specified, then a warning was issued in case any
  existing rules were found; otherwise an error was issued. The
  `--disable-updates` option was added to ensure that *ProxySQL* cluster
  updates did not interfere with the current command.
- :jira:`PSQLADM-200`: users were not created for `--syncusers` with
  *Percona XtraDB Cluster (PXC)* operator. When using the *Percona XtraDB Cluster (PXC)* operator for `Kubernetes`, the
  `--syncusers` command was run but the `mysql_users` table was not
  updated.  The fix for :jira:`PSQLADM-199` that suggested to use
  `--disable-updates` also applies here.

.. include:: _res/text/license.txt

.. |date| replace:: October 23, 2019
.. |release| replace:: 2.0.5

.. include:: _res/replace.txt
.. include:: _res/links.txt
