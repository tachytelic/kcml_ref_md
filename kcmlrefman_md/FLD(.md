# FLD(

> Accesses a named substring (field) within an alpha variable, defined by a field variable's start position and length.

## Syntax

```
FLD( alpha_variable . field_variable )
```

From KCML 6.20+, nested form:
```
FLD( alpha_variable . field_variable1 . field_variable2 )
```
(equivalent to `FLD(FLD(alpha_variable.field_variable1).field_variable2)`)

| Element | Description |
|---------|-------------|
| `alpha_variable` | The string variable holding the data |
| `field_variable` | A field variable (starts with `.`) that defines start position and length |

## Description

`FLD(` defines a substring within an alpha variable using the position and length stored in a field variable. It can appear on the left (assignment target) or right (value source) of an assignment.

Field variables are declared with:
- `DEFRECORD ... FLD ... END RECORD` (preferred)
- `.field$ = (start, length)` in a LET statement
- `READ .field$ : DATA (start, length)` from a DATA statement

```kcml
.description$ = (2, 16)
```
This defines `.description$` as starting at byte 2, length 16 bytes.

### Using FLD( vs STR(

`FLD(buffer$.description$)` and `STR(buffer$, 2, 16)` are equivalent, but:
- `FLD(` is more readable (the field name documents intent)
- `FLD(` executes faster
- `FLD(` allows the layout to be defined in one place (`DEFRECORD`)

### Numeric field variables

A field variable can define a **numeric** field within a string — e.g. `(start, "UINT(4)")` for a 4-byte unsigned integer. Reading such a field via `FLD(` returns the decoded numeric value.

## Examples

### Basic field access

```kcml
DEFRECORD CustomerRec
    FLD CustId$6
    FLD CustName$30
END RECORD

DIM rec$80
FLD(rec$.CustName$) = "Smith, John"
PRINT FLD(rec$.CustId$)
```

### Field defined via assignment

```kcml
.description$ = (2, 16)
result$ = FLD(buffer$.description$)
```

Equivalent to:
```kcml
result$ = STR(buffer$, 2, 16)
```

### Nested FLD (KCML 6.20+)

```kcml
FLD(a$.b$.c)
```

is equivalent to:
```kcml
FLD(FLD(a$.b$).c)
```

## Notes

- `FLD(` is faster than `STR(` for structured data access.
- Field variables must be defined (initialised) before use — an undefined field variable causes a runtime error.
- Numeric field variables allow KCML to automatically decode packed binary, BCD, or other numeric formats from raw byte strings.

## See Also

- `FLD` (in DEFRECORD) — define fields within a record structure
- `DEFRECORD` — define a named record type
- `STR(` — access substrings by numeric position and length
- `DIM` — declare field variables with `.field$=(pos, len)` syntax
