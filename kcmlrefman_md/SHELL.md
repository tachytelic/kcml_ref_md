# SHELL

> Executes a native OS command, script, or program from within KCML.

## Syntax

```
SHELL command$
exit_code = SHELL command$
```

## Description

Runs the specified shell command. If `command$` is blank, an interactive shell is launched.

Used as a numeric function, returns the completion code as a 16-bit value:
- **High byte**: return code from the command.
- **Low byte**: shell status (signal, etc.).
- **Negative**: errno if the child process could not be started.

### Shell redirection operators (all platforms)

| Operator | Purpose |
|----------|---------|
| `<` | Redirect stdin from a file |
| `>` | Redirect stdout to a file |
| `>>` | Append stdout to a file |
| `&` | Run asynchronously (KCML doesn't wait; no return code) |
| `!` | Windows only — run in a separate visible window |

### Windows notes

- Commands run via `%COMSPEC%` (COMMAND.COM / cmd.exe) unless byte 37 bit `HEX(02)` of `$OPTIONS RUN` is set.
- For commands needing user interaction (e.g. DOS EDIT), use `!` or set bit `HEX(04)` of `$OPTIONS RUN`.
- `/dev/null` is treated as Windows `NUL` automatically.

## Examples

```kcml
SHELL "ls -la /tmp"
SHELL "cp /data/file.dat /backup/file.dat"
```

```kcml
DIM rc
rc = SHELL "sort input.txt > sorted.txt"
PRINT "Exit code: "; rc / 256    : REM  high byte = command return code
```

```kcml
REM Async (fire and forget)
SHELL "generate_report.sh &"
```

```kcml
REM Interactive shell
SHELL ""
```

## Notes

- Prefer native KCML file operations (`COPY`, `MOVE`, `REMOVE`) over shelling out when possible.
- The `SHELL` environment variable on Unix controls which shell is used.
- On Unix, KCML restores the terminal to its original state before running an interactive command (unless `>` is detected in the command string).

## See Also

- `COPY` — copy a file
- `MOVE` — rename/move a file
- `REMOVE` — delete a file
- `$OPTIONS RUN` — byte 37 for Windows shell behaviour
