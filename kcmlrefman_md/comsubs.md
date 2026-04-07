# Objects and Subroutines

> How to pass objects to and return objects from KCML subroutines.

## Description

Objects can be passed as arguments to subroutines and returned from them. Both the call site and the `DEFSUB` definition must use the `OBJECT` keyword prefix on the object parameter.

Objects can only be passed into `DEFSUB` statements — not `DEFFN` functions.

## Passing an object to a subroutine

```kcml
'DoExcelStuff(OBJECT Sheet)

DEFSUB 'DoExcelStuff(OBJECT s)
    REM s is a local reference to Sheet
    PRINT s.Name$
END SUB
```

## Returning an object from a subroutine

```kcml
OBJECT Sheet = 'CreateExcelObject()

DEFSUB 'CreateExcelObject()
    LOCAL DIM OBJECT a
    OBJECT a = CREATE "clientCOM", "Excel.Application"
    REM ...
    RETURN OBJECT a
END SUB
```

The `RETURN OBJECT` form returns the object reference to the caller.

## Object lifetime in subroutines

Because subroutine parameters are local, the object reference lifetime is limited to the lifetime of the subroutine call. When `RETURN` is executed, local object variables go out of scope and their reference counts are decremented. Use `RETURN OBJECT` to pass the reference back to the caller before the local scope ends.

## Notes

- `OBJECT` prefix is required on both the `GOSUB`/call argument and the `DEFSUB` parameter.
- `DEFFN` (function) cannot receive object parameters — use `DEFSUB` instead.
- A `LOCAL DIM OBJECT` in a subroutine is automatically released on return unless returned via `RETURN OBJECT`.

## Examples

```kcml
DIM OBJECT ws
OBJECT ws = workbook.ActiveSheet
'ProcessSheet(OBJECT ws)

DEFSUB 'ProcessSheet(OBJECT s)
    LOCAL DIM OBJECT cell
    OBJECT cell = s.Range("A1")
    PRINT cell.Value$
    OBJECT cell = NULL
END SUB
```

## See Also

- `comdecl` — declaring object variables
- `comlife` — object lifetimes
- `comref` — object references
- `commethod` — calling object methods
