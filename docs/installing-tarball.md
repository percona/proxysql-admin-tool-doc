# Install ProxySQL 2.x.x from a binary tarball

Installing *ProxySQL* version 2.x from a tarball is an alternative method if the recommended method, using either the apt or the yum package manager (see /install-v2.md), is not available in your environment.

The tar file extraction procedure is the same for all versions. The difference between versions is the available tar files or the command to extract the file.

Follow these steps:

1. In [Download ProxySQL2](https://www.percona.com/downloads/proxysql2/), select the version.

2. In the *Software* field, select **Linux - Generic**.

3. Select the tar file.

    See [Available tar files for ProxySQL 2.3.2-1.2 and higher](#available-tar-files-for-proxysql-232-12-and-higher)

    See [Available tar files from ProxySQL 2.0.15 to ProxySQL 2.3.2(#available-tar-files-from-proxysql-2015-to-proxysql-232)

    See ProxySQL 2.0.15 and proxysql-admin

4. Navigate to the downloaded tar file.

5. Extract the files with the following commands:

    See [ProxySQL 2.0.14 or higher extraction commands](#proxysql-2014-or-higher-extraction-commands).

    See [ProxySQL 2.0.13 or lower extraction commands](#proxysql-2013-or-lower-extraction-commands)

6. Create a directory to store the *ProxySQL* data.

    ```sh
    $> mkdir /home/user/data
    ```

7. In the configuration file, update the `datadir` value to point
to the created data directory.

    ```text
    datadir="/home/user/data"
    ```

8. Set the other options, as needed.

## Available tar files for ProxySQL 2.3.2-1.2 and higher

Starting with **ProxySQL 2.3.2-1.2**, Percona no longer provides a tarball for
CentOS 6.

**NOTE**: For more information, see [Spring Cleaning: Discontinuing RHEL
6/CentOS 6 (glibc2.12) and 32-bit Binary Builds of Percona Software](https://www.percona.com/blog/spring-cleaning-discontinuing-rhel-6-centos-6-glibc-2-12-and-32-bit-binary-builds-of-percona-software/)

The following tar files are available:

| Name                                              | Description                           |
| ------------------------------------------------- | ------------------------------------- |
| proxysql-2-version-Linux-x86_64.glibc2.23.tar.gz  | For every supported operating system. |

## Available tar files from ProxySQL 2.0.15 to ProxySQL 2.3.2

 In [Download ProxySQL2](https://www.percona.com/downloads/proxysql2/), select the version and in the *Software* field select **Linux - Generic**. Download the package appropriate for your platform.

The tarball file is the following:

| Name                                                  | Description                                                                                        |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| proxysql-2.0.XX-Linux-x86_64.glibc2.12.tar.gz         | For every supported operating system but `xenial`. For CentOS 7, install OpenSSL 1.1.1, if needed. |
| proxysql-2.x.xx-Linux-x86_64.glibc2.17.tar.gz         | For every supported operating system                                                               |
| proxysql-2.0.XX-Linux-x86_64.glibc2.23.xenial.tar.gz  | For Ubuntu 16.04 `xenial` only.     

**Important**: The password-based file encryption requires OpenSSL 1.1.1, but Ubuntu 16.04 does not support this OpenSSL version. A special statically linked OpenSSL 1.1.1 binary is packaged with the executable. This packaged binary avoids conflicts with the system OpenSSL and any shared libraries. Each new release rebuilds the binary.

## ProxySQL 2.0.14 or higher extraction commands

The extraction commands for version 2.0.14 and higher:

```sh
$> # Extract the files to the download destination directory
$> tar xzf proxysql-2.X.X-<PLATFORM-ARCHITECTURE*>.tar.gz
$> # Change to the directory that contains the extracted files
$> cd proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE
```

## ProxySQL 2.0.13 or lower extraction commands

For versions 2.0.13 or lower, the step is the same except the extraction command is:

```sh
# Extract the files (assumes you have changed to the download destination directory)
$ tar xzf proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE*.tar.gz
# Change to the directory that contains the extracted files
$ cd proxysql-VERSION-Linux-PLATFORM-ARCHITECTURE
```

## Starting ProxySQL

Start *ProxySQL* with the `-c` option to pass the updated configuration
file:

```sh
$> /home/user/path-to-extracted-dir/usr/bin/proxysql \
-c /home/user/path-to-extracted-dir/etc/proxysql.cnf
```

**See also** [ProxySQL 2.x and proxysql-admin utility](/v2-config.md)
