# Known issues in Percona Scheduler Admin

This document lists the known issues in the Percona Scheduler Admin.

## Do not combine the certain options

The following options are mutually exclusive. An attempt to combine these options in a command creates in an error and no action is taken.

* –update-write-weight and –auto-assign-weights

* –write-node and –auto-assign-weights

* –write-node and –update-write-weight

## Do not place the log file or lock file in the Home directory

Do not place the log file or the lock file in the Home directory. The scheduler script runs under the context of the user `proxysql:proxysql` and cannot access the Home directory. Any attempt causes permission denied errors. If needed, you can override this limitation by setting  `ProtectHome=no` in `/etc/systemd/system/multi-user.target.wants/proxysql.service`. In the toml configuration file, the values are `logFile` and `lockfilepath`.
