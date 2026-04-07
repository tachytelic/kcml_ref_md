# Controlling the Screen in Text Mode

> How KCML accesses and controls the text terminal screen.

## Description

The terminal screen is accessed as device `/005` (predefined as stdout). It cannot be redefined with `$DEVICE` within KCML; only stdout redirection at startup can change it.

Use `PRINT`, `PRINTUSING`, or `$GIO` with `SELECT PRINT /005` to output to the screen.

## Screen width

```kcml
SELECT PRINT /005        : REM  default — depends on terminal
SELECT PRINT /005(80)    : REM  80 columns
SELECT PRINT /005(132)   : REM  132 columns (see TextTerm132)
```

The optional width (0–255) causes KCML to auto-insert a CR when a line exceeds the width. Width 0 disables autowrap detection.

## CR/LF handling — first digit of device address

The first digit of `/005` controls how KCML handles carriage returns:

| Digit | Effect |
|-------|--------|
| `0` | Map CR to CR/LF |
| `1` | Send LF instead of CR |
| `2` | Send CR only |
| `4` | As 0 but column count is not updated |

## Examples

```kcml
SELECT PRINT /005
PRINT "Hello world"

SELECT PRINT /005(80)    : REM  set 80-column width
```

## See Also

- `SELECT PRINT` — set print device
- `TextTerm132` — 132-column mode
- `PRINT` — output statement
