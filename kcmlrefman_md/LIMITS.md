# LIMITS

> Returns size and status information about a cataloged file in a platter image or a native OS file.

## Syntax

```
LIMITS #stream, start, end, current [, status]
LIMITS #stream, filename, start, end, current [, status]
LIMITS <filename_var>, start, end, current [, status]
```

| Element | Description |
|---------|-------------|
| `#stream` | Open stream number |
| `filename` | Literal or variable filename |
| `start` | Numeric receiver — start sector (or 0 for native files) |
| `end` | Numeric receiver — end sector (or file size in bytes for native files) |
| `current` | Numeric receiver — sectors used (or current byte position for native files) |
| `status` | Optional numeric receiver — file status code |

## Description

`LIMITS` reports the allocation and usage of a file:

- **With a filename**: returns the start sector, end sector, and sectors used for that file in the platter image or native directory. If `status` is omitted and the file does not exist, an error occurs.
- **With a stream number only** (no filename): returns info for the file currently open on that stream.
- **For native OS files** (opened with `OPEN#`): `start` is always 0, `end` is the file size in bytes, `current` is the current byte position. (Unreliable if file opened in append mode — use `SEEK #n, END` instead.)

### Status codes

| Value | Meaning |
|-------|---------|
| `-2` | Scratched data file |
| `-1` | Scratched program |
| `0` | File not found |
| `1` | Program file |
| `2` | Data file |
| `3` | Directory |
| `4` | Unix special file or device (e.g. FIFO) |

## Examples

```kcml
LIMITS #1, start1, end1, used1
LIMITS "FRED", start_1, end_1
LIMITS <fnm$>, st, ed
```

With status check:
```kcml
DIM st, ed, used, status
LIMITS "DATAFILE", st, ed, used, status
IF (status == 0)
    PRINT "File not found"
ELSE IF (status == 2)
    PRINT "Data file: sectors "; st; " to "; ed; ", used: "; used
END IF
```

## Notes

- If `status` is omitted and the file does not exist, a runtime error occurs.
- Omitting the `current` (used) parameter improves performance by avoiding a disk read of the system end block.
- For native OS files opened in **append mode**, `LIMITS` does not return reliable results; use `SEEK #n, END` to find the file size.
- LIMITS operates on the current platter (stream) — specify the correct `#stream` or use a filename with a device path.

## See Also

- `OPEN#` — open a native file
- `SEEK#` — position within an open stream
- `CATALOG` — list files in a platter image
