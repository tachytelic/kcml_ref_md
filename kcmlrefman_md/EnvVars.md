# KCML Environment Variables

> Reference for the environment variables recognised by the KCML runtime. Where a `$OPTIONS` byte equivalent exists, it is noted.

Many variables also correspond to bytes in `$OPTIONS`, `$OPTIONS LIST`, or `$OPTIONS RUN`. Setting an environment variable before starting KCML is equivalent to setting the corresponding options byte. Variables that affect `$OPTIONS` bytes must be set **before** KCML starts; changing them after startup has no effect.

---

## Quick Reference

| Variable | Platform | Purpose |
|----------|----------|---------|
| `_ANSWERBACK` | Unix | Set by kclient on login; used by `selfid` to identify terminal |
| `_KTERM` | Unix | Set by kclient on login; KTERM type + client version |
| `ATREPLACE` | All | Replacement for `@` prefix on global variables when importing ASCII source |
| `BCDPART` | All | Maximum partition number KCML may allocate (default 1024); background partitions allocated downward from this value |
| `BREAK30` | All | Restore KCML pre-3.20 `$BREAK` timing (50 ticks, ~1s) |
| `COMPAT2200` | All | LIST compatibility: suppress automatic statement recreation for BASIC-2 programs |
| `COMPATNIAKWA` | All | Additional listing compatibility; works with COMPAT2200 |
| `COMPAT30` | All | Warn on statements not supported in KCML 3.0 |
| `COMPAT32` | All | Warn on statements not supported in KCML 3.2x |
| `COMPAT40` | All | Generate backward-compatible code for KCML < 5.00 |
| `COREONBERROR` | All | Force core file creation on every PANIC |
| `CURCHAR` | All | Currency symbol (replaces `$` in PRINTUSING images) |
| `CWD` | All | Initial working directory for KCML |
| `DCINTERNAL` | All | Workaround for DATA LOAD/SAVE DC overflow bug |
| `DOSELECT` | Unix | Use `select()` syscall before terminal reads/writes |
| `DOTCHAR` | All | Decimal point character in PRINTUSING (e.g. `,` for European format) |
| `DUMPCORE` | Unix | Create a core file on abnormal KCML termination |
| `EDITOR` | Unix | Native text editor for the KCML `EDIT` command |
| `FORCETERM` | All | Override value returned by `#TERM` (1–512) |
| `FORCEWINDOWS` | Unix | Force KCML windowing sequences regardless of terminal type |
| `HALTCHAR` | Unix | Override HALT key (hex ASCII of desired char, e.g. `1A` = Ctrl+Z) |
| `HEAPINIT` | All | Initial heap allocation in kilobytes (for memory-mapped globals) |
| `HELPEXTENSION` | All | File extension appended to `$HELP` URLs (default `.html`) |
| `HELPSERVER` | All | Location of Windows Help file or HTML help directory / URL |
| `HOME` | All | Initial directory for the Workbench file browser |
| `HTTP_PROXY` | All | HTTP proxy for SOAP requests: `[user[:password]@]host[:port]` |
| `KBIN` | All | Directory containing `kmake`-generated files |
| `KCACHE` | All | Directory holding cached data tables |
| `KCMLDIR` | All | Read-only: absolute pathname of the KCML executable directory |
| `KCMLINI` | All | Path to editor preferences file (obsolete in KCML 6.0+) |
| `KCMLPATH` | All | Directory containing `berror.d` and `TERMINFO` |
| `KCML_ALLOW_SSL_V3` | Windows | Permit SSLv3 for backward compatibility (not recommended) |
| `KCML_ALT_KCML` | All | Path to alternative KCML for loading existing binary programs (6.20+) |
| `KCML_ALT_SRCDIR` | All | Alternative directory for `kmake` source file lookup |
| `KCML_BLOBSYM` | All | Expand BLOBSYM from 6 to 8 bytes for very large SYM values |
| `KCML_BROWSER_SCALE` | All | Scale factor (%) for browser form shrinking |
| `KCML_CALLSTAT_DIR` | All | Directory for Call Statistics results (default `$KBIN`) |
| `KCML_CHECK_TRUNCATED` | All (7.15+) | Print warning + PANIC CONTINUE when a `/`-prefixed string is truncated |
| `KCML_CLEAR_LOCALS` | All (6.20 only) | Aggressive recovery of local symbol space |
| `KCML_COVERAGE_DIR` | All | Directory for Code Coverage Analysis results (default `$KBIN`) |
| `KCML_DUAL_BINARIES_ALT_KCML` | All | Save dual-format binaries for both current and alternate KCML |
| `KCML_EXTENDED_PACK` | All | Replace `NUM(13,2)` / `UNUM(13,2)+` pack formats with V+/V- |
| `KCML_FNUSE_DIR` | All | Directory for Function Usage analysis results |
| `KCML_HEAP_PAGECHECK` | All | Enable 4 KB guard-page heap (memory boundary violation detection; high overhead) |
| `KCML_HEAP_SIZE` | Linux/AIX/HP-UX/Solaris | Maximum heap in MB (default 64; 128 in 6.40+) |
| `KCML_ID` | All | Override value returned by `#ID` function |
| `KCML_JSON_BOOL` | All | Serialize booleans as JSON `true`/`false` rather than 0/1 |
| `KCML_KAR_BUNDLE` | AIX | Path to KCML library archive |
| `KCML_KAR_BUNDLE_ALL` | All | Path to KCML library archive (cross-platform) |
| `KCML_LOG_SIZE` | All | Memory (MB) reserved for performance logging (default 256) |
| `KCML_MIN_SSL_PROTOCOL` | All | Minimum TLS version: `TLS`, `TLSv1`, `TLSv1_1`, `TLSv1_2` |
| `KCML_NOLOGIN` | All | Block user logins during maintenance |
| `KCML_NO_TERMFILE` | All | Ignore `$TERMFILE`; allocate `#TERM` from lowest unused value |
| `KCML_OIDC_SUBJECT` | All | OIDC subject claim |
| `KCML_OPENSSL_DIR` | All | Alternative directory for `libopenssl.so` / `libcrypto.so` |
| `KCML_OPENSSL_LOG` | All | File for OpenSSL library usage logging (development/debug) |
| `KCML_PANIC_CONF` | All | Panic configuration file name (default `panconf.xml` in KCML directory) |
| `KCML_PSTAT_SIZE` | All | Increase `$PSTAT` area beyond 1024 partitions/terminals |
| `KCML_RECORD_DIR` | All | Enable KCML-KClient data recording for headless tests |
| `KCML_REDUCTION` | All | Reduce JSON volume sent to browser client (in development) |
| `KCML_RETREAT_DISABLE` | All | Disable retreating code on `$SPACE` (diagnostic aid) |
| `KCML_SAVE_MINDIFF` | All | Suppress case/indentation-only changes when saving ASCII source |
| `KCML_SAVE_RELOAD` | All | Reload file after save to reflect removed changes (experimental; needs `KCML_SAVE_MINDIFF`) |
| `KCML_SESSION_UUID_PARENT` | All | Parent session UUID set by KCML when spawning a child process |
| `KCML_SHIM_LOG_PATH` | All | Logging directory for shim processes |
| `KCML_SHIM_PING_TIME` | All | Ping interval for shim client to verify KCML app existence |
| `KCML_SOAP_LIC` | All | Restrict SOAP server instances to prevent licence exhaustion (`0` = use foreground licence only) |
| `KCML_SOAP_LOCK` | All | Prevent SOAP server startup |
| `KCML_SSL_CIPHER_LIST` | All | SSL ciphers in OpenSSL format |
| `KCML_TERM_LIC` | All (6.20+) | Limit concurrent licences per terminal (first 4 sessions = 1 licence) |
| `KCML_TRACK_PTR_DELETE` | All | Track use-after-free conditions (`2` = include full stack trace) |
| `KCML_TRANSLATION_LOG` | All | Directory for translation log files |
| `KCML_TRANSLATION_PATH` | All | Directory for translation files |
| `KC_CHECK_TRANSLATION_MISMATCH` | All | Check for translation mismatch at compile time |
| `KDB_DATA_BRIDGE` | All | Path to `.so` file handling data bridge push events |
| `KDB_DATA_BRIDGE_JSON` | All | Path to JSON output file for data bridge |
| `KDB_LOW_PRIORITY` | All | Allow tables to open in exclusive mode without blocking EOD |
| `KDB_ODBC_LOADLIB` | All | Pathname of application library defining `odbc()` for Oracle/PostgreSQL |
| `KDB_RECORD_LOCK` | All | Use file record locking instead of lock bytes within table |
| `KDB_SERVER` | All | KDB database server: `host:port` |
| `KDB_SERVER_CACHE` | All | Enable read-ahead caching for `KI_READ_NEXT` on application server |
| `KDB_SERVER_DIR` | All | Working directory for relative path names on KDB server |
| `KEEPSHARED` | All | Prevent global partitions being de-selected on `LOAD` |
| `KINDENT` | All | Indentation spaces for LIST (default 4) |
| `KLANG` | All | Default language byte for multilingual strings |
| `KLOGKEY` | All | 4-char key for journal shared memory (default `KLOG`) |
| `KPLIC_PSTAT_SIZE` | All | Increase Remote Licence Daemon KPrint licence table area |
| `KSSL_CLIENT_CERT` | All | SSL certificate path when KCML acts as SSL client |
| `KSSL_SERVER_CERT` | All | SSL certificate path when KCML acts as SSL server |
| `KTERM` | Unix | Terminal type (takes precedence over `TERM`) |
| `LINELEN` | All | Maximum program line length (0 = disabled) |
| `LOGNAME` | All | Read-only: user account name for the running process |
| `MALLOCSPACE` | Unix | Space (KB) reserved at start of data segment for `malloc()` |
| `NOENDDOERROR` | All | Suppress unmatched `DO...END DO` errors at resolve time |
| `NOGLOBMAP` | Unix | Disable pre-mapping of existing global partitions |
| `NOHALT` | All | Disable the HALT key |
| `NOPROG` | All | Block programming commands and program editing |
| `NORESET` | All | Disable the RESET key |
| `OPTIONS_nn` | All | Preset byte `nn` of `$OPTIONS` (two-digit hex string) |
| `OPTIONS_LIST_nn` | All | Preset byte `nn` of `$OPTIONS LIST` |
| `OPTIONS_RUN_nn` | All | Preset byte `nn` of `$OPTIONS RUN` |
| `PANICDIR` | All | Directory for `PANIC` dump files |
| `PATH` | Unix | Search path for OS commands called by KCML |
| `PROGRAMS` | All | Path for program location in certain contexts |
| `PSEUDOTTY` | Unix | Enable pseudo-TTY for interactive shell commands via Connection Manager |
| `R7FIX` | All | Restore KCML 2.0 behaviour for old Rev7 programs |
| `SCREENDIR` | Unix | Directory for screen dump files (on SIGUSR2) |
| `SEPCHAR` | All | Digit-group separator in PRINTUSING (e.g. `.` for European format) |
| `SERVER_HTTP_URI` | All | URI prefix for HTTP URL construction (`http:` or `https:`) |
| `SERVER_NAME` | All | Server name for client connection to application |
| `SERVER_PORT` | All | Network port number for service connections |
| `SERVICE` | All | Read-only: service name operating under Connection Manager |
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
| `UMASK` | Unix | File creation mode mask (e.g. `007`); Windows 7.04+: `001` enables ACL inheritance |
| `UNIXPROGS` | Unix | Load/save programs as native OS files (not platter images) |
| `USEMALLOC` | Unix | Use standard `malloc()` instead of KCML's private allocator |
| `USING_UTF8` | All | Treat all strings and DB columns as UTF-8 encoded |
| `WORKSPACE` | All | Directory for FSORT temporary work files (default `/tmp`) |

---

## Selected Variable Details

### ATREPLACE
Replacement prefix for `@` (global variable marker) when importing ASCII source from environments that use a different prefix. Byte 28 of `$OPTIONS RUN` can also set this; `HEX(00)` in that byte enables `ATREPLACE`.
```sh
ATREPLACE=Glob_ ; export ATREPLACE
```

### BCDPART
Controls the maximum partition number KCML may allocate. Background partitions are allocated **downward** from this value (default 1024; 254 on NT). This is not a fixed partition number assignment — it is a ceiling for dynamic allocation. Supply a range for non-standard bounds:
```sh
BCDPART=1024 ; export BCDPART
BCDPART="100,255" ; export BCDPART

# Tie to KCML_PSTAT_SIZE when expanding beyond defaults:
KCML_PSTAT_SIZE=4096 ; export KCML_PSTAT_SIZE
BCDPART=$KCML_PSTAT_SIZE ; export BCDPART
```

### CURCHAR / DOTCHAR / SEPCHAR
Formatting characters for `PRINTUSING`:
```sh
CURCHAR='FF' ; export CURCHAR          # currency symbol
DOTCHAR=',' ; export DOTCHAR           # decimal point (European)
SEPCHAR='.' ; export SEPCHAR           # digit separator (European)
```

### HEAPINIT
Initial heap allocation in kilobytes for memory-mapped global partitions. Increase if memory allocation fails at startup:
```sh
HEAPINIT=2048 ; export HEAPINIT
```

### HELPSERVER
Help file or directory for `$HELP` and form Help buttons. Three modes:

- **Windows Help:** set `$OPTIONS RUN` byte 41 bit `HEX(10)`, point to `.hlp` file
- **HTML directory:** set byte 41 to `HEX(0C)`, point to local directory
- **Web server:** set byte 41 to `HEX(0C)`, point to URL
```sh
ENV("HELPSERVER")="C:\\HelpFiles"
ENV("HELPSERVER")="http://www.kerridge.com"
```

### HTTP_PROXY
Proxy for SOAP/HTTP requests:
```sh
HTTP_PROXY=proxy.bigco.com:8080 ; export HTTP_PROXY
```

### KCML_HEAP_SIZE
Maximum heap in MB (default 64; 128 in 6.40+):
```sh
KCML_HEAP_SIZE=128 ; export KCML_HEAP_SIZE
```

### KCML_PSTAT_SIZE
Increases the `$PSTAT` area, raising the maximum number of concurrently active partitions and terminals above the default of 1024. Must be set identically in `kconf.xml` for all KCML processes sharing the same memory segment. Only effective for the first KCML instance started after boot:
```sh
KCML_PSTAT_SIZE=4096 ; export KCML_PSTAT_SIZE
```

### KCML_TERM_LIC
Limits concurrent licences consumed per terminal. The first four sessions on a terminal count as one licence; each session beyond that counts individually (e.g. five sessions = two licences):
```sh
KCML_TERM_LIC=1 ; export KCML_TERM_LIC
```

### KEEPSHARED
Prevents selected global partitions from being de-selected during `LOAD`. When enabled, the subroutine search algorithm checks the original home partition before the currently executing partition — useful for shared text libraries where callers can override subroutines:
```sh
KEEPSHARED=true ; export KEEPSHARED
```

### KLOGKEY
Four-character shared-memory key for the KCML journal system (default `KLOG`). Change to isolate multiple KCML environments on the same host:
```sh
KLOGKEY=TEST ; export KLOGKEY
```

### OPTIONS_nn / OPTIONS_LIST_nn / OPTIONS_RUN_nn
Preset individual bytes at startup. Values must be two-digit hex strings:
```sh
OPTIONS_38="01" ; export OPTIONS_38          # force error on un-DIM'd variables
OPTIONS_LIST_20="02" ; export OPTIONS_LIST_20 # 2-space indentation in LIST
OPTIONS_RUN_40="06" ; export OPTIONS_RUN_40   # load/save ASCII with .src extension
```

### START
Auto-run a program at KCML startup:
```sh
START=DEVICES ; export START
```

### SYSTEMID
Identifies a KCML instance (0–65535) when running multiple independent instances on the same host. Each instance requires its own licence file and `$PSTAT` table. KCML searches for `lic.n.txt` (where n = SYSTEMID) before falling back to `lic.txt`:
```sh
SYSTEMID=2 ; export SYSTEMID
```

### TERMFILE
Path to the KCML terminal allocation file. All users on a system must share the same value — set it in `/etc/profile` or `kconf.xml`. Do not edit the file while KCML is running; editors may change the inode, breaking `#ID` and global partition access:
```sh
TERMFILE=/usr/local/kcml/TERMFILE ; export TERMFILE
```

### TOMFILE / TOMDIR
Enable native OS file-based program storage with name transformation. When both are set, spaces in program names become `/` (directory separator) and subsequent spaces become `_`. If a same-named directory already exists, `TOMDIR` additionally converts the name to lowercase to prevent save errors:
```sh
TOMFILE=true ; TOMDIR=true ; export TOMFILE TOMDIR
# "AB C D E" → "AB/C_D_E"
```

### USING_UTF8
Treat all strings and database columns as UTF-8. Sets byte 59 of `$MACHINE` to `HEX(01)`. Client strings sent in UTF-8:
```sh
USING_UTF8=true ; export USING_UTF8
```

### WORKSPACE
Directory for FSORT temporary files and other KCML work files:
```sh
WORKSPACE=/user1/tmpdir ; export WORKSPACE
```

---

## Notes

- On Unix, use `VAR=value ; export VAR` (Bourne/POSIX) or `setenv VAR value` (csh).
- `TERMFILE` should be the same for all users on a system — set it in `/etc/profile`. Do not edit it while KCML is running.
- `KCML_PSTAT_SIZE` and `BCDPART` must match across all KCML processes sharing the same memory segment. Set both in the system boot script or `kconf.xml`.
- Variables marked **read-only** (`KCMLDIR`, `LOGNAME`, `SERVICE`) can be read via `ENV()` but should not be set manually.

## See Also

- `ENV(` — read or write an environment variable from within KCML
- `$OPTIONS` / `$OPTIONS RUN` / `$OPTIONS LIST` — runtime option byte strings
- `$MACHINE` — machine/environment flags (byte 59 = UTF-8 mode)
- `FSORT BU` — uses `WORKSPACE`
- `#ID` — uses `KCML_ID` / `TERMFILE`
- `#TERM` — uses `FORCETERM` / `TERMFILE`
