# kcml — KCML Interpreter

> Invoke the KCML interpreter from the command line.

## Syntax

```
kcml [-gcdfnprwzv] [program] [param...]
```

## Description

`kcml` invokes the KCML interpreter (from `kserver.so`/`kserver.dll`). It reads commands from standard input and is interactive if stdin is a terminal.

- EOF on stdin causes an exit unless interactive (where `$END` is required).
- If `program` is given, it is run as a compiled program or executed as ASCII immediate statements before reading stdin.
- If `program` is omitted but the `START` environment variable names a file, that file is used as the startup program.
- Parameters after `program` are not used by KCML and are available via `$ARG()`.

### Standard streams

| Stream | KCML use |
|--------|----------|
| stdin | CI and `INPUT` |
| stdout | CO, `PRINT`, `LIST` |
| stderr | `TRACE` |

## Options

| Option | Description |
|--------|-------------|
| `-b` | Act as a SOAP server listening for web service requests |
| `-c` | Batch compile mode (same as `compile`); must be first switch |
| `-d` | Dongle test — print dongle/licence info |
| `-e envvar[=value]` | Set an environment variable before KCML starts (e.g. `HEAPINIT`) |
| `-g` | Load program into shared memory and execute as a global partition |
| `-k low,hi[,timeout]` | Run persistently, reconnecting to a port in range (for mod_kcml) |
| `-l` | Direct telnet support (deprecated in KCML 6.20) |
| `-n` | NPL compatibility mode (disables `@` globals, 24-line INPUT SCREEN, scroll) |
| `-p prog` | Non-interactive script mode; run `prog` as a batch script |
| `-q` | Connect to a CORBA ORB (act as CORBA server); ORB flags follow |
| `-s` | Switch to the program's directory before starting execution |
| `-S service` | Load environment from the named service in `kconf.xml` |
| `-v` | Display build version |
| `-x lib.so` | (Unix) Load a KCML shared library for use with `CALL` |
| `-y` | Use C runtime memory allocator (same as `USEMALLOC` env var) |

## Examples

```sh
kcml -p myscript.kcml          # Run a batch script
kcml -p prog arg1 arg2         # Run with arguments (available via $ARG())
kcml                           # Interactive mode
kcml -S myservice myprog       # Load service env from kconf.xml, run myprog
```

## See Also

- `compile` — compile ASCII source files
- `bkstat` — partition status utility
- `kconf` — kconf.xml configuration
- `script` — scripting with KCML
- `$ARG(` — access command-line parameters
