# Object Properties

> How to read and write properties on KCML objects.

## Description

Objects can have properties (called attributes in CORBA) that can be inspected or modified. Some properties are read-only.

Numeric properties:

```kcml
count = Table.RowCount
```

String properties — use a trailing `$`:

```kcml
m$ = Obj.HelpText$
```

A property can be used anywhere an equivalent variable would be allowed.

## Setting properties

```kcml
app.Visible = TRUE
worksheet.Name$ = "Sheet1"
Table.RowCount = 10
```

## Notes

- Properties are implemented internally as special methods. KCML handles the method call transparently.
- Use the Object Browser in the KCML Workbench to see all properties available for an object.
- String properties require a trailing `$` for KCML grammatical reasons — this differs from VB/VBA syntax.
- Some properties may be read-only; attempting to write them will result in an object error (`O30`).

## See Also

- `commethod` — calling object methods
- `comconst` — `ENUM` constants for property values
- `combrowse` — Object Browser
- `comautomation` — VBA property syntax differences
