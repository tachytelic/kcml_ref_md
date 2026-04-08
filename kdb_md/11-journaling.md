# KDB Journal (Transaction Logging)

## Overview

The KDB journal is a crash-recovery mechanism that protects against data loss or corruption caused by system failures. It is managed by the `krecover` utility daemon.

The journal works by writing copies of all database writes to a dedicated log file. In the event of a crash, `krecover` reads the log and re-applies the writes to restore consistency.

The journal and transactions are independent — either can be used without the other.

---

## Two Protection Scenarios

### Scenario 1: OS Crash or Power Failure (Small Looping Log)
A small log is used. When the end is reached, KCML loops back and reuses the log. A background sync daemon periodically flushes OS disk buffers and notes the sync in the log. On restart, `krecover` replays from the last-but-one sync entry.

### Scenario 2: Hardware Failure with Backup Restore (Large Log)
A large log records all writes since the last backup. The log cannot be reused until a new backup is taken. After hardware repair and backup restore, `krecover` re-applies the full log.

Both scenarios can be protected simultaneously with a large log plus a sync daemon.

---

## Hardware Setup

The journal requires a dedicated raw disk partition — no filesystem buffering. For best performance, use a dedicated disk with no other I/O.

Two device names are required:
- `/dev/kisamlogread` — block device (b) used by `krecover` to read (benefits from disk cache)
- `/dev/kisamlogwrite` — character device (c) used by KCML processes to write synchronously

Link your raw partition to these names:
```bash
/sbin/mknod /dev/kisamlogread b <major> <minor>
/sbin/mknod /dev/kisamlogwrite c <major> <minor>
```

---

## Journal Lifecycle

Three basic activities managed by `krecover`:

1. **Initialise** — defines log location, size, mode. Done once at commissioning.
2. **Open (startup)** — reads header from log into shared memory; replays if system crashed. Done at OS boot before any KCML processes start.
3. **Close (shutdown)** — marks log as cleanly closed. Done after all KCML processes have terminated.

---

## Example 1: Small Looping Log (crash/power protection)

**Initialise the log (once):**
```bash
krecover -m 512 -v 2 -l /tmp/krecover.log
```
Creates and initialises shared memory and the log with a 500MB maximum.

**Open at system startup:**
```bash
krecover -e -v 2 -l /tmp/krecover.log
if [ $? != 0 ]; then
    echo "Failed to open database journal"
else
    echo "Database logging started"
fi
```
If the system crashed, `krecover` will replay the log before starting normally.

**Close at system shutdown:**
```bash
krecover -d -v 2 -l /tmp/krecover.log
if [ $? == 0 ]; then
    krecover -k -v 2 -l /tmp/krecover.log
    if [ $? == 0 ]; then
        echo "Database logging stopped"
    fi
fi
```

---

## Example 2: Large Log (backup + crash protection)

**Initialise:**
```bash
krecover -n -m 9000 -S -v 2 -l /tmp/krecover.log
```
`-n` = huge log, `-S` = sync daemon even with huge log, `-m 9000` = 9GB maximum.

**Open at startup:**
```bash
krecover -e -n -S -v 2 -l /tmp/krecover.log
```

**Full restore after hardware failure:**
```bash
# Stop the daemon (leaves log open)
krecover -K

# Restore from full log after backup has been applied
krecover -T -n -S -v 2 -l /tmp/krecover.log
echo $?  # Should be 0
```

**Re-initialise after a successful backup** (to restart the log):
```bash
krecover -d -v 2 -l /tmp/krecover.log
krecover -k -v 2 -l /tmp/krecover.log
krecover -n -m 9000 -S -v 2 -l /tmp/krecover.log
```

---

## Monitoring

```bash
# Show settings from shared memory and log header
krecover -i

# Tail the log (shows tables being written to)
krecover -t -v 2

# Force a sync
krecover -s
```

**Monitoring flags reported by `krecover -i`:**

Transaction mode byte:

| Bit | Value | Meaning |
|-----|-------|---------|
| 0 | `0x01` | KDB transaction logging ON |
| 1 | `0x02` | Check that tables are locked |
| 2 | `0x04` | Take transaction system lock |
| 3 | `0x08` | Take KDB logging system lock |
| 4 | `0x10` | ERR if transaction locking is off |
| 5 | `0x20` | Automatic KI_ROLLBACK on error |

Enabled byte:

| Bit | Value | Meaning |
|-----|-------|---------|
| 0 | `0x01` | KDB transactions enabled |
| 1 | `0x02` | Write to log — sync daemon running |
| 2 | `0x04` | Large log, no sync daemon |
| 3 | `0x08` | Force sync daemon even with huge log |

For testing — clean reset:
```bash
krecover -d -k -D    # disable, kill daemon, delete shared memory
```
