.. _proxy-tarball:

Installing ProxySQL v2 using a tarball
-----------------------------------------

You can install ProxySQL v2 and ProxySQL-admin from a tarball if the recommended package manager method is not applicable in your environment.

Download a file from the [ProxySQL v2 downloads page](https://www.percona.com/downloads/proxysql2/)
and install to a custom directory.

1. Visit one of the downloads pages, select **Linux - Generic** in the *Software* field and download the package appropriate for your platform.

    > Note:

	>As of ProxySQL 2.0.15 and later, the multiple tarball files are combined into the following files:

 > | Name | Description |
   |------|-------------|
   |proxysql-2.0.XX-Linux-x86_64.glibc2.12.tar.gz | For every supported operating system but `xenial` For CentOS 7, install OpenSSL 1.1.1, if needed. |
   | proxysql-2.0.XX-Linux-x86_64.glibc2.23.xenial.tar.gz | For Ubuntu 16.04 `xenial` only. The password-based file encryption requires OpenSSL 1.1.1, but Ubuntu 16.04 does not support this OpenSSL version. A special, statically linked OpenSSL 1.1.1 binary is packaged with the executable. This packaged binary avoids conflicts with the system OpenSSL and any shared libraries. Each new release rebuilds the binary.

For version 2.0.14, download `proxysql-2.0.14-Linux-x86_64.glibc2.12.tar.gz`.

2. For versions 2.0.13 or lower, extract the files from the archive and
    change to the directory that contains the extracted files:

    ``` bash
    $ # Extract the files (assuming you have changed to the download destination directory)
    $ tar xzf proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE*.tar.gz
    $ # Change to the directory that contains the extracted files
    $ cd proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE
    ```
 For version 2.0.14 and higher, the step is the same except the extraction command is:

 ``` bash
tar xzf proxysql-2.0.XX-<PLATFORM-ARCHITECTURE*>.tar.gz
```

2. Create a directory to store data:

    ``` bash
    $ mkdir /home/user/data
    ```

2.  Update the value of the `datadir` in the configuration file to point to the
    data directory you have created.

    ``` bash
    datadir="/home/user/data"
    ```

2.  Set other options as needed.

Now, you can start ProxySQL. Use the option to pass the configuration file you
have updated:

``` bash
$ /home/user/path-to-extracted-dir/usr/bin/proxysql \
-c /home/user/path-to-extracted-dir/etc/proxysql.cnf

... [INFO] Using config file proxysql.cnf
```
