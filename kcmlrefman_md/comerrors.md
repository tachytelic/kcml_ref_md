# Object Error Handling

> How KCML handles errors from COM, CORBA, and SOAP objects.

## Description

Any object error — such as a COM `HRESULT` not equal to `S_OK`, or a CORBA exception like `OBJECT_NOT_EXIST` — causes an execution error inside KCML that can be trapped with standard KCML error handling.

**Error code:** `O30` — recoverable object error.

KCML returns the COM/CORBA/SOAP error message text as the KCML error text, making it available to error handlers.

## Error handling

Use `ON ERROR` or `ERROR` clauses to catch object errors:

```kcml
DIM OBJECT rs
OBJECT rs = CREATE "clientCOM", "ADODB.Recordset"

ON ERROR DO
    PRINT "Object error O30: "; $ERRTEXT
END DO

rs.Open("SELECT * FROM Orders", OBJECT conn)
```

```kcml
REM Using ERROR clause on a method call
rs.MoveNext() ERROR PRINT "Recordset error: "; $ERRTEXT
```

## Notes

- All object-type errors (COM, CORBA, SOAP) map to error code `O30`.
- `$ERRTEXT` contains the full error message from the underlying object framework.
- Standard KCML error recovery applies — execution can continue after an `ON ERROR DO ... END DO` block.

## See Also

- `ON_ERROR` — `ON ERROR` error handler
- `error-handling` — KCML error handling reference
- `cominst` — object instantiation
- `commethod` — object method calls
- `ObjCOM` — COM client overview
