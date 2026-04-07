# Data and Program File Access

> How KCML creates, reads, writes, seeks, and manages data files and program files in the native filesystem, including file locking, streams, and program protection.

## Overview

KCML stores both data and program files directly in the native operating system filesystem (UNIX or Windows). A legacy concept called a *platter image* is also available for backward compatibility, but all new development should use native filesystem files.

When naming files in the native filesystem, avoid special characters that carry meaning in UNIX shells:

```
`  |  "  $  ^  &  (  )  [  ]  {  }  \  /  <  >  ;  *  ?  !
```

---

## Data Files

Two file access methods are available:

- **K-ISAM** (Kerridge Indexed Sequential Access Method) — an efficient access method designed for large, complex databases. Covered separately.
- **Standard file access** — conforms to the UNIX/DOS/ANSI model. Works on regular files, named pipes, and character devices. Described below.

### Opening and Creating Files

Use `OPEN #` to open an existing file or create a new one. Files are opened on a numbered *stream*. The stream can be pre-pointed to a directory with `SELECT #`. When finished, release the stream with `CLOSE #`.

```
OPEN #stream, file$[, mode$][, permissions$][, buffersize]
```

| Parameter | Description |
|-----------|-------------|
| `stream` | Stream number to associate with the file. |
| `file$` | Filename or full path. |
| `mode$` | Open mode (see table below). |
| `permissions$` | Unix-style octal permissions for newly created files, e.g. `"0666"`. |
| `buffersize` | Read buffer size in bytes (affects buffered line reads). |

**Common open modes:**

| Mode | Meaning |
|------|---------|
| `"r"` | Read only. File must exist. |
| `"r+"` | Read and write. File must exist. |
| `"w"` | Write only. Creates new file; truncates if it exists. |
| `"w+"` | Read and write. Creates new file; truncates if it exists. |
| `"a"` | Append only. Creates file if it does not exist. |
| `"a+"` | Read and append. Creates file if it does not exist. |

Appending `"t"` to the mode (e.g. `"w+t"`) opens the file in text mode on DOS/Windows systems, which translates `HEX(0D0A)` line endings to `HEX(0A)` on read.

**Examples:**

```kcml
REM open existing file for read and write
OPEN #10, "/user1/FILE1", "r+"

REM create or truncate a file, set permissions
OPEN #10, "/user1/FILE1", "w+", "0666"

REM close the stream when done
CLOSE #10
```

### Writing to Files

`WRITE #` writes the full contents of an alpha variable (including trailing spaces) to the file on the specified stream. The file pointer advances by the number of bytes written. The return value is the number of bytes written, or `-1` on error.

```
bytes_written = WRITE #stream, buffer$
```

**Example:**

```kcml
OPEN #10, "/user1/FILE1", "w+"
offset = WRITE #10, buffer$
```

On error, use `ERR` to retrieve the error code:

```kcml
IF WRITE #10, buffer$ = -1 THEN DO
    PRINT "Write failed - error code: "; ERR
ENDDO
```

### Reading from Files

`READ #` reads data from the file into an alpha variable. The return value is the number of bytes read, or `-1` on error. When fewer bytes than the variable size are available, the variable is partially filled, the return value reflects the actual count, and the `END` condition is set.

```
bytes_read = READ #stream, buffer$
```

**Example — read a file to end:**

```kcml
OPEN #10, "/user1/FILE1", "r"
WHILE NOT END DO
    BytesRead = READ #10, Buffer$
    REM process STR(Buffer$,,BytesRead)
WEND
CLOSE #10
```

**Line-at-a-time reading:**  
Enable line-mode reading by ORing `HEX(01)` into byte 2 of `$OPTIONS #` for the stream and setting byte 5 to the line terminator character. The terminator is not copied into the buffer. When the terminator is found, bit `HEX(04)` of byte 4 in `$OPTIONS #` is set. A return value of zero can mean either a blank line or end of file — check `$OPTIONS #` byte 4 to distinguish.

### Changing the File Pointer

`SEEK #` repositions the file pointer before a `READ #` or `WRITE #`. It returns the new pointer position, or `-1` on error.

```
new_pos = SEEK #stream, [BEG | END | FOR] [, offset]
```

| Form | Meaning |
|------|---------|
| `SEEK #s, BEG` | Move to the start of the file (position 0). |
| `SEEK #s, BEG, n` | Move to byte `n` from the start. |
| `SEEK #s, END` | Move to the end of the file. |
| `SEEK #s, END, -n` | Move to `n` bytes before the end. |
| `SEEK #s, FOR n` | Advance `n` bytes from the current position. |

**Examples:**

```kcml
new_pos = SEEK #10, BEG        : REM go to start
new_pos = SEEK #10, BEG, 120   : REM go to byte 120
new_pos = SEEK #10, END        : REM go to end
new_pos = SEEK #10, END, -120  : REM 120 bytes before end
new_pos = SEEK #10, FOR 120    : REM advance 120 bytes
```

Seeking beyond the end of the file is permitted. A subsequent `WRITE #` automatically extends the file to reach the new position.

### File Locking

Advisory file locks are acquired with `$OPEN` and released with `$CLOSE` or `CLOSE #`. Advisory locking means other partitions can still read or write the file but cannot `$OPEN` it themselves.

If the file is already `$OPEN`ed by another partition, the statement blocks until the file is released, unless an optional branch-on-timeout line number is specified.

```kcml
OPEN #10, "NEWFILE", "r+"
$OPEN #10, 1000
REM ... exclusive access ...
$CLOSE #10
```

An `I92 Time out error` occurs if you attempt to lock a file that was not opened with write access.

### Miscellaneous File I/O

**Get file position details:**

```kcml
LIMITS T#10, file_start, file_end, current_pos
```

Returns the start (always 0 for `OPEN #` files), end, and current pointer position in bytes.

**Remove a file:**

```kcml
REMOVE "NEWFILE"
```

**Rename a file:**

```kcml
RENAME T#10, "OLDFILE" TO "NEWFILE"
```

**Print to a file:**

```kcml
OPEN #10, "/tmp/TESTFILE", "w+"
PRINTUSING #10, "#####.##", total
CLOSE #10
```

Each `PRINT #` or `PRINTUSING #` line is terminated with `HEX(0A)`. On DOS/Windows systems, open the file with the `"t"` mode flag (e.g. `"w+t"`) to write `HEX(0D0A)` line endings instead.

---

## Program Files

### Saving Programs

Use `SAVE` to write the program currently in memory to a new file. Use `RESAVE` to overwrite an existing file. Both accept a full pathname or work relative to the stream selected with `SELECT DISK`.

```kcml
SELECT DISK "/user1/PROGS"
SAVE "M-MENU"
```

Or using an absolute path:

```kcml
SAVE "/user1/PROGS/M-MENU"
```

Or using a stream:

```kcml
SELECT #27, "/user1/PROGS"
SAVE "M-MENU"
```

`SAVE` errors with `D83 Cannot save file` if the file already exists. Use `RESAVE` to overwrite.

In the KCML Workbench, both `SAVE` and `RESAVE` are available via Ctrl-S or the File menu.

### Removing Programs

```kcml
REMOVE "/user1/PROGS/M-MENU"
```

`SCRATCH` is the older, deprecated alternative that operates relative to the stream table:

```kcml
SELECT #46 "/user1/PROGS"
SCRATCH "M-MENU"
```

Use `REMOVE` in new code.

### Loading Programs

```kcml
LOAD "/user1/PROGS/TESTPROG"
LOAD RUN "/user1/PROGS/TESTPROG"
```

Or via `SELECT DISK`:

```kcml
SELECT DISK "PROGS"
LOAD "TESTPROG"
```

`LOAD RUN` loads and immediately starts execution.

### Scrambling (Password-Protecting) Programs

KCML can protect programs by scrambling them with a password. A scrambled program cannot be `LIST`ed, edited, or `TRACE`d while running. Pressing HALT stops execution but only allows `CLEAR` and `LOAD RUN`.

**To scramble:** use `SELECT PASSWORD` before a `SAVE!` or `RESAVE!`. KCML prompts for the password twice (input is not echoed).

**To reveal:** load the program, then issue `SELECT PASSWORD` with the original password.

**Partial reveal for support:** it is possible to temporarily reveal a scrambled program without disclosing the master password — see the `SELECT PASSWORD` reference and the `checknum` utility in the KCML Utilities chapter.

---

## Notes

- Streams 0–255 are available. Stream #0 is the default stream used when no stream is specified. `SELECT DISK` sets stream #0.
- `OPEN #` streams are separate from device-addressed streams managed by `$DEVICE` and `SELECT`. Both coexist in the Device Table.
- Wildcard characters (`*`, `?`) and UNIX shell metacharacters in filenames will cause unpredictable behaviour; always use clean alphanumeric filenames.
- On Windows, KCML automatically translates forward slashes (`/`) in paths to backslashes (`\`).
