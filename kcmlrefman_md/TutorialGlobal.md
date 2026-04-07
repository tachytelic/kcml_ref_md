# Global and Background Partitions

> How KCML partitions share code and data through global partitions, and how Unix foreground partitions can manage switchable background tasks.

## Overview

KCML supports two related but distinct mechanisms for multi-partition work:

1. **Global partitions** — a special partition loaded into shared memory whose subroutines and `@`-prefixed variables are accessible by all other partitions that select it. Available on all versions of KCML.
2. **Background (switchable) partitions** — additional KCML processes attached to the same terminal, allowing a user to switch between tasks without logging out. Unix only.

> **Note:** Global partitions were largely superseded by the [library](TutorialModules.md) concept introduced in KCML 6.0. For new applications, use libraries. Global partitions are documented here for maintenance of existing systems.

---

## Background Partitions (Unix only)

Background partitions let a single terminal run several KCML tasks concurrently. The user switches between them using a hot key or under program control.

### Starting a background partition

```kcml
$RELEASE LOAD RUN "BACK1"
```

This creates a copy of the current foreground partition, loads and runs `BACK1` in it, and detaches the terminal from the new process. The background partition keeps running until it executes `$END`. Any keyboard read in a background partition suspends until the terminal reattaches.

A chain of `$END` statements automatically releases through waiting background partitions in order; the user returns to the OS only when the last one finishes.

### Switching between partitions

Under program control:

```kcml
$RELEASE TERMINAL          REM switch to next available background partition
$RELEASE TERMINAL TO 253   REM switch to a specific partition number
```

Using a hot key:

```kcml
$RELEASE KEY=20            REM function key 20 now triggers a partition switch
```

When `$RELEASE TERMINAL` executes, the screen is saved. When control returns to the original partition, the screen is restored.

### Checking partition status with $PSTAT

`$PSTAT(partition_number)` returns 48 bytes of status information. Byte 16 indicates terminal attachment:

| Value | Meaning |
|-------|---------|
| `A` | Partition is attached to the terminal |
| `D` | Partition is detached and still running |
| `W` | Partition is detached and waiting on I/O |

```kcml
IF STR($PSTAT(#PART),16,1)=="D" THEN 9000
REM jump to line 9000 if this partition is currently running in background
```

### The $RELEASE function

`$RELEASE` clones the current program and runs it as a child process. Available on both Unix and NT. The parent waits until the child executes `$END`. Useful when a called program would otherwise overwrite common variables or program lines.

---

## Global Partitions

### What a global partition is

A global partition is a KCML process running in shared memory. Other partitions "select" the global to gain access to its subroutines and `@`-prefixed variables. The global partition itself typically just initializes its variables and then sleeps.

### Starting a global partition

Global partitions are started with the `-g` switch:

```bash
HEAPINIT=512 export HEAPINIT
kcml -g GLOBAL1 &
```

The `HEAPINIT` environment variable sets the shared memory size in kilobytes. The `&` puts the process in background — without it the terminal would be captured by the global partition.

In the Korn shell, redirect stdin to prevent job-control problems:

```bash
kcml -g GLOBAL1 </dev/null &
```

### Startup script for automatic launch

Globals are normally started during system boot. A startup script looks like:

```bash
# Script to start KCML global partition
KCMLDIR=/usr/lib/kcml
PATH=$PATH:$KCMLDIR
TERMFILE=$KCMLDIR/TERMFILE
HEAPINIT=512
KTERM=dumb
export PATH TERMFILE HEAPINIT KTERM

( cd /user1 ; kcml -g PROGS/GLOBAL1 >/tmp/gblog1 )

HEAPINIT=50 ; export HEAPINIT
( cd /user2 ; kcml -g PROGS/GLOBAL2 >/tmp/gblog2 )
```

Add a line to `/etc/inittab` to call this script at boot:

```
gb:2345:boot:/usr/lib/kcml/kcmlsetup 1>/dev/syscon 2>&1
```

Don't forget to set execute permissions:

```bash
chmod +x /usr/lib/kcml/kcmlsetup
```

### If KCML was installed with kcmladmin

`kcmladmin` auto-generates the startup script. To add a global partition, save a loader program into the KCML utilities directory with the naming convention:

```
GLOBAL<n1>.<n2>
```

Where `n1` is a unique sequence number (counting from 1) and `n2` is the heap size in KB. Example:

```kcml
$DEVICE /D10="/usr/kcml/D10.bin"
$DEVICE /D11="/usr/lib/kcml/D11.bin"
SELECT DISK D10
LOAD RUN "GBLPRG"
```

Saved as:

```kcml
SAVE "/usr/lib/kcml/GLOBAL1.100"
```

(First global, 100 KB.) Restart the machine to activate.

### Naming the global partition

The global program must contain a `DEFFN @PART` statement that assigns the partition's name — other programs use this name in `SELECT @PART`:

```kcml
DEFFN @PART "GBMAIN1"
```

A typical global program initializes variables, names itself, then sleeps:

```kcml
COM @junk$1000, @lockvar=99
INIT(HEX(FF)) @junk$
DEFFN @PART "TESTGBL"
$BREAK !          REM sleep forever - subroutines below are never called by us

DEFFN 'one
    REM ... subroutine body available to other partitions ...
RETURN
```

### Accessing a global partition from another program

```kcml
SELECT @PART "TESTGBL"    REM attach to the global

REM GOSUB searches the executing partition first, then the global
GOSUB 'test               REM found in global if not in this program
GOSUB 'local              REM found locally
```

To detach from a global:

```kcml
SELECT @PART " "
```

A global stays selected across subsequent `LOAD` statements unless:
- A new program is loaded (default behaviour)
- Another global is selected
- The `KEEPSHARED` environment variable is set (prevents deselection on `LOAD`)

### Global variables

Global variables are identified by a leading `@` sign. They are declared in the global partition using `COM` or `DIM`:

```kcml
COM @counter, @name$40, @table(100)
```

Once declared, they are visible from any partition that has selected the global. Modifications are instantly visible to all other partitions.

Local (non-global) variables and global variables are completely separate namespaces — `abc$` and `@abc$` are different variables.

### Locking global variables

When multiple partitions may update a shared global variable, wrap the update in `@LOCK`/`@UNLOCK`:

```kcml
@LOCK
    REM only one partition can be between @LOCK and @UNLOCK at a time
    @counter = @counter + 1
@UNLOCK
```

This is *advisory* locking: other partitions can still read or write the variable, but any partition that tries to `@LOCK` will block until the current holder executes `@UNLOCK`.

### Listing global program text

Most `LIST` commands can be prefixed with `@` to operate on the selected global partition:

```
@LIST 1000,        REM list lines from 1000 onwards in the global
@LIST T"ABC"       REM search global for "ABC" and "abc"
@LIST '            REM list all subroutines in the global
```

Lines listed from the global are identified by the `@` prefix on the line number.

---

## Notes

- **Prefer libraries for new code.** Libraries (KCML 6.x, see [TutorialModules](TutorialModules.md)) provide the same code-sharing capability without the complexity of shared memory management and system-boot configuration.
- **Background partitions are Unix-only.** `$RELEASE LOAD RUN`, `$RELEASE KEY`, and `$RELEASE TERMINAL` produce an `A08 Statement not legal here` error on NT/Windows.
- **`HEAPINIT` must be set before starting the global.** You cannot resize shared memory after the fact.
- **Symbol index values for global variables are always negative.** This distinguishes them from local/program variables in `SYM(` results.
- **Deselecting a global invalidates all `SYM(` pointers** to global variables. Pointer values become meaningless if the global is deselected or replaced.
- See also: `$RELEASE`, `$RELEASE LOAD RUN`, `$RELEASE KEY`, `$RELEASE TERMINAL`, `$PSTAT`, `SELECT @PART`, `DEFFN @PART`, `@LOCK`, `@UNLOCK`, `COM`, `HEAPINIT`
