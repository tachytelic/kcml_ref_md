# FLD (in DEFRECORD)

> Defines a named field within a `DEFRECORD` structure, specifying its size, format, and position.

## Syntax

```
FLD fldname [= packspec]
FLD SKIP( numexpr )
FLD AT( numexpr )
```

Where `packspec` is a string expression or field definition.

Must appear inside a `DEFRECORD ... END RECORD` block.

## Description

`FLD` statements define the fields that make up a record structure. They are processed at resolve time. The field name is used (with a leading `.`) to access the field in code.

### Automatic positioning

Fields are laid out sequentially starting at byte 1. The start byte of each field is automatically calculated from the accumulated lengths of previous fields.

### Field naming

Inside a `DEFRECORD`, field names do **not** have the leading `.` (that dot is required everywhere else). Field names must be unique across all records in the program — two records cannot define the same field name.

After definition, a field is immutable — attempting to change its definition (e.g. `.a=(3,"UINT(4)")`) causes a recoverable runtime error.

### Type specifications (size/format)

The field type is specified in the same notation as `DIM`:

| Declaration | Type |
|-------------|------|
| `FLD a` | Numeric field in KCML internal format (8 bytes) |
| `FLD b$24` | String field, 24 bytes |
| `FLD c$(10)16` | Array field, 10 elements × 16 bytes (OCCURS(10)) |
| `FLD d$<<9>>30` | Language field, LANG(30,9) |
| `FLD e = "UINT(4)"` | 4-byte unsigned integer packed format |

### FLD SKIP and FLD AT

| Statement | Effect |
|-----------|--------|
| `FLD SKIP(n)` | Skip `n` bytes (pad/align) |
| `FLD AT(n)` | Position the next field at byte `n` |

### Scope

- `PUBLIC` (default if not prefixed): fields accessible from any program or library
- `PRIVATE`: fields visible only within the library
- `LOCAL` (with `LOCAL DEFRECORD`): fields visible only within the subroutine

You can find which record defines a field with `LIST R`.

## Example

```kcml
DEFRECORD TestRec
    FLD a                REM KCML internal numeric, 8 bytes
    FLD b$24             REM string, 24 bytes; starts at byte 9
    FLD c$(10)16         REM array of 10 × 16-byte strings
    FLD d$<<9>>30        REM language field LANG(30,9)
END RECORD
```

Field access:
```kcml
DIM rec$200
FLD(rec$.b$) = "Hello"
PRINT FLD(rec$.a)
```

### Record with packed binary fields

```kcml
DEFRECORD OrderHeader
    FLD OrderId = "UINT(4)"
    FLD OrderDate = "DATE"
    FLD CustomerCode$8
    FLD TotalAmount = "#####.##"
END RECORD
```

## Notes

- `FLD` is a resolve-time declaration — skipped at runtime.
- Fields do not allocate storage — storage comes from the DIM'd string variable holding the record.
- Use `LIST R` in the Workbench to show which record defines a given field.
- Two records cannot define the same field name (use `PRIVATE` in libraries to avoid clashes).

## See Also

- `DEFRECORD` — define a record structure
- `FLD(` — access a field within a variable
- `DIM` — declare storage for a record variable
- `LOCAL DEFRECORD` — record with subroutine-local scope
