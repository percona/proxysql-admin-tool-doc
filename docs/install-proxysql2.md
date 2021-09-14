
# Installing ProxySQL v2 using a Package Manager


Like any other Percona software, you can install ProxySQL 2.0.x using the package manager of your operating system. Use the corresponding command relevant to your operating system:

## Installing on Debian or the supported derivatives:

1. Set up Percona repositories

    * Install percona-release tool:

       ```bash
       wget https://repo.percona.com/apt/percona-release_latest.generic_all.deb 
       sudo dpkg -i percona-release_latest.generic_all.deb
       ```

    * Refresh the local cache
    
       ```bash
       sudo apt-get update      
       ```

    * Enable the repository

      ```bash
      percona-release enable proxysql release
      ```

2. Install ProxySQL 2.0.x and ProxySQL Admin packages

   ```bash
   sudo apt-get install proxysql2
   ```

## Installing on Red Hat Enterprise Linux or the supported derivatives

1. Set up Percona repositories

    * Install percona-release

       ```bash
       sudo yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm     
       ```

    * Enable the repository

      ```bash
      percona-release enable proxysql release
      ```

2. Install ProxySQL 2.0.x and ProxySQL Admin packages

   ```bash
   sudo yum install proxysql2
   ```

## Starting ProxySQL

To start ProxySQL 2.0.x or ProxySQL 2.1.x, run the following command: 

``` bash
sudo service proxysql2 start
```

!!! Warning


    Do not run ProxySQL with default credentials in production.

    Before starting the `proxysql` service, you can change the defaults in
    the `/etc/proxysql.cnf`{.interpreted-text role="file"} file by changing
    the `admin_credentials` variable. For more information, see [Global
    Variables](https://github.com/sysown/proxysql/blob/master/doc/global_variables.md).

!!! Seealso

    * [Installing from a tarball](installing-tarball.md)
    * ProxySQL Documentation: [Getting Started](https://proxysql.com/documentation/getting-started/)
