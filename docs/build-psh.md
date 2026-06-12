# Build the pxc_scheduler_handler tool

This task guide builds `pxc_scheduler_handler` from source. For package manager installs, see [Install Percona build of ProxySQL and the admin tools](install-v2.md).

The `pxc_scheduler_handler` tool includes two main files: the `pxc_scheduler_handler` binary and the `percona_scheduler_admin` script.

The `pxc_scheduler_handler` binary performs the following tasks:

* Evaluates the cluster state and scenario

* Monitors cluster health

* Performs actions, including failover during an incident

The `percona_scheduler_admin` script runs `pxc_scheduler_handler` and returns responses from the configuration file.

`pxc_scheduler_handler` requires `percona_scheduler_admin` for normal operation. Manual intervention is required without `percona_scheduler_admin`.

A git clone with submodules does not check out submodule content. Submodules require initialization and update before the build.

## Build the scheduler submodule

Complete the following steps to build `pxc_scheduler_handler`:
{.power-number}

1. Initialize git submodules:

    ```{.bash data-prompt="$"}
    $ git submodule update --init
    ```

2. Build the scheduler submodule:

    ```{.bash data-prompt="$"}
    $ build_scheduler.sh
    ```

The build writes the `pxc_scheduler_handler` binary to the repository base directory.

Do not run multiple instances of `pxc_scheduler_handler`. A second instance started while another instance runs causes the following results:

* Additional network and system resource consumption

* Identical results from both instances because both read the same configuration file

## Create a MySQL admin account

Create an `admin` user account for communication between ProxySQL and `pxc_scheduler_handler`.

Create the account with `mysql_native_password` authentication:

```{.bash data-prompt="mysql>"}
mysql> CREATE USER 'admin'@'192.%' IDENTIFIED WITH 'mysql_native_password'
by 'admin';
```

[ProxySQL 2.6.2](2.6.2.md) and later releases support `caching_sha2_password` authentication. Create the account with that method when your environment requires it:

```{.bash data-prompt="mysql>"}
mysql> CREATE USER 'admin'@'192.%' IDENTIFIED WITH 'caching_sha2_password' BY 'admin';
```

Grant privileges to the `admin` account:

```{.bash data-prompt="mysql>"}
mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'192.%' WITH GRANT OPTION;
```

For configuration details, see [pxc_scheduler_handler overview](psh-overview.md) and [configuration file reference](psh-configuration.md).

!!! note "Related topic"

    [Log file or lock file locations](psh-known-limitations.md#do-not-place-the-log-file-or-lock-file-in-the-home-directory)
