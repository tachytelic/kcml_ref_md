# Configuring syslog for KCML

> How to configure the Unix syslog daemon to capture KCML log messages.

## Description

KCML uses the Unix syslog facility to log warnings and error messages. Applications can also generate log entries with `WRITE LOG`. In exceptional cases, KClient raises log messages directly on the server's syslog.

### Facility codes

| KCML version | Facility |
|-------------|---------|
| KCML 5.02 | `LOG_USER` |
| KCML 6.00+ | `LOG_LOCAL1` |

### Priority levels used

- `LOG_INFO` — informational
- `LOG_WARNING` — warnings
- `LOG_ERR` — errors
- `LOG_DEBUG` — KClient GPF stack dumps

## `/etc/syslog.conf` configuration

Each entry is: `selector<TAB>action`

The selector is `facility.level` (semicolon-separated for multiple). The action is a filename (starting with `/`) or a remote host (`@hostname`).

### Examples

```
# Capture all KCML messages (KCML 5 uses user, KCML 6 uses local1):
local1.info;user.info    /var/adm/log/kcml.log

# Capture KClient debug dumps:
*.debug                  /var/adm/log/debug.log
```

## Log rotation

As logs grow over time, add a cron job to rotate them daily. Many modern Unix systems handle this automatically.

## See Also

- `WRITE_LOG` — write to syslog from within KCML
- `kwritelog` — write to syslog from shell scripts
- `SELECT LOG` — configure KCML's log stream
