# KCML/KClient Operating System Requirements

> Summary of platform support for KCML 6.x and KClient.

## Description

KCML runs on a range of Unix/Linux platforms and Windows. Key capabilities vary by platform.

## KCML 6.20 server platforms

| Platform | Xerces XML | SSL | SOAP | Notes |
|----------|-----------|-----|------|-------|
| AIX 4.3 | No | Yes | Yes | Requires specific OpenSSL |
| AIX 5.1/5.2 | Yes | Yes (OpenSSL 0.9.7) | Yes | |
| AIX 5.3+ | Yes | Yes (OpenSSL 0.9.8) | Yes | Power4+ CPU |
| HP-UX 11.x | Yes | Yes | Yes | PA-RISC or Itanium |
| Linux 2.4 x86 | Yes | Yes (OpenSSL 0.9.7) | Yes | Various distros |
| Linux 2.6 x86 | Yes | Yes (OpenSSL 0.9.8) | Yes | |
| Solaris 8+ SPARC | Yes | Yes | Yes | |
| UnixWare 7.0.1 | No | Yes | Yes | |
| UnixWare 7.1.1+ | Yes | Yes | Yes | |
| Windows XP SP2+ | Yes | Yes (OpenSSL 0.9.7) | Yes | 32- and 64-bit |

## KClient versions by Windows platform

| Windows | 5.02 | 5.50 | 6.00 | 6.20 | 6.90 |
|---------|------|------|------|------|------|
| XP | Yes | Yes | Yes | Yes | Yes |
| Vista 32-bit | No | Yes | Yes | Yes | Yes |
| Vista 64-bit | No | Yes* | Yes* | Yes* | Yes |
| Windows 7 32-bit | No | Yes | Yes | Yes | Yes |
| Windows 7 64-bit | No | Yes* | Yes* | Yes* | Yes |
| Server 2003/2008 | No | Yes | Yes | Yes | Yes |

*32-bit KClient on 64-bit Windows

## Notes

- SSL requires OpenSSL to be installed separately on most Unix platforms.
- Large files (>2GB) are supported on all listed platforms in KCML 6.00+.

## See Also

- `SSL` — working with secure sockets
- `ObjSoap` — SOAP web services
