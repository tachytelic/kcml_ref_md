# SELECT CO

> Sets the Console Output device — where terminal responses, traces, and echoed input are displayed.

## Syntax

```
SELECT CO /device_addr
SELECT CO "filename"
co_device$ = SELECT CO
co_device$ = SELECT CO WIDTH
```

## Description

Redirects console output to the specified device or file. All responses to `LINPUT`, `LINPUT LINE`, `LINPUT LIST`, `KEYIN`, `TRACE`, etc. are echoed to the CO device.

Used as a function (no argument), returns the currently assigned device name. With `WIDTH`, returns the device name followed by the width in parentheses.

```kcml
PRINT SELECT CO          : REM  e.g.  005
PRINT SELECT CO WIDTH    : REM  e.g.  005(80)
```

`WIDTH` is only returned for devices defined in the device table.

## Examples

```kcml
SELECT CO /005                      : REM  default terminal output
SELECT CO "outputfile"              : REM  redirect to a file
SELECT CO /005, CI /001, LIST /204  : REM  set multiple selects
array$(2) = SELECT CO               : REM  get current device name
width$ = SELECT CO WIDTH            : REM  device name + width
```

## Notes

- `/005` is the default console output device (terminal).
- Redirecting CO to a file captures all console output for logging or testing.
- The `WIDTH` form is useful for screen layout calculations.

## See Also

- `SELECT CI` — console input device
- `SELECT PRINT` — print output device
- `SELECT` — overview of all SELECT parameters
