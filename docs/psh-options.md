# pxc_scheduler_handler statements

## Statement reference

The standard pxc_scheduler_handler statement includes
`percona-scheduler-admin --config-file=<configuration file name and
extension>`. A pxc_scheduler_handler example statement has the following syntax:

```{.text .no-copy}
percona-scheduler-admin --config-file=config.toml [option] [option]
```

If you do not include the configuration file in the command, the result is an error and nothing happens.

```{.text .no-copy}
$ percona-scheduler-admin --debug
ERROR : The --config-file option is required but is missing from the command.
```

The options determine what the statement does. The pxc_scheduler_handler statement must include at least one option. A command without an option returns an error and nothing happens.

For most options, two hyphens (--) precede an option name. The [disable](psh-detailed-options.md#disable) and the [enable](psh-detailed-options.md#enable) option can be selected with one hyphen (-) and the appropriate abbreviation.

For example, the following commands return the same result:

```{.bash data-prompt="$"}
$ percona-scheduler-admin --config-file=config.toml -e

$ percona-scheduler-admin --config-file=config.toml --enable
```

You can combine some options with other, optional options to modify the statement behavior. Multiple options are separated by a space. You can combine the options in any order.

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

For the available options, see [pxc_scheduler_handler options](psh-detailed-options.md)
