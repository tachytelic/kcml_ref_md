# Compound Object References

> How to chain object property and method calls in a single expression.

## Description

When navigating a hierarchy of objects, it is not necessary to extract each object reference separately. Compound expressions can chain multiple method/property calls:

```kcml
REM Verbose form:
OBJECT b = a.List()
OBJECT c = b.Next()

REM Compound form (equivalent):
OBJECT c = a.List.Next()
```

Compound expressions can be arbitrarily long:

```kcml
OBJECT a = A.B.C(10, 20).D(1).E("hello")
```

## Performance considerations

Each evaluation of a compound expression requires KCML to traverse the full chain. If you access the same sub-object repeatedly, it is faster to cache a direct reference:

```kcml
REM Better — cache the font object:
FOR OBJECT ww IN worksheet.Range("A14:F18")
    OBJECT font = ww.Font
    font.ColorIndex = i++
    font.Bold = TRUE
NEXT OBJECT ww

REM Slower — re-traverses the chain each time:
FOR OBJECT ww IN worksheet.Range("A14:F18")
    ww.Font.ColorIndex = i++
    ww.Font.Bold = TRUE
NEXT OBJECT ww
```

## See Also

- `commethod` — calling object methods
- `comprops` — object properties
- `comenum` — enumerating collections
- `comref` — object references and assignment
