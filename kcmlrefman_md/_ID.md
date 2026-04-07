# #ID

> Returns the KCML installation-specific identifier number (1–65535).

## Syntax

```
#ID
```

## Description

Returns a number in the range 1–65535 identifying the KCML installation. Valid wherever a numeric expression is valid.

- On **DOS**: taken from the Network Interface Card (NIC) address. If no NIC is present, the hard-disk serial number is used.
- On **all other platforms**: identical to `#GOLDKEY`.
- Can be overridden on any platform by setting the `KCML_ID` environment variable to the desired value.

## Examples

```kcml
DIM id
id = #ID
PRINT id
```

```kcml
REM Override: if KCML_ID is set in the environment, that value is returned
PRINT #ID
```

## Notes

- On modern Unix/Linux KCML 5+, `#ID` and `#GOLDKEY` return the same value.
- `KCML_ID` takes precedence over the hardware-derived value on all platforms.

## See Also

- `#GOLDKEY` — installation licence number (same as `#ID` on non-DOS)
