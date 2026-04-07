# DOM Example: Serializing a DOM tree (DOM Level 3)

> Shows how to serialize (print) a DOM tree to a string using the DOM Level 3 LS serializer. Note: considered experimental as the DOM3 specification was not yet finalized when this support was added to Xerces 2.x.

## Description

DOM Level 3 defines a serialization API via a `DOMWriter` object. The KCML `dyndom` library exposes this through the LS implementation.

Steps:
1. Get the LS `DOMImplementation` via `getDOMImplementation("LS")`.
2. Call `createDOMWriter()` to get a writer object.
3. Optionally set `writer.Encoding$` (default: UTF-8) and `writer.newline$`.
4. Optionally set features (e.g. `"format-pretty-print"`).
5. Call `writer.writeToString$(OBJECT node)` to get the serialized XML as a string.

## Example

```kcml
DIM OBJECT x, OBJECT impls, OBJECT writer, OBJECT p, OBJECT root
REDIM z$

OBJECT x = CREATE "dynamic", "dyndom"

REM get the LS DOM implementation
OBJECT impls = x.getDOMImplementation("LS")

REM create a writer
OBJECT writer = impls.createDOMWriter()

REM optional: pretty-print with indentation
writer.setFeature("format-pretty-print", TRUE)

REM parse a file to get a DOM tree
OBJECT p = x.CreateParser()
p.parse("books.xml")
OBJECT root = p.Document

REM serialize to string
REDIM z$ = writer.writeToString$(OBJECT root)
PRINT z$

OBJECT writer = NULL
OBJECT p = NULL
OBJECT x = NULL
```

## WriterFilter (optional)

A `WriterFilter` object can be used to filter which nodes are included in the output. This requires implementing a callback function that KCML calls for each node, returning one of:

| Constant | Value | Meaning |
|----------|-------|---------|
| `_FILTER_ACCEPT` | 1 | Include this node |
| `_FILTER_REJECT` | 2 | Exclude this node and its subtree |
| `_FILTER_SKIP` | 3 | Exclude this node but include its children |

```kcml
DIM _FILTER_ACCEPT=1, _FILTER_REJECT=2, _FILTER_SKIP=3
DIM OBJECT filter
REM ... set up filter callback and assign to writer.Filter before calling writeToString$
```

## Notes

- DOM3 serialization support in Xerces 2.x is experimental (but unlikely to change substantially).
- `writeToString$(OBJECT node)` can be passed any node — the subtree below that node is serialized.
- Default encoding is UTF-8; set `writer.Encoding$` to change it.
- Newline handling: `writer.newline$` defaults to OS-specific (`HEX(0A)` on Unix, `HEX(0D0A)` on Windows).
- Use `REDIM z$` to avoid truncation since the output length is variable.

## See Also

- `DOMprint` — DOM Level 2 manual tree walker (no serializer dependency)
- `DOMcreate` — creating a DOM document from scratch
- `DOMcount` — parsing and iterating nodes
- `CREATE` — instantiate dynamic objects
