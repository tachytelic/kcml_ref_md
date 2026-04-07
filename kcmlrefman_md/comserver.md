# KCML as a COM Server

> How to expose KCML subroutines as a COM object for use by VBScript, JavaScript, and other COM clients.

## Description

KCML can act as an in-process COM server using the `kserver.dll` DLL. The DLL is loaded into the caller's address space on demand and unloads when the reference count reaches zero.

**Limitation:** KCML cannot simultaneously act as a COM server and a COM client.

## How it works

1. On first reference, `kserver.dll` is loaded.
2. KCML initialises by running the program named in the registry entry for the object.
3. The KCML program overlays/attaches to libraries as needed, then blocks on `$BREAK!` with exposed `DEFSUB` statements visible.
4. When COM unloads the DLL, `$BREAK!` is interrupted, cleanup code runs, then `$END`.

KCML implements the default `IDispatch` interface (used by VBScript, JavaScript, Perl, etc.). It does **not** implement a vtable interface. For Visual Basic clients, declare KCML objects as plain `Object` and use `CreateInstance` to instantiate them.

## Interface definition

Exposed methods must be defined in an IDL file and compiled with `midl` (from Microsoft Visual C++ or Visual Basic tools). Example:

```idl
import "oaidl.idl";

[ uuid(10B96EB5-66C7-11d4-9CF6-0060080393F0) ]
dispinterface Icomtest {
  properties:
    [id(0)] double  numprop;
    [id(1)] BSTR    strprop;
  methods:
    [id(3)] double  Sum([in] double x, [in] double y);
    [id(5)] double  Len([in] BSTR a);
    [id(6)] BSTR   *Upper([in] BSTR a);
};

[ uuid(10B96EB3-66C7-11d4-9CF6-0060080393F0),
  helpstring("Example KCML COM server"), version(1.0) ]
library comtestlib {
  importlib("stdole32.tlb");
  interface Icomtest;
  [ uuid(10B96EB1-66C7-11d4-9CF6-0060080393F0) ]
  coclass comtest { interface Icomtest; }
};
```

The IDL contains three GUIDs (interface, type library, class). Each object you create must have its own unique GUIDs — use `guidgen.exe` to generate them.

## Publishing the interface

In the KCML program, publish the interface with a `KCMLOBJECTExport()` `$DECLARE` call, specifying the interface name and version:

```kcml
$DECLARE KCMLOBJECTExport() ...
```

Once published, the interface is fixed — new methods can be added but existing ones cannot change.

## Data type mapping

KCML handles type conversion automatically:
- COM integers and doubles → KCML numerics
- Microsoft `BSTR` strings → KCML strings

## KCML server program requirements

- Must run standalone without relying on environment variables or command-line settings.
- May overlay internally and access global partitions or libraries.
- Must eventually execute `$BREAK!` with all exposed methods reachable as `DEFSUB` statements.

## See Also

- `ObjServer` — server overview
- `ObjCOM` — COM client usage
- `comintro` — distributed objects introduction
- `$BREAK` — block waiting for COM events
