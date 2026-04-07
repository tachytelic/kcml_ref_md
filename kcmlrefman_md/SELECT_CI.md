# SELECT CI

> Sets the Console Input device — where immediate-mode commands and program editing input comes from.

## Syntax

```
SELECT CI /device_addr
SELECT CI "filename"
ci_device$ = SELECT CI
```

## Description

Redirects console input to the specified device or file. Characters entered at the console input device are automatically echoed to the Console Output device (`SELECT CO`).

Can be used as a function (no argument) to return the currently assigned input device name.

When input is redirected from a file, KCML reads commands from it until EOF, then automatically reverts to `/001` (the default terminal input).

## Examples

```kcml
SELECT CI /001                   : REM  reset to default terminal input
SELECT CI "inputfile"            : REM  read commands from a file
SELECT CO /005, CI /001, LIST /204  : REM  set multiple selects at once
array$(1) = SELECT CI            : REM  get current CI device name
```

## Notes

- `/001` is the default console input device (terminal).
- Redirecting CI to a file allows batch processing of immediate-mode commands.
- After the input file is exhausted, KCML reverts to `/001` automatically.

## See Also

- `SELECT CO` — console output device
- `SELECT` — overview of all SELECT parameters
- `$DEVICE` — define a device
