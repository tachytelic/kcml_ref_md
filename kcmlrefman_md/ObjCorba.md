# CORBA Support in KCML

> Reference for using CORBA distributed objects from KCML.

## Description

CORBA (Common Object Request Broker Architecture) is a cross-platform, language-neutral standard for distributed objects. Unlike COM, CORBA runs on both Unix and Windows.

KCML supports CORBA as both **client** and **server**:

- **Client**: call methods on remote CORBA objects.
- **Server**: expose KCML subroutines to CORBA clients written in Java, C++, etc.

CORBA support requires the `kcorba.so` shared library. At time of writing, this was built against MICO 2.3.3 and available on Linux and UnixWare 7.

### Requirements

- Objects must support `get_interface()` — an interface repository must be deployed.
- Environmental information (ORB location, repository) is passed via the `-q` command-line switch.

## Client example

```kcml
REM Connect to a CORBA object
OBJECT svc
svc = CREATE "CORBA", "IOR:010000002b..."   : REM Interoperable Object Reference
DIM result$200
result$ = svc.GetData$("query")
OBJECT svc = NULL
```

## Server setup

```kcml
$DECLARE 'KCMLOBJECTExport(STR(), STR())="*"
'KCMLOBJECTExport("Corba", "TimeService")
$END

DEFSUB 'TimeService_getTime$()
  LOCAL DIM t$24
  CONVERT #DATE TO t$
  RETURN t$
END SUB
```

## Notes

- CORBA allows KCML on a Unix server to be called from Java, C++, and other languages.
- The ORB and interface repository must be running before KCML starts.
- `kcorba.so` platform availability is limited — check current build notes.

## See Also

- `CREATE` — create object instance
- `ObjCOM` — COM support
- `ObjSoap` — SOAP support (more widely supported alternative)
- `ObjServer` — KCML as object server
