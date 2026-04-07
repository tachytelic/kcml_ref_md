# Installing KCML on Unix

> How to download and install KCML on Unix/Linux systems.

## Prerequisites

Some KCML version / OS combinations require packages before installation:

| OS | KCML versions | Required packages |
|----|--------------|-------------------|
| AIX | All | None |
| HP-UX | 6.0, 6.20 | None |
| Linux | All | `ncompress`, `cpio`, `xinetd` |
| Solaris 8 | 6.0, 6.20 | None |
| Solaris 10 | 6.20, 7 | `CSWlibgcc-s1`, `CSWlibstdc++6` |
| UnixWare | 6.0, 6.20 | None |

## Preparation

1. Download the compressed cpio archive (`.Z` image file) to `/tmp`.
2. Uncompress: `uncompress IMAGE.Z`
3. Extract the installation script:
   - Linux or KCML 7: `cpio -iv kcmlinst <IMAGE`
   - KCML 6.00/6.20/6.90 on non-Linux: `cpio -icv kcmlinst <IMAGE`
4. Make executable: `chmod +x kcmlinst`

## Installation

Must be run as `root`:

```sh
./kcmlinst
```

The installer extracts files and runs the setup program.

## See Also

- `installers` — Windows installer overview
- `kcml` — KCML interpreter command reference
- `bkstat` — partition status utility
