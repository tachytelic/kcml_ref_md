# Instantiating Objects

> How to create object instances with the `CREATE` statement.

## Syntax

```
OBJECT objname = CREATE strexpr1, strexpr2 [, extra_args...]
```

## Description

`CREATE` instantiates an object and assigns it to an object variable. The object variable must have been declared with `DIM OBJECT` or `LOCAL DIM OBJECT`.

- `strexpr1` — object type: `"clientCOM"`, `"serverCOM"`, `"Corba"`, or `"SOAP"`
- `strexpr2` — object identifier (see below per type)

## COM objects

For COM, `strexpr2` is a ProgID or CLSID (GUID string):

```kcml
DIM OBJECT doc, OBJECT rs
OBJECT doc = CREATE "clientCOM", "Word.Basic"
OBJECT rs  = CREATE "serverCOM", "ADODB.Recordset"
OBJECT rs  = CREATE "serverCOM", "{00000535-0000-0010-8000-00AA006D2EA4}"
```

- `"clientCOM"` — object runs in the client process (in-process)
- `"serverCOM"` — object runs as a separate process (out-of-process)

## CORBA objects

For CORBA, `strexpr2` is the object name in the naming service or an IOR:

```kcml
DIM OBJECT Add
REM With ORB address specified in CREATE:
OBJECT Add = CREATE "Corba", "Add", "-ORBNamingAddr", "inet:evb:9876"

REM Or with kcml started with -q flag:
REM  kcml -q -ORBNamingAddr inet:evb:9876
OBJECT Add = CREATE "Corba", "Add"

REM Full naming path:
OBJECT Add = CREATE "Corba", "kerridge/my_context/Add/Object/"
```

Only one ORB connection is supported — `CREATE` arguments for the ORB are ignored after the first connection is established. KCML defaults to context `"kerridge"` and type `"my_context"` if not fully specified.

## SOAP objects

```kcml
DIM OBJECT svc
OBJECT svc = CREATE "SOAP", "http://example.com/service?wsdl"
```

## Notes

- An object variable starts at `NULL` and becomes non-NULL after `CREATE`.
- Only one ORB connection per KCML process.
- To release an object, set it to `NULL` (see `comlife`).

## See Also

- `comdecl` — declaring object variables
- `comlife` — object lifetimes and `NULL`
- `comref` — referencing existing objects
- `ObjCOM` — COM client overview
- `ObjCorba` — CORBA client overview
- `ObjSoap` — SOAP client overview
