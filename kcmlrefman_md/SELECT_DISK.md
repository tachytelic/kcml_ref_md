# SELECT DISK / SELECT #stream

> Sets the default disk directory or assigns a device to a numbered stream.

## Syntax

```
SELECT DISK /device_addr
SELECT #stream /device_addr
SELECT #stream "directory_path"
SELECT #stream <variable$>
device$ = SELECT #stream
```

## Description

Assigns a device or directory to a stream number in the device table. Stream `#0` is the default used for `LIST DC`, `LOAD`, `SAVE`, etc.

`SELECT DISK` is equivalent to `SELECT #0`.

When used as a function (right-hand side), returns the current device address or directory path assigned to the stream.

## Examples

```kcml
SELECT DISK /D10                       : REM  set default disk to device D10
SELECT #1 "D:\KCC", #2 /D99           : REM  set two streams at once
SELECT #22 <data_directory$>           : REM  variable path (angle-bracket syntax)
address$ = SELECT #27                  : REM  query current path of stream 27
```

## Notes

- Device addresses (`/D10`, `/D99`, etc.) reference the device table configured with `$DEVICE`.
- Literal directory paths and variable paths (using `< >`) are both supported.
- Stream `#0` is the default for all file operations unless overridden by specifying `#stream` explicitly.

## See Also

- `SELECT` — overview
- `$DEVICE` — define a device address
- `LOAD` — load a program (uses SELECT DISK stream)
- `SAVE` — save a program
