# SPACE / SPACEF / SPACEK / SPACEV / SPACEW (obsolete)

> Legacy functions that return available memory information. Obsolete in KCML.

## Description

These functions date from BASIC-2 with its fixed memory partitions. In KCML with dynamic memory, they return fixed arbitrary values and should **not be used in new programs**.

| Function | Original purpose | KCML returns |
|----------|-----------------|-------------|
| `SPACE` | Available memory in partition (bytes) | 57344 (56k), or value of `SPACE` env var |
| `SPACEF` | Available free space | 1048576 (1MB) |
| `SPACEK` | Fixed partition size | 99, or value of `SPACEK` env var |
| `SPACEP` | Space available for programs | 57344 |
| `SPACEV` | Space available for data | 57344 |
| `SPACEW` | Available free space | 1048576 (1MB) |

The `SPACE` and `SPACEK` environment variables can override the returned values for backward compatibility with BASIC-2 programs that test these values.

To inspect actual memory usage, use `LIST SPACE`.

## Notes

- Do not use these in new code.
- See `NPLcompat` for the full list of backward-compatibility features.

## See Also

- `LIST SPACE` — display actual memory usage
- `NPLcompat` — BASIC-2C / NPL compatibility features
