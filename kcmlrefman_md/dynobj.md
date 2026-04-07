# Dynamic C++ Objects (dynobj / KIDL)

> How to access arbitrary C++ objects from KCML using dynamic object libraries.

## Description

Arbitrary C++ objects can be accessed from KCML using object notation (`OBJECT`, `CREATE`, method calls), provided:
- The code is available as a shared library or DLL.
- The interfaces are described using KCML's KIDL (KCML Interface Description Language) — an XML document.

KIDL descriptions are processed by XSLT transforms to produce C++ wrapper code, which is then compiled and linked with the original library.

KCML tracks object references automatically and calls object destructors when objects go out of scope. The library is unloaded when the last object is destroyed. Enumerated constants declared in the library are visible in the Workbench functions browser.

## Creating a dynamic object

```kcml
OBJECT x = CREATE "dynamic", "dyndom"
```

The first argument is `"dynamic"`, the second is the library name.

## Example: Xerces DOM parser

```kcml
DIM OBJECT x, OBJECT p, OBJECT list
OBJECT x = CREATE "dynamic", "dyndom"
OBJECT p = x.CreateParser()
p.DoSchema = FALSE
p.DoNamespaces = FALSE
p.Parse("books.xml")
OBJECT list = p.Document.GetElementsByTagName("book")
PRINT list.Length
OBJECT list = NULL
OBJECT p = NULL
OBJECT x = NULL
```

## See Also

- `dynidl` — KIDL interface description language
- `xerces` — Xerces XML DOM parser
- `comintro` — distributed objects overview
- `cominst` — `CREATE` statement
