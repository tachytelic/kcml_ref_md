# NT Printing

> Reference for printing from KCML on Windows NT via the Windows print subsystem.

## Description

On Windows NT, KCML can print through the Windows print driver (using `LCL=Y` with `DIR=N`) or directly to the printer port. See the `LocalPrinters` article for the full setup details.

### Key settings

- `$DEVICE /004="stdout,LCL=Y,DIR=Y"` — direct mode (bypass Windows driver)
- `$DEVICE /019="stdout,LCL=Y,DIR=N"` — via Windows printer driver

### Spooler considerations

Windows spools print output. Always bracket print jobs with `$OPEN`/`$CLOSE` so KCML signals completion to the client:

```kcml
$OPEN /019
SELECT PRINT /019
PRINT "Print content here"
SELECT PRINT /005
$CLOSE /019
```

### KCML 5.x and KClient 5.02

For KCML 5.x (which lacks `DIR=Y`/`DIR=N`), create `login.ini` in the KClient directory:
```ini
[printer]
TextMode=1
```

## See Also

- `LocalPrinters` — full local printing reference
- `$DEVICE` — device configuration
- `$OPEN` / `$CLOSE` — print job bracketing
- `SELECT PRINT` — select print device
