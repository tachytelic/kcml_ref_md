# CLOSE #

> Closes the file open on the specified stream number and frees the stream for reuse.

## Syntax

```
CLOSE #stream_number
```

| Parameter | Description |
|-----------|-------------|
| `stream_number` | The numeric stream number previously opened with `OPEN #` |

## Description

`CLOSE #` closes the file associated with the given stream number and releases it. After a `CLOSE #`, the stream number is free to be reused with a new `OPEN #`.

Any data buffered for writing is flushed to disk before the file is closed.

## Example

```kcml
: DIM stream, rec$80
: stream = 1
: OPEN #stream, "/tmp/myfile.txt", OUTPUT
: WRITE #stream, "Hello World"
: CLOSE #stream
: $END
```

## Notes

- Always `CLOSE #` a file when done to ensure all data is written and the stream is freed.
- Streams are automatically closed when the program exits or when `CLEAR` is called.
- Closing an already-closed stream may cause a runtime error.

## See Also

- `OPEN #` — open a file on a stream
- `READ #` — read from an open stream
- `WRITE #` — write to an open stream
- `SEEK #` — position within an open stream
