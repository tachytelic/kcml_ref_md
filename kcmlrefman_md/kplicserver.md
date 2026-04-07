# kplicserver — Remote Licence Daemon

> Manage network licences for KPrint and KMail from a central server.

## Description

The Remote Licence Daemon manages licences for KPrint and KMail 3.0, allowing multiple machines to share a central licence file rather than each having an individual licence.

The daemon:
1. Reads `[KPrint]` and `[KMail]` sections from the licence file for pool user counts.
2. Listens on **UDP port 1791** for licence requests.
3. Books out licences against the requesting machine's IP address.
4. Returns a reply acknowledging the request (or an error if the pool is exhausted).

## Installation

### Windows

The installer creates a Windows service automatically. It can be managed via:
- KCML Service Administrator (`KServAdm`)
- Web-based Remote Administration Tool

### Unix

Installed as part of KCML. Start it in the system startup script alongside KCML:

```sh
/usr/lib/kcml/kplicserver &
```

## Inspecting the KPrint licence table

```sh
bkstat -r
```

## See Also

- `bkstat` — partition and licence status utility
- `kconf` — Connection Manager configuration
