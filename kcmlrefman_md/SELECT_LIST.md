# SELECT LIST

> Sets the output device for the LIST command.

## Syntax

```
SELECT LIST /device_addr
SELECT LIST /device_addr(width)
SELECT LIST "filename"
device$ = SELECT LIST
device$ = SELECT LIST WIDTH
```

## Description

Defines where `LIST` output is sent. The optional `width` parameter restricts the listing to the given line width (0–255 characters).

Used as a function, returns the current device name. With `WIDTH`, returns the device name followed by the width in parentheses (for device table entries only).

```kcml
PRINT SELECT LIST         : REM  e.g.  215
PRINT SELECT LIST WIDTH   : REM  e.g.  215(132)
```

## Examples

```kcml
SELECT LIST /215                          : REM  send LIST to device 215
SELECT LIST /204(80)                      : REM  device 204, max 80 columns
SELECT LIST "/tmp/report1"               : REM  send to a file
SELECT LIST <address$(2)>, PRINT <address$(2)>  : REM  set list and print together
listfile$ = SELECT LIST                   : REM  query current device
width$ = STR(SELECT LIST WIDTH, 5, 3)    : REM  extract width portion
```

## Notes

- The default list device is `/204` (terminal, 132 columns) on most systems.
- Redirecting LIST to a file captures program source for documentation or version control.

## See Also

- `LIST` — list program source
- `SELECT CO` — console output device
- `SELECT` — overview
