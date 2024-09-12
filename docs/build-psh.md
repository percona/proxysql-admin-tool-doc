# Build the pxc_scheduler_handler tool

The pxc_scheduler_handler tool has two main files: the `pxc_scheduler_handler` binary and the `percona_scheduler_admin` script.

The `pxc_scheduler_handler` does the following tasks:

* Monitors the cluster health

* Processes the cluster state and evaluates the scenario

* Performs actions, such as failover in case of an incident

The `percona_scheduler_admin` script runs and provides responses based on the
configuration file for the `pxc-scheduler_handler` binary.

Running `pxc_scheduler_handler`  without `percona_scheduler_admin` requires
manual intervention.

Cloning a git project that contains submodules does not automatically check out the submodule content. The submodules require initialization and updating before they are functional.

## Build the module

You can perform the submodule initialization by running the following statement:

```{.bash data-prompt="$"}
$ git submodule update --init
```

Run the following command to build the scheduler submodule.

```{.bash data-prompt="$"}
$ build_scheduler.sh
```

The `pxc_scheduler_handler` binary is located in the base directory.

We do not recommend running multiple instances of the same binary. If you start a new instance when an instance of
`pxc_scheduler_handler` is already running, the binary runs, but the second instance does the following:

* Consumes network and system resources

* Returns the same results since multiple versions use the same configuration file

## Create an account

Create an `admin` user account. Use this account for communication through ProxySQL and pxc_scheduler_handler.

The following example uses the `mysql_native_password` authentication method to create an admin user account:

```{.bash data-prompt="mysql>"}
mysql> CREATE USER 'admin'@'192.%' IDENTIFIED WITH 'mysql_native_password'
by 'admin';
```

If you are using a [ProxySQL version 2.6.2](2.6.2.md) or later, you can use the `caching_sha2_password` authentication method. The following example creates an admin user account using that method:

```{.bash data-prompt="mysql>"}
mysql> CREATE USER 'admin'@'192.%' IDENTIFIED WITH 'caching_sha2_password' BY 'admin';
```

Grant privileges to the `admin` user account:

```{.bash data-prompt="mysql>"}
mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'192.%' WITH GRANT OPTION;
```

!!! admonition "See also"
    
    [Log file or lock file locations](psh-known-limitations.md#do-not-place-the-log-file-or-lock-file-in-the-home-directory)

