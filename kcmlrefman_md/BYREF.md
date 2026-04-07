# BYREF

> Passes a subroutine argument by reference rather than by value, so changes made inside the subroutine are reflected in the caller's variable.

## Syntax

```
'routine(BYREF arg [, ...])

DEFSUB 'routine(BYREF param [, ...])
```

`BYREF` must be specified in **both** the call site and the `DEFSUB` declaration.

## Description

By default, KCML subroutine arguments are passed by value — the subroutine gets a local copy and changes do not propagate back to the caller. `BYREF` changes this so the subroutine receives a reference to the original variable; modifications made inside the subroutine are immediately visible to the caller.

`BYREF` can be applied to numeric, string, and label arguments.

### Compared to SYM(

`BYREF` achieves the same effect as passing `SYM(variable)`, but without requiring special constructs inside the subroutine body when reading or writing the variable. Use `BYREF` in preference to `SYM(` for this purpose.

### With $DECLARE (C/external functions)

`BYREF` can also be used with `$DECLARE`d external functions to pass a pointer to a number rather than the value. Strings are always passed as pointers, so `BYREF` is not needed for string parameters in that context.

Note: `RETURN` was previously used as a synonym for `BYREF` in external function calls but is now deprecated; use `BYREF`.

## Example

```kcml
aValue = 10
aString$ = "Hello"
'aRoutine(BYREF aValue, BYREF aString$)
PRINT aValue      REM prints 110
PRINT aString$    REM prints Hello World!

...

DEFSUB 'aRoutine(BYREF Total, BYREF Name$)
    Total += 100
    Name$ = & " World!"
RETURN
```

After the call, `aValue` is 110 and `aString$` is `"Hello World!"`.

## Notes

- Both the call (`GOSUB'`) and the definition (`DEFSUB`) must have `BYREF` on the relevant parameters; mismatching them causes a runtime error.
- Passing a literal or expression with `BYREF` is not valid — the argument must be a variable.

## See Also

- `DEFSUB` — define a structured subroutine
- `GOSUB'` — call a structured subroutine
- `RETURN` — return from a subroutine (also deprecated as a synonym for BYREF)
- `SYM(` — obtain a symbol reference to a variable
