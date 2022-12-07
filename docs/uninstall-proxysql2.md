# Uninstall ProxySQL 2.x.x

You can uninstall *ProxySQL 2.x.x* using the command line.

=== "List package contents using APT"

    To find information before uninstalling or removing the `ProxySQL2` package, run the following command:

    ```{.bash data-prompt="$"}
    $ apt search proxysql2
    ```

    ??? example "Expected output"

        ```{.text .no-copy}
        Sorting... Done
        Full Text Search... Done
        proxysql2/unknown,now 2.4.4-1.1.focal amd64 [installed]
          High performance MySQL proxy
        ```



=== "List package contents in a Red Hat-derived distribution"

    To display package information, use the following command:

    ```{.bash data-prompt="$"}
    $ sudo yum info proxysql2
    ```

    ??? example "Expected output"

        ```{.text .no-copy}
        Last metadata expiration check: 0:07:36 ago on Wed Oct  5 14:42:00 2022.
        Installed Packages
        Name         : proxysql2
        Version      : 2.4.4
        Release      : 1.1.el8
        Architecture : x86_64
        Size         : 88 M
        Source       : proxysql2-2.4.4-1.1.el8.src.rpm      Repository   : @System
        From repo    : tools-release-x86_64
        Summary      : A high-performance MySQL proxy
        URL          : http://www.proxysql.com/
        License      : GPL+
        Description  : A high-performance MySQL proxy
        ```

To uninstall ProxySQL 2, the following instructions are based on the package manager.

=== "Uninstall in a Debian-based distribution"

    The Advanced Package Tool (APT) handles the software installation and removal on Debian and Debian-based Linux distributions.

    The `apt remove` removes the packages. Any configuration files, data, and dependencies remain in the system. If you reinstall *ProxySQL 2.x.x*, the software uses the same configuration files, data, and dependencies. The reinstallation may ask to override the existing files.

    You can uninstall `ProxySQL 2.x.x` with the following command:

    ```{.bash data-prompt="$"}
    $ sudo apt remove proxysql2
    ```

    The `apt purge` removes the packages and any configuration files and data. You can also use `apt purge` to remove packages for an uninstalled application.

    ```{.bash data-prompt="$"}
    $ sudo apt purge proxysql2
    ```

    The `apt autoremove` removes the packages, configuration files, data, and any unused libraries or dependent packages that were installed when the application was installed.

    To remove them, run the following command:

    ```{.bash data-prompt="$"}
    $ sudo apt autoremove
    ```

=== "Uninstall in a Red Hat-derived distribution"

    To uninstall *ProxySQL 2.x.x*, use the following command:

    ```{.bash data-prompt="$"}
    $ sudo yum remove proxysql2
    ```

    To uninstall *ProxySQL 2.x.x* along with unused dependencies, use the following command:

    ```{.bash data-prompt="$"}
    $ sudo yum autoremove proxysql2
    ```
