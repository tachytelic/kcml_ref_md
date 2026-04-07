# Windows Installer

> Overview of the KCML installer for Windows NT/2000/XP/95/98.

## Description

KCML 6.00 and related products use purpose-built Windows installers. Advantages:
- Minimise the need for a system reboot
- Automatically configure software settings
- Built-in licensing check

## Installation process

1. The installer extracts files to a temporary directory (may take time if downloaded from a remote location).
2. The setup program runs and presents installation options.

## Options

| Option | Description |
|--------|-------------|
| **Install Directory** | Target directory (default: `C:\Kerridge\KCML` for first install). Accepts typed path or Browse dialog. |
| **Make default product** | Register the product (on by default). Under Windows NT4/2000/XP requires an administrative user. |
| **Add to 'Start Menu'** | Add entries to the Windows Start Menu (for helpfiles, KClient, etc.). |
| **Update examples** | For files installed as editable examples (e.g. `kconf.xml`, `kwroot`). Clear to skip overwriting your customised versions on upgrade. |

## Notes

- First-time installations should leave "Make default product" checked.
- Existing `kconf.xml` and other example files are only overwritten if "Update examples" is checked.

## See Also

- `kcmlinst` — Unix installation
- `kconf` — Connection Manager configuration
