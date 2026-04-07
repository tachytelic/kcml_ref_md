# General Configuration

> How KCML allocates and tracks partitions, terminals, and memory; and how to configure the Device Equivalence Table (DET) and Device Table (DT) for I/O routing.

## Overview

KCML is largely self-configuring. Each running instance of KCML is an OS process, automatically assigned a partition number and a terminal number. The Device Equivalence Table (DET) and Device Table (DT) together govern all I/O device routing, from the keyboard and screen through to files, pipes, and printers.

---

## Partitions and Terminals

### Partition Numbers

Each instance of KCML is assigned a unique *partition number* — an integer in the range 1 to 32767. The partition number is shown below the copyright message when `CLEAR` is entered or RESET is pressed. It can also be read programmatically with the `#PART` function.

The default working limit is 1024 partitions on UNIX, and 512 on NT/Windows 5.03. The `bkstat` utility can raise the limit up to 32767.

### Terminal Numbers

Each KCML instance also has a *terminal number* (0 to 32767) representing the physical terminal it is connected to. The terminal number is returned by `#TERM`. A background partition disconnected from a physical terminal gets terminal number 0.

### The TERMFILE

On UNIX, terminal numbers are stored in an ASCII file whose path is set by the `TERMFILE` environment variable (default `/tmp/TERMFILE`). KCML creates this file automatically if it does not exist.

Each line of `TERMFILE` maps a terminal identity to a set of partition numbers:

```
/dev/term/45    50  51  52  53
```

- The first column is the terminal identifier (tty name, IP address, or client hostname).
- The second column is the `#TERM` and `#PART` value for the first KCML on that terminal.
- Additional numbers on the line are allocated as `#PART` for further concurrent KCML processes on the same terminal (they all share the same `#TERM`).
- If more KCML processes are started than there are numbers on the line, the extra partitions count down from the value of the `BCDPART` environment variable (default 512).

On NT or WKCML, the same information is held in the Windows server registry.

### Restricting Partition Numbers

The `BCDPART` environment variable caps the maximum partition number:

```sh
BCDPART=400
export BCDPART
```

Secondary partitions created via `$RELEASE LOAD RUN` or `SHELL "kcml"` keep the same `#TERM` as the parent but get a new `#PART` counted down from `BCDPART`.

---

## Memory Allocation

KCML starts with an initial memory region called the *heap*, whose size is controlled by the `HEAPINIT` environment variable. If `HEAPINIT` is not set, the heap size is chosen automatically.

The heap holds all internal tables, program lines, and variables. If a program needs more memory, the heap expands automatically. However, freed variables and smaller programs do not automatically shrink the heap. Use `$SPACE` from within menu programs to trigger a memory compaction and recover unused heap space.

Use `LIST SPACE` to display a breakdown of current memory usage for the running partition.

---

## Configuring KCML Devices

### The Device Equivalence Table (DET)

The DET is a per-partition table that maps three-character hexadecimal *device addresses* (e.g. `/215`) to actual files or devices. Each character of the address must be a valid hex digit (0–9, A–F). The DET is consulted on every I/O operation.

#### Pre-allocated Device Addresses

| Address | Default file | Purpose |
|---------|-------------|---------|
| `/000` | `/dev/null` | Null device (bit bucket) |
| `/001` | `stdin` | Standard input (keyboard) |
| `/005` | `stdout` | Standard output (screen) |
| `/215` | `/dev/lp` | Line printer |
| `/204` | `stdout` | Local printer |

`/000`, `/001`, and `/005` are fixed and cannot be redefined. Printer devices can be redirected.

#### Defining and Modifying DET Entries

Use `$DEVICE` to add, modify, or remove DET entries:

```kcml
$DEVICE /215 = "/dev/term/27"       : REM redirect line printer
$DEVICE /D10 = "G:\demo\accounts.bs2"
$DEVICE /920 = "/dev/rfd096ds15", DISK
$DEVICE(/01C) = "COM1", TC
```

- The `DISK` keyword marks the device as a platter image. Device addresses beginning with `3`, `B`, or `D` are automatically treated as platter images.
- The `TC` keyword marks the device as a 2227B device.
- Parentheses around the address are optional.

Remove a DET entry by setting its filename to blank or by omitting the filename entirely:

```kcml
$DEVICE /217 = " "
REM or:
$DEVICE /217
```

A device can only be removed if it is not currently open.

#### Using $DEVICE as a Function

`$DEVICE` can return the native file path associated with a device address:

```kcml
prdev$ = $DEVICE /215
```

### The Device Table (DT) and Default Devices

The DT contains named *select parameters* that route specific I/O operations to device addresses. These can be modified with `SELECT name device_address`:

| Select parameter | Default | Purpose |
|----------------|---------|---------|
| `CI` | `/001` | Console Input — keyboard for immediate mode and editing. |
| `CO` | `/005` | Console Output — screen for echo and prompts. Also holds the screen line width (default 80). |
| `INPUT` | `/001` | Device for `INPUT`, `KEYIN`, `LINPUT`, etc. |
| `LIST` | `/005` | Output device for `LIST`. Also holds the line width (default 80). |
| `LOG` | `/005` | Device on which keyboard input is recorded. |
| `PRINT` | `/005` | Output device for `PRINT` and `PRINTUSING`. Also holds the line width (default 80). |
| `TAPE` | `/005` | Default device for tape-class operations (`$GIO`, `$IF ON`, etc.) that omit an explicit device address. |
| `TRACE` | `/005` | Output device for `TRACE` and `$COMPILE`. |

**Example — redirect INPUT:**

```kcml
SELECT INPUT /009
```

All subsequent `KEYIN`, `LINPUT`, etc. now read from device `/009`.

**Example — redirect LIST output to a Unix pipe:**

```kcml
SELECT LIST "|lpr"
LIST
SELECT LIST /005
```

Devices can also be selected directly to native files or pipes using a string literal rather than a device address.

### Streams

The DT provides 256 *streams* (numbered 0–255). Each stream holds one device address, selected with `SELECT #stream`. All I/O referencing a stream number is directed to the associated device address. Stream `#0` is the default; `SELECT DISK` sets stream `#0`.

Streams can also be pointed directly to filesystem directories:

```kcml
SELECT #129 "/usr/PROGRAMS"
```

On Windows, KCML translates `/` to `\` automatically.

#### Deselecting Streams

Each active stream consumes memory. When no longer needed, release it:

```kcml
DESELECT #129
```

Streams are automatically cleared on `CLEAR`, `LOAD RUN`, RESET, or when `$SELECT "."` is executed.

#### Using SELECT as a Function

`SELECT` can return the device address or native file currently associated with a stream or select parameter:

```kcml
PRINT SELECT PRINT, SELECT #27
```

**Output:**
```
005         /user1/PROGS
```

### Changing the Current Working Directory

`$SELECT` changes the current working directory. All currently selected streams are automatically closed; DET entries remain intact.

```kcml
$SELECT "/user1/tmpdir"
PRINT $SELECT
```

**Output:**
```
/user1/tmpdir
```

Use `$REWIND` to clear DET entries pointing to files in the old directory.

### Displaying the DET and DT

`LIST DT` displays the full contents of both tables:

- **Section 1** — Device Table: stream numbers with their allocated files, plus start/end/used/free byte counts and lock status.
- **Section 2** — Device Equivalence Table: default select devices (LIST, TRACE, CI, CO, etc.) followed by all additional devices defined with `$DEVICE`.

---

## Notes

- The working limit of 1024 partitions (UNIX) / 512 (NT) can be raised with `bkstat`, up to the theoretical maximum of 32767.
- `$SPACE` should be called from menu programs and other long-running foreground programs to prevent unbounded heap growth.
- Addresses starting with `3`, `B`, or `D` are assumed to be platter images; use the `DISK` keyword explicitly for addresses with other leading characters.
- `DESELECT` does not close any file open on the stream — use `CLOSE #` first if a file is open.
