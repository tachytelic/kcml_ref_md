# SELECT (overview)

> Sets one or more KCML runtime parameters in a single statement.

## Syntax

```
SELECT param1 [, param2 ...]
```

## Description

`SELECT` is a multi-purpose statement that assigns runtime configuration parameters. Multiple parameters can be combined in one `SELECT` statement, separated by commas.

Each parameter is documented on its own page:

| Parameter | Purpose |
|-----------|---------|
| `SELECT CI` | Console Input device |
| `SELECT CO` | Console Output device |
| `SELECT DISK` | Default disk/directory |
| `SELECT ERROR` | Error output device |
| `SELECT INPUT` | Default input device |
| `SELECT LIST` | List output device |
| `SELECT LOG` | Log output device |
| `SELECT MODULE` | Module (library) path |
| `SELECT ON ALARM` | Alarm handler |
| `SELECT ON ALERT` | Alert handler |
| `SELECT @PART` | Partition/environment |
| `SELECT PASSWORD` | Program encryption password |
| `SELECT PRECISION` | Numeric precision |
| `SELECT PRINT` | Print output device |
| `SELECT TRACE` | Trace output device |

## Example — multiple parameters

```kcml
SELECT CO /005, CI /001, LIST /204
SELECT PRINT #9, DISK "/data"
```

## See Also

- Individual `SELECT_*` pages for details on each parameter
