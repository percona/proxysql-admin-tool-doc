.. _proxysql-release-notes-2.0.3:

|proxysql| |release| and |command.proxysql-admin|
================================================================================

.. include:: _res/text/release-notes/attr-v2.txt
.. include:: _res/text/release-notes/description.txt

With |proxysql| |release|, |proxysql-admin| now uses the native
|proxysql| support for |pxc| and does not require custom bash scripts
to keep track of |abbr.pxc| status.  As a result,
|command.proxysql-galera-checker| and |command.proxysql-node-monitor|
have been removed.

.. rubric:: Improvements

- The |command.proxysql-admin| tool is |mysql| 8.0 compatible

.. rubric:: New features

- New option |opt.use-ssl| to use |abbr.ssl| for connections between |proxysql|
  and the backend database servers New option |opt.max-transactions-behind| to
  determine the maximum number of writesets that can be queued before the node
  is *SHUNNED* to avoid stale reads. The default value is *100*.
- New operation |opt.update-cluster| to update the cluster membership by adding
  server nodes as found. (Note that nodes are added but not removed).  The
  |opt.writer-hg| option may be used to specify which galera hostgroup to
  update. The |opt.remove-all-servers| option instructs to remove all servers from
  the |table.mysql-servers| table before updating the cluster.  Hostgroups can now
  be specified on the command-line: |opt.writer-hg|, |opt.reader-hg|, |opt.backup-writer-hg|,
  and |opt.offline-hg|.  Previously, these host groups were only read from the
  configuration file.
- The |opt.enable| and |opt.update-cluster| options used simultaneously have special
  meaning. If the cluster has not been enabled, then |opt.enable| is run.  If the
  cluster has already been enabled, then |opt.update-cluster| is run.
- New command |opt.is-enabled| to see if a cluster has been enabled. This command
  checks for the existence of a row in the |table.mysql_galera_hostgroups| table.
  |opt.writer-hg| may be used to specify the writer hostgroup used to
  search the |table.mysql-galera-hostgroups| table.
- New command |opt.status| to display galera hostgroup information. This command
  lists all rows in the current |table.mysql-galera-hostgroups| table as well as all
  servers that belong to these hostgroups.  With the |opt.writer-hg| option, only
  the information for the galera hostgroup with that writer hostgroup is
  displayed.

.. rubric:: Changed features

- Setting |opt.node-check-interval| now changes the |proxysql| global variable
  |opt..healthcheck| Note that this is a global variable, not a per-cluster
  variable.
- The option |opt.write-node| now takes only a single address as a parameter. In
  the singlewrite mode we only set the weight if |opt.write-node| specifies
  address:port. A priority list of addresses is no longer accepted.
- The option |opt.writers-as-readers| option now accepts a different set of
  values. Due to changes in the behavior of |proxysql| between version 1.4 and
  version 2.0 related to |galera| support, the values of |opt.writers-as-readers| have
  been changed. This option now accepts the following values: yes, no, and
  backup.

  yes:
     writers, backup-writers, and read-only nodes can act as readers.
  no:
     only read-only nodes can act as readers.
  backup:
     only backup-writers can act as readers.
     
- The commands |opt.syncusers|, |opt.sync-multi-cluster-users|, |opt.adduser|,
  and |opt.disable can now use the |opt.writer-hg| option.
- The command |opt.disable| removes all users associated with the galera cluster
  hostgroups. Previously, this command only removed the users with the
  |const.cluster-app-username|.
- The command |opt.disable| now accepts the |opt.writer-hg| option to disable
  the |galera| cluster associated with that hostgroup overriding the value
  specified in the configuration file.

.. rubric:: Removed features

- Asynchronous slave reader support has been removed: the |opt.include-slaves|
  option is not supported.
- A list of nodes in the priority order is no longer supported. Only a single
  node is supported at this time.
- Since the |command.proxysql-galera-checker| and
  |command.proxysql-node-monitor| scripts are no longer run in
  |command.proxysql-scheduler|, automatic cluster membership updates are not
  supported.
- Checking the |opt.pxc-maint-mode| variable is no longer supported
- Using desynced nodes if no other nodes are available is no longer supported.
- The server status is no longer maintained in the |table.mysql-servers| table.

.. rubric:: Limitations

- With |opt.writers-as-readers|=backup read-only nodes are not allowed. This a
  limitation of |proxysql| 2.0.  Note that *backup* is the default value
  of |opt.writers-as-readers| when |opt.mode|=singlewrite

.. include:: _res/text/license.txt

.. |date| replace:: May 7, 2019
.. |release| replace:: 2.0.3

.. include:: _res/replace.txt
.. include:: _res/links.txt
