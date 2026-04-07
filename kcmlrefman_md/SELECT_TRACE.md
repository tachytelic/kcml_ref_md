# SELECT TRACE

> Redirects TRACE and $COMPILE output to a device or file.

## Syntax

```
SELECT TRACE /device_addr
SELECT TRACE "filename"
SELECT TRACE <variable$>
SELECT TRACE              (reset to default)
```

## Description

By default, `TRACE` output goes to the Workbench trace window; on non-Workbench terminals it goes to the `/005` device (which can corrupt the screen display). `SELECT TRACE` redirects this output to a file or device.

`SELECT TRACE` alone resets to the default.

## Examples

```kcml
TRACE 1000, 5000
SELECT TRACE "/tmp/TRACEfile"
REM  TRACE output now goes to the file instead of the screen
```

```kcml
SELECT TRACE /204                       : REM  send to device 204
SELECT TRACE <tracefile$>               : REM  variable path
SELECT TRACE "/user1/tracefile"
SELECT TRACE /204, PRINT /005           : REM  combined select
```

## Notes

- Redirecting TRACE to a file allows debugging without disturbing the application screen.
- `$COMPILE` output also goes to the TRACE device.

## See Also

- `TRACE` — program execution tracing
- `$COMPILE` — compile a program
- `SELECT` — overview
