# KCML Object Servers

> Reference for exposing KCML subroutines as COM, CORBA, or SOAP servers.

## Description

KCML can act as a server for COM, CORBA, and SOAP protocols. Once exported, subroutines can be called by other KCML clients or by third-party programs (Java, VB, .NET, etc.).

### How it works

1. The KCML program runs normally until it reaches a `'KCMLOBJECTExport()` call.
2. At that point the program **blocks**, waiting for the first incoming method call.
3. When a client calls a method, KCML executes the matching `DEFSUB` and returns the result.
4. After the export call returns, any cleanup code before `$END` runs.

### Naming convention

Exposed method subroutines must be named `InterfaceName_MethodName` (case-insensitive). String-returning methods must end with `$`.

## Setup

```kcml
$DECLARE 'KCMLOBJECTExport(STR(), STR())="*"
```

## Example — SOAP server

```kcml
REM Initialization code here (open files, etc.)

'KCMLOBJECTExport("SOAP", "TimeService")

REM Cleanup code here
$END

DEFSUB 'TimeService_getTime$()
  LOCAL DIM t$24
  CONVERT #DATE TO t$
  CONVERT #TIME TO STR(t$, LEN(t$)+2)
  RETURN t$
END SUB
```

Run as a daemon:
```sh
kcml -p timeserver.kcml &
```

Browse the WSDL: point a browser at the endpoint URL — KCML generates WSDL automatically.

## COM server notes

- COM servers are started by the Windows COM subsystem; the program is registered in the registry.
- The interface name must match the registered ProgID.

## CORBA server notes

- Run with the `-q` switch to pass ORB environment information.
- Requires `kcorba.so` and a running interface repository.

## See Also

- `ObjCOM` — COM client
- `ObjCorba` — CORBA support
- `ObjSoap` — SOAP client
- `DEFSUB` — define a subroutine
