# ASP (Application Service Provider) Configuration

> How to run multiple independent KCML systems on a shared server.

## Description

The ASP (Application Service Provider) model hosts multiple customer KCML systems on a single server. Each customer system must be isolated so that its users and data are independent of other systems on the same machine.

## Two deployment models

### 1. Separate KCML directories per system

Each customer has their own KCML installation directory with their own `lic.txt` and `TERMFILE`. Flexible — allows different KCML versions per customer. Harder to manage upgrades.

### 2. Shared KCML directory

All systems share a common KCML binary directory. Simpler version management — an upgrade affects all customers simultaneously.

## Isolating $PSTAT shared memory

By default, all KCML processes on a server share a common `$PSTAT` shared memory segment regardless of which directory they run from. To isolate systems:

1. Number each system (1–65535).
2. Set the `SYSTEMID` environment variable before KCML starts.

KCML will create a dedicated `$PSTAT` segment for that system number. `#PART` numbers are then unique within the system.

## Licence files

Each system needs its own licence file with a `Systemid` line matching the `SYSTEMID` environment variable.

- **Separate KCML directories**: use the standard `lic.txt` filename.
- **Shared directory**: rename to `lic.x.txt` where `x` is the `SYSTEMID` number. KCML looks for this name first when `SYSTEMID` is set, then falls back to `lic.txt`.

## TERMFILE isolation

Each system needs its own `TERMFILE` — set the `TERMFILE` environment variable per system so that `#TERM` allocations do not collide.

## Connection Manager

When using the KCML Connection Manager (`kconf.xml`):

- Define a `<service>` block per customer system.
- Set `SYSTEMID` and other system-specific variables in the `<environment>` section.
- List all users explicitly in `<validusers>`.
- Set the `SERVICE` environment variable to the service name.

## File permissions

Give each customer system its own Unix group. Set users' supplementary group to the system group and ensure `umask 007` so that data files are not accessible across systems.

## See Also

- `#PART` — partition number (unique within a SYSTEMID)
- `#TERM` — terminal number
- `bkstat` — partition status utility
- `$PSTAT` — shared memory partition table
