# ENV(

> Gets or sets a native OS environment variable.

## Syntax

```
receiver$ = ENV( name_expression )
ENV( name_expression ) = value_expression
```

| Form | Effect |
|------|--------|
| `x$ = ENV("NAME")` | Read the value of environment variable `NAME` |
| `ENV("NAME") = val$` | Set environment variable `NAME` to `val$` |

Valid wherever an alpha expression is legal.

## Description

`ENV(` provides access to the OS environment. Reading returns the current value of the named variable; if the variable is not defined, spaces are returned.

Setting an environment variable makes it available to child processes created with `SHELL`, `$RELEASE`, or `$RELEASE LOAD RUN`.

`LIST E` displays a list of environment variables that have been locally modified.

To unset a variable, set it to spaces — this reverts it to the value inherited from the parent process.

### Read-only variables (KCML 6.20+)

These variables are read-only and cannot be set:
- `LOGIN`
- `LOGNAME`
- `KCMLDIR`
- `SYSTEMID`
- `TERMFILE`

### Compatibility

From KCML 5.0+, setting an environment variable makes it visible in child process environments. To disable this (for compatibility with earlier KCML), set byte 39 of `$OPTIONS RUN` to `HEX(00)`.

## Examples

### Read environment variable

```kcml
: DIM terminal$20, home$60
: terminal$ = ENV("TERM")
: PRINT "TERM="; terminal$
: home$ = ENV("HOME")
: PRINT "HOME="; home$
: $END
```

Output:
```
TERM=vt100
HOME=/home/paul
```

### Set environment variable

```kcml
ENV("PROG") = new$
```

### Pass parameter to child process

```kcml
ENV("REPORT_DATE") = today$
SHELL "/usr/local/bin/report_generator"
```

## See Also

- `SHELL` — execute an OS command in a child process
- `$RELEASE` — release KCML to run a system command
- `LIST E` — list locally modified environment variables
- `$OPTIONS RUN` — runtime options (byte 39 controls env inheritance)
