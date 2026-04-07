# KPrint — Network Printing

> How to send output to KPrint queues from KCML.

## Description

KPrint is a Kerridge product that acts as an LPD print server: it accepts raw text, merges it with locally cached form specifications, and produces rich formatted printer output. LPD is a network printing protocol supported on Unix, Windows, and many network printers.

## Accessing KPrint from Unix

Use a spooled Unix printer device:

```kcml
$DEVICE /015="|lp -d kprintq"
```

Where `kprintq` is the KPrint queue name configured with `lpadmin`.

## Accessing KPrint directly over LPD

This works on both Unix and Windows:

```kcml
$DEVICE /015="kprintq@kprintserver LPD=Y"
$DEVICE /016="queue2@10.0.1.10,LPD=Y"
```

- `LPD=Y` specifies the LPD protocol.
- The `@serverhostname` part is optional if the KPrint server is on the same machine as the KCML process.

## Notes

- `LPD=Y` may also work with network printers that support LPR/LPD — the queue name is printer-dependent (check the printer documentation).
- For more about KPrint, see the Kerridge website.

## See Also

- `$DEVICE` — device configuration
- `SELECT PRINT` — select print device
- `UnixPrinting` — Unix printing overview
- `kplicserver` — KPrint network licence daemon
