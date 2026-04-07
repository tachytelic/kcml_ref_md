# Field Variables

> Named sub-string descriptors that give symbolic names to fixed offsets and lengths within string buffers — a faster and more readable alternative to `STR(` everywhere.

## Overview

A field variable is a symbol that records the *position* and *length* of a sub-string within a larger string buffer. Once defined, the field variable can be applied to any string variable using the `FLD(` function, eliminating the need to hard-code byte offsets throughout your code.

Compare these two equivalent statements:

```kcml
STR(paint$,6,5) = "Blue "     REM old style - magic numbers
FLD(paint$.color$) = "Blue "  REM field style - self-documenting
```

Fields are not just for readability: KCML can apply a field more efficiently than repeatedly calling `STR(`, which matters in tight loops over large records.

Numeric field variables go further — they treat the sub-string as a packed or formatted number, so `FLD(` automatically unpacks on read and repacks on write.

## Defining Field Variables

### In a DEFRECORD block (recommended)

The cleanest way to define fields is inside a `DEFRECORD` / `END RECORD` block. KCML calculates offsets automatically — you only specify lengths.

```kcml
DEFRECORD MyRec
  FLD part$5          REM 5-byte alpha field
  FLD color$5         REM 5-byte alpha field (follows part$)
  FLD price="-###.##" REM numeric field with $FORMAT image
END RECORD
```

Fields defined inside `DEFRECORD` do not need a leading period; the record name provides the namespace.

### Standalone field variables (must start with `.`)

Outside a `DEFRECORD`, field variable names must begin with a period. They can be initialized in three ways:

**In a DIM statement (resolved at load time):**

```kcml
DIM .part$ = (1,5), .color$ = (6,5), .price$ = (11,5)
```

**In a LET statement (set at runtime):**

```kcml
.price$ = (11,5)
.@types$(1) = (16,10)    REM array of field variables also supported
```

**From a DATA statement (KCML calculates start positions automatically):**

```kcml
READ .part$, .color$, .price$, .@type$(1)
DATA (1,5),(,5),(,5),(,10)
```

When the start position is omitted in a DATA statement (i.e. `(,5)`), KCML picks up where the previous field ended. This makes it easy to lay out a record without arithmetic.

### Numeric field variables

Numeric fields describe how a number is encoded within the string. The image can be a `PACK` format or a `$FORMAT` string:

```kcml
.value = (1,"-####.###")     REM $FORMAT image - length implied by image
.count = (start, "B4")       REM PACK image starting at variable 'start'
```

When used in an expression, `FLD(` automatically unpacks the number. When assigned, it automatically repacks.

## Using Field Variables

### Reading and writing alpha sub-strings

```kcml
DIM record$20
.name$ = (1,5)
.code$ = (6,5)

FLD(record$.name$) = "Alan "
FLD(record$.code$) = "AB543"
PRINT FLD(record$.name$), FLD(record$.code$)
```

**Output:**
```
Alan  AB543
```

### Reading and writing numeric sub-strings

```kcml
DIM record$20
.count = (1,"-####")

FLD(record$.count) = 42
PRINT FLD(record$.count)
```

**Output:**
```
42
```

Arithmetic on numeric fields works in-place:

```kcml
FLD(record$.count) = FLD(record$.count) + 1
```

Shorthand operators (`+=`, `-=`, etc.) also work, but prefix/postfix operators (`++`, `--`) force an unpack-change-repack cycle on every use — avoid them on fields in hot loops.

### Expressions using fields

Alpha fields are valid wherever an alpha expression is valid; numeric fields are valid wherever a numeric expression is valid:

```kcml
total = FLD(record$().count) * discount
```

### Packing and unpacking whole arrays

An entire numeric array can be unpacked from a string buffer in one operation:

```kcml
DIM display(3)
.form = (1,"P2")
record$ = HEX(0102 1234 9999)
display() = FLD(record$.form)
PRINT display()
```

**Output:**
```
102
1234
9999
```

The `.form` specification is applied repeatedly, extracting successive packed values until the array is filled.

The reverse operation packs an array back into a string:

```kcml
FLD(record$.form) = display()
```

Individual packed elements can be accessed with the `<n>` subscript:

```kcml
test = FLD(record$.form<2>)   REM extracts the second packed element
```

## Inspecting Field Variables

### POS(, LEN( and PACK(

```kcml
DIM .part$ = (1,5), .color$ = (6,5)
PRINT POS(.color$), LEN(.color$)
```

**Output:**
```
6    5
```

`PACK(` returns the pack format string for numeric fields.

### Array fields and DIM(

```kcml
DIM .totals(15), .discounts(10,20)
PRINT DIM(.totals(),1), DIM(.discounts(),2)
```

**Output:**
```
15    20
```

### LIST DIM

`LIST DIM` lists all variables including their field specifications. Field variables appear with a `D` type marker.

## Passing Field Variables to Subroutines

Field variables can be passed to `DEFSUB` subroutines:

```kcml
'qsort(.name$, (2,"#.#"), (9,9), .ab())
```

The `DEFSUB` signature must declare matching field variable parameters:

```kcml
DEFSUB 'qsort(.nm$, .num, .type$, .totals())
```

Parameters declared inside the `DEFSUB` parentheses are automatically local.

## Testing Field Variables in Conditions

Field variables can be compared directly in `IF` statements:

```kcml
IF (.name$ == .owner$) THEN ...
END IF

IF (.legs$ <> (5,9)) THEN ...
```

## Notes

- **Search order for undefined fields:** If a field is not found in the executing program, KCML searches loaded libraries in order before reporting an error. This also applies to `SELECT @PART` process globals.
- **Avoid `++`/`--` on numeric fields** — the operator forces an unpack/repack on every use, hurting performance.
- **`MAT REDIM` restriction:** You cannot `MAT REDIM` a locally dimensioned field variable to a larger size.
- **`DEFRECORD` is preferred** over raw `(offset, length)` tuples for any record with more than a couple of fields. It eliminates offset arithmetic entirely and makes layout changes easy.
- See also: `DEFRECORD`, `FLD`, `FLD(`, `DATA`, `LEN(`, `POS(`, `READ`, `STR(`
