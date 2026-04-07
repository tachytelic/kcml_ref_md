# PACK( (function)

> Returns the packing specifier string for a declared field variable.

## Syntax

```
result$ = PACK(.field_var)
```

## Description

`PACK(` is a function (note the dot before the field name) that returns the format/packing specifier string associated with a field variable that was declared with a BCD pack image. This lets you inspect how a field was declared at runtime.

The returned string describes the numeric format of the field (e.g. number of digits, decimal places).

Not to be confused with the `PACK` statement which performs BCD packing.

## Examples

```kcml
REM Inspect the format of a packed field
DIM rec$50
DIM price$ = FLD(rec$, 10, 4) FORMAT "####.##"
DIM spec$20
spec$ = PACK(.price$)
PRINT spec$              : REM  returns packing specifier for price$
```

```kcml
REM Use PACK( to dynamically determine field format before unpacking
DIM packspec$20
packspec$ = PACK(.price$)
PRINT "Format: "; TRIM(packspec$)
```

## Notes

- The argument must be a field variable (declared with `FLD(` or a sub-field declaration), not an ordinary string variable.
- Returns an empty string if the field has no pack format.
- Complement to `POS(.field)` (start position) and `LEN(.field)` (byte length).

## See Also

- `PACK` — statement: pack a numeric value to BCD
- `UNPACK` — unpack BCD to numeric
- `FLD(` — declare a field within a record string
- `POS(` — start position of a field
- `LEN(` — size of a field
