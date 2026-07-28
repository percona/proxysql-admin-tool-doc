# Install Percona build of ProxySQL and the admin tools

This task guide installs the Percona build of ProxySQL and Percona admin tools with a package manager.

Use the same package manager that installs [Percona XtraDB Cluster](https://www.percona.com/doc/percona-xtradb-cluster/8.0/install/index.html) or other Percona software. Matching package managers ensures repository compatibility.

For tarball or offline installs, see the [tarball installation guide](install-proxysql2-tarball.md) or the [download locations guide](where-to-download-proxysql.md).

!!! tip "Recommended version"

    Install the latest ProxySQL 3 release with the `proxysql3` package. Use `proxysql2` only for an existing ProxySQL 2.x deployment or a version lock. See [release notes](release-notes.md) for the current ProxySQL 3 version.

## Install ProxySQL with a package manager

Select the tab that matches your Linux distribution.

=== "On a Debian-derived distribution"

    Use APT when Percona software is installed from APT repositories. Run one of the following commands as root or with `sudo`.

    For ProxySQL 3 (recommended):

    ```{.bash data-prompt="$"}
    $ sudo apt install proxysql3
    ```

    For ProxySQL 2 (legacy deployments only):

    ```{.bash data-prompt="$"}
    $ sudo apt install proxysql2
    ```

    ??? example "Expected output"

        ```{.text .no-copy}
        Reading package lists... Done
        Building dependency tree
        Reading state information... Done
        The following additional packages will be installed:
          debconf-utils logrotate
        The following NEW packages will be installed:
          debconf-utils logrotate proxysql2
        0 upgraded, 3 newly installed, 0 to remove and 3 not upgraded.
        Need to get 7259 kB of archives.
        ...
        ```

=== "On a Red Hat-derived distribution"

    Use YUM or DNF when Percona software is installed from YUM repositories. Run one of the following commands as root or with `sudo`.

    For ProxySQL 3 (recommended):

    ```{.bash data-prompt="$"}
    $ sudo yum install proxysql3
    ```

    For ProxySQL 2 (legacy deployments only):

    ```{.bash data-prompt="$"}
    $ sudo yum install proxysql2
    ```

    ??? example "Expected output"

        ```{.text .no-copy}
        Last metadata expiration check: 0:01:47 ago on Wed Oct  5 14:42:00 2022.
        Dependencies resolved.
        =========================================================================================================================
        Package                  Architecture          Version                        Repository                           Size
        =========================================================================================================================
        Installing:
        proxysql2                x86_64                2.4.4-1.1.el8                  tools-release-x86_64                 21 M
        Installing dependencies:
        logrotate                x86_64                3.14.0-4.el8                   baseos                               85 k

        Transaction Summary
        =========================================================================================================================
        Install  2 Packages

        Total download size: 21 M
        Installed size: 88 M
        Is this ok [y/N]: y
        Downloading Packages:
        (1/2): logrotate-3.14.0-4.el8.x86_64.rpm                                                 371 kB/s |  85 kB     00:00
        (2/2): proxysql2-2.4.4-1.1.el8.x86_64.rpm                                                3.6 MB/s |  21 MB     00:05
        -------------------------------------------------------------------------------------------------------------------------
        Total                                                                                    3.3 MB/s |  21 MB     00:06
        ...
        ```

## Verify pxc_scheduler_handler installation

ProxySQL 3 releases and [ProxySQL 2.3.2-1.2](release-notes-2.3.2-1.md) and later 2.x releases include [pxc_scheduler_handler](psh-overview.md). Verify the installation with the following command:

```{.bash data-prompt="$"}
$ percona-scheduler-admin --debug
```

Without the [pxc_scheduler_handler configuration file](psh-configuration.md), the command reports an error.

??? example "Error message"

    ```{.text .no-copy}
    ERROR : The --config-file option is required but is missing from the command.
    ```

## Run ProxySQL in Docker

Pull a Docker image from one of the following repositories:

* ProxySQL 3 (recommended) — [percona/proxysql3](https://hub.docker.com/r/percona/proxysql3)

* ProxySQL 2 (legacy deployments only) — [percona/proxysql2](https://hub.docker.com/r/percona/proxysql2)

## MySQL 8.4 and Percona Server for MySQL 8.4 considerations

--8<--- "note-8.4.md"

## MySQL 9.x considerations

MySQL 9.x removes `mysql_native_password`. After you install ProxySQL:

* For MySQL 9.x clients, set ProxySQL’s `mysql-default_authentication_plugin` to `caching_sha2_password` in `proxysql.cnf` (preferred). This is a ProxySQL setting, not a separate package.
* With admin tools 3.0.9 and later, set `AUTH_PLUGIN` in `/etc/proxysql-admin.cnf` if you need a non-default value. The default is already `caching_sha2_password`; you do not install an auth plugin package.

For full configuration and troubleshooting steps, see [Connect to ProxySQL with MySQL 9.x clients](mysql-9-authentication.md).
