# Download locations for Percona build of ProxySQL and ProxySQL admin tools

This task guide documents download locations for the Percona build of ProxySQL and Percona admin tools.

!!! tip "Start here"

    Servers with Percona repositories install ProxySQL through the [package manager installation guide](install-v2.md). Install the latest ProxySQL 3 release with the `proxysql3` package. Example repositories include those used for [Percona XtraDB Cluster](https://www.percona.com/doc/percona-xtradb-cluster/8.0/install/index.html).

    Use the following guide when you browse builds on the Percona download site, install from a binary tarball, or download packages for an offline install.

## Select a ProxySQL product line

Percona recommends the latest ProxySQL 3 release for standard deployments. See [release notes](release-notes.md) for the current version and the compatibility note on the [home page](index.md).

Review the following table before you open the Percona download page.

| Your situation | What to select |
| -------------- | -------------- |
| Air-gapped server, custom layout, or no package manager | ProxySQL 3 binary tarball; see [tarball installation guide](install-proxysql2-tarball.md) |
| Debian or Ubuntu server with Percona repositories | `proxysql3` through the [package manager installation guide](install-v2.md) |
| Percona XtraDB Cluster with [proxysql-admin](proxysql-admin-tool-v2-config.md) | ProxySQL 3, latest version |
| RHEL-family server with Percona repositories | `proxysql3` through the [package manager installation guide](install-v2.md) |
| Standard MySQL-compatible deployment | ProxySQL 3, latest version |
| Existing ProxySQL 2.x deployment or version lock | ProxySQL 2.x matching your installed release |
| [pxc_scheduler_handler](psh-overview.md) on ProxySQL 2.x only | ProxySQL 2.4.2 or later |

Percona download packages can include the following components:

* `proxysql-admin` — configures Percona XtraDB Cluster nodes in ProxySQL

* `pxc_scheduler_handler` — automates failover on supported ProxySQL versions

* ProxySQL — the proxy daemon

## Download files from the Percona download page

Complete the following steps on the [Percona ProxySQL download page](https://www.percona.com/proxysql-download/):
{.power-number}

1. Open the download page in a browser.

2. Select *Installation Options*.

3. Select a *Product Group* value. Choose *ProxySQL 3* for the latest release. Choose *ProxySQL 2* only for an existing 2.x deployment or a version lock. ProxySQL version 1 is not actively maintained.

4. Select the latest *Version* value for ProxySQL 3. For ProxySQL 2, select the version that matches your environment.

5. Select a *Platform* value for your Linux distribution. Available distributions depend on the selected version.

After you complete these steps, the download page lists available files. Package files use the `.deb` or `.rpm` extension for your platform. Generic Linux builds list tarball file names.

Download all required packages as a single tar archive, or download packages individually.

### Download binary tarballs

Select *Platform*, *Linux*, and *Generic* to list tarball binaries. See the [tarball installation guide](install-proxysql2-tarball.md) for installation steps.

!!! note

    [pxc_scheduler_handler](psh-overview.md) is included in ProxySQL 3 releases. On ProxySQL 2.x, the tool requires version 2.4.2 or later.

## Install or configure ProxySQL after download

Select the guide that matches your installation method:

* Binary tarball — [Install Percona build of ProxySQL binary tarball](install-proxysql2-tarball.md)

* Docker image — [Run Docker](install-v2.md#run-docker) in the installation guide

* Package manager (APT or YUM) — [Install Percona build of ProxySQL and the admin tools](install-v2.md)

* Percona XtraDB Cluster configuration — [proxysql-admin utility](proxysql-admin-tool-v2-config.md)

* ProxySQL service control — [Start and stop ProxySQL](start-or-stop-proxysql2.md)

## Locate source code repositories

The following table lists source repositories for ProxySQL and Percona admin tools.

| Component | Repository |
| --------- | ---------- |
| Percona proxysql-admin tool | [percona/proxysql-admin-tool](https://github.com/percona/proxysql-admin-tool) |
| ProxySQL upstream | [sysown/proxysql](https://github.com/sysown/proxysql) |
| This documentation | [percona/proxysql-admin-tool-doc](https://github.com/percona/proxysql-admin-tool-doc) |
