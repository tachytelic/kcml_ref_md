# Enumerating Object Collections

> How to iterate over a collection of objects with `FOR OBJECT`.

## Syntax

```
FOR OBJECT varname IN collection_expr
    ...
NEXT OBJECT varname
```

## Description

Some objects represent collections — arrays of sub-objects. The `FOR OBJECT` statement iterates over each element in a collection, assigning it to the loop variable in turn.

`FOR OBJECT` works with any collection object, including KCML's built-in form collections.

## Examples

```kcml
REM ADO: iterate columns in a recordset row
DIM OBJECT a
FOR OBJECT a IN rsTable.Fields()
    PRINT a.Name$, a.Value$
NEXT OBJECT a
```

```kcml
REM Double the height of every control on a form
DIM OBJECT c
FOR OBJECT c IN Form1
    c.Height = c.Height * 2
NEXT OBJECT c
```

```kcml
REM Excel: iterate cells in a range
DIM OBJECT ww, OBJECT font
FOR OBJECT ww IN worksheet.Range("A1:D4")
    OBJECT font = ww.Font
    font.Bold = TRUE
NEXT OBJECT ww
```

## Notes

- The loop variable must be declared with `DIM OBJECT` or `LOCAL DIM OBJECT`.
- Special enumeration properties for form elements (listboxes, tabs, trees): `First`, `Next`, `SelectedFirst`, `SelectedNext`, `Index`, `TabFirst`, `TabNext`, `Parent`, `Child`.
- See `comcompound` for performance advice when accessing nested properties inside a loop.

## See Also

- `comref` — object references
- `comcompound` — compound object expressions
- `comforms` — form control enumeration
- `commethod` — object methods
