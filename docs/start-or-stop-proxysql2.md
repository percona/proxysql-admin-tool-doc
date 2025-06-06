# Start and stop Percona build of ProxySQL

There are several methods to start or stop ProxySQL. You can invoke the commands with either `systemctl` or `service`. Currently, both are supported.

Make sure to use the correct package name for the version you installed, such as `proxysql2` or `proxysql3`.

## Start ProxySQL with a service manager

=== "service"

    ```{.bash data-prompt="$"}
    $ sudo service proxysql2 start
    ```

=== "systemd"

    ```{.bash data-prompt="$"}
    $ sudo systemctl start proxysql
    ```

If you have updated the configuration, start *ProxySQL* with the `-c` option to pass the updated configuration file:

```{.bash data-prompt="$"}
$ /home/user/<path-to-extracted-dir>/usr/bin/proxysql \
-c /home/user/<path-to-extracted-dir>/etc/proxysql.cnf
```

!!! admonition "See also"

    [ProxySQL Documentation: Getting Started](https://proxysql.com/documentation/getting-started/).

## Stop ProxySQL

To stop ProxySQL, run any of the following commands:

=== "service and proxysql3"

    ```{.bash data-prompt="$"}
    $ sudo service proxysql3 stop
    ```

=== "service and proxysql2"

    ```{.bash data-prompt="$"}
    $ sudo service proxysql2 stop
    ```

=== "systemctl and proxysql3"

    ```{.bash data-prompt="$"}
    $ sudo systemctl stop proxysql3 
    ```

=== "systemctl and proxysql2"

    ```{.bash data-prompt="$"}
    $ sudo systemctl stop proxysql2 
    ```