# Install Percona build of ProxySQL binary tarball

This task guide installs the Percona build of ProxySQL from a binary tarball.

Servers with Percona repositories should use the [package manager installation guide](install-v2.md) and install `proxysql3`. Tarball installs differ by ProxySQL version in file names and extraction commands.

Percona recommends a ProxySQL 3 tarball for standard deployments. Select a ProxySQL 2 tarball only for an existing 2.x deployment or a version lock.

## Review version-specific tarball changes

### CentOS 6 discontinuation

[_ProxySQL 2.3.2-1.2_](release-notes-2.3.2-1.md) and later releases omit a CentOS 6 tarball. See [Spring Cleaning: Discontinuing RHEL 6/CentOS 6 (glibc2.12) and 32-bit Binary Builds of Percona Software](https://www.percona.com/blog/spring-cleaning-discontinuing-rhel-6-centos-6-glibc-2-12-and-32-bit-binary-builds-of-percona-software/) for details.

### OpenSSL 1.1.1 on Ubuntu 16.04

Password-based file encryption requires OpenSSL 1.1.1. Ubuntu 16.04 does not include OpenSSL 1.1.1. Percona packages a statically linked OpenSSL 1.1.1 binary with the executable. The packaged binary avoids conflicts with the system OpenSSL and shared libraries. Each release rebuilds the binary.

## Identify tarball file name format

Tarball binaries use the following file name pattern:

proxysql-&lt;version&gt;-&lt;operating_system&gt;-&lt;architecture&gt;-&lt;glibc_version&gt;.tar.gz

The following file name is an example for ProxySQL 3.0.6:

proxysql-3.0.6-Linux-x86_64.glibc2.34.tar.gz

## Download the tarball

Follow the [download locations guide](where-to-download-proxysql.md) to select *Platform*, *Linux*, and *Generic* on the Percona download page.

Select a ProxySQL 3 tarball that matches your operating system and `glibc` version. Select a ProxySQL 2 tarball only when your deployment requires the 2.x product line.

!!! note

    Tarball file names can list different `glibc` versions by ProxySQL version and operating system. See the [Percona download page](https://www.percona.com/download-proxysql) for options for your version and platform.

??? note "Tarball file names for ProxySQL 3.x or higher"

    | Name | Description |
    | ---- | ----------- |
    | proxysql-&lt;version&gt;-Linux-x86_64.glibc&lt;glibc_version&gt;.tar.gz | Supported operating systems with `glibc` &lt;glibc_version&gt;. See the [Percona download page](https://www.percona.com/download-proxysql) for options. |

??? note "Tarball file names for ProxySQL 2.4.4 and higher"

    | Name | Description |
    | ---- | ----------- |
    | proxysql-2-&lt;version&gt;-Linux-x86_64.glibc&lt;glibc_version&gt;.xenial.tar.gz | Ubuntu 16.04 `xenial` only |
    | proxysql-2-&lt;version&gt;-Linux-x86_64.glibc&lt;glibc_version&gt;.tar.gz | Every supported operating system |
    | proxysql-2-&lt;version&gt;-Linux-x86_64.glibc&lt;glibc_version&gt;.tar.gz | Every supported operating system except `xenial`. On CentOS 7, install OpenSSL 1.1.1 when required. See the download page for available `glibc` options. |

??? note "Tarball file names from ProxySQL 2.3.2-1.2 to ProxySQL 2.4.3"

    | Name | Description |
    | ---- | ----------- |
    | proxysql-2-&lt;version&gt;-Linux-x86_64.glibc&lt;glibc_version&gt;.xenial.tar.gz | Ubuntu 16.04 `xenial` only |

??? note "Tarball file names from ProxySQL 2.0.15 to ProxySQL 2.3.2"

    | Name | Description |
    | ---- | ----------- |
    | proxysql-2-&lt;version&gt;-Linux-x86_64.glibc&lt;glibc_version&gt;.tar.gz | Every supported operating system except `xenial`. On CentOS 7, install OpenSSL 1.1.1 when required. |
    | proxysql-2-&lt;version&gt;-Linux-x86_64.glibc&lt;glibc_version&gt;.tar.gz | Every supported operating system |
    | proxysql-2-&lt;version&gt;-Linux-x86_64.glibc&lt;glibc_version&gt;.xenial.tar.gz | Ubuntu 16.04 `xenial` only. See the download page for available `glibc` options. |

## Install the tarball

Complete the following steps after you download the tarball:
{.power-number}

1. Change to the directory that contains the downloaded tarball.

2. Extract the tarball with the command that matches your ProxySQL version:

    ??? "Extract ProxySQL 2.0.14 or higher"

        ```{.bash data-prompt="$"}
        $ tar xzf proxysql-<VERSION>-Linux-<PLATFORM_ARCHITECTURE>-<GLIBC_VERSION>.tar.gz
        $ cd proxysql-<VERSION>-Linux-<PLATFORM_ARCHITECTURE>
        ```

    ??? "Extract ProxySQL 2.0.13 or lower"

        ```{.bash data-prompt="$"}
        $ tar xzf proxysql-<VERSION>-<LINUX_PLATFORM_ARCHITECTURE>.tar.gz
        $ cd proxysql-<VERSION>-Linux-<PLATFORM_ARCHITECTURE>
        ```

3. Create a directory to store ProxySQL data.

      ```{.bash data-prompt="$"}
      $ mkdir /home/user/data
      ```

4. Set the `datadir` value in the configuration file to the data directory path.

      ```{.text .no-copy}
      datadir="/home/user/data"
      ```

5. Set the remaining ProxySQL options as required.

## MySQL 8.4 and Percona Server for MySQL 8.4 considerations

--8<--- "note-8.4.md"
