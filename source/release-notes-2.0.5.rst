.. _proxysql-release-notes-2.0.5:

|proxysql| |release| and |command.proxysql-admin|
================================================================================

.. include:: _res/text/release-notes/attr-v2.txt
.. include:: _res/text/release-notes/description.txt
.. include:: _res/text/release-notes/upstream.txt

The |command.proxysql-admin| tool has been enhanced to support the following new options and commands:

.. list-table::
   :header-rows: 1

   * - Option
     - Description
   * - |opt.add-query-rule|
     - Creates query rules for synced |mysql| users. This option is only
       applicable for the singlewrite mode and works together with the
       |opt.syncusers| and |opt.sync-multi-cluster-users| options.
   * - |opt.force|
     - Skips existing configuration checks in |table.mysql-servers|,
       |table.mysql-users| and |table.mysql-galera-hostgroups| tables. This
       option will only work together with the |opt.enable| option:

       .. code-block:: bash

	  $ proxysql-admin --enable --force
	  
   * - |command.update-mysql-version| (command)
     - Updates the |opt.mysql-server-version| variable in |proxysql| with the
       version from a node in |pxc|.

.. rubric:: Improvements

- :jira:`PSQLADM-49`: Create rules for |opt.syncusers|. When running with
  |opt.syncusers| or |opt.sync-multi-cluster-users|, the |opt.add-query-rule|
  option can now be specified to add the singlewriter query rules for the new
  users.
- :jira:`PSQLADM-51`: Update |opt.mysql-server-version| variable. The
  |command.update-mysql-version| command has been added to set the
  |opt.mysql-server-version| global variable in ProxySQL. This will take the
  version from a node in the cluster and set it in |proxysql|.

.. rubric:: Bugs fixed

- :jira:`PSQLADM-190`: The |opt.remove-all-servers| option did not work on
  enable. When running with proxysql-cluster, the galera hostgroups information
  was not replicated, which could result in failing to run |opt.enable| on a
  different |proxysql| node.  The |opt.force| option was added for |opt.enable|
  to be able to ignore any errors and always configure the cluster.
- :jira:`PSQLADM-199`: query-rules removed during proxysql-cluster creation with
  |abbr.pxc| operator. When using the |abbr.pxc| operator for |kubernetes| and
  creating a proxysql-cluster, the query rules could be removed. The code was
  modified to merge the query rules (rather than deleting and recreating).  If
  the |opt.force| option was specified, then a warning was issued in case any
  existing rules were found; otherwise an error was issued. The
  |opt.disable-updates| option was added to ensure that |proxysql| cluster
  updates did not interfere with the current command.
- :jira:`PSQLADM-200`: users were not created for |opt.syncusers| with
  |abbr.pxc| operator. When using the |abbr.pxc| operator for |k8s|, the
  |opt.syncusers| command was run but the |table.mysql-users| table was not
  updated.  The fix for :jira:`PSQLADM-199` that suggested to use
  |opt.disable-updates| also applies here.

.. include:: _res/text/license.txt

.. |date| replace:: October 23, 2019
.. |release| replace:: 2.0.7

.. include:: _res/replace.txt
.. include:: _res/links.txt
