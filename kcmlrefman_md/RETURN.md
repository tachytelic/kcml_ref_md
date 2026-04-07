# RETURN

> Returns from a subroutine to the caller, optionally returning a value.

## Syntax

```
RETURN
RETURN expr
```

## Description

Marks the end of a subroutine (`GOSUB` / `GOSUB'` / `DEFSUB` / `DEFFN`) and returns execution to the statement immediately after the call.

- Terminates any open `FOR … NEXT` loops within the subroutine.
- Removes local variables (`LOCAL DIM`) from scope.
- `RETURN expr` returns a value when the subroutine was called as a function expression.

The return type (alpha or numeric) must match the subroutine type:

```kcml
search$ = 'Next_rec$(stream)    : REM  alpha function — RETURN must return string
total   = 'Calculate(bal())     : REM  numeric function — RETURN must return number
```

### RETURN in $DECLARE / object method calls

`RETURN` is also a keyword prefix in `$DECLARE` calls and object method calls for output parameters:

```kcml
'KCMLCORBACreate("myObject", "Add", RETURN myhandle)
worksheet.Range("A9").Value(RETURN t)
worksheet.Range("A10:D11").Value(RETURN t())
```

## Examples

```kcml
REM Simple subroutine return
GOSUB 1000
PRINT "Back from subroutine"
$END

1000 PRINT "In subroutine"
     RETURN
```

```kcml
REM Return value from named subroutine
DIM result$50
result$ = 'GetName$(1)
PRINT result$
$END

DEFSUB 'GetName$(id)
  LOCAL DIM name$30
  name$ = "Customer " & STR(id)
  RETURN name$
END SUB
```

```kcml
REM Return from function key handler
REM  (RETURN resumes the interrupted LINPUT)
```

## Notes

- `RETURN` with a value from a subroutine called as a statement (not expression) is valid but the value is discarded.
- Bare `RETURN` from a numeric function returns 0; from an alpha function returns empty string.
- `RETURN CLEAR` clears the return stack entry without returning control to the caller.

## See Also

- `RETURN CLEAR` — clear return stack without returning
- `GOSUB` — call a subroutine by line number
- `GOSUBquote` — call a named subroutine
- `DEFSUB` — define a subroutine
