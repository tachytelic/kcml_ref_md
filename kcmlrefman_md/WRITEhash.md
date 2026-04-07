# WRITE #

> Writes raw bytes from an alpha variable to an open file stream.

## Syntax

```
bytes_written = WRITE #stream, buffer$
```

## Description

Writes the **entire contents** of `buffer$` (including trailing spaces/nulls) to the file open on `#stream`. Returns the number of bytes written, or `-1` on error.

After writing, the file pointer advances by `bytes_written`. If the pointer was positioned past the end of file (via `SEEK #`), KCML automatically extends the file.

### Error codes

| Error | Meaning |
|-------|---------|
| `D80` | File not open |
| `I96` | File opened read-only |

## Examples

```kcml
DIM buffer$512, written
buffer$ = "Hello, World!"
OPEN #1, "/tmp/output.dat", "w"
written = WRITE #1, buffer$
PRINT "Wrote "; written; " bytes"
CLOSE #1
```

```kcml
REM Binary write
DIM data$4
data$ = HEX(DEADBEEF)
written = WRITE #2, data$
```

```kcml
REM Check for error
IF WRITE #1, buffer$ == -1 THEN PRINT "Write failed: "; $ERR
```

```kcml
REM Write only content (no trailing spaces)
written = WRITE #1, RTRIM(buffer$)
```

## Notes

- All bytes including trailing spaces are written — use `RTRIM(` to exclude them.
- `WRITE #` is for binary/raw writes; for text line writing use `PRINT #stream`.
- Use `SEEK #` to position the file pointer before writing.

## See Also

- `OPEN #` — open a stream
- `READ #` — read bytes from a stream
- `SEEK #` — reposition file pointer
- `PRINT #` — write text to a stream
- `RTRIM(` — strip trailing spaces
