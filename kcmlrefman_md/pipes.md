# Working with Pipes as Devices

> How to connect KCML device addresses to Unix pipeline processes.

## Description

`$DEVICE` can connect a KCML device address to a Unix pipeline, either for output (KCML sends to a process) or input (a process supplies data to KCML).

## Output pipes

The string starts with `|` or `^`:

```kcml
$DEVICE /290="|lp"
```

Any output directed to device `/290` is sent to the Unix `lp` spooler, which runs in parallel with the KCML process.

**Important:** You must explicitly close the device before the spooler can spool the file:

```kcml
$DEVICE /290="|lp"
$OPEN /290
SELECT PRINT /290
REM ... print report ...
SELECT PRINT /005
$CLOSE /290
```

Alternatively, use `$REWIND` to close the device, or use bare `$DEVICE /290` to remove the device from the DET permanently.

## Input pipes

The string ends with `|`:

```kcml
$DEVICE /290="someprog|"
```

Runs `someprog` and makes its stdout available for reading on device `/290`.

## Alternative: SELECT streams

`SELECT INPUT`, `SELECT PRINT`, and `SELECT LIST` can also connect streams to pipelines without needing `$DEVICE`.

## See Also

- `$DEVICE` — device address configuration
- `SELECT` — select input/print/list streams
- `$OPEN` — open a device
- `$CLOSE` — close a device
- `UnixPrinting` — Unix printing overview
