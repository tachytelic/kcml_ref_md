# #TERM

> Returns the terminal number identifying the physical terminal or client owning this KCML process.

## Syntax

```
#TERM
```

## Description

Returns a small integer uniquely identifying the terminal or client that owns the KCML process. All KCML processes started from the same terminal share the same `#TERM` value, making it useful for tracking physical location or per-terminal attributes (e.g. local printer type).

Returns `0` if KCML's standard input is not a terminal (e.g. running as a batch job with `-p`).

### TERMFILE

`#TERM` values are stored in the `TERMFILE` file — a plain text file in the KCML executable directory (overridable with the `TERMFILE` environment variable). Format: one line per terminal, with the terminal name and `#TERM` number separated by a tab. The file is created/updated automatically as new terminals connect.

- Comments: `#` to end of line.
- Blank lines and whitespace ignored.
- Can be hand-edited to pre-assign `#TERM` values.

### Terminal limits

| Method | Effect |
|--------|--------|
| Default maximum | 1024 |
| `bkstat -y size` | Extend maximum to `size` (max 32768) |
| `BCDPART` env var | Restrict maximum for a KCML process |

`bkstat -y` must be run before any KCML process starts.

### Compatibility

- KCML 4: terminal identified by tty name (e.g. `/dev/tty01`) or IP address.
- KCML 5+: KClient terminals identified by PC computer name (IP addresses can change with DHCP).
- Prior to KCML 5, default maximum `#TERM` was 512.

## Examples

```kcml
DIM term
term = #TERM
PRINT "Terminal "; term
```

```kcml
REM Route print jobs by terminal
IF #TERM < 40 THEN SELECT PRINT "PRINTA"
IF #TERM >= 40 THEN SELECT PRINT "PRINTB"
```

```kcml
DIM terminal(100)
terminal(#TERM) = 1    : REM  Mark this terminal as active
```

## Notes

- `#TERM` identifies the *terminal*; `#PART` identifies the *process*.
- Usually `#PART == #TERM`, but not if `#TERM` is 0 or there are multiple KCML processes on the same terminal.

## See Also

- `#PART` — unique process/partition number
- `bkstat` — partition and terminal status utility
