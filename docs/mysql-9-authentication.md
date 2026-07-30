# Connect to ProxySQL with MySQL 9.x clients

MySQL 9.x removes the `mysql_native_password` authentication plugin. ProxySQL still defaults `mysql-default_authentication_plugin` to `mysql_native_password`, so a MySQL 9 client cannot complete the handshake to the admin interface (port `6032`) or the MySQL frontend until you change that default.

This requirement applies when the only available `mysql` client is MySQL 9.x (or another client that no longer ships `mysql_native_password`). Full `caching_sha2_password` support for frontend and backend connections requires [ProxySQL 2.6.2](2.6.2.md) or later.

ProxySQL’s own default for `mysql-default_authentication_plugin` is still `mysql_native_password` through 3.0.9. For MySQL 9.x clients, set that variable to `caching_sha2_password` in the ProxySQL config file. Separately, the Percona admin tools in 3.0.9 default `AUTH_PLUGIN` to `caching_sha2_password` for user creation and client connections.

## Symptoms

Connection attempts to ProxySQL fail during authentication. Typical client errors include:

```text
ERROR 2059 (HY000): Authentication plugin 'mysql_native_password' cannot be loaded: ...
```

or an authentication failure before any SQL is accepted. The ProxySQL process can still be running; only clients that lack `mysql_native_password` are blocked.

Confirm the client version:

```{.bash data-prompt="$"}
$ mysql --version
```

MySQL 9.x output confirms the client no longer provides `mysql_native_password`.

## Why this happens

`mysql-default_authentication_plugin` controls which authentication method ProxySQL announces in the Initial Handshake Packet. The default remains `mysql_native_password`.

| Component | Default / behavior |
| :--- | :--- |
| ProxySQL `mysql-default_authentication_plugin` | `mysql_native_password` |
| MySQL 9.x client | Does not load `mysql_native_password` |
| Required setting for MySQL 9.x clients | `caching_sha2_password` |

Setting `mysql-default_authentication_plugin` to `caching_sha2_password` also forces frontend SSL (`mysql-have_ssl`), because `caching_sha2_password` needs a secure channel for full authentication.

## Recommended: set the plugin in the config file

If you intend to use ProxySQL with MySQL 9.x clients (for example 9.7), set `mysql-default_authentication_plugin` in the ProxySQL config file. That is the standard approach. Do not rely on connecting with an older client only to change the setting, then switching to a MySQL 9 client.

On a new install, or when you deliberately reinitialize from the config file, set the variable in `/etc/proxysql.cnf` (or your active config path) under `mysql_variables`:

```text
mysql_variables=
{
    default_authentication_plugin="caching_sha2_password"
    # ... other mysql_variables ...
}
```

Then start ProxySQL normally for a first-time datadir, or reinitialize from the config file if you intend to rebuild `proxysql.db` from that file:

=== "systemd"

    ```{.bash data-prompt="$"}
    $ sudo systemctl start proxysql-initial
    ```

=== "service"

    ```{.bash data-prompt="$"}
    $ sudo service proxysql initial
    ```

!!! warning

    Reinitialization loads configuration from the config file into a new on-disk database. Use it only when you mean to replace the existing `proxysql.db` contents. After the first successful start, ProxySQL ignores later edits to `proxysql.cnf` unless you reinitialize or apply changes through the admin interface.

## Workaround: change the setting with an older MySQL client

Connecting with a MySQL 8.4 (or other pre-9) client that still supports `mysql_native_password`, running `SET mysql-default_authentication_plugin='caching_sha2_password'`, then switching to a MySQL 9.7 client is a workaround, not the preferred procedure. Prefer the [config file](#recommended-set-the-plugin-in-the-config-file) when MySQL 9.x is the intended client.

If ProxySQL is already running and you can still reach the admin interface with an older client, you can apply the change at runtime:

```{.bash data-prompt="Admin>"}
Admin> SET mysql-default_authentication_plugin='caching_sha2_password';
Admin> LOAD MYSQL VARIABLES TO RUNTIME;
Admin> SAVE MYSQL VARIABLES TO DISK;
```

Verify:

```{.bash data-prompt="Admin>"}
Admin> SELECT * FROM global_variables
    -> WHERE variable_name='mysql-default_authentication_plugin';
```

Expected value: `caching_sha2_password`.

## Recover when only a MySQL 9 client is available

If admin connections already fail and you cannot use an older client, fix the setting through the config file rather than relying on a temporary MySQL 8.4 session.

1. Stop ProxySQL.

2. Set the plugin in `/etc/proxysql.cnf` (or your active config path) under `mysql_variables`:

    ```text
    mysql_variables=
    {
        default_authentication_plugin="caching_sha2_password"
        # ... other mysql_variables ...
    }
    ```

3. Reinitialize ProxySQL from the config file so the on-disk database picks up the change:

    ```{.bash data-prompt="$"}
    $ sudo systemctl start proxysql-initial
    # or: sudo service proxysql initial
    ```

!!! warning

    Reinitialization replaces the existing `proxysql.db` contents from the config file. Use it only when that is acceptable for the deployment. Do not edit `proxysql.db` with SQLite while ProxySQL is running.

4. Connect with SSL enabled, for example:

    ```{.bash data-prompt="$"}
    $ mysql -u admin -padmin -h 127.0.0.1 -P6032 --ssl-mode=REQUIRED \
      --prompt='Admin> '
    ```

## Connect after enabling `caching_sha2_password`

Use a client that supports `caching_sha2_password` and a TLS connection to ProxySQL:

```{.bash data-prompt="$"}
$ mysql -u admin -padmin -h 127.0.0.1 -P6032 --ssl-mode=REQUIRED \ 
--default-auth=caching_sha2_password --prompt='Admin> '
```

For application traffic on the MySQL frontend port (default `6033`), enable SSL in the connector. ProxySQL does not support RSA public-key retrieval over a non-SSL channel for frontend `caching_sha2_password` full authentication.

## Configure `AUTH_PLUGIN` in proxysql-admin (3.0.9+)

Starting with the ProxySQL admin tools in the 3.0.9 release, `proxysql-admin` and `percona-scheduler-admin` no longer hardcode `mysql_native_password` when creating users. Both tools use `AUTH_PLUGIN` in `CREATE USER` statements, and both pass `default-auth=${AUTH_PLUGIN}` to the `mysql` client.

Set the plugin in `/etc/proxysql-admin.cnf`:

```{.bash data-prompt="$"}
# MySQL authentication plugin to use when creating users.
# Valid values: 'caching_sha2_password' (default) or 'mysql_native_password'
export AUTH_PLUGIN='caching_sha2_password'
```

| Detail | Behavior |
| :--- | :--- |
| Default | `caching_sha2_password` |
| Allowed values | `caching_sha2_password`, `mysql_native_password` |
| Invalid value | Script exits with an error |
| Used for | `CREATE USER` for monitor and application users; client `default-auth` |

`AUTH_PLUGIN` controls how the admin tools create PXC users and how they authenticate as a client. It does **not** replace `mysql-default_authentication_plugin` on ProxySQL. For MySQL 9.x clients connecting to ProxySQL admin or frontend ports, still configure ProxySQL as described earlier in this document.

Do not set `AUTH_PLUGIN='mysql_native_password'` against MySQL 9.x / PXC 9.x backends; that plugin was removed in MySQL 9.0.

See [Preparing the configuration file](proxysql-admin-tool-v2-config.md#preparing-the-configuration-file).

## Troubleshooting checklist

| Check | What to look for |
| :--- | :--- |
| Client version | MySQL 9.x lacks `mysql_native_password`; use `caching_sha2_password` on ProxySQL. |
| Announced plugin | `mysql-default_authentication_plugin` must be `caching_sha2_password`. Set it in `proxysql.cnf` when MySQL 9.x is the intended client. |
| Admin tools | ProxySQL admin tools 3.0.9+ default `AUTH_PLUGIN` to `caching_sha2_password`; older tools hardcode `mysql_native_password`. |
| SSL | Frontend SSL is required for hashed `caching_sha2_password` auth; connect with `--ssl-mode=REQUIRED` (or equivalent). |
| ProxySQL version | Need 2.6.2 or later for full frontend/backend `caching_sha2_password` support. |
| Config not applied | If `proxysql.db` already exists, editing `proxysql.cnf` alone has no effect until you reinitialize from the config file or apply changes through the admin interface. Do not edit `proxysql.db` while ProxySQL is running. |
| Health probes / monitor | After switching the default plugin, probes that connect without SSL or with an incompatible auth plugin can fail ([#5363](https://github.com/sysown/proxysql/issues/5363)). Update probe commands to use SSL and `caching_sha2_password`. |
| Monitor password | Backend monitor credentials in `mysql-monitor_password` must be clear text, whether backends use `mysql_native_password` or `caching_sha2_password` ([#4845](https://github.com/sysown/proxysql/issues/4845)). |

## Related topics

* [Start and stop ProxySQL](start-or-stop-proxysql2.md)
* [ProxySQL limitations](limitations.md)
* [proxysql-admin configuration](proxysql-admin-tool-v2-config.md#preparing-the-configuration-file)
* [Create a MySQL admin account for pxc_scheduler_handler](build-psh.md#create-a-mysql-admin-account)
* Upstream: [ProxySQL authentication methods](https://proxysql.com/documentation/authentication-methods/)
