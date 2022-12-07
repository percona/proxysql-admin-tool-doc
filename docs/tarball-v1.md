# Install ProxySQL 1.X from a binary tarball

Installing *ProxySQL* from a tarball is an alternative method if the recommended method, using either the apt or the yum package manager, is not applicable in your environment.

1. In [Download ProxySQL 1.x page](https://www.percona.com/downloads/proxysql/), select the *ProxySQL* version, and select **Linux - Generic** in the *Software* field. Download the appropriate package for your platform.

2. Extract the files from the archive and change to the directory that contains the extracted files.

    ```{.bash data-prompt="$"}
    # Extract the files (assuming you have changed to the download destination directory)
    $ tar xzf proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE*.tar.gz
    # Change to the directory that contains the extracted files
    $ cd proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE
    ```

3. Create a directory to store the *ProxySQL* data:

    ```{.bash data-prompt="$"}
    $ mkdir /home/user/data
    ```

4. Update the value of the `datadir` in the configuration file to point to the data directory you have created.

    ```text
    datadir="/home/user/data"
    ```

5. Set the other options, as needed.

6. Start *ProxySQL* with the `-c` option to pass the configuration file you have updated:

    ```{.bash data-prompt="$"}
    $ /home/user/path-to-extracted-dir/usr/bin/proxysql \
    -c /home/user/path-to-extracted-dir/etc/proxysql.cnf
    ```
