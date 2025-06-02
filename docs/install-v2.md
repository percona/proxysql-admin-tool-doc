# Install Percona's build of ProxySQL 2.x.x and the admin utilities


Select the same package installer used to install [Percona XtraDB Cluster](https://www.percona.com/doc/percona-xtradb-cluster/8.0/install/index.html) or other Percona software.

=== "On a Debian-derived distribution"

    If you used APT to install Percona software, run the following command as sudo or as root:
    
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

    If you used YUM to install Percona software, run the following command:
    
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

## Verify the pxc_scheduler_handler installation

If you have installed [ProxySQL 2.3.2-2.1](release-notes-2.3.2-1.md) or later, verify the pxc_scheduler_handler installation with the following command:

```{.bash data-prompt="$"}
$ percona-scheduler-admin --debug
```

Running this command without the [pxc_scheduler_handler configuration file](psh-configuration.md) generates an error.

??? example "Error message"

    ```{.text .no-copy}
    ERROR : The --config-file option is required but is missing from the command.
    ```

## Run Docker

To run ProxySQL2 in Docker, download the latest image at [percona/proxysql2](https://hub.docker.com/r/percona/proxysql2).

## MySQL 8.4 and Percona Server for MySQL 8.4 considerations

--8<--- "note-8.4.md"
