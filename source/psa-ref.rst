.. _psa-ref:

================================================================================
Percona Scheduler Admin Statements and Options
================================================================================

Statement reference
------------------------

The standard percona-scheduler-admin statement includes
``percona-scheduler-admin --config-file=<configuration file name and
extension>``. A Percona Scheduler Admin example statement has the following syntax:

.. sourcecode:: text

   percona-scheduler-admin --config-file=config.toml [option] [option]
   
If you do not include the :ref:`configuration file <toml>`, the result is an error and nothing happens.

.. sourcecode:: bash

    $> ./percona-scheduler-admin --debug

    ERROR : The --config-file option is required but is missing from the command.


.. seealso:: :ref:`psa-options` for common option details.

Options determine what the statement does. The `percona-scheduler-admin` statement must include at least one option. If you do not include at least one option, the tool returns an error and nothing happens.

Two hyphens (--) precede an option name. The options
:ref:`disable <psa-disable>` and :ref:`enable <psa-enable>` can also be selected with one hyphen (-) and an abbreviation.

The following examples return the same result:

.. sourcecode:: bash

    $> ./percona-scheduler-admin --config-file=config.toml -e 

    $> ./percona-scheduler-admin --config-file=config.toml --enable

You can combine some options with other, optional options to modify the
statement's behavior. Multiple options are separated by a space.
You can combine options in any order. 

.. sourcecode:: bash

    $> ./percona-scheduler-admin --config-file=config.toml --write-node=127.0.0.1:4130 --update-cluster

Certain options must be combined with a
required option to return a result. 

.. sourcecode:: bash

    $> ./percona-scheduler-admin --config-file=config.toml --force -e

If you do not combine the
option with the required option, the statement does not run and returns an
error.

.. sourcecode:: bash

    $> ./percona-scheduler-admin --config-file=tests/testsuite.toml  --update-write-weight="127.0.0.1:33,112"

    ERROR : --update-write-weight requires --update-cluster.

Specific options, such as :ref:`psa-write-node` or :ref:`psa-server`, require a value.

.. sourcecode:: bash

    $> ./percona-scheduler-admin --config-file=config.toml --server=192.168.56.32:3306

Option Reference
--------------------------------------------

.. list-table:: 
   :header-rows: 1
   
   * - Option name
     - Acceptable values
     - Other options
     - Mode
     - Description
   * - :ref:`--add-query-rule <psa-add-query>`
     -
     - Requires either: :ref:`psa-syncusers` or :ref:`psa-sync-multi`
     - Requires:``singlewrite``
     - Creates query rules for the synced mysql user. See
       :ref:`add-query-rule <psa-add-query>`
       for details.
   * - :ref:`--adduser <psa-adduser>`
     -
     -
     -
     - Adds the Percona XtraDB Cluster application user to the ProxySQL
       database. See :ref:`adduser <psa-adduser>` for more details.`
   * - :ref:`--auto-assign-weights <psa-auto-assign-weights>`
     -
     - Requires: :ref:`psa-update-cluster`
     - Requires: ``singlewrite``
     - Auto-assigns weights. See
       :ref:`auto-assign-weights <psa-auto-assign-weights>` for details.
   * - ``--config-file``
     - <config.toml>
     -
     -
     - Reads login credentials from a configuration file. Command-line options
       override configuration file values. For more information, see :ref:`psa-config`.
   * - ``--debug``
     -
     -
     -
     - Enables additional debug logging.
   * - :ref:`--disable <psa-disable>` or ``-d``
     -
     -
     -
     - Removes any Percona XtraDB Cluster configurations from ProxySQL. See
       :ref:`disable <psa-disable>` for more details.
     
   * - ``--disable-updates``
     -
     -
     -
     - Disables admin updates for ProxySQL cluster for the current operation by
       setting the values to false. The default setting does not change the
       admin variable settings.
   * - :ref:`--enable <psa-enable>` or ``-e``
     -
     -
     -
     - Configures, without manual intervention, the Percona XtraDB Cluster nodes
       into ProxySQL. See :ref:`enable <psa-enable>` for more details.
   * - ``--force``
     -
     - Requires at least one of the following options: :ref:`--enable <psa-enable>`, :ref:`--disable <psa-disable>`, :ref:`--update-cluster <psa-update-cluster>`, :ref:`--is-enabled <psa-is-enabled>`, :ref:`--adduser <psa-adduser>`, :ref:`--syncusers <psa-syncusers>`, :ref:`--sync-multi-cluster-users <psa-sync-multi>`, or :ref:`--update-mysql-version <psa-update-mysql-v>`
     -
     - Skips any mysql_servers table, mysql_users table, and
       mysql_galera_hostgroups table configuration checks. Certain checks issue
       warnings instead of errors.
   * - ``--help``
     -
     -
     -
     - Displays the help text.
   * - :ref:`is-enabled <psa-is-enabled>`
     -
     -
     -
     - Checks if the current configuration is enabled in ProxySQL. See
       :ref:`is-enabled <psa-is-enabled>` for more details.
   * - ``--remove-all-servers``
     -
     - Requires::ref:`--update-cluster <psa-update-cluster>`
     -
     - Removes all servers belonging to the current cluster before updating the
       list.
   * - :ref:`--status <psa-status>`
     -
     -
     -
     - Returns a status report on the current configuration. See :ref:`status
       <psa-status>` for more details.
   * - :ref:`--server <psa-server>`
     - <IPADDRESS>:<PORT>
     - Optional: :ref:`psa-syncusers` or :ref:`psa-sync-multi`
     -
     - Specifies the IP address and port for a single server. This option can be
       combined with :ref:`psa-syncusers` or :ref:`psa-sync-multi` to sync a
       single non-cluster server node.
   * - :ref:`sync-multi-cluster-users
       <psa-sync-multi>`
     -
     - Optional: :ref:`--enable <psa-enable>`, :ref:`--server <psa-server>`
     -
     - Syncs the user accounts currently configured in MySQL to ProxySQL.
       Combine with the :ref:`--server <psa-server>` option to a sync to a single server. 
       Does not delete ProxySQL users not in MySQL. 
       See :ref:`sync-multi-cluster-users <psa-sync-multi>` for more details.

   * - :ref:`--syncusers <psa-syncusers>`
     -
     - Optional: :ref:`--enable <psa-enable>`, :ref:`--server <psa-server>`
     -
     - Syncs the user accounts currently configured in MySQL to ProxySQL. Use
       with the :ref:`--server <psa-server>` option to specify a single server to sync. 
       Deletes ProxySQL users not in MySQL. 
       See :ref:`--syncusers <psa-syncusers>` for more details.

   * - ``--trace``
     -
     -
     -
     - Enables shell-level tracing for this shell script.
   * - :ref:`--update-cluster <psa-update-cluster>`
     -
     -
     -
     - Updates the cluster membership, adds new cluster nodes to the
       configuration. See
       :ref:`update-cluster <psa-update-cluster>` for more details.

   * - :ref:`update-mysql-version <psa-update-mysql-v>`
     -
     -
     -
     - Updates the mysql server version variable in *ProxySQL* based on the
       node version. See :ref:`update-mysql-version <psa-update-mysql-v>`for
       more details.
   * - :ref:`update-read-weight <psa-update-read-weight>`
     - <IP:PORT,WEIGHT>
     - Requires::ref:`update-cluster <psa-update-cluster>`
     -
     - Assigns the specified read weight to the given node. See
       :ref:`update-read-weight <psa-update-read-weight>` for more details.
   * - :ref:`update-write-weight <psa-update-write-weight>`
     - <IP:PORT,WEIGHT>
     - Requires::ref:`update-cluster <psa-update-cluster>`
     -
     - Assigns the specified write weight to the given node. See
       :ref:`update-write-weight <psa-update-write-weight>` for more details.
   * - ``--use-stdin-for-credentials``
     -
     -
     -
     - Uses stdin to send credential to the MySQL client instead of process
       substitution. The default setting disables the option and uses process
       substitution.
   * - ``--version`` or  ``-v``
     -
     -
     -
     - Prints the version information.
   * - :ref:`--write-node <psa-write-node>`
     - <IPADDRESS>:<PORT>
     -
     - Requires:``singlewrite``
     - Specifies the node to be used for writes for `singlewrite` mode. If left
       unspecified, the cluster node is the write node.

