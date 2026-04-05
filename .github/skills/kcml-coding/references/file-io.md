# KCML File I/O Reference

Complete reference for file operations in KCML.

## File Streams

KCML uses numbered streams (1-99) for file operations. Each stream can have one file open at a time.

## OPEN# - Open a File

```kcml
OPEN #stream, filename$, mode$
```

### File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read only - file must exist |
| `"w"` | Write only - creates or truncates |
| `"a"` | Append - creates if needed, writes at end |
| `"r+"` | Read/write - file must exist |
| `"w+"` | Read/write - creates or truncates |
| `"a+"` | Read/append - creates if needed |

### Mode Flags (append to mode)

| Flag | Description |
|------|-------------|
| `t` | Text mode (Windows: converts CR/LF) |
| `b` | Binary mode (default on Unix) |
| `@` | Socket connection (filename is host:port) |
| `p` | Pipe to command |
| `s` | Synchronous I/O |
| `x` | Exclusive create (fail if exists) |

### Examples

```kcml
REM Open file for reading
: OPEN #1, "data.txt", "r"

REM Open for write (create/truncate)
: OPEN #1, "output.txt", "w"

REM Open for append
: OPEN #1, "log.txt", "a"

REM Open for read/write
: OPEN #1, "records.dat", "r+"

REM Open socket connection
: OPEN #1, "server.example.com:8080", "r@"

REM Open pipe to command
: OPEN #1, "ls -la", "rp"
```

## READ# - Read from File

```kcml
bytes_read = READ #stream, buffer$
```

### Return Values

- Returns number of bytes read
- Returns -1 on error
- Sets END condition when EOF reached

### Checking for EOF

```kcml
DIM buffer$1024
: OPEN #1, "input.txt", "r"
: REPEAT
:   bytes = READ #1, buffer$
:   IF (bytes > 0) THEN DO
:     REM Process buffer$
:     PRINT STR(buffer$, 1, bytes)
:   ENDDO
: UNTIL END
: CLOSE #1
```

### Read with Error Handling

```kcml
bytes = READ #1, buffer$
: IF (bytes == -1) THEN DO
:   PRINT "Error reading file: "; ERR
: ENDDO
```

## WRITE# - Write to File

```kcml
bytes_written = WRITE #stream, buffer$
```

### Return Values

- Returns number of bytes written
- Returns -1 on error

### Examples

```kcml
DIM data$100
: data$ = "Hello, World!"
: OPEN #1, "output.txt", "w"
: ret = WRITE #1, data$
: CLOSE #1
```

### Write with Error Check

```kcml
ret = WRITE #1, buffer$
: IF (ret == -1) THEN DO
:   PRINT "Write error: "; ERR
: ELSE DO
:   PRINT "Wrote "; ret; " bytes"
: ENDDO
```

## SEEK# - Position File Pointer

```kcml
position = SEEK #stream, [BEG|END|FOR], [offset]
```

### Seek Origins

| Origin | Description |
|--------|-------------|
| `BEG` | From beginning of file (default) |
| `END` | From end of file |
| `FOR` | Relative to current position |

### Examples

```kcml
REM Get current position
: pos = SEEK #1

REM Go to beginning
: pos = SEEK #1, BEG

REM Go to position 100 from start
: pos = SEEK #1, BEG, 100

REM Go to 50 bytes before end
: pos = SEEK #1, END, -50

REM Move forward 100 bytes
: pos = SEEK #1, FOR, 100

REM Move backward 50 bytes
: pos = SEEK #1, FOR, -50
```

### Random Access File Example

```kcml
DIM rec$100
: OPEN #1, "records.dat", "r+"
: REM Read record at position 500
: pos = SEEK #1, BEG, 500
: bytes = READ #1, rec$
: REM Modify and write back
: rec$ = "Updated record"
: pos = SEEK #1, BEG, 500
: ret = WRITE #1, rec$
: CLOSE #1
```

## CLOSE# - Close a File

```kcml
CLOSE #stream
```

### Example

```kcml
OPEN #1, "file.txt", "r"
: REM ... work with file ...
: CLOSE #1
```

## $OPTIONS# - Stream Options

Configure stream behavior:

```kcml
$OPTIONS #stream, option$
```

Common options include setting line terminators and buffer sizes.

## Complete File Copy Example

```kcml
DIM buffer$4096, infile$100, outfile$100
: infile$ = "source.txt"
: outfile$ = "dest.txt"
: OPEN #1, infile$, "r"
: OPEN #2, outfile$, "w"
: REPEAT
:   bytes = READ #1, buffer$
:   IF (bytes > 0) THEN DO
:     ret = WRITE #2, STR(buffer$, 1, bytes)
:   ENDDO
: UNTIL END
: CLOSE #1
: CLOSE #2
: PRINT "File copied"
: $END
```

## Read Lines from Text File

```kcml
DIM line$256
: OPEN #1, "text.txt", "r"
: $OPTIONS #1, "L" : REM Line mode
: REPEAT
:   bytes = READ #1, line$
:   IF (bytes > 0) THEN DO
:     PRINT STR(line$, 1, bytes)
:   ENDDO
: UNTIL END
: CLOSE #1
```

## Error Codes

| Code | Description |
|------|-------------|
| D80 | File not open |
| I96 | File has read access only |
| P82 | File not found |
| P83 | Permission denied |

## File Existence Check

KCML doesn't have a direct file existence function, but you can try to open:

```kcml
TRY
:   OPEN #1, filename$, "r"
:   CLOSE #1
:   exists = TRUE
: CATCH ERR 82, 83
:   exists = FALSE
: END TRY
```

## Socket Communication Example

```kcml
DIM response$4096, request$256
: request$ = "GET / HTTP/1.0" & HEX(0D0A0D0A)
: OPEN #1, "www.example.com:80", "r+@"
: ret = WRITE #1, request$
: REPEAT
:   bytes = READ #1, response$
:   IF (bytes > 0) THEN DO
:     PRINT STR(response$, 1, bytes);
:   ENDDO
: UNTIL END
: CLOSE #1
```

## Pipe Example

```kcml
DIM output$1024
: OPEN #1, "ls -la", "rp"
: REPEAT
:   bytes = READ #1, output$
:   IF (bytes > 0) THEN PRINT STR(output$, 1, bytes);
: UNTIL END
: CLOSE #1
```

## Best Practices

1. **Always close files** - Use CLOSE# when done to free resources
2. **Check return values** - READ# and WRITE# return -1 on error
3. **Use TRY/CATCH** - Wrap file operations in error handlers
4. **Buffer appropriately** - Use reasonably sized buffers (1024-4096 bytes)
5. **Handle EOF** - Use the END condition for read loops

## See Also

- [string-functions.md](string-functions.md) - STR() for extracting bytes read
- [error-handling.md](error-handling.md) - TRY/CATCH for file errors
- [control-flow.md](control-flow.md) - REPEAT/UNTIL for read loops
