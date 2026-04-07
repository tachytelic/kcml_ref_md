# NULL (object release)

> Releases an object reference, freeing any associated resources.

## Syntax

```
OBJECT objname = NULL
```

## Description

Sets an object variable to the null/unassigned state, releasing any COM, SOAP, CORBA, or dyndom object it references. After the assignment the variable holds no object and any attempt to call methods on it will raise an error.

Useful for:
- Explicitly releasing COM objects before a program exits
- Freeing a large DOM document when it is no longer needed
- Resetting an object variable before reassigning it to a new instance

## Examples

```kcml
REM Create a DOM parser, use it, then release it
OBJECT parser
CREATE "DOM" TO parser
REM ... use parser ...
OBJECT parser = NULL     : REM release DOM object and free memory
```

```kcml
REM Release a COM object
OBJECT xl
CREATE "Excel.Application" TO xl
REM ... automate Excel ...
OBJECT xl = NULL
```

## Notes

- `OBJECT var = NULL` is the correct KCML idiom; do not use bare assignment (`var = NULL`).
- Releasing a NULL object that is already null is harmless.
- For COM objects, this triggers the COM release sequence — the object's reference count is decremented.

## See Also

- `CREATE` — create an object instance
- `OBJECT` — declare an object variable
- `$DECLARE` — declare external (Win32/DLL) functions
