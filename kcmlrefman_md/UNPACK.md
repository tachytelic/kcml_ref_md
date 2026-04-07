# UNPACK

> Unpacks BCD-encoded numeric values from an alpha variable back to numeric variables.

## Syntax

```
UNPACK (image) alpha_var TO numeric_var [, numeric_var ...]
```

## Description

The inverse of `PACK`. Reads packed BCD data from `alpha_var` and converts it back to numeric values using the same image specification used when packing.

Values are unpacked sequentially from the beginning of the alpha variable. If multiple numeric variables are listed, they are filled in order from consecutive packed fields.

## Examples

```kcml
REM Round-trip pack/unpack
DIM price$4, amount
amount = 1234.56
PACK "######.##", amount TO price$
UNPACK (######.##) price$ TO amount
PRINT amount        : REM  1234.56
```

```kcml
UNPACK (###.###) file$ TO total
UNPACK (+###.##) FLD(record$.type$) TO type
UNPACK (form$) file$ TO price()     : REM  image in a variable
```

## Notes

- The **same image** must be used for both `PACK` and `UNPACK`.
- The image can be a literal string in parentheses or a variable.
- For field variables with a declared pack format, use `PACK(` function to retrieve the specifier.

## See Also

- `PACK` — pack numeric to BCD string
- `PACKfn` — `PACK(` function: return field packing specifier
