# #PART

> Returns the partition number that uniquely identifies the running KCML process.

## Syntax

```
#PART
```

## Description

Returns a number (counted from 1) that uniquely identifies the currently running KCML process within the system. Each KCML partition has its own data space, screen, and execution context.

Normally `#PART` equals `#TERM`, unless:
- `#TERM` is zero (stdin is not a terminal), or
- Multiple KCML processes are owned by the same terminal.

Secondary processes (via `SHELL`, `$RELEASE`, or additional kclient sessions on the same terminal) take partition numbers from a dynamically allocated pool, counting down from the maximum.

### Partition limits

| Method | Effect |
|--------|--------|
| Default maximum | 1024 |
| `bkstat -x size` | Extend maximum to `size` (max 32768) |
| `BCDPART` env var | Restrict maximum for a KCML process |
| `$MACHINE` bytes 36–37 | System-wide maximum at runtime |
| `$OPTIONS RUN` bytes 55–56 | Maximum set via BCDPART |
| `$OPTIONS RUN` bytes 25–26 | Minimum set via BCDPART |

`bkstat -x` must be run before any KCML process starts (typically at boot time).

### Compatibility

Prior to KCML 5, the default maximum partition number was 512.

## Examples

```kcml
DIM partition
partition = #PART
PRINT "Running in partition "; partition
```

```kcml
IF #PART <= 50 THEN PRINT "Primary range partition"
```

```kcml
REM Identify this process in a shared log
PRINT "Process "; #PART; " started at "; TIME
```

## Notes

- Use `bkstat` to inspect live partition status on the system.
- `#PART` is the correct identifier to use for inter-process or cross-partition logic; `#TERM` identifies the terminal, not the process.

## See Also

- `#TERM` — terminal number owning this process
- `bkstat` — partition status utility
