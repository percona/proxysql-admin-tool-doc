# Build the Percona Scheduler admin tool

In the command line, run the following statement to initialize all
submodules and retrieve the latest code from the submodule:

```bash
$> git submodule update --init
```

Run the following command to build the scheduler submodule.

```bash
$> build_scheduler.sh
```

Percona Scheduler Admin has two main files: the `pxc_scheduler_handler` binary
and the `percona_scheduler_admin` script.

The `pxc_scheduler_handler` does the
following:


* Monitors the cluster’s health


* Processes the cluster’s state and evaluates the scenario


* Performs actions, such as failover in case of an incident

The `percona_scheduler_admin` script runs and provides responses based on the
configuration file for the `pxc-scheduler_handler` binary.

Running `pxc_scheduler_handler`  without `percona_scheduler_admin` requires
manual intervention.

We do not recommend running multiple instances of the same binary. If you
attempt this task when an instance of
`pxc_scheduler_handler` is running the binary runs, but the following occurs:


* Consumes network and system resources


* Returns the same results since the multiple versions use the same
configuration file

The `pxc_scheduler_handler` binary is located in the base directory.

Create an `admin` user account. Use this account for communication through
proxysql and pxc_scheduler_handler.

```
mysql> CREATE USER 'admin'@'192.%' IDENTIFIED WITH 'mysql_native_password'
by 'admin';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'192.%' WITH GRANT OPTION;
```

See [Log file or lock file locations](/docs/psa-known-limitations.md)

