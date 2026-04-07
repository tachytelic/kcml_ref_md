# PRINT #

> Sends PRINT output to a numbered file stream.

## Syntax

```
PRINT #stream [, expr [, | ; expr] ...]
```

## Description

Directs PRINT output to the file opened on `#stream` with `OPEN #`. The stream must be open; otherwise an error occurs. Stream 0 is treated as the screen (normal PRINT).

Screen-positioning functions (`AT(`, `BOX(`, `TAB(`) are silently ignored when printing to a stream.

### Line ending translation

| Platform | Behaviour |
|----------|-----------|
| Unix | `HEX(0D)` → `HEX(0A)` (LF) |
| DOS/Windows | `HEX(0D)` → `HEX(0D0A)` (CRLF) |

## Examples

```kcml
REM Write to a file
OPEN #1, "/tmp/report.txt", "w"
PRINT #1, "Report header"
PRINT #1, "Value: "; 42
PRINT #1, "Done"
CLOSE #1
```

```kcml
REM Stream 0 = screen
PRINT #0, "This is the same as PRINT"
```

```kcml
REM Tab separators work but AT/BOX are ignored
OPEN #3, "/tmp/csv.txt", "w"
PRINT #3, "Name", "Amount", "Date"   : REM comma = tab spacing
CLOSE #3
```

## Notes

- The `#stream` form is shorthand — see `OPEN #` for how to open a stream.
- When printing to a file, `PRINT #stream` and `PRINT` on its own (after `SELECT PRINT #stream`) produce the same result.
- `AT(`, `BOX(`, and `TAB(` are ignored on file streams.

## See Also

- `OPEN #` — open a file stream
- `CLOSE` — close a stream
- `PRINT` — standard print to current device
- `SELECT PRINT` — change current print device
