# Local Printing

> Reference article for printing to a local client printer from KCML via the `LCL=Y` device specifier.

## Description

KCML supports local printing via the client (KClient, WDW terminal emulator) using `$DEVICE` with `LCL=Y`. By default, device `/004` is configured as a local printer:

```kcml
$DEVICE /004="stdout,LCL=Y,DIR=Y"
```

When `LCL=Y` is set, the filename is irrelevant — `stdout` is conventional.

### DIR=Y (Direct printing)

Bytes are sent directly to the printer, bypassing the Windows printer driver. The application is responsible for:
- Page orientation, fonts, escape sequences
- Sending `HEX(0C)` to flush the last page on page printers (LaserJet etc.)
- Ensuring the correct code page (HP printers don't default to Latin-1)

Highest performance; required for legacy software that embeds control sequences.

### DIR=N (Windows printer driver)

Print stream is sent through the Windows printer driver. Escape sequences in the data are ignored. Use for special devices like fax printers.

### Spooling and print jobs

Windows spools all printer output. To ensure Windows flushes the job:

```kcml
$DEVICE /019="stdout,LCL=Y,DIR=N"
$OPEN /019
SELECT PRINT /019
PRINT "This will use default printer driver settings"
SELECT PRINT /005
$CLOSE /019
```

The `$OPEN`/`$CLOSE` bracket tells KCML (and therefore the client) when the job is complete, triggering spooler release.

**Warning:** If the printer is not spooled and goes offline, the print stream (multiplexed with screen output) will hang the terminal.

### KCML 5.x compatibility

With KClient 5.02, create a `login.ini` file in the kclient directory:
```ini
[printer]
TextMode=1
```
This routes all printing through the Windows printer driver.

## Notes

- `DIR=Y`/`DIR=N` was introduced in KCML 6.0. Not available in KCML 5.x without the `login.ini` workaround.

## See Also

- `$DEVICE` — configure a device
- `$OPEN` / `$CLOSE` — bracket a print job
- `SELECT PRINT` — select the print device
