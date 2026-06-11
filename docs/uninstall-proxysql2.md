# Uninstall Percona build of ProxySQL

This task guide removes the Percona build of ProxySQL with a package manager. For installation steps, see [Install Percona build of ProxySQL and the admin tools](install-v2.md).

Identify the installed package name: `proxysql3` for ProxySQL 3 or `proxysql2` for ProxySQL 2.

## List the installed ProxySQL package

Select the tab that matches your Linux distribution.

=== "List package contents using APT"

    Run one of the following commands to list package information before uninstall:

    For ProxySQL 3:

    ```{.bash data-prompt="$"}
    $ apt search proxysql3
    ```

    For ProxySQL 2:

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

    Run one of the following commands to display package information:

    For ProxySQL 3:

    ```{.bash data-prompt="$"}
    $ sudo yum info proxysql3
    ```

    For ProxySQL 2:

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

## Uninstall ProxySQL

Select the tab that matches your package manager.

=== "Uninstall in a Debian-based distribution"

    APT manages software installation and removal on Debian and Debian-based distributions.

    `apt remove` uninstalls packages and retains configuration files, data, and dependencies. A later reinstall of the same major version reuses those files.

    Run one of the following commands to remove ProxySQL:

    For ProxySQL 3:

    ```{.bash data-prompt="$"}
    $ sudo apt remove proxysql3
    ```

    For ProxySQL 2:

    ```{.bash data-prompt="$"}
    $ sudo apt remove proxysql2
    ```

    !!! warning "Data loss"

        `apt purge` removes packages, configuration files, and data. Run `apt purge` only when you do not need ProxySQL configuration or data.

    Run one of the following commands to purge ProxySQL:

    For ProxySQL 3:

    ```{.bash data-prompt="$"}
    $ sudo apt purge proxysql3
    ```

    For ProxySQL 2:

    ```{.bash data-prompt="$"}
    $ sudo apt purge proxysql2
    ```

    `apt autoremove` removes unused libraries and dependent packages from prior installs. Run the following command after `apt remove` or `apt purge`:

    ```{.bash data-prompt="$"}
    $ sudo apt autoremove
    ```

=== "Uninstall in a Red Hat-derived distribution"

    Run one of the following commands to uninstall ProxySQL:

    For ProxySQL 3:

    ```{.bash data-prompt="$"}
    $ sudo yum remove proxysql3
    ```

    For ProxySQL 2:

    ```{.bash data-prompt="$"}
    $ sudo yum remove proxysql2
    ```

    Run one of the following commands to uninstall ProxySQL and unused dependencies:

    For ProxySQL 3:

    ```{.bash data-prompt="$"}
    $ sudo yum autoremove proxysql3
    ```

    For ProxySQL 2:

    ```{.bash data-prompt="$"}
    $ sudo yum autoremove proxysql2
    ```
