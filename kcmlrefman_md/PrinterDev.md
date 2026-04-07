# Working with Printers

> Overview of printing in KCML — local, server-attached, network, and spooled printers.

## Description

KCML programs generate print output using `PRINT` and `PRINTUSING` after selecting a print device with `SELECT PRINT`. The printer device must be defined with `$DEVICE` and locked with `$OPEN` / `$CLOSE`.

## Basic printing pattern

```kcml
$DEVICE /015="LPT1"
SELECT #9/015
$OPEN #9
SELECT PRINT #9
PRINT "Hello, printer"
SELECT PRINT /005        : REM restore to default
$CLOSE #9                : REM signals end of print job to spooler
```

`$OPEN` / `$CLOSE` bracket the print job:
- On a directly connected printer: prevents two processes writing simultaneously.
- On a spooled printer: `$CLOSE` signals the spooler to release the job to the printer.

## Line terminator control

The first digit of the device address controls line termination:

| First digit | Behaviour |
|-------------|-----------|
| `0` | Automatic: appends `HEX(0A)` after each `HEX(0D)` |
| `2` | Pass-through: `HEX(0D)` sent as-is |

The example above uses `/015` (first digit `0`) for automatic LF addition.

## Printer types

| Type | Description |
|------|-------------|
| Local (client) | Printer on the user's PC via KClient — see `LocalPrinters` |
| Server-attached | Printer connected to the KCML server (Unix or Windows) |
| Network (Kprint) | Shared network printer via the Kprint spooler |
| NT Windows driver | Via Windows print subsystem — see `NTPrinting` |

## See Also

- `LocalPrinters` — local (client-side) printing setup
- `NTPrinting` — printing on Windows NT via Windows driver
- `$DEVICE` — define a device
- `$OPEN` / `$CLOSE` — lock/unlock a device
- `SELECT PRINT` — set the active print device
- `PRINT` — output statement
- `PRINTUSING` — formatted output
