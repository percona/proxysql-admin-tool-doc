# Percona Scheduler Admin statements

## Statement reference

The standard percona-scheduler-admin statement includes
`percona-scheduler-admin --config-file=<configuration file name and
extension>`. A Percona Scheduler Admin example statement has the following syntax:

```{.text .no-copy}
percona-scheduler-admin --config-file=config.toml [option] [option]
```

If you do not include the configuration file in the command, the result is an error and nothing happens.

```{.text .no-copy}
$ percona-scheduler-admin --debug
ERROR : The --config-file option is required but is missing from the command.
```

The options determine what the statement does. The percona-scheduler-admin statement must include at least one option. A command without an option returns an error and nothing happens.

For most options, two hyphens (--) precede an option name. The [disable](./percona-scheduler-admin-options-detail.md#-disable---d) and the [enable](./percona-scheduler-admin-options-detail.md#–enable---e) option can be selected with one hyphen (-) and the appropriate abbreviation.

For example, the following commands return the same result:

```{.bash data-prompt="$"}
$ percona-scheduler-admin --config-file=config.toml -e

$ percona-scheduler-admin --config-file=config.toml --enable
```

You can combine some options with other, optional options to modify the statement’s behavior. Multiple options are separated by a space. You can combine the options in any order.

An example of combining options in one statement:

```{.bash data-prompt="$"}
$ percona-scheduler-admin --config-file=config.toml --write-node=127.0.0.1:4130 --update-cluster
```

For some options, they must be combined with a required option to return a result.

An example of an option combined with a required option:

```{.bash data-prompt="$"}
$ percona-scheduler-admin --config-file=config.toml --force -e
```

If you do not combine the option with the required option, the statement does not run and returns an error.

```{.bash data-prompt="$"}
$ percona-scheduler-admin --config-file=tests/testsuite.toml  --update-write-weight="127.0.0.1:33,112"
```

??? example "Expected output"

    ```{.text .no-copy}
    ERROR : --update-write-weight requires --update-cluster.
    ```

Specific options, such as -–write-node or –-server, require a value.

```{.bash data-prompt="$>"}
$> percona-scheduler-admin --config-file=config.toml --server=192.168.56.32:3306
```

For the available options, see [Percona Scheduler Admin options](percona-scheduler-admin-options-detail.md)
