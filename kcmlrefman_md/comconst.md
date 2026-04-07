# COM Constants and Enumerations

> Using symbolic constants defined by COM type libraries in KCML.

## Description

COM type libraries can define symbolic constants and enumerations (lists of legal values for properties or method arguments). In KCML, these must be prefixed with the `ENUM` keyword to distinguish them from regular KCML variables:

```kcml
rsTable.CursorType = ENUM .adOpenKeyset
record.Open("Customers", OBJECT connect, ENUM adOpenForwardOnly)
```

## Rules

- `ENUM` constants can only be used in **method and property expressions** on the object that defines them.
- They cannot be used outside the object context — KCML treats them as symbols and does not know their numeric value.
- They cannot be converted to or from regular KCML numeric variables.

## Browsing available enumerations

Use the Object Browser in the KCML Workbench to inspect the enumerations defined by a COM object's type library. Each enumeration member is listed with its name and value.

## Examples

```kcml
DIM OBJECT rs
OBJECT rs = CREATE "clientCOM", "ADODB.Recordset"
rs.CursorType = ENUM adOpenKeyset
rs.LockType = ENUM adLockOptimistic
rs.Open("SELECT * FROM Orders", OBJECT conn)
```

## See Also

- `commethod` — passing `ENUM` arguments to methods
- `comautomation` — VBA property/method syntax
- `combrowse` — Object Browser for inspecting type libraries
