# DOM Example: Parsing XML from memory

> Shows how to parse an XML string held in a KCML variable (rather than a file) using a `MemBufInputSource`.

## Description

Instead of calling `p.parse("filename")`, create a `MemBufInputSource` object from the string buffer and call `p.parseIS()`. This is useful when the XML is generated at runtime or received from a network call.

## Example

```kcml
DIM OBJECT x, OBJECT p, OBJECT Is, n

REM create root dyndom object
OBJECT x = CREATE "dynamic", "dyndom"

REM create a parser
OBJECT p = x.CreateParser()
p.DoSchema = FALSE
p.DoNamespaces = FALSE

REM build some XML in a variable
DIM z$="<?xml version=" & HEX(22) & "1.0" & HEX(22) & "?><root><tag>Hello</tag></root>"

REM create an input-stream object from the buffer
OBJECT Is = p.MemBufInputSource(z$, LEN(z$), "test")

REM parse from the stream
p.parseIS(OBJECT Is)
OBJECT Is = NULL

REM count all element nodes
n = p.Document.getElementsByTagName("*").length
PRINT "Element count: "; n    REM prints 2  (root + tag)

OBJECT p = NULL
OBJECT x = NULL
```

## Notes

- `MemBufInputSource(buffer$, length, id$)` — the `id$` is an arbitrary identifier string used in error messages.
- Pass `OBJECT Is` explicitly to `parseIS()` to hand over the object reference.
- Set `OBJECT Is = NULL` after parsing to release the input-stream memory.
- `getElementsByTagName("*")` returns every element node (wildcard).
- Parsing errors (malformed XML) raise an **O30** runtime error.

## See Also

- `DOMcount` — parsing from a file
- `DOMattr` — accessing element attributes
- `DOMprint` — serializing a DOM tree back to a string
- `CREATE` — load dynamic libraries
