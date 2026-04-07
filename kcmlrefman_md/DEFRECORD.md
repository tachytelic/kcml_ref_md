# DEFRECORD

> Defines a named record structure (similar to a C struct) using field variables.

## Syntax

```
[PRIVATE | PUBLIC | LOCAL] DEFRECORD recordname
    FLD fldname [= packspec]
    ...
END RECORD
```

| Keyword | Effect |
|---------|--------|
| `PRIVATE` | Record and fields visible only within the library |
| `PUBLIC` | Record and fields accessible from foreground and other libraries (default) |
| `LOCAL` | Record has local scope inside a `DEFSUB` |
| `packspec` | Optional string expression for packed field format |

## Description

`DEFRECORD` defines a structured record type. Fields within the record are defined with `FLD` statements between `DEFRECORD` and `END RECORD`. A record variable is then declared as a string with `DIM` or `COM` to hold the data, and fields are accessed with the `FLD()` operator.

`DEFRECORD` is a **resolve-time** declaration — it is skipped at runtime. It does not allocate any storage; storage is allocated when a variable of the record's size is declared.

**Benefits of DEFRECORD:**
- Clear structure for record layouts
- Field names are defined once and reused
- Compatible with data-aware form binding
- Can be passed as a single `BYREF` argument to functions

### Nesting and scope

- `DEFRECORD` blocks cannot nest.
- `DEFRECORD` must normally be outside subroutines. Using the `LOCAL` prefix allows it inside a `DEFSUB`, giving it subroutine scope (fields are only visible within that subroutine and any nested subroutines).
- Two `LOCAL DEFRECORD` blocks in separate subroutines can reuse the same field names without conflict.

### Executable statements inside DEFRECORD

`REM` statements and other executable statements may appear inside the block but are never executed.

## Example

```kcml
DEFRECORD CustomerRec
    FLD CustId   = (1, 6)
    FLD CustName = (7, 30)
    FLD CustBal  = (37, "####.##")
END RECORD

DIM rec$50
```

Access fields:
```kcml
FLD(rec$.CustName) = "Smith"
PRINT FLD(rec$.CustId)
```

## Notes

- `DEFRECORD` is recommended for any structured data stored in a string variable — it makes field layout explicit and maintainable.
- Structures passed as a single `BYREF` argument reduce function parameter counts and avoid dependency on out-of-scope variables.

## See Also

- `FLD(` — access fields within a record
- `DIM` — declare storage for a record variable
- `BYREF` — pass a record variable by reference to a subroutine
- `DEFSUB` — subroutine definition (LOCAL DEFRECORD used inside DEFSUB)
