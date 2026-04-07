# Working with Secure Sockets (SSL/TLS)

> Reference for using SSL/TLS encrypted socket connections in KCML.

## Description

KCML supports SSL v3 and TLS v1 on supported platforms. It can act as both **client** (connecting to SSL servers) and **server** (accepting SSL connections).

SSL is provided via the OpenSSL library on Unix/Linux. Most Linux distributions include OpenSSL.

## Client — connecting to an SSL server

Add `SSL=Y` to the OPEN address string after the IP/hostname. Use the appropriate SSL port.

```kcml
DIM h, tx$200, rx$3000, nSent, nRead
h = OPEN "www.example.com:https,SSL=Y", "@"
IF h > 0 THEN DO
  tx$ = "GET / HTTP/1.1" & HEX(0D0A) & "Host: www.example.com" & HEX(0D0A) & "Connection: close" & HEX(0D0A0D0A)
  nSent = WRITE #h, tx$
  nRead = READ #h, rx$
  PRINT rx$
  CLOSE #h
END DO
```

## STARTTLS (upgrade plaintext to SSL)

For protocols that start as plaintext and upgrade to SSL (e.g. SMTP STARTTLS):

```kcml
$DECLARE 'KCML_Socket_SetSSL(INT()) = "*"
REM  Open plaintext connection, negotiate STARTTLS, then:
'KCML_Socket_SetSSL(h)    : REM  upgrade the connection to SSL
```

## SSL options string

| Option | Meaning |
|--------|---------|
| `SSL=Y` | Enable SSL on the connection |
| `PROXY=host:port` | Use HTTP proxy |

## Server certificates

KCML SSL servers require an X.509 certificate. Certificates can be:
- **CA-signed** (Thawte, Verisign, etc.) — trusted by clients without extra config.
- **Self-signed** — sufficient for internal use; clients may warn about authenticity.

See `SSLcert` for generating self-signed certificates with OpenSSL.

## Notes

- SSL available on Linux (OpenSSL 0.9.7+), AIX 5.x, HP-UX 11, Solaris 8+, Windows.
- Client certificate authentication is not currently supported.
- See `SystemRequirements` for platform-specific SSL support.

## See Also

- `SSLcert` — generating SSL certificates with OpenSSL
- `ObjSoap` — SOAP over HTTPS
- `SystemRequirements` — platform SSL support matrix
