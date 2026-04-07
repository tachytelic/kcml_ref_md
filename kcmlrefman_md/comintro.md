# Distributed Objects Introduction

> Overview of COM, CORBA, and SOAP object support in KCML.

## Description

KCML supports several industry standards for distributed objects, allowing KCML programs to invoke objects on the same machine or on remote machines — written in KCML or in other languages. KCML can act as either a **client** (consuming objects) or a **server** (exposing objects).

The `OBJECT` grammar provides a common, intuitive method for KCML programs to create and manipulate objects across all supported standards.

## COM

COM (Component Object Model) is a Microsoft standard for binary objects on Windows. It is available **on Windows platforms only**, though Unix KCML servers can use KClient to access COM servers.

KCML supports:
- COM client: instantiate and use Windows COM/ActiveX objects
- COM server: expose KCML subroutines as COM objects (in-process DLL)

See: `ObjCOM`, `comautomation`, `comdecl`, `cominst`

## CORBA

CORBA (Common Object Request Broker Architecture) is an industry standard for distributed objects, available on **both Unix and Windows**. KCML can act as both a CORBA client and server.

See: `ObjCorba`

## SOAP

SOAP (Simple Object Access Protocol) is an XML-based standard for remote procedure calls over HTTP. Available on **both Unix and Windows**. KCML can currently act as a SOAP **client** only.

See: `ObjSoap`

## Common grammar elements

All object types share the same KCML grammar:

| Concept | See |
|---------|-----|
| Declaring objects | `comdecl` |
| Creating (instantiating) objects | `cominst` |
| Object properties | `comprops` |
| Object methods | `commethod` |
| Object collections / enumeration | `comenum` |
| Compound object references | `comcompound` |
| Object lifetimes | `comlife` |
| Error handling | `comerrors` |
| Passing objects to subroutines | `comsubs` |
| Referencing existing objects | `comref` |
| COM constants and enumerations | `comconst` |
| Objects in forms (OCX) | `comforms` |
| COM Automation issues | `comautomation` |
| KCML as COM server | `ObjServer` |

## See Also

- `OBJECT` — object declaration and instantiation grammar
- `ObjCOM` — COM client reference
- `ObjCorba` — CORBA client reference
- `ObjSoap` — SOAP client reference
- `ObjServer` — KCML as a server
