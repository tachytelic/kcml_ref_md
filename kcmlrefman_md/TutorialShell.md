# Invoking Unix and NT Commands

> Explains how to run operating system commands from KCML, redirect I/O to files and pipes, adjust process scheduling priority, and read or set environment variables.

---

## Running OS Commands from Immediate Mode

The `!` command entered at the KCML Workbench console provides direct access to the operating system shell:

- Entering `!` alone drops into the Unix shell or Windows command processor. Typing `exit` returns to KCML.
- Entering `!` followed by a command executes that single command and returns to KCML.

```
!ls -l
```
```
!DIR
```

Any Unix or Windows command available to the user — including piping and redirection — can be used with `!`.

On Unix, the shell used defaults to the Bourne shell. This can be changed by setting the `SHELL` environment variable in the user's `.profile`.

---

## SHELL Statement

`SHELL` executes an operating system command from within a KCML program. It can be used anywhere a numeric expression is valid; on Unix it returns the exit status of the command. On Windows the return value is always zero.

### Syntax

```
SHELL "command-string"
```

or as a numeric expression:

```
IF SHELL "command" == 0 THEN ...
```

### Examples

```kcml
SHELL "ls -l | pg"
SHELL "DIR \p"
```

**Effect:** Lists the contents of the current directory.

```kcml
IF SHELL"ubackup"==0 THEN PRINT "Backup completed O.K."
ELSE PRINT "Backup Failed"
```

**Effect:** Runs the Unix program `ubackup`, prints a message based on its exit status.

### Notes

- On Unix, take care when removing, renaming, or changing the permissions of KCML files or platter images while other KCML tasks may have them open. Changes do not take effect until the file is closed and reopened.
- On Windows, a new DOS box is started for each `SHELL` execution. This may cause screen flicker and affect performance when shells are called repeatedly. Setting byte 37 of `$OPTIONS RUN` to `HEX(01)` forces KCML to run DOS boxes minimized, hiding their output.

---

## Redirecting Input and Output

KCML can redirect the following devices to and from native OS files using `SELECT` parameters:

| SELECT parameter | Device |
|----------------|--------|
| `CI` | Console Input |
| `INPUT` | Standard Input |
| `CO` | Console Output |
| `LIST` | List device |
| `LOG` | Log device |
| `TRACE` | Trace device |
| `PRINT` | Print device |

A literal string or an alpha variable holding a native filename may be specified in place of a device address.

### Example — Redirecting LIST output to a file

```kcml
SELECT LIST "G:\TMP/LISTFILE.TXT"
LIST
SELECT LIST /005
```

**Effect:** Sends the output of `LIST` to the file `G:\TMP\LISTFILE.TXT`. The final `SELECT` restores the list device to its default.

### Example — Driving immediate-mode commands from a file

If the file `ren1` contains:
```
RENAME a$ TO junk$
RENAME b$ TO test$
```

Then in KCML:
```kcml
LOAD "OLDPROG"
SELECT CI "ren"
SELECT CI /001
SAVE "NEWPROG"
```

**Effect:** Replays the rename commands as if typed at the console, then restores normal keyboard input.

---

## Using Pipes

KCML applications can open pipes for reading or writing via `$DEVICE` and `SELECT`.

### Writing to a pipe

```kcml
$DEVICE /290="|lpr"
SELECT LIST /290
LIST
SELECT LIST /005
$DEVICE /290=" "
```

**Effect:** Routes `LIST` output to the Unix print spooler. The final `$DEVICE` statement closes the pipe. `$REWIND /290` can be used as an alternative to close it.

The pipe can also be specified directly in `SELECT`:

```kcml
SELECT LIST "|lpr"
LIST
SELECT LIST /005
```

### Reading from a pipe

```kcml
DIM abc$30
$DEVICE /01F="date|"
SELECT INPUT /01F
LINPUT abc$
SELECT INPUT /001
```

**Effect:** Reads the output of the Unix `date` command into `abc$`.

Or without `$DEVICE`:

```kcml
DIM abc$
SELECT INPUT "date|"
LINPUT abc$
SELECT INPUT /001
```

**Notes:**
- To re-read from a pipe the device must be closed and reopened, either by removing and re-specifying the `$DEVICE` or by using `$REWIND`.
- Attempting to re-read without closing generates an `X70 Insufficient data` error.
- On Windows, KCML emulates pipes by writing a temporary file to the `\` directory of the current drive. Piping large amounts of data requires corresponding disk space.
- Data can be read from a pipe character by character with `KEYIN`, or in groups with `INPUT` or `LINPUT`.

---

## Changing Scheduling Priority (Unix Only)

The `$NICE(` function adjusts the Unix scheduling nice factor of the current KCML task. A higher nice factor means lower scheduling priority. This is useful for background or batch tasks that should not compete aggressively for CPU time.

### Syntax

```
$NICE(expression)
```

The expression is added to the current nice factor, and the resulting nice factor is returned. Specifying `0` returns the current nice factor without changing it.

| Value | Meaning |
|-------|---------|
| 20 | Normal nice factor (default) |
| 40 | Maximum nice factor (lowest priority) |
| < 20 | Higher than normal priority — superuser only |
| -1 | Return value when `$NICE` fails |

Child processes inherit the current nice factor.

### Example

```kcml
PRINT $NICE(0)
PRINT $NICE(5)
```

**Effect:** Displays the current nice factor, then displays the new nice factor after adding 5.

The current nice factor for a terminal can be found on most Unix systems with `ps -lt`, under the `NI` column.

---

## Environment Variables

Operating system environment variables can be read or set locally using the `ENV(` function.

### Reading an environment variable

```kcml
PRINT ENV("TERM")
```

**Effect:** Prints the value of the `TERM` environment variable.

### Setting an environment variable

```kcml
ENV("TERM") = "vt100"
```

**Effect:** Sets `TERM` to `vt100` for the current task. New background partitions started for the terminal will inherit the new value; existing background partitions retain the original value.

### Listing locally set variables

```
LIST E
```

Lists all locally set environment variables and their contents.

---

## See Also

- `SHELL` — execute OS commands from KCML programs
- `$DEVICE` — define device addresses including pipes
- `SELECT` — redirect I/O devices
- `$REWIND` — close and rewind a device or pipe
- `$NICE(` — adjust Unix scheduling priority
- `ENV(` — read and set environment variables
- `LIST E` — list local environment variables
- `$OPTIONS RUN` byte 37 — minimize Windows DOS boxes
- `LINPUT` — read a line of input
- `INPUT` — read formatted input
