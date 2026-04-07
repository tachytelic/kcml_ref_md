# DESELECT #

> Frees the memory allocated for one or more stream numbers after their files have been closed.

## Syntax

```
DESELECT #stream [, #stream] ...
```

| Parameter | Description |
|-----------|-------------|
| `#stream` | A stream number (0–255) to deallocate |

## Description

KCML supports up to 256 stream numbers (0–255). Each active stream number uses a small amount of memory. `DESELECT #` releases this memory for stream numbers that are no longer needed.

Before calling `DESELECT #`, the file on that stream must have been closed (`CLOSE #`). If a file is still open on the stream, a P48 error occurs.

## Examples

```kcml
DESELECT #25, #89, #250
DESELECT #file1, #27, #present
```

## Notes

- Only needed when managing many stream numbers and memory is tight. For typical programs using a small number of streams, `DESELECT` is rarely necessary.
- The stream number must be closed before deselecting.
- After `DESELECT`, the stream number can be reused with `OPEN #`.

## See Also

- `OPEN #` — open a file on a stream number
- `CLOSE #` — close a file on a stream number
- `SELECT DISK` — select a disk/directory for subsequent file operations
