.. _psa-config:

==========================================================================
Percona Scheduler Admin configuration file
==========================================================================

*ProxySQL* with the ``percona-scheduler-admin`` stores the parameters in a
configuration file that uses the `toml` format. This file defines
the server credentials and other settings.

Use the ``--config-file`` option to run the *percona-scheduler-admin* script.

.. note::

    It is not recommended to store the scheduler config file in the Home directory.

.. _toml:

Example of a configuration file
----------------------------------------

.. sourcecode:: text

  # For the detailed manual, see
  # https://github.com/percona/pxc_scheduler_handler#how-to-configure-pxc-scheduler-handler
  #

  [pxccluster]
  activeFailover = 1
  failBack = false
  checkTimeOut = 2000
  mainSegment = 0
  sslClient = "client-cert.pem"
  sslKey = "client-key.pem"
  sslCa = "ca.pem"
  sslCertificatePath = "/path/to/ssl_cert"
  hgW = 100
  hgR = 101
  configHgRange =8000
  maintenanceHgRange =9000

  # --------------------------------
  # Set to true if there is a single writer node.  If this is set,
  # then maxNumWriters is assumed to be 1.
  #
  # Allowable values: true,false
  # Default: false
  #
  singlePrimary = true

  # --------------------------------
  # Set to the number of writer nodes desired.
  #
  # The value of this is assumed to be 1 if singlePrimary is true.
  #
  # If this is set to a value from 1 to 100, then the query rules
  # are setup for a distinct writer hostgroup (writes are sent to the
  # writer hostgroup and read are sent to the reader hostgroup).
  #
  # If this is set to a value > 100, then all queries (writes and reads)
  # are sent to the writer hostgroup.  This is assumed to be a
  # load-balancing scenario, where all nodes are equivalent and accept
  # both reads and writes.
  #
  # Default: (none)
  #
  maxNumWriters = 1
  writerIsAlsoReader = 1
  retryUp = 0
  retryDown = 2
  clusterId = 10

  # Controls the primary settings during failover.
  # More details at https://github.com/percona/pxc_scheduler_handler#persist-primary-values
  #
  # Allowed values:
  #
  #       0 Disable
  #       1 Persist only write settings
  #       2 Persist both read and write settings
  persistPrimarySettings=0



  # == proxysql ===================================================
  # The proxysql section is for ProxySQL-specific information.
  #
  # These settings will be read and used whenever the scheduler is run.
  #
  [proxysql]
  port = 6032
  host = "127.0.0.1"
  user = "<valid user to connect from real ip as for proxysql_server table>"
  password = "<password>"
  clustered = false
  lockfilepath ="/var/run/pxc_scheduler_handler"
  respectManualOfflineSoft=false



  #== global ======================================================
  # The global section are for variables that are not ProxySQL or
  # cluster specific.
  #
  # These settings will be read and used whenever the scheduler is run.
  #
  [global]
  debug = true

  # stdout: output is redirected to proxysql logs
  # file: output is written to the file pointed by logFile
  logTarget = "stdout" #stdout | file

  # Defines the log level to be used.
  # Allowed options are [error,warning,info,debug]
  logLevel = "info"
  logFile = "/var/log/pxc_scheduler_handler/pscheduler.log"

  # Should be set to false if we are pxc_scheduler_handler through percona-scheduler-admin.
  daemonize = false
  daemonInterval = 2000

  # boolean variable which enables reporting of statistics.
  performance = true

  # Not used currently
  OS = "na"

  # Time in seconds after which the file lock is considered expired [local instance lock]
  lockFileTimeout = 60 #seconds

  # Time in seconds after which the cluster lock is considered expired
  lockClusterTimeout = 600 #seconds



  #== setup =======================================================
  # These variables are used only upon Setup
  # Changing these variables after setup will not affect operation
  #
  [setup]

  # --------------------------------
  # The clusterAppUser is the ProxySQL user account that should be
  # used by clients to access the cluster.
  #
  # Uncomment the following options (clusterAppUser and clusterAppUserPassword)
  # to enable the setting of the clusterAppUser for this cluster.
  #
  #clusterAppUser="proxysql_user"
  #clusterAppUserPassword="passw0rd"

  # --------------------------------
  # The monitorUser is used by ProxySQL to access the servers and
  # check the connections.
  #
  monitorUser="monitor"
  monitorUserPassword="monitor"

  # --------------------------------
  # The clusterXXX information is used to setup the cluster for
  # use by ProxySQL.
  #
  clusterHost="<IP_ADDRESS>"
  clusterPort=3306
  clusterUser="admin"
  clusterUserPassword="admin"

  # --------------------------------
  # ProxySQL will use SSL to connect to the backend servers
  #
  useSSL=0

  # --------------------------------
  # Max number of connections from ProxySQL to the backend servers.
  #
  maxConnections=1000


  # --------------------------------
  # Defines how frequently (in milliseconds) the scheduler must be run
  #
  nodeCheckInterval=2000

  
  
