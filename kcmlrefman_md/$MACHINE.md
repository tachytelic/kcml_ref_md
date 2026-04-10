# $MACHINE

> A read-only 128-byte system variable containing information about the hardware, operating system, terminal, and licence configuration in use.

## Syntax

```
$MACHINE
```

`$MACHINE` is an alpha variable — it can be read and passed to functions, but cannot appear on the left-hand side of an assignment.

## Description

`$MACHINE` encodes system state into a fixed 128-byte string. Each byte or byte range has a defined meaning. Access individual fields using `STR()` or `ASC()`, or use the built-in `KCML_MACHINE` `DEFRECORD` structure for named field access via `FLD(`.

```kcml
: DIM machine$128
: machine$ = $MACHINE
```

## Byte Map

| Byte(s) | Content | Values |
|---------|---------|--------|
| 1 | Operating environment | `U` = UNIX/Linux, `N` = MS Windows |
| 2 | Terminal capabilities (bitfield) | `HEX(01)` = window rendering; `HEX(04)` = screen saving; `HEX(40)` = KCML forms support |
| 3 | Monitor/terminal type | Blank = dumb terminal; `W` = Kclient or variant |
| 4 | Graphics support | `G` = text-mode box graphics available |
| 6 | User count at startup | Binary count of users active when this process started, excluding current process |
| 8 | Screen width | Binary column count; default `HEX(50)` (= 80 columns) |
| 12 | Colour availability | `HEX(02)` = monochrome; `HEX(10)` = colour display |
| 23–24 | Mouse position | Last known row (byte 23) and column (byte 24); `HEX(FF)` = mouse unavailable |
| 27–28 | Maximum licensed users | Binary; maximum concurrent users permitted by licence |
| 40–41 | Maximum client connections | Binary; maximum licensed client connections |
| 45–48 | Server IP address | 4-byte network address of server; zero = direct connection mode |
| 57 | Compliance level | Binary; compliance level of the currently executing program (see `$COMPLIANCE`) |

## KCML_MACHINE Record Structure

KCML provides a built-in `DEFRECORD` named `KCML_MACHINE` that maps named fields onto the `$MACHINE` byte layout, allowing `FLD(` access without hardcoded offsets:

```kcml
: DIM maxpart
: maxpart = FLD($MACHINE.MACHINE_MaxPart)
```

This is the preferred approach when reading multiple fields, as it avoids magic byte offsets in application code.

## Examples

### Detect operating system

```kcml
: DIM machine$128, os$1
: machine$ = $MACHINE
: os$ = STR(machine$, 1, 1)
: IF os$ == "U" THEN PRINT "Running on UNIX/Linux"
: IF os$ == "N" THEN PRINT "Running on Windows"
```

### Check for KCML forms support

```kcml
: DIM machine$128, caps
: machine$ = $MACHINE
: caps = ASC(STR(machine$, 2, 1))
: IF BOOL(caps AND HEX(40)) THEN PRINT "Forms supported"
```

### Read screen width

```kcml
: DIM machine$128, width
: machine$ = $MACHINE
: width = ASC(STR(machine$, 8, 1))
: PRINT "Terminal width:"; width
```

### Read compliance level

```kcml
: DIM machine$128, level
: machine$ = $MACHINE
: level = ASC(STR(machine$, 57, 1))
: PRINT "Compliance level:"; level
```

## Notes

- `$MACHINE` is **read-only** — assigning to it is a compile error.
- The full string is 128 bytes; unused bytes may be null (`HEX(00)`) or space-padded depending on the field.
- Byte 2 is a **bitfield** — use `AND` to test individual capability bits rather than comparing the whole byte.
- Byte 8 (screen width) is a **binary** value, not an ASCII digit — use `ASC()` to read it as a number.
- The user count at byte 6 reflects the state at process startup; it does not update dynamically during execution.

## See Also

- `$COMPLIANCE` — sets/reports the language compliance level (readable via byte 57)
- `FLD(` — field accessor, used with `KCML_MACHINE` record structure
- `DEFRECORD` — defines named field layouts over string buffers
- `STR(` — extract a substring by position and length
- `ASC(` — convert a single character to its numeric (ASCII/binary) value
