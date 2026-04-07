# #GOLDKEY

> Returns the KCML installation-specific licence number (1–65535).

## Syntax

```
#GOLDKEY
```

## Description

Returns a number in the range 1–65535 that is specific to the KCML installation. Used to ensure that an application will only work with a particular licensed copy of KCML. Valid wherever a numeric expression is valid.

The source of the value depends on the licence type and platform:

| Dongle/Licence | OS | KCML Version | Value source |
|---|---|---|---|
| Branded | All | KCML 5+ | Taken from `lic.txt` licence file |
| Parallel DK12 | Unix only | KCML 4 | Inode number of `TERMFILE` |
| Parallel DK12 | DOS (single user) | KCML 4 | NIC address; or hard-disk serial if no NIC |
| Parallel DK2 / PCMCIA DK38 | Unix / Networked DOS | KCML 4 | Taken from the dongle |
| Serial DK96 | Unix only | KCML 4 | Taken from the dongle |

## Examples

```kcml
DIM key
key = #GOLDKEY
PRINT key
```

```kcml
REM Licence-lock an application
IF #GOLDKEY <> 12345 THEN PRINT "Unlicensed copy" : $END
```

## Notes

- On KCML 5+, the value is read from `lic.txt`.
- `#ID` returns the same value as `#GOLDKEY` on all non-DOS platforms.
- The value can be used in application licence checks and serialisation.

## See Also

- `#ID` — same value on most platforms; originally NIC-based on DOS
- `$SER` — serial number string from the licence file
