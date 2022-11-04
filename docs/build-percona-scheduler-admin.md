# Build the Percona Scheduler admin tool

The Percona Scheduler Admin has two main files: the `pxc_scheduler_handler` binary and the `percona_scheduler_admin` script.

The `pxc_scheduler_handler` does the following tasks:

* Monitors the cluster’s health

* Processes the cluster’s state and evaluates the scenario

* Performs actions, such as failover in case of an incident

The `percona_scheduler_admin` script runs and provides responses based on the
configuration file for the `pxc-scheduler_handler` binary.

Running `pxc_scheduler_handler`  without `percona_scheduler_admin` requires
manual intervention.

Cloning a git project that contains submodules does not automatically check out the submodule content. The submodules require initialization and updating before they are functional.

## Build the module

You can perform the submodule initialization by running the following statement:

```bash
$> git submodule update --init
```

Run the following command to build the scheduler submodule.

```bash
$> build_scheduler.sh
```

The `pxc_scheduler_handler` binary is located in the base directory.

We do not recommend running multiple instances of the same binary. If you start a new instance when an instance of
`pxc_scheduler_handler` is already running, the binary runs, but the second instance does the following:

* Consumes network and system resources

* Returns the same results since the multiple versions use the same configuration file

## Create an account

Create an `admin` user account. Use this account for communication through *ProxySQL* and pxc_scheduler_handler.

```sql
mysql> CREATE USER 'admin'@'192.%' IDENTIFIED WITH 'mysql_native_password'
by 'admin';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'192.%' WITH GRANT OPTION;
```

See [Log file or lock file locations](/docs/psa-known-limitations.md)

