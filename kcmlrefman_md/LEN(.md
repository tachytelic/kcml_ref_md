# LEN(

> Returns the content length of an alpha variable (excluding trailing spaces) or the defined size of a field variable.

## Syntax

```
LEN( alpha_expression )
LEN( field_variable )
LEN( STR( alpha_variable ) )
```

Returns a numeric value. Valid wherever a numeric function is legal.

## Description

`LEN(` returns the length in **bytes** of the content of an alpha expression, after stripping trailing spaces:

- If a variable contains only spaces, returns **1** (not 0).
- Counts **bytes**, not characters — for UTF-8 strings use `ULEN8(` instead.

### Special forms

| Form | Returns |
|------|---------|
| `LEN(alpha_variable)` | Content length (trailing spaces stripped) |
| `LEN(STR(alpha_variable))` | Defined (DIM'd) length of the variable |
| `LEN(.field_variable)` | Defined byte-length of the field |

## Examples

```kcml
: DIM a$20
: a$ = "Hello"
: PRINT "LEN(Hello$)="; LEN(a$)       REM 5
: a$ = "  "
: PRINT "LEN(two spaces)="; LEN(a$)   REM 1
: PRINT "LEN(STR(a$))="; LEN(STR(a$)) REM 20
: $END
```

Output:
```
LEN(Hello$)= 5
LEN(two spaces)= 1
LEN(STR(a$))= 20
```

### Checking defined size

```kcml
DIM a$32
IF (LEN(STR(a$)) <> 32) THEN PANIC   REM assert buffer is 32 bytes
```

### Field variable length

```kcml
.fred$ = (1, 16)
.value = (17, "-###.##")
First = LEN(.fred$)     REM = 16
Second = LEN(.value)    REM = length of the numeric pack format
```

Use `POS(` for the start position of a field variable, and `PACK(` for its packing specifier.

### Typical expression use

```kcml
Red = 100 + LEN(Actual$)
Green = LEN(.Field_Name$)
```

## Notes

- Trailing spaces are **not counted** — use `LEN(STR(var))` to get the total allocated size.
- A string of all spaces returns `LEN = 1`, not 0.
- For UTF-8 encoded strings, use `ULEN8(` to count characters rather than bytes.

## See Also

- `STR(` — extract substring or get the raw allocated area
- `POS(` — start position of a field variable
- `PACK(` — packing specifier of a field variable
- `ULEN8(` — length in UTF-8 characters
