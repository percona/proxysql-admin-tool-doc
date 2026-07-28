# ProxySQL limitations

## MySQL 9.x clients and `mysql_native_password`

MySQL 9.x removes `mysql_native_password`. ProxySQL still defaults `mysql-default_authentication_plugin` to `mysql_native_password`, so MySQL 9 clients cannot connect to the admin interface until you set the variable to `caching_sha2_password`.

For symptoms, configuration, recovery, and troubleshooting, see [Connect to ProxySQL with MySQL 9.x clients](mysql-9-authentication.md).

Upstream issue: [sysown/proxysql#5347](https://github.com/sysown/proxysql/issues/5347). The ProxySQL process default is unchanged through 3.0.9. The Percona admin tools in 3.0.9 add a configurable `AUTH_PLUGIN` (default `caching_sha2_password`) for user creation and client connections ([PR #287](https://github.com/percona/proxysql-admin-tool/pull/287)).

## ProxySQL 3 and OpenSSL

ProxySQL 3 removed support for the following distributions ([#4749](https://github.com/sysown/proxysql/pull/4749)) due to two key reasons: they are either officially past their end-of-life or they lack native support for OpenSSL 3.0, a library required for modern security features:

| Distribution | Reason for Removal | EOL Date / Notes |
| :--- | :--- | :--- |
| CentOS 8 | Past official EOL | December 31, 2021 |
| Debian 10 (Buster) | Does not ship with OpenSSL 3.0 | LTS ended June 30, 2024 |
| Debian 11 (Bullseye) | Does not include OpenSSL 3.0 | Currently in LTS until Aug 2026 |
| Ubuntu 18.04 (Bionic Beaver) | EOL and does not support OpenSSL 3.0 | EOL May 2023 |
| Ubuntu 20.04 (Focal Fossa) | Does not ship with OpenSSL 3.0 | EOL April 2025 |
