# SELECT PRINT

> Sets the output device for PRINT and PRINTUSING statements.

## Syntax

```
SELECT PRINT /device_addr
SELECT PRINT /device_addr(width)
SELECT PRINT "filename"
SELECT PRINT                   (reset to default)
device$ = SELECT PRINT
device$ = SELECT PRINT WIDTH
```

## Description

Directs all `PRINT` and `PRINTUSING` output to the specified device or file. `SELECT PRINT` alone resets to the default output device.

Used as a function, returns the current device name. With `WIDTH`, returns the name and width in parentheses (for device-table entries).

```kcml
PRINT SELECT PRINT         : REM  e.g.  215
PRINT SELECT PRINT WIDTH   : REM  e.g.  215(132)
```

## Examples

```kcml
SELECT PRINT /215                         : REM  send PRINT to device 215
SELECT PRINT /204(80)                     : REM  device 204, 80 column width
SELECT PRINT "/tmp/report1"              : REM  send to a file
SELECT LIST <addr$(2)>, PRINT <addr$(2)> : REM  set list and print together
printer$ = SELECT PRINT                   : REM  query current device
width$ = STR(SELECT PRINT WIDTH, 5, 3)   : REM  extract width
```

```kcml
REM Typical printer pattern
$DEVICE /015="LPT1"
SELECT #9/015
$OPEN #9
SELECT PRINT #9
PRINT "Invoice output here"
SELECT PRINT              : REM  reset to default (/005)
$CLOSE #9
```

## Notes

- `/005` is the default terminal output device.
- Use `SELECT PRINT #stream` after opening a file or device on that stream.
- Resetting with bare `SELECT PRINT` restores the default device.

## See Also

- `PRINT` — output statement
- `PRINTUSING` — formatted output
- `SELECT CO` — console output device
- `SELECT` — overview
