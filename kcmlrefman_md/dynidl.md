# KIDL — Dynamic Object Interface Description

> XML-based interface description language for KCML dynamic C++ object libraries.

## Description

KIDL (KCML Interface Description Language) is an XML document format that defines the interfaces exposed by a dynamic object library. It is used to generate C++ glue code that allows KCML to call the methods of C++ objects via KCML's object notation.

## Process

1. Write KIDL XML describing the C++ object's interface.
2. Process with an XSLT stylesheet to generate C++ wrapper code.
3. Compile the generated C++ and link it with the original object code.
4. The resulting shared library/DLL is loaded via `CREATE "dynamic", "libname"`.

The build process is platform-specific (differs between Unix and Windows, and may differ between Unix platforms).

## See Also

- `dynobj` — using dynamic C++ objects from KCML
- `xerces` — Xerces XML DOM parser (example of a dynamic object)
- `cominst` — `CREATE` statement
