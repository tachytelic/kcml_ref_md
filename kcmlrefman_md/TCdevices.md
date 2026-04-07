# Working with Serial Line Devices (TC)

> Reference for configuring RS-232 serial line devices in KCML.

## Description

KCML supports two modes of serial (RS-232) device access:

1. **2227B emulation** (`TC` type in `$DEVICE`) — legacy compatibility mode using `$GIO`. Not documented here.
2. **Keyword configuration** — preferred mode; parameters supplied as a keyword string in `$DEVICE`.

Parameters are set at `$DEVICE` time and applied when `$OPEN` is called on the device.

By convention, device addresses `/01C`–`/01F` are used for serial devices (not enforced).

### Platform paths

- **Unix**: `/dev/tty01` (exact name varies by Unix variant)
- **Windows**: `COM1`–`COM9`

## Device configuration keywords

Keywords are comma-separated, case-insensitive. Defaults: 9600 baud, no parity, 8 data bits, 1 stop bit, no flow control, MIN=1, TIME=1.

### Baud rate

`300`, `600`, `1200`, `2400`, `4800`, `9600`, `19200`, `38400`

### Data bits

`CS5`, `CS6`, `CS7`, `CS8`

### Stop bits

`STOP1`, `STOP2`

### Parity

`ODD` / `PARODD`, `EVEN` / `PARENB`, `NONE`

### Flow control

| Keyword | Effect |
|---------|--------|
| `IXON` | React to XON/XOFF flow control (software) |
| `IXOFF` | Generate XON/XOFF |
| `IXANY` | Any character after XOFF treated as XON |
| `RTSFLOW` | RTS flow control (SCO Unix only) |
| `CTSFLOW` | CTS flow control (SCO Unix only) |

### Modem control

`MODEM` — enable modem control signals; `LOCAL` — no modem control.

### Buffering

`MIN0` — minimum chars = 0; `TIME0` — maximum wait = 0 (allows 0.1s timeout).

## Example

```kcml
$DEVICE /01C="COM1","9600,CS8,STOP1,NONE"
$OPEN /01C
SELECT INPUT /01C
SELECT CO /01C
```

## See Also

- `$DEVICE` — define a device
- `$OPEN` — open/lock a device
- `$GIO` — 2227B emulation mode (legacy)
