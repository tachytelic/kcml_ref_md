# TCP/IP Sockets

> How to use KCML as a TCP/IP socket client or server with `OPEN #`.

## Description

The `OPEN #` statement supports TCP/IP sockets. The `"@"` mode character specifies socket mode. The filename argument specifies the address as `host:port`.

## Client usage

```kcml
OPEN #1, "alpha.bigco.com:10000", "@"
OPEN #stream, "10.1.1.2:rexec", "@"
```

- Port numbers can be numeric or service names (e.g. `telnet`, `smtp`).
- Host can be a hostname (if DNS available) or a dotted IP address.
- If no server is listening, `OPEN` fails with a `D82` error.
- On success, use `READ #`, `WRITE #`, `$IF #`, and `CLOSE #` on the stream.

## Server usage

```kcml
REM Listen on port 8123:
OPEN #ConnectStream, " :8123", "@"

REM Check for incoming connection:
a = $IF #ConnectStream, timeout

REM Accept the connection and get a working stream:
OPEN #MsgStream, $PRINTF("#%d", ConnectStream), "@"
```

- The server `OPEN #` returns immediately; the network layer is primed.
- `$IF #ConnectStream` returns 1 when a client connects, 0 on timeout.
- The listen stream (`ConnectStream`) is reserved for connections only — use only with `$IF #` and `CLOSE #`.
- The message stream (`MsgStream`) is used for `READ #`, `WRITE #`, and data exchange.

## Multi-client servers

For multiple simultaneous clients:
- Allocate message streams from a pool array.
- Use `$IF #` to test for available data before `READ #` (which blocks if no data).
- Process each message quickly to remain responsive.

**Windows note:** Server `$IF #` for accepted connections requires KCML 6.0+ with Winsock 2. KCML 5.02 only supported Winsock 1.1 which always returned 1.

## Example: simple SMTP client

```kcml
DIM CRLF$2, MailHost$30, msg$80
CRLF$ = HEX(0D0A)
MailHost$ = "mail.example.com:smtp"

OPEN #1, MailHost$, "@"
WRITE #1, "HELO myhost.example.com" & CRLF$
READ #1, msg$
WRITE #1, "QUIT" & CRLF$
CLOSE #1
```

## See Also

- `OPEN #` — open file or socket stream
- `READ #` — read from stream
- `WRITE #` — write to stream
- `$IF #` — test stream for available data
- `CLOSE #` — close stream
