# READ #

> Reads raw bytes from an open file stream into an alpha variable.

## Syntax

```
bytes_read = READ #stream, buffer$
```

## Description

Reads bytes from the file open on `#stream` into `buffer$`, filling it up to its declared length. Returns the number of bytes actually read in `bytes_read`. After reading, the file pointer advances by `bytes_read`.

If fewer bytes are available than the buffer length (end of file), `bytes_read` is less than `LEN(buffer$)` and the end-of-file flag is set (testable with the `END` condition or `$EOF(`).

Returns `-1` on error; check `$ERR` for the error code.

### Error codes

| Error | Meaning |
|-------|---------|
| `D80` | File not open |
| `I92` | Timeout |
| `I96` | File has read access only |

## Examples

```kcml
DIM buffer$128
OPEN #1, "/tmp/data.bin", "rb"
WHILE TRUE DO
  posn = READ #1, buffer$
  IF (END)
    BREAK
  END IF
  REM process buffer$
WEND
CLOSE #1
```

```kcml
REM Check exact read count
DIM buf$512, got
OPEN #2, "/tmp/file.dat", "rb"
got = READ #2, buf$
IF got == LEN(buf$) THEN PRINT "Full block read"
IF got < LEN(buf$) THEN PRINT "Partial: "; got; " bytes"
CLOSE #2
```

```kcml
REM Loop while full blocks available
WHILE (READ #1, buffer$) == LEN(buffer$) DO
  REM process full block
WEND
```

## Notes

- `READ #` is for binary/raw reads; use `LINPUT #` for text line reading.
- Use `SEEK #` to reposition the file pointer before reading.
- The `END` condition after a `READ #` inside an `IF` block tests for end of file.

## See Also

- `OPEN #` — open a stream
- `WRITE #` — write to a stream
- `SEEK #` — reposition file pointer
- `LINPUT #` — read a text line
- `$EOF(` — end-of-file test
