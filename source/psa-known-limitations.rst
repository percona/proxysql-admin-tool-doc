.. _psa-known-limitations:

================================================================================
Percona Scheduler Admin tool known limitations
================================================================================


.. _do-not-combine:

Do not combine the following options
---------------------------------------------------

The following options are mutually exclusive. An attempt to run them together
results in error.

*  :ref:`psa-update-write-weight` and :ref:`psa-auto-assign-weights`

*  :ref:`psa-write-node` and :ref:`psa-auto-assign-weights`

*  :ref:`psa-write-node` and :ref:`psa-update-write-weight`


.. _locations:

Log file or lock file locations
---------------------------------------

Do not place the log file or the lock file in the Home directory. In the toml configuration file, these values are ``logFile`` and ``lockfilepath``. The scheduler script runs under the context of the user ``proxysql:proxysql`` and cannot access the Home directory. Any attempt causes permission denied errors. If needed, you can override this limitation by setting  ``ProtectHome=no`` in ``/etc/systemd/system/multi-user.target.wants/proxysql.service``.
