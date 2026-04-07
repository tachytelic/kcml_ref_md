# Xerces XML DOM Parser

> Apache Xerces XML DOM/SAX parser accessible from KCML as a dynamic object.

## Description

The Xerces XML DOM parser is an Apache XML project product available as a shared library. In KCML it is accessed via the dynamic object mechanism, allowing an XML Document Object Model (DOM) tree to be built in the KCML program's memory.

Xerces implements:
- DOM Level 2 (W3C standard object model for XML)
- SAX2 (streaming parser interface)
- Partial DOM3 (including serialisation)
- Partial XML Schema support

## When to use DOM vs SAX

| Approach | Best for |
|----------|---------|
| **DOM** | Documents that need random access or manipulation after loading; builds full tree in memory |
| **SAX2** | Large documents that should be streamed; much less memory; but tags are lost after parsing unless explicitly saved |

## Creating a DOM parser

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

## Notes

- KCML does not implement all features of the Xerces model.
- Documentation for the exposed objects follows the Xerces website documentation.

## See Also

- `dynobj` — accessing C++ objects from KCML
- `dynidl` — KIDL interface description
- `ObjSoap` — SOAP (XML-based web services)
