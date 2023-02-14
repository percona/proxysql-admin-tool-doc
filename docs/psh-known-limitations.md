# Known issues in pxc_scheduler_handler

This document lists the known issues in the pxc_scheduler_handler.

## Do not combine certain options

The following options are mutually exclusive. An attempt to combine these options in a command creates in an error and no action is taken.

* [-–update-write-weight](./psh-detailed-options.md#-update-write-weight) and [-–auto-assign-weights](./psh-detailed-options.md#-auto-assign-weights)

* [-–write-node](./psh-detailed-options.md#-write-node) and [-–auto-assign-weights](./psh-detailed-options.md#-auto-assign-weights)

* [-–write-node](./psh-detailed-options.md#-write-node) and [-–update-write-weight](./psh-detailed-options.md#-update-write-weight)

## Do not place the log file or lock file in the Home directory

Do not place the log file or the lock file in the Home directory. The scheduler script runs under the context of the user `proxysql:proxysql` and cannot access the Home directory. Any attempt causes permission denied errors. If needed, you can override this limitation by setting  `ProtectHome=no` in `/etc/systemd/system/multi-user.target.wants/proxysql.service`. In the toml configuration file, the values are `logFile` and `lockfilepath`.
