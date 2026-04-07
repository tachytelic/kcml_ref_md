# KCML as a SOAP Server

> How to expose KCML subroutines as SOAP web service methods.

## Description

KCML can act as a SOAP server, exposing `DEFSUB` subroutines as web service methods. The server can run:
- As a standalone daemon
- Invoked by Apache (via `mod_kcml`)
- As an NT service

In all cases, KCML loads the program, executes initialisation code, then blocks on `$BREAK!` awaiting requests.

## SOAP server program structure

1. Load files, overlay, attach to global libraries as needed.
2. Call `'KCMLObjectExport()` to register the interface.
3. Execute `$BREAK!` — the server blocks here awaiting SOAP requests.
4. When the client disconnects, `$BREAK!` exits and cleanup code runs before `$END`.

All exposed methods must be visible as `DEFSUB` statements when `$BREAK!` is reached.

## Exporting the interface

```kcml
DIM interface$20, endpoint$0, wsdl$0
interface$ = "pjcsoaptest"
REDIM endpoint$ = "http://www.pjcserver.com/" & interface$
REDIM wsdl$ = "htdocs/" & interface$ & ".wsdl"
'KCMLObjectExport("SOAP", interface$, wsdl$, endpoint$)
```

By convention, the interface name forms part of the endpoint URL. All public methods have `DEFSUB` names prefixed with the interface name.

## Method signatures

- All parameters are strings or numerics.
- `BYREF` and `REDIM` parameters are supported.
- Optional string and numeric parameters are allowed.
- `BYREF` strings must be scalars, not arrays (SOAP provides no dimensioning information).
- Returned strings are limited to approximately 64 KB.

## Running the server

```sh
kcml -b myprog         # Standalone SOAP server daemon
kcml -k 8000,8010 myprog   # Persistent, reconnecting to port range (for mod_kcml)
```

## See Also

- `ObjSoap` — SOAP client usage
- `comserver` — KCML as a COM server
- `corbaserver` — KCML as a CORBA server
- `$BREAK` — block awaiting COM/SOAP events
