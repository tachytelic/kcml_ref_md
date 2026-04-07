# KCML Environment Variables

> Reference for the environment variables recognised by the KCML runtime. Where a `$OPTIONS` byte equivalent exists, it is noted.

Many variables also correspond to bytes in `$OPTIONS`, `$OPTIONS LIST`, or `$OPTIONS RUN`. Setting an environment variable before starting KCML is equivalent to setting the corresponding options byte.

---

## Quick reference

| Variable | Platform | Purpose |
|----------|----------|---------|
| `_ANSWERBACK` | Unix | Set by kclient on login; used by `selfid` to identify terminal |
| `_KTERM` | Unix | Set by kclient on login; KTERM type + client version |
| `ATREPLACE` | All | Replacement for `@` prefix on global variables when importing ASCII source |
| `BCDPART` | All | Maximum partition number KCML may allocate (default 1024) |
| `BREAK30` | All | Restore KCML pre-3.20 `$BREAK` timing (50 ticks, ~1s) |
| `COMPAT2200` | All | LIST compatibility: suppress automatic statement recreation |
| `COMPAT30` | All | Warn on statements not supported in KCML 3.0 |
| `COMPAT32` | All | Warn on statements not supported in KCML 3.2x |
| `COMPAT40` | All | Generate backward-compatible code for KCML < 5.00 |
| `CURCHAR` | All | Currency symbol (replaces `$` in PRINTUSING images) |
| `CWD` | All | Initial working directory for KCML |
| `DCINTERNAL` | All | Workaround for DATA LOAD/SAVE DC overflow bug |
| `DOSELECT` | Unix | Use `select()` syscall before terminal reads/writes |
| `DOTCHAR` | All | Decimal point character in PRINTUSING (e.g. `,` for European format) |
| `DUMPCORE` | Unix | Create a core file on abnormal KCML termination |
| `EDITOR` | Unix | Native text editor for the KCML `EDIT` command |
| `FORCETERM` | All | Override value returned by `#TERM` function |
| `FORCEWINDOWS` | Unix | Force KCML windowing sequences regardless of terminal type |
| `HALTCHAR` | Unix | Override HALT key (hex ASCII of desired char, e.g. `1A` = Ctrl+Z) |
| `HEAPINIT` | All | Initial heap allocation in kilobytes (for memory-mapped globals) |
| `HELPEXTENSION` | All | File extension appended to `$HELP` URLs (default `.html`) |
| `HELPSERVER` | All | Location of Windows Help file or HTML help directory / URL |
| `HOME` | All | Initial directory for the Workbench file browser |
| `HTTP_PROXY` | All | HTTP proxy for SOAP requests: `proxyhost:port` |
| `KCML_HEAP_SIZE` | All | Maximum KCML heap size in MB (default 64) |
| `KCML_ID` | All | Override value returned by `#ID` function |
| `KCML_CLEAR_LOCALS` | All | Aggressive recovery of local symbol space |
| `KCMLINI` | All | Path to editor preferences file (obsolete in KCML 6.0+) |
| `KCMLPATH` | All | Directory containing `berror.d` and `TERMINFO` |
| `KEEPSHARED` | All | Prevent global partitions being de-selected on `LOAD` |
| `KINDENT` | All | Indentation spaces for LIST (default 4) |
| `KLANG` | All | Default language byte for multilingual strings |
| `KLOGKEY` | All | 4-char key for journal shared memory (default `KLOG`) |
| `KTERM` | Unix | Terminal type (takes precedence over `TERM`) |
| `LINELEN` | All | Maximum program line length (0 = disabled) |
| `MALLOCSPACE` | Unix | Space (KB) reserved at start of data segment for `malloc()` |
| `NOENDDOERROR` | All | Suppress unmatched `DO...END DO` errors at resolve time |
| `NOHALT` | All | Disable the HALT key |
| `NOGLOBMAP` | Unix | Disable pre-mapping of existing global partitions |
| `NORESET` | All | Disable the RESET key |
| `OPTIONS_nn` | All | Preset byte `nn` of `$OPTIONS` (hex value string) |
| `OPTIONS_LIST_nn` | All | Preset byte `nn` of `$OPTIONS LIST` |
| `OPTIONS_RUN_nn` | All | Preset byte `nn` of `$OPTIONS RUN` |
| `PANICDIR` | All | Directory for `PANIC` dump files |
| `PATH` | Unix | Search path for OS commands called by KCML |
| `PSEUDOTTY` | Unix | Enable pseudo-TTY for interactive shell commands via Connection Manager |
| `R7FIX` | All | Restore KCML 2.0 behaviour for old Rev7 programs |
| `SCREENDIR` | Unix | Directory for screen dump files (on SIGUSR2) |
| `SEPCHAR` | All | Digit-group separator in PRINTUSING (e.g. `.` for European format) |
| `SHELL` | Unix | Override shell used by the `SHELL` statement |
| `SOAPSTART` | All | Program name to run when acting as a SOAP server |
| `SPACE` | All | Override value returned by `SPACE`, `SPACEF`, etc. functions |
| `SPACEK` | All | Override value returned by `SPACEK` function |
| `SPOOL` | Unix | Lock file used by the UNIX spooler for the main system printer |
| `START` | All | Program to `LOAD RUN` automatically when KCML starts |
| `SYSTEMID` | All | KCML instance number (0–65535) for multi-instance ASP systems |
| `TERM` | Unix | Terminal type (used if `KTERM` is not set) |
| `TERMFILE` | All | Path to the KCML terminal allocation file |
| `TOMDIR` | All | Enable directory-style program storage (space → `/`) |
| `TOMFILE` | All | Enable filename case change when directory already exists |
| `UNIXPROGS` | Unix | Load/save programs as native OS files (not platter images) |
| `USEMALLOC` | Unix | Use standard `malloc()` instead of KCML's private allocator |
| `USING-UTF8` | All | Treat all strings and DB columns as UTF-8 encoded |
| `WORKSPACE` | All | Directory for FSORT temporary work files (default `/tmp`) |

---

## Selected variable details

### ATREPLACE
Replacement prefix for `@` (global variable marker) when importing ASCII source from environments that use a different prefix. Byte 28 of `$OPTIONS RUN` can also set this; `HEX(00)` in that byte enables `ATREPLACE`.
```sh
ATREPLACE=Glob_ ; export ATREPLACE
```

### BCDPART
Maximum partition number KCML may allocate for background partitions (default 1024; 512 on NT for KCML 5.03). Supply a range for non-standard starting values:
```sh
BCDPART=1024 ; export BCDPART
BCDPART="100,255" ; export BCDPART
```

### CURCHAR / DOTCHAR / SEPCHAR
Formatting characters for `PRINTUSING`:
```sh
CURCHAR='FF' ; export CURCHAR          # currency symbol
DOTCHAR=',' ; export DOTCHAR           # decimal point (European)
SEPCHAR='.' ; export SEPCHAR           # digit separator (European)
```

### HTTP_PROXY
Proxy for SOAP/HTTP requests. Format: `[user[:password]@]host[:port]`
```sh
HTTP_PROXY=proxy.bigco.com:8080 ; export HTTP_PROXY
```

### KCML_HEAP_SIZE
Maximum heap in MB (default 64):
```sh
KCML_HEAP_SIZE=128 ; export KCML_HEAP_SIZE
```

### OPTIONS_nn / OPTIONS_LIST_nn / OPTIONS_RUN_nn
Preset individual bytes at startup:
```sh
OPTIONS_38="01" ; export OPTIONS_38          # force error on un-DIM'd variables
OPTIONS_LIST_20="02" ; export OPTIONS_LIST_20 # 2-space indentation
OPTIONS_RUN_40="06" ; export OPTIONS_RUN_40   # load/save ASCII with .src extension
```

### START
Auto-run a program at KCML startup:
```sh
START=DEVICES ; export START
```

### WORKSPACE
Directory for FSORT temporary files:
```sh
WORKSPACE=/user1/tmpdir ; export WORKSPACE
```

---

## Notes

- Environment variables affecting `$OPTIONS`, `$OPTIONS LIST`, or `$OPTIONS RUN` must generally be set **before** KCML is started; changing them after startup has no effect.
- On Unix, use `export VAR=value` (Bourne shell) or `setenv VAR value` (csh).
- `TERMFILE` should be the same for all users on a system — set it in `/etc/profile`. Do not edit it while KCML is running (editors may change the inode, breaking `#ID` and global partition access).

## See Also

- `ENV(` — read an environment variable from within KCML
- `$OPTIONS` / `$OPTIONS RUN` / `$OPTIONS LIST` — runtime option byte strings
- `FSORT BU` — uses `WORKSPACE`
- `#ID` — uses `KCML_ID` / `TERMFILE`
