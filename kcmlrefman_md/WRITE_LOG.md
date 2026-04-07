# WRITE LOG

> Writes a message to the system log (syslog on Unix, Application Event Log on Windows NT).

## Syntax

```
WRITE LOG [level,] message$
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `level` | Log level: 0 = information, 1 = warning, 2 = error (default: 0) |
| `message$` | Alpha expression containing the log message |

### Log level constants

| Constant | Value | Unix syslog | NT Event Log |
|----------|-------|-------------|--------------|
| `_LOG_INFORMATION` | 0 | `LOG_INFO` | Information |
| `_LOG_WARNING` | 1 | `LOG_WARNING` | Warning |
| `_LOG_ERROR` | 2 | `LOG_ERR` | Error |

## Description

Writes a message to the OS log. On Unix, uses `syslog` with `LOG_LOCAL1` facility (KCML 6+) or `LOG_USER` (KCML 5.02). On Windows NT, writes to the Application Event Log.

### Filtering

`$OPTIONS RUN` byte 52 sets a minimum log level threshold:
- `HEX(00)` (default): all messages logged.
- `HEX(01)`: only level 1 (warning) and above.
- `HEX(02)`: only level 2 (error).
- `HEX(FF)`: all logging disabled.

### Windows 95/98 fallback

No OS event log on Win95/98. Configure a text file via the registry:
- Key: `HKEY_LOCAL_MACHINE\Software\Kerridge\EventLogging`
- `LogFile` (STRING): path to log file
- `Enabled` (DWORD): 1 = on, 0 = off

## Examples

```kcml
WRITE LOG _LOG_WARNING, Message$
WRITE LOG "Application started"
WRITE LOG _LOG_ERROR, "Fatal: unable to open " & TRIM(filename$)
```

## See Also

- `$OPTIONS RUN` — byte 52 for log level threshold
- `PANIC` — force a diagnostic dump
