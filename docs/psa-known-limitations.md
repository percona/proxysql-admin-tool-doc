# Percona Scheduler Admin tool known limitations

## Do not combine the following options

The following options are mutually exclusive. An attempt to run them together
results in error.

* –update-write-weight and –auto-assign-weights

* –write-node and –auto-assign-weights

* –write-node and –update-write-weight

## Log file or lock file locations

Do not place the log file or the lock file in the Home directory. In the toml configuration file, these values are `logFile` and `lockfilepath`. The scheduler script runs under the context of the user `proxysql:proxysql` and cannot access the Home directory. Any attempt causes permission denied errors. If needed, you can override this limitation by setting  `ProtectHome=no` in `/etc/systemd/system/multi-user.target.wants/proxysql.service`.
