# SEEK #

> Repositions the file pointer for a stream opened with OPEN #.

## Syntax

```
offset = SEEK #stream [, BEG [, offset]]
offset = SEEK #stream [, END [, offset]]
offset = SEEK #stream [, FOR, offset]
offset = SEEK #stream [, offset]       (shorthand for BEG)
offset = SEEK #stream                  (query current position)
```

Returns the new file position (bytes from start of file), or `-1` on error.

## Anchor keywords

| Anchor | Meaning |
|--------|---------|
| `BEG` | Offset from beginning of file (default) |
| `END` | Offset from end of file (negative offset moves backward) |
| `FOR` | Offset relative to current position |

## Examples

```kcml
DIM file$1000
OPEN #1, "./file1", "w+"
ret = WRITE #1, file$

offset = SEEK #1, BEG          : REM  → 0    (go to start)
offset = SEEK #1, BEG, 100     : REM  → 100  (100 bytes from start)
offset = SEEK #1, END, -100    : REM  → 900  (100 bytes before end)
offset = SEEK #1, 500          : REM  → 500  (shorthand: BEG,500)
offset = SEEK #1, FOR, 100     : REM  → 600  (100 forward from current)
offset = SEEK #1               : REM  → 600  (query: no movement)
CLOSE #1
```

## Notes

- Returns `-1` on error — check `$ERR`.
- A negative offset is valid with `END` and `FOR`; with `BEG` a negative offset raises a `P34` error.
- Unexpected results may occur in text mode on Windows or when `$OPTIONS #` sets ignore/termination characters — these affect byte counts returned by `READ #` / `WRITE #`.

## See Also

- `OPEN #` — open a stream
- `READ #` — read bytes
- `WRITE #` — write bytes
- `CLOSE #` — close stream
