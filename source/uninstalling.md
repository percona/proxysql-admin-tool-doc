# Uninstalling ProxySQL and ProxySQL Admin

## Debian or Ubuntu

In order to uninstall ProxySQL and ProxySQL Admin you must find the exact package name. 

### Find Specific Package Name

You can use the following command to retrieve the name:

```bash
	sudo dpkg --list proxy*
```
The result lists all installed packages with the specified phrase.

### Remove Package with Apt

The `apt remove` command only removes the packages when these packages were installed by `apt`. The configuration files and dependencies are not removed. To uninstall ProxySQL 2.x on Debian or Ubuntu, use the following command:

```bash
    sudo apt remove proxysql2 -y
```

> Note:
> 
> When you are removing a package, apt may ask for confirmation. Add the `-y` to answer "yes".


### Remove Packages with Dependencies

To remove ProxySQL and the ProxySQL Admin applications, configuration files, and dependencies, use the following command:

```bash
	sudo apt purge --auto-remove proxysql2 -y
```
> Note:
> 
> Automatically installed "recommended" or "suggested" packages may be ignored.

## Red Hat or CentOS


In order to uninstall ProxySQL and ProxySQL Admin you must find the exact package name.
### Finding a Specific Package

If you are not sure of the exact file name, use the following command:

```bash
	yum list | grep proxy*
```
The result lists all installed packages with the specified phrase.

## Remove Packages with Yum

The `yum remove` command removes only the packages when these packages were installed by `yum`. The configuration files and dependencies are not removed. 

```bash
    sudo yum remove proxysql2 -y
```
> Note:
> 
> When you are removing a package, yum may ask for confirmation. Add the `-y` to answer "yes".

## Remove Package with Dependencies with Yum
To remove ProxySQL and the ProxySQL Admin applications and uneeded dependencies, use the following command:

```bash
	yum autoremove proxysql2
```
> Note:
> 
> If other applications are using the dependencies, they are not removed.
