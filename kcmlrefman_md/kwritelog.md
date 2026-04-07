# kwritelog — Write to System Log

> Shell utility to write messages to the system log from scripts.

## Syntax

```
kwritelog [-l level] message
```

## Description

`kwritelog` writes a message to the Unix system log (syslog). It provides the same functionality as the KCML `WRITE LOG` statement but can be used in shell scripts — useful for startup scripts and daemon management.

## Options

| Option | Description |
|--------|-------------|
| `-l level` | Log severity level (default: 0) |

### Severity levels

| Level | Purpose | Unix syslog level |
|-------|---------|------------------|
| 0 | Information | `LOG_INFO` |
| 1 | Warning | `LOG_WARNING` |
| 2 | Error | `LOG_ERR` |

## Examples

```sh
kwritelog -l 1 "Starting background daemon ..."
/usr/app/start_daemon.ksh
rc=$?
if [ "$rc" = "0" ]; then
    kwritelog "Daemon has started"
else
    kwritelog -l 2 "Daemon failed to start, error code $rc"
fi
```

## See Also

- `WRITE_LOG` — write to syslog from within KCML
- `syslog` — configuring the syslog daemon
