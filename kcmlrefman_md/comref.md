# Referencing Existing Objects

> How to get a second reference to an existing object.

## Syntax

```
OBJECT a = b
OBJECT Range = Sheet.Range()
OBJECT Excel = "Sheet1"
```

## Description

An `OBJECT LET` assigns an object reference to an object variable. The right-hand side can be:

- Another object variable (`OBJECT a = b`)
- A method that returns an object (`OBJECT Range = Sheet.Range()`)
- A string — the COM Moniker of a running object (`OBJECT Excel = "Sheet1"`)

**Important:** `OBJECT a = b` does **not** copy the object. It creates a second reference to the same underlying object. KCML uses reference counting internally — both references must be dropped (set to `NULL` or go out of scope) before the object is destroyed.

## Examples

```kcml
REM Get reference to a sub-object
DIM OBJECT Range, OBJECT Sheet
OBJECT Sheet = workbook.Sheets(1)
OBJECT Range = Sheet.Range("A1:D10")
```

```kcml
REM Moniker — bind to a running COM object by name
DIM OBJECT xl
OBJECT xl = "Sheet1"
```

```kcml
REM Second reference — both must be NULLed
DIM OBJECT a, OBJECT b
OBJECT a = CREATE "clientCOM", "Word.Application"
OBJECT b = a             : REM  second reference
OBJECT a = NULL          : REM  still alive; b holds it
OBJECT b = NULL          : REM  now destroyed
```

## See Also

- `cominst` — creating new objects with `CREATE`
- `comlife` — reference counting and lifetimes
- `comdecl` — declaring object variables
