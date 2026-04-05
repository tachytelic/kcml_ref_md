# KCML Global Partitions and Libraries

The mechanism by which KCML ERP systems share subroutines, variables, and database access routines across all user partitions simultaneously.

## Architecture of This ERP System

The actual system uses a **hybrid architecture** — both the traditional global partition mechanism and the modern library system, combined:

```
Boot time:
  kcml -g GB/START  →  names itself "KOPEN3GB"
                    →  LOAD <n>libraries$()  ← loads all libGN, libKI, libWI, libPF...
                    →  $BREAK !              ← sleeps forever

User login:
  runs GB/INIT     →  SELECT @PART "KOPEN3GB"  ← attaches to global's code
                   →  declares all COM variables ← session-level shared state
                   →  opens all database files   ← populates gb_h() handles
                   →  LOAD "PF/START" 1000       ← enters main menu
```

The global partition provides **code** (subroutines). The COM variables provide **state** (file handles, user info, today's date) that persists across LOAD within one user session.

**Libraries** (KCML 6.0+) are the modern replacement. Functionally similar but compiled as `.klib` files rather than running as separate processes.

---

## Global Variables — The `@` Prefix

Global variables are declared within the global partition and accessible by all selecting partitions. They are identified by the `@` prefix:

```kcml
REM In the global partition program:
COM @junk$1000, @lockvar = 99
DIM @shared_counter, @company_name$30
```

Accessing from a regular program (after `SELECT @PART`):
```kcml
@shared_counter += 1
PRINT @company_name$
```

**Important:** The symbol number returned by `SYM()` for a global variable is always a **negative integer**, distinguishing it from local variables.

### GB_ Naming Convention

In practice, many ERP systems drop the `@` in their naming convention and instead use a `GB_` prefix for readability. Variables declared in the global with names like `GB_H`, `GB_FNAME$`, `GB_ABORT$`, `GB_DEPOT_LOCN` are accessed as regular variables once the global is selected:

```kcml
REM GB_H is a numeric array in the global holding file handles
REM GB_H(234) = handle for file number 234
GOSUB 'KI_READ(GB_H(234), search_key$, 1, SYM(record$))
```

---

## Loading Libraries into the Global

`GB/START` uses `LOAD <n>array$()` — the library batch-load syntax — to load all library files:

```kcml
REM GB/START structure
: prog_dir$ = (ENV("PROGRAMS") == " " ? "D40" : ENV("PROGRAMS"))
: SELECT DISK <prog_dir$>         : REM Angle brackets = use variable as disk name
: lib_progs = 0
: RESTORE LINE 9000               : REM Reposition DATA read pointer to line 9000
: REPEAT
:   READ prog$
:   IF prog$ <> " " THEN DO
:     LIMITS T#0, prog$, q8, q8, q8, q9    : REM q9==1 = file exists
:     IF q9 == 1 THEN DO
:       IF STR(prog$, 7, 2) == "KI" AND $VERSION >= "05" THEN STR(prog$, 7, 2) = "K5"
:       MAT REDIM libraries$(++lib_progs) 8
:       libraries$(lib_progs) = prog$
:     END DO
:   END DO
: UNTIL prog$ == " "
: LOAD <lib_progs>libraries$()    : REM Load all libraries at once

09000 DATA "GB/libGN"
    : DATA "GB/libKI"
    : DATA "GB/libWI"
    : DATA "GB/libPF"
    : REM ... more libraries ...
09090 DATA " "                     : REM Sentinel value ends the list
```

Key points:
- `RESTORE LINE n` repositions the DATA pointer for subsequent READ statements
- `LIMITS T#0, prog$, ..., q9` — q9==1 = library file found (q9==2 = KDB file found, different)
- `$VERSION` is a string like `"05.00.00"` — compare with `>=` for version checks
- `LOAD <n>array$()` — loads n libraries from a string array all at once
- `SELECT DISK <var$>` — angle brackets around a variable name select it as the disk

## Starting a Global Partition

Globals are started at boot time with `kcml -g`:

```bash
# Start global partition in background (Unix)
HEAPINIT=512 export HEAPINIT
kcml -g PROGS/GLOBAL1 </dev/null >/tmp/gblog1 &
```

The global program itself must:
1. Declare all shared variables
2. Name itself with `DEFFN @PART`
3. Put itself to sleep with `$BREAK !`
4. Define subroutines below the sleep line

```kcml
REM Global partition program structure
COM @junk$1000, @lockvar = 99
INIT(HEX(FF)) @junk$
DEFFN @PART "TESTGBL"    : REM Name this global
$BREAK !                  : REM Sleep forever - subroutines only execute when called

REM Subroutines defined here are never called by the global itself
REM They are called by other partitions that SELECT @PART "TESTGBL"
DEFFN 'KI_READ(handle, key$, index, sym_rec)
: REM ... database read logic ...
: RETURN

DEFFN 'MESS_BOX(msg$, style)
: REM ... display message box ...
: RETURN
```

---

## Selecting a Global Partition

```kcml
SELECT @PART "TESTGBL"   : REM Connect to global named TESTGBL
```

After selection, all `GOSUB '` calls search the calling program first, then the global. This is transparent — programs call global subroutines the same way as local ones:

```kcml
REM These could be local or global subroutines — KCML checks local first
: GOSUB 'MESS_BOX("File not found", 0)
: GOSUB 'KI_READ(GB_H(51), part_key$, 1, SYM(pf_rec$))
: GOSUB 'SELSCREEN()
```

### Deselecting

```kcml
SELECT @PART " "    : REM Deselect current global
```

A global is automatically deselected when a `LOAD` is executed, unless the `KEEPSHARED` environment variable is set.

---

## Concurrent Access and Locking

Many KCML partitions can call into the global simultaneously. For operations that modify global variables, use advisory locking:

```kcml
@LOCK              : REM Acquire advisory lock on global
: @shared_counter += 1
: @last_user$ = user_name$
@UNLOCK            : REM Release lock
```

**Advisory** means: other partitions can still *read* global variables freely. The lock only blocks other partitions that also try to `@LOCK`. Always keep locked sections brief.

```kcml
REM Pattern: lock, read-modify-write, unlock
@LOCK
: GOSUB 'updte_global_record()
@UNLOCK
```

---

## Listing Global Content

From the workbench or immediate mode, prefix LIST commands with `@` to inspect the global:

```kcml
@LIST 1000,          : REM List program lines from 1000 onwards in global
@LIST T"KI_READ"     : REM Search global for subroutine text
@LIST '              : REM List all subroutine names in global
```

Lines from the global are prefixed with `@` in output, distinguishing them from local program lines.

---

## Libraries — Modern Replacement (KCML 6.0+)

Libraries replace global partitions for new development. They are compiled `.klib` files that are mapped into the foreground program's address space.

### Loading a Library

```kcml
LIBRARY ADD "CoreFunctions" = "../libraries/CoreFunctions.klib"
LIBRARY ADD "StockIO" = "libraries/StockIO.klib"
```

Libraries are searched in load order when resolving subroutine calls. Once loaded, calling a library subroutine is identical to calling a local one:

```kcml
: GOSUB 'KI_READ(handle, key$, 1, SYM(rec$))  : REM Could be in any library
```

### Library Variables (Persistent Across LOAD)

Variables declared with `PUBLIC DIM` in a library persist across `LOAD` statements, like `COM` variables:

```kcml
REM In library source:
PUBLIC DIM @shared_data(100)   : REM @ variables = shared data library
PUBLIC DIM file_handle(50)     : REM Regular library variable, persists across LOAD
```

### Library Constructor

If a library defines `'Constructor()`, it runs automatically when loaded:

```kcml
DEFSUB 'Constructor()
:   REM Initialize library state
:   file_handle() = ZER
:   db_connected = FALSE
: END SUB
```

### Building a Library

```bash
kc6 -o MyLib.klib -i BaseLib.klib myprog.src anotherprog.src
```

### Encapsulation

```kcml
PRIVATE DEFSUB 'internal_helper()    : REM Only visible within this library
PUBLIC DEFSUB 'exported_function()   : REM Visible to foreground and other libraries
PRIVATE DIM _MAX_RETRIES = 3         : REM Private constant
```

### Unloading

```kcml
LIBRARY REMOVE "CoreFunctions"   : REM Not recommended — library variables not destroyed
LIBRARY REMOVE ALL
```

---

## GB/INIT — Session Initialisation

Every user terminal runs `GB/INIT` at login. This program:
1. Attaches to the global: `SELECT @PART ENV("LIBRARY")` (defaults to "KOPEN3GB")
2. Declares all COM variables (shared within one session across all LOADs)
3. Opens all database files, populating `gb_h()` handles
4. Sets up user, date, and configuration state
5. LOADs the main menu program

```kcml
REM GB/INIT (abbreviated)
: COM a9$1
: IF ENV("LIBRARY") == " " THEN ENV("LIBRARY") = "KOPEN3GB"
: SELECT @PART ENV("LIBRARY")
: ERROR DO
:   PRINT HEX(0607); "GLOBAL memory not resident. Press RETURN"
:   KEYIN a9$
:   $END
: END DO
: REM All COM declarations follow...
: LOAD "PF/START" 1000
```

The `ERROR DO` block on `SELECT @PART` handles the case where the global hasn't been started — showing a clear error and exiting gracefully.

## COM Variable Layout (Session Memory)

`GB/INIT` declares the complete shared memory structure for a user session. All programs see these same COM variables because they persist across LOAD. Key groups:

### File Management
```kcml
COM gb_fname$(255)10    : REM Filenames (10 chars each, indexed by file slot)
COM gb_h(255)           : REM File handles (numeric, indexed by file slot)
COM gb_fdesc$(255)30    : REM File descriptions (for error messages)
COM gb_ftype$(255)1     : REM File type flag
COM gb_dir$(255)15      : REM File directory path
```
`gb_h(n)` is populated once at session open and used by all programs. Constants like `GB_H(51)` refer to specific file slots defined per module.

### Date and Time
```kcml
COM today$10            : REM Display date: "DD/MM/YYYY" (updated by global)
COM todayp$4            : REM Packed 4-byte date (for record field storage)
COM todayj              : REM Julian day integer
```
**Important:** `today$` (lowercase, 10-char dd/mm/yyyy) ≠ `$TODAY` (built-in, YYYYMMDD 8-char).

### Audit Field Definitions
```kcml
COM .user_create$       : REM Field variable: offset of user_create field in records
COM .user_amend$        : REM Field variable: offset of user_amend field
COM .date_create$       : REM Field variable: offset of date_create field
COM .date_amend$        : REM Field variable: offset of date_amend field
```
These are **field variable definitions** (dot-prefix) stored in COM. KI_WRITE/KI_REWRITE automatically write to `FLD(record$.user_amend$)` etc.

### KDB State
```kcml
COM ki_status           : REM Last operation status (0=ok, 1=not found, 12=locked...)
COM ki_dataptr$3        : REM Record pointer set by successful reads
COM ki_key$64           : REM Key returned by KI_READ_NEXT
COM ki_val(4)           : REM File stats from KI_INFO2
COM ki_ferr$256         : REM Work buffer for KI_INFO2 raw data
COM ki_lockby           : REM Partition holding a lock (when status=12)
COM ki_handle           : REM Working handle for current KI operation
```

### User and Security
```kcml
COM user_rec$1586       : REM Full user record
COM user_acs$(20)20     : REM User access level strings (20 modules)
COM usr1(20)            : REM Field start positions in user_rec$ per module
COM usr2(20)            : REM Field lengths in user_rec$ per module
COM user_dept$2         : REM User's department
COM user_stock_location : REM User's default stock location
COM u6$(20)1            : REM User access level per module (1 char: 1-9)
```
`U6$(1)` = access level for module 1. `U6$(8)` = the username.

### Window State
```kcml
COM wi_title$80         : REM Current window title
COM wi_in$1             : REM Input character from window
COM wi_current(9)       : REM Current highlighted item per window level
COM wi_top(9)           : REM Top visible item per window level
COM wi_close            : REM Flag: close all windows on next key
```

### Spool/Print
```kcml
COM sp_on$1             : REM "Y" = spool active
COM sp_name$80          : REM Spool output filename
COM sp_desc$30          : REM Spool description (for spool queue display)
COM sp_file$12          : REM Short spool filename
```

### Pack Format Field Variables
```kcml
COM .gb_pack_num        : REM Standard numeric pack format
COM .gb_pack_currency   : REM Currency pack format
COM .gb_pack_perc       : REM Percentage pack format
COM .gb_pack_time       : REM Time pack format
COM .gb_pack_bin3       : REM 3-byte binary integer pack format
```
These field variable definitions are set once in INIT and used globally for packing/unpacking record fields.

## Common Global Subroutines in ERP Systems

In the stock control suite source code, the global provides these services (via `GB_*` naming convention):

### Database I/O (KDB via Global)

**File management:**
```kcml
: GOSUB 'KI_OPEN(GB_H(id), GB_H(id), GB_FNAME$(id), "W")         : REM Open for read/write
: GOSUB 'KI_OPEN(GB_H(id), GB_H(id), filename$, "R")             : REM Open read-only
: GOSUB 'KI_CLOSE(GB_H(id))                                       : REM Close file
: GOSUB 'KI_CREATE(GB_H(id), GB_H(id), filename$, idx_sz, dat_sz, SYM(init$)) : REM Create new file
: GOSUB 'KI_INITIALISE(GB_H(id))                                  : REM Initialise after create
: GOSUB 'KI_UNLOCK_FILE(GB_H(id), 0)                              : REM Release file-level lock
: GOSUB 'KI_INFO2(GB_H(id))                                       : REM Get file statistics
```

**Record access:**
```kcml
: GOSUB 'KI_READ(GB_H(id), key$, index, SYM(record$))            : REM Read by key
: GOSUB 'KI_READ_HOLD(GB_H(id), key$, 1, SYM(record$))           : REM Read + lock record
: GOSUB 'KI_READ_HOLD_PTR(GB_H(id), dataptr$, SYM(record$))      : REM Read by pointer + lock
: GOSUB 'KI_WRITE(GB_H(id), SYM(record$))                        : REM Create new record
: GOSUB 'KI_REWRITE(GB_H(id), dataptr$, SYM(record$))            : REM Update existing record
: GOSUB 'KI_DELETE(GB_H(id), dataptr$)                            : REM Delete record by pointer
: GOSUB 'KI_UNLOCK(GB_H(id), dataptr$)                           : REM Release record lock
```

**Sequential access:**
```kcml
: GOSUB 'KI_START(GB_H(id), start_key$, direction)               : REM Position at key (1=fwd,-1=rev)
: GOSUB 'KI_START_BEG(GB_H(id), index)                           : REM Position at file start
: GOSUB 'KI_READ_NEXT(GB_H(id), 1, SYM(record$))                 : REM Read next record
```

**Error handling:**
```kcml
: GOSUB 'KI_FATAL_ERROR("Error message")                          : REM Unrecoverable — halts
: GOSUB 'KI_ERROR(SYM(msg$))                                      : REM Recoverable — sets msg$
```

**`KI_STATUS`** is set after every KDB operation:

| Value | Meaning |
|-------|---------|
| `0` | Success |
| `1` | Record not found |
| `2` | End of file (sequential read) |
| `5` | Index area full (on write) |
| `6` | Data area full (on write) |
| `12` | Record locked by another partition |

**`KI_LOCKBY`** — when `KI_STATUS == 12`, holds the partition number of the lock owner:
```kcml
: IF KI_STATUS == 12 THEN DO
:   CONVERT KI_LOCKBY TO Q6$, (###)
:   Q7$ = "Record locked by partition " & Q6$ & " - Retry?"
:   GOSUB 'LINPUT_LINE(Q7$, "Yes No", 1, 10, 5, 1, TRUE, " ")
: END DO
```

**`KI_VAL()`** — array populated by `KI_INFO2`:
```kcml
: GOSUB 'KI_INFO2(GB_H(id))
: record_count = KI_VAL(4)    : REM Total records in file
```

**`KI_DATAPTR$`** — set after a successful read; holds the record pointer used for rewrite/delete/unlock.

### File Reference Arrays
```kcml
GB_H(n)       : REM File handle/index for file n (numeric array in global)
GB_FNAME$(n)  : REM Native filename for file n (string array in global)
```

### Additional KDB Routines
```kcml
: GOSUB 'KI_READ_HOLD_NEXT(GB_H(id), path, SYM(rec$))   : REM Sequential read + lock
: GOSUB 'KI_READ_PTR(GB_H(id), dataptr$, SYM(rec$))     : REM Read by pointer (no lock)
: GOSUB 'KI_WRITE_PTR(GB_H(id), dataptr$, SYM(rec$))    : REM Write to existing pointer
: GOSUB 'KI_WRITE_LOCKED(GB_H(id), SYM(rec$))           : REM Write and keep lock
: GOSUB 'KI_VERIFY(GB_H(id), flag)                       : REM Verify file integrity
: GOSUB 'KI_REBUILD(GB_H(id), mode, filename$)           : REM Rebuild file index
: GOSUB 'KI_EXTEND(h, size, type, file$, flag)           : REM Extend file capacity
: GOSUB 'KI_DIR(key$, depth, key1$, filelen, SYM(arr$)) : REM Directory listing
: result = 'KI_FILE_FULL()                               : REM TRUE if last write was full
```

`KI_FILE_FULL()` is a DEFSUB that checks `KI_STATUS` for 5 or 6, shows an error using `GB_FDESC$(KI_HANDLE)` for the file name, and returns TRUE/FALSE.

### Audit Logging

`KI_WRITE` and `KI_REWRITE` automatically stamp audit fields on every record unless `KI_NOLOG = TRUE`:

```kcml
: KI_NOLOG = TRUE     : REM Suppress audit fields for this write
: GOSUB 'KI_WRITE(GB_H(id), SYM(rec$))
: KI_NOLOG = FALSE    : REM Re-enable audit logging

REM Fields written automatically when KI_NOLOG is FALSE:
REM FLD(rec$.USER_CREATE$) = U6$(8)    ← username (on create only)
REM FLD(rec$.USER_AMEND$) = U6$(8)     ← username (on every write)
REM FLD(rec$.DATE_CREATE$) = TODAYP$   ← packed date (on create only)
REM FLD(rec$.DATE_AMEND$) = TODAYP$    ← packed date (on every write)
```

`U6$(8)` is the current username. `TODAYP$` is today's date in 4-byte packed format.

### PANIC — Fatal Termination

```kcml
PANIC    : REM Terminates the program immediately with an error
```

Used by `KI_FATAL_ERROR` after showing the error message — there is no recovery from PANIC.

### UI Helpers
```kcml
: GOSUB 'MESS_BOX("Message text", style)    : REM Display a message box
: GOSUB 'MESSBOX_RETURN(msg$, style)         : REM Message box + wait for return
: GOSUB 'SELSCREEN()                         : REM Activate terminal output
: GOSUB 'SELPRINT()                          : REM Activate printer output
: GOSUB 'KEY_RETURN()                        : REM Wait for Return key
: GOSUB 'GB_WAIT()                           : REM Pause ~1 second
: GOSUB 'KEYSTR(var$, row, col, maxlen)      : REM Input string at screen position
: GOSUB 'GB_SCREEN_HEADER(title$)            : REM Draw standard screen header
```

### Terminal/Session Info
```kcml
GB_ABORT$      : REM The Escape/abort key character (usually Escape)
GB_DEPOT_LOCN  : REM Current user's depot/location number
U7$            : REM 2-char terminal ID suffix (COM variable, not global)
TODAY$         : REM Today's date string (YYYYMMDD) — global variable, not a function
TIME           : REM Current time string (HHMMSS) — global variable
```

Note: `TODAY$` and `TIME` in this codebase are **global variables** (populated by the global at startup/refresh), distinct from the `$TODAY` and `$TIME` language built-ins.

### Progress Window (Long Operations)
```kcml
: GOSUB 'KI_INFO2(GB_H(id))        : REM Get record count
: RUN_PERC() = ZER
: RUN_PERC(2) = KI_VAL(4)          : REM Set total (denominator)
: GB_COMPTITLE$ = "Printing Report" : REM Title for progress window
: GOSUB 'COMPLETED_WINDOW()         : REM Open progress window
: REPEAT
:   GOSUB 'KI_READ_NEXT(GB_H(id), 1, SYM(rec$))
:   IF KI_STATUS == 0 THEN DO
:     GOSUB 'SELSCREEN()            : REM Switch to screen to update progress
:     GOSUB 'UPDATE_COMPLETED()     : REM Increment progress bar
:     GOSUB 'SELPRINT()             : REM Switch back to printer for output
:     REM ... print the record ...
:   END DO
: UNTIL KI_STATUS <> 0
: GOSUB 'SELSCREEN()
: WINDOW CLOSE #1                   : REM Close progress window
```

### Spool File Pattern (Printed Reports)
```kcml
: IF SP_ON$ == "Y" THEN GOSUB 'SET_SPOOLFILE()
: PAGE = 0 : LN = 99
: REPEAT
:   GOSUB 'KI_READ_NEXT(GB_H(id), 1, SYM(rec$))
:   IF KI_STATUS == 0 THEN DO
:     IF ++LN > 60 THEN DO           : REM New page when line count exceeded
:       PRINT HEX(0C); header$; TAB(99); time$; "  "; date$; "  Page"; ++PAGE
:       PRINT HEX(0E); TAB(27 - LEN(title$)/2); "****  "; title$; "  ****"
:       PRINT
:       LN = 1
:     END DO
:     PRINTUSING image$, fields...
:   END DO
: UNTIL KI_STATUS <> 0
: IF SP_ON$ == "Y" THEN DO
:   IF PAGE == 0 THEN GOSUB 'DELETE_SPOOLFILE()    : REM Nothing printed
:   ELSE DO
:     SP_DESC$ = report_name$
:     GOSUB 'SAVE_SPOOLFILE()
:   END DO
: END DO
: WINDOW CLOSE #1
```

---

## SYM() — Variable Pointers

`SYM()` returns the symbol index of a variable, allowing it to be passed generically into subroutines (particularly useful for passing records into database routines without copying the data):

```kcml
REM Pass a record buffer by reference to a global routine
: GOSUB 'KI_READ(GB_H(51), part_key$, 1, SYM(pf_rec$))

REM The global subroutine receives it as a symbol and accesses via SYM(*sym)$
DEFFN 'KI_READ(handle, key$, index, rec_sym)
: REM Use SYM(*rec_sym)$ to access the variable
: SYM(*rec_sym)$ = fetched_data$
: RETURN
```

Global variable symbol numbers are always **negative**; local variable symbols are always **positive**.

---

## $PSTAT — Partition Status

`$PSTAT` holds 48 bytes of partition information. Key bytes for background/global work:

```kcml
REM Byte 16: terminal attachment status
IF STR($PSTAT(#PART), 16, 1) == "D" THEN ...  : REM "D" = detached from terminal
IF STR($PSTAT(#PART), 16, 1) == "W" THEN ...  : REM "W" = detached, waiting on I/O
IF STR($PSTAT(#PART), 16, 1) == "A" THEN ...  : REM "A" = attached to terminal
```

Setting the status display (common in all programs):
```kcml
$PSTAT = "S/MANG" & U7$    : REM Sets display like "S/MANG01"
```

---

## Background Partitions (Unix Only)

In addition to globals, KCML supports background partitions for multi-tasking from one terminal:

```kcml
$RELEASE LOAD RUN "BACK1"   : REM Clone current partition and run BACK1 in background
$RELEASE TERMINAL            : REM Switch to next waiting background partition
$RELEASE TERMINAL TO 253     : REM Switch to specific partition number
$RELEASE KEY = 20            : REM F20 becomes a hot key to switch partitions
```

Each `$END` automatically releases to the next waiting background partition. Only relevant on Unix — these statements error on Windows.

---

## Key Points for ERP System Analysis

When reading ERP source code that uses a global partition:

1. **Any `GOSUB '` call not defined locally is in the global** — e.g., `'KI_READ`, `'MESS_BOX`, `'SELSCREEN`
2. **`GB_*` variables are global arrays** — `GB_H(n)` is a file handle array, `GB_FNAME$(n)` is filename array
3. **`KI_STATUS` is a global variable** — always check it after database operations
4. **`U7$`** is a COM variable (not global) holding the 2-char terminal ID
5. **`SELECT @PART` is called at program start** — usually via `GOSUB 'SELSCREEN()` or a standard library open sequence
6. **Libraries in 6.0+ work identically from the caller's perspective** — the `LIBRARY ADD` replaces the `SELECT @PART`

---

## KISAM Direct File Access (Standalone Scripts)

KISAM is the schema-less KCML file system — the underlying store for all KDB files, accessible without going through the KDB catalog/SQL layer. This is the correct approach for standalone `kcml -p` scripts that need to read ERP data files directly.

### How Connections Work in KCML 6.x

When any KCML script starts, **connection 1 is automatically created as a KISAM (schema-less) connection**. No `KI_ALLOC_CONNECT` or `KI_CONNECT` call is needed.

- Connection 1 = KISAM (direct file access, no catalog)
- Connection 2 = KDB LIVE (catalog-based, requires `KI_CONNECT`)

For reading KISAM files directly, always use connection 1.

### KI_OPEN Parameter Change in KCML 6.x

**IMPORTANT:** The `libKI` wrapper source (in `kcml_source/GB/libKI`) uses the old 4-parameter form:
```kcml
CALL KI_OPEN KI_HANDLE, KI_STREAM, KI_FILE$, KI_MODE$ TO ki_status
```
This was valid in older KCML. In **KCML 6.x**, `KI_OPEN` takes **3 parameters** (no stream):
```kcml
CALL KI_OPEN handle, file$, mode$ TO ki_status
```
Using the 4-parameter form causes an **S24 "Stack frame problem" panic** that bypasses `ERROR DO` and terminates KCML immediately.

### Working KISAM Read Pattern (Verified by Execution — KCML 06.00.88)

```kcml
: DIM ki_status, handle, ki_sym, ki_dataptr$6, ki_key$64, rec$512, count
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: PRINT "ALLOC_HANDLE: "; ki_status
: IF ki_status <> 0 THEN $END
: CALL KI_OPEN handle, "/user1/kopen3/sop/OEHDR01", "R" TO ki_status
: PRINT "OPEN: "; ki_status
: IF ki_status <> 0 THEN $END
: CALL KI_START_BEG handle, 1 TO ki_status
: PRINT "START_BEG: "; ki_status
: IF ki_status <> 0 THEN $END
: ki_sym = SYM(rec$)
: count = 0
: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status == 0 THEN DO
:     count++
:     PRINT "--- Record "; count; " ---"
:     PRINT "Key: ["; STR(ki_key$, 1, 20); "]"
:     PRINT "Rec: ["; STR(rec$, 1, 60); "]"
:   END DO
: UNTIL ki_status <> 0 OR count >= 3
: PRINT "Read "; count; " records, final status="; ki_status
: CALL KI_CLOSE handle TO ki_status
: $END
```

Key rules:
- `KI_ALLOC_HANDLE 0, 1` — auto-allocate (0) on KISAM connection (1). Returns numeric handle.
- `KI_OPEN handle, file$, mode$` — 3 params only in KCML 6.x. Full absolute path or relative to current SELECT DISK.
- `ki_sym = SYM(rec$)` — pre-assign to a variable before passing to `KI_READ_NEXT`. Do not pass `SYM(rec$)` inline.
- `ki_dataptr$` must be declared as **6 bytes** (`DIM ki_dataptr$6`), not 3.
- Status 2 = EOF (normal end of sequential read), 0 = success, 1 = not found.

### KI_START — Positioning by Key (KCML 6.x)

```kcml
: CALL KI_START handle, key$, path TO ki_status
```

**Parameter order: `handle, key$, path`** — key comes before path in KCML 6.x.

The `libKI` wrapper calls `CALL KI_START handle, path, key$` (path before key) — this is the old order and causes an S24 panic in KCML 6.x. Use `key$` before `path`.

After `KI_START`, a `KI_READ_NEXT` returns the first record with key >= the supplied key. Always check the returned key matches exactly if you want a specific record.

```kcml
: DIM search_key$20, read_ok
: search_key$ = "016519"
: CALL KI_START handle, search_key$, 1 TO ki_status
: ki_sym = SYM(rec$)
: CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
: IF ki_status == 0 THEN read_ok = 1
: IF read_ok == 0 THEN PRINT "Not found" : CALL KI_CLOSE handle TO ki_status : $END
: IF STR(ki_key$, 1, 20) <> search_key$ THEN read_ok = 0
: IF read_ok == 0 THEN PRINT "Not found" : CALL KI_CLOSE handle TO ki_status : $END
```

### Conditional $END Pattern in KCML

**Critical**: `IF condition THEN action : $END` makes `$END` **always execute** — the `:` returns to the top level. Only one statement is bound to `THEN`.

Wrong:
```kcml
: IF ki_status <> 0 THEN PRINT "<error>" : $END   ← $END always fires
```

Correct — use separate IF lines:
```kcml
: IF ki_status <> 0 THEN PRINT "<error>"
: IF ki_status <> 0 THEN $END
```

When `KI_CLOSE` appears between the error print and `$END`, use a flag variable to avoid `KI_CLOSE` resetting `ki_status` to 0:
```kcml
: CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
: IF ki_status == 0 THEN read_ok = 1
: IF read_ok == 0 THEN PRINT "<error>Not found</error>"
: IF read_ok == 0 THEN CALL KI_CLOSE handle TO ki_status
: IF read_ok == 0 THEN $END   ← ki_status now 0 from KI_CLOSE, so check read_ok not ki_status
```

### S24 Panic — Cannot Be Caught

The KCML S24 panic ("Stack frame problem, possibly wrong parameters supplied to user function") is caused by calling a KI_ native function (UFN) with the wrong parameter count or type. It:
- **Cannot be caught** by `ERROR DO` — it bypasses all error handlers
- Writes a panic XML file to `/home/interpartuk/panic<pid>.xml`
- Terminates KCML immediately

Common causes:
- Using 4-param `KI_OPEN` (handle, stream, file$, mode$) in KCML 6.x — use 3-param form
- Passing `SYM(rec$)` inline to `KI_READ_NEXT` instead of pre-assigning

### Blank Lines Terminate KCML -p Scripts

In `kcml -p` (script mode), **a blank line terminates script execution immediately** — no error, no warning. Code after the blank line simply does not run.

Rules for `-p` scripts:
- Never use blank lines anywhere in the script
- Use `: REM comment text` for visual spacing between sections
- Every comment line must have the `: ` prefix — a bare `REM` line (no `: `) also terminates the script

---

---

## KCML CGI — Rules Verified by Testing

### Apache setup

`runkcml` must use `$DOCUMENT_ROOT$PATH_INFO`, **not** `$PATH_TRANSLATED`:

```sh
#!/bin/sh
/usr/lib/kcml/kcml -p $DOCUMENT_ROOT$PATH_INFO
```

`$PATH_TRANSLATED` is either unset or wrong in Apache's CGI Action context on this server.

### Blank line HTTP header separator

Use bare `PRINT` (no argument) to output the blank line that separates HTTP headers from body. **`PRINT ""`** does not output a blank line — it appears to be a no-op for the blank line.

```kcml
: PRINT "Content-type: text/xml"
: PRINT
: REM body starts here
```

### `&` string concatenation in PRINT — rules

`&` (string concatenation) works in `PRINT` for single-argument functions like `HEX()`:
```kcml
: PRINT "<?xml version="; HEX(22); "1.0"; HEX(22); "?>"   ← safe, use ; not &
```

**`&` breaks when the operand is a multi-argument function** like `STR(var, start, len)`. KCML's parser confuses the commas inside the function call with PRINT's argument separator. Always use `;` in PRINT:

```kcml
: PRINT "  <key>"; STR(ki_key$, 1, 20); "</key>"     ← correct
: PRINT "  <key>" & STR(ki_key$, 1, 20) & "</key>"   ← WRONG — syntax error
```

### `&` inside a THEN clause

In `IF cond THEN PRINT "str" & var`, KCML ends the THEN clause after the first closing `"`. The `& var` is then treated as a new (invalid) statement. Only use simple string literals in THEN-clause PRINT:

```kcml
: IF ki_status <> 0 THEN PRINT "<error>open failed</error>"   ← correct
: IF ki_status <> 0 THEN PRINT "err: " & msg$                 ← WRONG
```

---

## See Also

- [com-chaining.md](com-chaining.md) — COM variables, LOAD, program structure
- [subroutines.md](subroutines.md) — DEFSUB, DEFFN, GOSUB calling conventions
- [screen-io.md](screen-io.md) — $PSTAT, terminal control
- [arrays-variables.md](arrays-variables.md) — DIM, MAT, variable types
