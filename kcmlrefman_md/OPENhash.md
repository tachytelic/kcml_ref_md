# OPEN #

> Opens a sequential file (or socket) on a numbered stream for reading or writing.

## Syntax

```
OPEN #stream, filename$ [, mode$] [, permissions] [, buffersize]
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `stream` | Stream number (1–255) |
| `filename$` | Path to file, or `"host:port"` for TCP socket |
| `mode$` | Access mode string (see below); default `"r"` |
| `permissions` | Unix permissions for new files (octal, e.g. `0644`) |
| `buffersize` | I/O buffer size in bytes |

### Mode flags

| Flag | Meaning |
|------|---------|
| `r` | Read (file must exist) |
| `w` | Write (creates or truncates) |
| `a` | Append (creates if missing) |
| `r+` | Read + write (file must exist) |
| `w+` | Read + write (creates or truncates) |
| `a+` | Read + append |
| `b` | Binary mode (no CR/LF translation) |
| `t` | Text mode (default; CR/LF translated on Windows) |
| `s` | Shared access |
| `n` | Non-blocking I/O |
| `p` | Pipe/process |
| `@` | TCP/IP socket mode |

Combine flags: `"rb"` = binary read, `"w+"` = read/write create.

## Description

Opens the named file on `#stream`. After a successful open, use `PRINT #stream` / `INPUT #stream` / `LINPUT #stream` for I/O, and `CLOSE #stream` when done.

Use `@` mode with `"host:port"` filename to open a TCP/IP socket connection:

```kcml
OPEN #3, "10.1.1.1:80", "@"
```

## Examples

```kcml
REM Write a text file
OPEN #1, "/tmp/output.txt", "w"
PRINT #1, "Line one"
PRINT #1, "Line two"
CLOSE #1
```

```kcml
REM Read a text file line by line
DIM line$256
OPEN #2, "/tmp/output.txt", "r"
REPEAT
  LINPUT #2, line$
UNTIL $EOF(2)
CLOSE #2
```

```kcml
REM Binary write
OPEN #4, "/tmp/data.bin", "wb"
PRINT #4, HEX(01020304)
CLOSE #4
```

```kcml
REM TCP socket
OPEN #5, "time.example.com:13", "@"
DIM resp$512
LINPUT #5, resp$
PRINT resp$
CLOSE #5
```

## Notes

- Stream numbers 1–255; stream 0 is stdout.
- Opening an already-open stream raises an error — always `CLOSE` before reopening.
- `$EOF(stream)` returns true after the last record/line has been read.
- Error on open: check `$ERR` or use `ON ERROR` / `TRY/CATCH`.
- For KISAM/KDB indexed files use `CALL KI_OPEN` instead.

## See Also

- `CLOSE` — close a stream
- `PRINT #` — write to a stream
- `LINPUT #` — read a line from a stream
- `$EOF(` — end-of-file test
- `KI_OPEN` — KISAM indexed file open
