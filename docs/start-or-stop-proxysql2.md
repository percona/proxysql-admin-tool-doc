# Start and stop ProxySQL

There are several methods to start or stop ProxySQL 2. You can invoke the commands with either `systemctl` or `service`. Currently, both are supported.

## Start ProxySQL 2.x.x with a service manager

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

## Stop ProxySQL 2.x.x

To stop ProxySQL 2.x, run any of the following commands:

=== "service and proxysql"

    ```{.bash data-prompt="$"}
    $ sudo service proxysql stop
    ```

=== "service and proxysql2"

    ```{.bash data-prompt="$"}
    $ sudo service proxysql2 stop
    ```

=== "systemctl and proxysql"

    ```{.bash data-prompt="$"}
    $ sudo systemctl stop proxysql 
    ```

=== "systemctl and proxysql2"

    ```{.bash data-prompt="$"}
    $ sudo systemctl stop proxysql2 
    ```