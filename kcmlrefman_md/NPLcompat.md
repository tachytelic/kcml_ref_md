# BASIC-2C / NPL Compatibility

> Reference for KCML statements and functions supported for compatibility with BASIC-2C and NPL.

## Description

The following KCML features exist solely for backward compatibility with BASIC-2C and NPL programs:

| Statement / Function | Purpose |
|---------------------|---------|
| `$DEMO` | Demo mode |
| `$DET(` | Determinant (legacy form) |
| `$ENVIRONMENT` | Environment access (legacy) |
| `$KEEPREMS` | Keep remarks when compiling |
| `$NETID` | Network ID |
| `$NUMBERS` | Number formatting |
| `$OBJECT(` | Object handling (legacy) |
| `$PRINTER` | Printer control |
| `$PROGRAM` | Program name |
| `$SOURCE(` | Source code access |
| `SPACEF` | Space function |
| `SPACEK` | Space K function |
| `SPACEP` | Space P function |
| `SPACEV` | Space V function |
| `SPACEW` | Space W function |

The `SPACE*` function return values can be overridden with the `SPACE` and `SPACEK` environment variables (for backward compatibility with BASIC-2 software that tests these before certain operations).

## Notes

- These features are available but should not be used in new KCML programs.
- See the individual reference pages or the KCML compatibility guide for details.

## See Also

- `EnvVars` — SPACE, SPACEK environment variables
