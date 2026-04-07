# bkstat (Unix)

> Partition status utility — reports on running KCML processes and shared memory.

## Syntax

```
bkstat [-agkrsCTSPDBF] [-c part] [-p pid] [-u [sem_id]] [-t term_no] [-P part]
       [-x size] [-y size] [-R size] [-B part_no] [-K part_no:sig[:action]]
```

## Description

`bkstat` is a Unix utility that reports the status of KCML partitions and provides system information about running KCML processes. It uses the KCML TERMINFO database and `KTERM` environment variable to control the screen.

By default, `bkstat` shows only partitions sharing the same `TERMFILE`. Use `-g` to show all partitions.

Output can be redirected: `bkstat -M >mem.txt`

## Options

| Option | Description |
|--------|-------------|
| `-a` | Display alternate listing (Table 2 columns) |
| `-c part` | Clear entry for the specified unused partition |
| `-C` | Clear all unused partition entries |
| `-D part` | Display process information for the specified partition |
| `-g` | Show all partitions regardless of `TERMFILE` |
| `-k` | Return the shared memory partition identifier |
| `-p pid` | Show information for the specified process only |
| `-P part` | Show information for the specified partition only |
| `-M` | List all partitions with memory usage |
| `-s` | Enable the Signal option on the ring menu |
| `-S` | Display `$PSTAT` semaphore status |
| `-t term_no` | Show information for the specified terminal |
| `-T` | Display the `$PSTAT` terminal ID (TERMFILE inode number) |
| `-u [semid]` | Unlock a `$PSTAT` semaphore locked with `@LOCK` |
| `-w` | Wide display (128+ column screens) |
| `-r` | Display the KPrint Licence Table |
| `-x size` | Set `$PSTAT` partition array size (run before any KCML starts) |
| `-y size` | Set `$PSTAT` terminal array size (run before any KCML starts) |
| `-R size` | Set KPrint Licence table size |
| `-F` | List all foreground KCML partitions attached to a terminal |
| `-B part_no` | Send broadcast signal: 0=all, >0=specific, <0=all except |
| `-K part_no:sig[:action]` | Send signal `sig` to partition; action: `Snoop`, `Panic Continue`, `Panic+`, `Broadcast` |

## Standard listing columns (Table 1)

| Col | Heading | Description |
|-----|---------|-------------|
| 1 | PART | Partition number |
| 2 | TERM | Terminal number |
| 3 | USERMSG | `$PSTAT` message set by program |
| 4 | USERID | Name of the user running KCML |
| 5 | @NAME | `DEFFN @PART` name if global |
| 6 | VER | KCML version number |
| 7 | ERR | Last error (including minor code) |
| 8 | DEV | Device number or event code if blocked |
| 9 | PID | Unix process ID |
| 10 | GLOB | Current global partition selected |
| 11 | TEXT | Partition number of text being executed |
| 12 | DATA | Partition number of RESTORE pointer |
| 13 | S | Terminal status (A/D/W) |
| 14 | P | Programmability — `P` if programmable |
| 15 | T | TERMFILE group (0 on simple systems) |
| 16 | F | Terminal type: Forms/Text/Batch/Support/None/G |

## Alternate listing columns (Table 2, with `-a`)

| Col | Heading | Description |
|-----|---------|-------------|
| 1 | PART | Partition number |
| 2 | TERM | Terminal number |
| 3 | USERID | Logged-on userid |
| 4 | DEV | Device number or event code if blocked |
| 5 | PID | Unix process ID |
| 6 | CHILD | Partition number of `$RELEASE`d child |
| 7 | CHAIN | Chain information |
| 8 | Mem | Dynamic data segment size (1024-byte pages) |
| 9 | LastAcc | Time since last access (key press, mouse click) |
| 10 | IPADDR | IP address or computer name of client |
| 11 | SERIAL | WDW serial number |

## Notes

- Use **Terminate** (not Kill) via the signal menu — killing without cleanup can leave locks/shared memory dangling.
- If a process dies while holding an `@LOCK`, use `bkstat -u` to release the semaphore.
- `-x` and `-y` changes must be made **before** any KCML process runs; insert into the boot script before the system goes multi-user.
- When run as `root`, `-F` shows foreground partitions for all `$SYSTEMID` values.

## Examples

```sh
bkstat              # Interactive partition status
bkstat -g           # All partitions (all TERMFILE groups)
bkstat -M >mem.txt  # Memory usage to file
bkstat -x 3000      # Extend partition table to 3000 (at boot)
bkstat -y 8000      # Extend terminal table to 8000 (at boot)
bkstat -C           # Clear all unused partition entries
bkstat -B 0         # Broadcast to all partitions
```

## See Also

- `#PART` — partition number function
- `#TERM` — terminal number function
- `$PSTAT` — shared memory partition table
- `@LOCK` — semaphore lock for globals
