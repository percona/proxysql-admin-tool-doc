# Installing ProxySQL 2.x.x and the admin utilities 

## Using APT on a Debian-based Linux distribution

If you used APT to install [Percona XtraDB Cluster](https://www.percona.com/doc/percona-xtradb-cluster/8.0/install/index.html)
or other Percona software on Debian and Debian-based Linux distributions, run the following command: 

```sh
$ sudo apt install proxysql2
```

The output could be the following:

```text
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  debconf-utils logrotate
The following NEW packages will be installed:
  debconf-utils logrotate proxysql2
0 upgraded, 3 newly installed, 0 to remove and 3 not upgraded.
Need to get 7259 kB of archives.
...
```

## Using YUM on a Red Hat-based Linux distribution

If you used YUM to install [Percona XtraDB Cluster](https://www.percona.com/doc/percona-xtradb-cluster/8.0/install/index.html)
or other Percona software on Red Hat-based Linux distributions, run the following command:

```shell
$ sudo yum install proxysql2
```

The output could be the following:

```text
Last metadata expiration check: 0:01:47 ago on Wed Oct  5 14:42:00 2022.
Dependencies resolved.
=========================================================================================================================
 Package                  Architecture          Version                        Repository                           Size
=========================================================================================================================
Installing:
 proxysql2                x86_64                2.4.4-1.1.el8                  tools-release-x86_64                 21 M
Installing dependencies:
 logrotate                x86_64                3.14.0-4.el8                   baseos                               85 k

Transaction Summary
=========================================================================================================================
Install  2 Packages

Total download size: 21 M
Installed size: 88 M
Is this ok [y/N]: y
Downloading Packages:
(1/2): logrotate-3.14.0-4.el8.x86_64.rpm                                                 371 kB/s |  85 kB     00:00
(2/2): proxysql2-2.4.4-1.1.el8.x86_64.rpm                                                3.6 MB/s |  21 MB     00:05
-------------------------------------------------------------------------------------------------------------------------
Total                                                                                    3.3 MB/s |  21 MB     00:06
...
```

## Verifying the installation of the Percona_Scheduler_Admin utility

You can verify that the Percona_Scheduler_Admin was installed with the following command:

```shell
$ percona-scheduler-admin --debug
```

Running the command without the [configuration file](/psa-config.md) results in an error and does nothing.

```text
ERROR : The --config-file option is required but is missing from the command.
```