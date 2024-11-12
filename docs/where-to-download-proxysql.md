# Download locations for ProxySQL 2.x.x and ProxySQL admin utilities

In an MySQL 8.4 or Percona Server for MySQL 8.4 environment, you may have the following issues:

* ProxySQL contains counters that have not been updated to use the new terminology. Unexpected results may occur
* The binlog reader errors out during initialization due to the use of the old terminology, such as SHOW MASTER STATUS command.

The binaries, packages, and tarballs are available at [Percona Download ProxySQL](https://www.percona.com/download-proxysql).

On the **Download ProxySQL** page, select the following:

* *Product* - ProxySQL 2
* *Product Version* - the version of ProxySQL2
* *Platform* - the Linux distribution

The available software platforms are based on the selected version. 
You can either download all packages together in a single tar file or download the packages separately. Select **Linux - Generic** to download [binary tarballs](install-proxysql2-tarball.md).

!!! note

    You must download ProxySQL 2.4.2 or later to install the Percona Scheduler Admin tool.

## Find the source code

The source code is located at [Percona/proxysql-admin-tool](https://github.com/percona/proxysql-admin-tool). The documentation source code is located at [Percona/proxysql-admin-tool-doc](https://github.com/percona/proxysql-admin-tool-doc).

