# Unix Server Printing

> Reference for printing from KCML programs on Unix servers.

## Two approaches

### 1. Direct printing (to a device file)

Write directly to a device special file. Suitable for alignment-sensitive forms.

```kcml
$DEVICE /015="/dev/tty09 ALF=Y"
$OPEN /015
SELECT PRINT /015
PRINT "Invoice line 1"
SELECT PRINT /005
$CLOSE /015
```

Use `$OPEN`/`$CLOSE` even for direct devices — parallel printer drivers enforce their own locking; it's better to force the issue once with `$OPEN` than to error-trap `PRINT` statements.

### 2. Spooled printing (via `lp`)

Use a pipe to the `lp` spooler. The pipe is opened on `$OPEN` and the job is submitted on `$CLOSE`.

```kcml
$DEVICE /015="|lp -d 3rdFloorLaser ALF=Y"
$OPEN /015
SELECT PRINT /015
PRINT "Invoice line 1"
SELECT PRINT /005
$CLOSE /015
```

Common `lp` switches:
- `-d queue` — specify print queue
- `-n copies` — number of copies
- `-t title` — job title

Most Unix spoolers support network printing via `lpr` protocol.

## ALF=Y

The `ALF=Y` option in `$DEVICE` causes KCML to append a line feed (`HEX(0A)`) after each carriage return — needed for most modern printers.

## See Also

- `$DEVICE` — define a device
- `$OPEN` / `$CLOSE` — open/close a device
- `SELECT PRINT` — set print device
- `PrinterDev` — printer overview
- `LocalPrinters` — local/client-side printing
- `NTPrinting` — Windows NT printing
