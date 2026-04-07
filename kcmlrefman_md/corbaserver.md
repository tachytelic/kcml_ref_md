# KCML as a CORBA Server

> How to run a KCML program as a CORBA server using the MICO ORB.

## Description

KCML can act as a CORBA server, exposing KCML subroutines as CORBA objects. The server supports:
- A Naming Service for object location
- An Interface Repository for publishing method interfaces

## Starting the server

Use the `-q` flag followed by ORB-specific parameters:

```sh
kcml -q -ORBImplRepoAddr inet:evb:9876 -ORBNamingAddr inet:evb:9876 \
     -ORBIfaceRepoAddr inet:evb:9999 getadd.src
```

Omit `-ORBNamingAddr` if the exported objects do not need to be registered with a naming service.

## Prerequisites (MICO ORB)

Before starting the KCML server, the following daemons must be running:
- `ird` — Interface Repository daemon
- `micod` — MICO POA/BOA daemon
- `nsd` — Naming Service daemon (or registered in `micod` to start automatically)

Example startup sequence:

```sh
ird -ORBIIOPAddr inet:evb:9999 &
sleep 2
micod -ORBIIOPAddr inet:evb:9999 -ORBIfaceRepoAddr inet:evb:9876 &
sleep 4
imr create NameService poa `which nsd` IDL:omg.org/CosNaming/NamingContext:1.0#NameService inet:evb:9876
```

ORB flags can be stored in `.micorc` in the home directory to avoid repeating them on each command line.

## IDL to KCML mapping

Define the interface in IDL and register it with the Interface Repository. Mapping rules:

| IDL | KCML |
|-----|------|
| `interface Foo { method(...) }` | `DEFSUB 'Foo_method(...)` |
| `attribute short myNumber` (get) | `DEFSUB 'Foo__get_myNumber()` |
| `attribute short myNumber` (set) | `DEFSUB 'Foo__set_myNumber(n)` |
| `in` parameter | string or numeric argument |
| `out` / `inout` parameter | `BYREF` string or numeric |

Read-only attributes only need a `__get_` DEFSUB.

### Example IDL

```idl
#pragma prefix "kerridge.com/CORBA/test"
interface Add {
    attribute short myNumber;
    short addShort(in short number1, in short number2);
    boolean addNums(in double n1, in double n2, out double n3);
    boolean addString(in string s1, in string s2, out string s3);
};
```

Maps to KCML DEFSUBs: `'Add__get_myNumber`, `'Add__set_myNumber`, `'Add_addShort`, `'Add_addNums`, `'Add_addString`.

## See Also

- `ObjCorba` — CORBA client overview
- `comintro` — distributed objects introduction
- `cominst` — CREATE for CORBA clients
