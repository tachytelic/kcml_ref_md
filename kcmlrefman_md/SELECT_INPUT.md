# SELECT INPUT

> Sets the input device for KEYIN, LINPUT, LINPUT LINE, and LINPUT LIST.

## Syntax

```
SELECT INPUT /device_addr
SELECT INPUT "filename"
SELECT INPUT <variable$>
device$ = SELECT INPUT
```

## Description

Directs all interactive input statements (`KEYIN`, `LINPUT`, `LINPUT LINE`, `LINPUT LIST`) to the specified device or file.

When used as a function (right-hand side), returns the current input device name.

## Examples

```kcml
SELECT INPUT /001                        : REM  default terminal input
SELECT INPUT <address$(value)>           : REM  variable device address
SELECT INPUT "/user1/input_file", LIST /204  : REM  from file + set list device
test$ = SELECT INPUT                     : REM  query current input device
```

## Notes

- `/001` is the default terminal input device.
- Redirecting input to a file allows automated/scripted data entry.
- Unlike `SELECT CI` (which affects immediate-mode and editor input), `SELECT INPUT` affects program-mode input statements.

## See Also

- `SELECT CI` — console input (immediate mode)
- `SELECT CO` — console output
- `LINPUT` — line input statement
- `KEYIN` — single-character input
- `SELECT` — overview
