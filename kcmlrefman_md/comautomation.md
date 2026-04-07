# COM Automation Issues

> Practical notes on using Microsoft COM Automation (OLE Automation) from KCML.

## Description

COM Automation (formerly OLE Automation) is the Microsoft standard for VBA/VBScript-style programmable objects that expose the `IDispatch` interface. KCML can control any Automation-compliant object.

## Properties and methods

KCML exposes VB-style property syntax where it fits KCML grammar:

```kcml
app.Visible = TRUE           : REM  Set property
name$ = worksheet.Name$      : REM  Get string property (note trailing $)
```

Properties can also be accessed via the underlying method call:

```kcml
app.Visible(TRUE)
name$ = worksheet.Name$()
```

**String properties require a trailing `$`** for grammatical reasons in KCML.

## VBA lvalue functions

In VBA, functions can appear on the left-hand side of an assignment (e.g. setting a default template path in Word). KCML does not support functions as lvalues. Use the method call form with the new value as the last argument:

```kcml
REM VBA:  app.Options.DefaultFilePath(wdUserTemplatesPath) = "\mytemplates"
REM KCML equivalent:
app.Options.DefaultFilePath(ENUM wdUserTemplatesPath, "\mytemplates")
```

## Default properties

VB supports a default property (e.g. `.Value` for an Excel cell) that can be omitted. KCML does **not** support default properties — all properties must be explicitly specified.

## Word and Excel

Word and Excel are implemented as `.EXE` executables rather than `.DLL` libraries. They start hidden; make them visible if you need user interaction:

```kcml
DIM OBJECT app
OBJECT app = CREATE "clientCOM", "Word.Application"
app.Visible = TRUE
REM ... use Word ...
app.Quit()
OBJECT app = NULL
```

**Important:**
- Word/Excel will **not** terminate automatically when the last KCML object reference is dropped — call `.Quit()` explicitly.
- Word will not shut down while any of its sub-objects are still referenced — set all sub-objects to `NULL` before calling `.Quit()`.

## See Also

- `ObjCOM` — COM client overview
- `comdecl` — declaring object variables
- `cominst` — instantiating objects with `CREATE`
- `commethod` — calling object methods
- `comprops` — accessing object properties
- `comconst` — `ENUM` constants
- `comlife` — object lifetime and `NULL`
