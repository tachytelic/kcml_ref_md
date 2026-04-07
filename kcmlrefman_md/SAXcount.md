# SAX2 Example — Element Counter

> Example of using the Xerces SAX2 parser via the KCML DOM object to count XML elements.

## Description

SAX (Simple API for XML) is an event-driven XML parser. Unlike DOM, SAX does not build a tree — it fires callbacks as it encounters elements, text, etc. This is memory-efficient for large documents.

In KCML, SAX is accessed through the `dyndom` dynamic library. The programmer installs `DEFSUB` callbacks using the `ContentHandler` object, then calls `parse()`.

### Key SAX callbacks

| Setter | Called when |
|--------|-------------|
| `setStartElement` | Opening tag encountered |
| `setEndElement` | Closing tag encountered |
| `setCharacters` | Text content between tags |
| `setStartDocument` | Start of document |
| `setEndDocument` | End of document |

**`BYREF` is required** when passing DEFSUB names to setter methods.

## Example — count elements

```kcml
DIM charcount, attrcount, tagcount, level, maxlevel
DIM OBJECT x, OBJECT p, OBJECT h

REM Load the dyndom library
OBJECT x = CREATE "dynamic", "dyndom"
REM Create SAX parser
OBJECT p = x.CreateSAXParser()
REM Create a ContentHandler and register callbacks
OBJECT h = p.ContentHandler()
h.setStartElement(BYREF 'startElement)
h.setEndElement(BYREF 'endElement)
h.setCharacters(BYREF 'chars)
h.setStartDocument(BYREF 'startDoc)
h.setEndDocument(BYREF 'endDoc)
REM Assign handler to parser
p.setContentHandler(OBJECT h)
REM Parse the document
p.parse("books.xml")
REM MUST free in reverse order
OBJECT h = NULL
OBJECT p = NULL
OBJECT x = NULL
$END

DEFSUB 'startDoc()
  charcount = 0 : attrcount = 0 : tagcount = 0 : level = 0 : maxlevel = 0
END SUB

DEFSUB 'startElement(uri$, localname$, qname$, OBJECT attrs)
  tagcount++
  level++
  IF level > maxlevel THEN maxlevel = level
  attrcount = attrcount + attrs.getLength()
END SUB

DEFSUB 'endElement(uri$, localname$, qname$)
  level--
END SUB

DEFSUB 'chars(text$, length)
  charcount = charcount + length
END SUB

DEFSUB 'endDoc()
  PRINT "Tags: "; tagcount; "  Attrs: "; attrcount; "  Chars: "; charcount
  PRINT "Max depth: "; maxlevel
END SUB
```

## Notes

- Free objects in **reverse** creation order: `h` → `p` → `x`. Not doing so causes memory leaks or crashes.
- `BYREF` is **required** when passing DEFSUB references to setter methods.
- The `characters` callback may fire multiple times for a single text node (especially for text containing XML entities like `&amp;`).
- SAX2 is namespace-aware: for unnamespaced tags, `uri$` is empty and `localname$` = `qname$`.
- Character `length` is the number of **Unicode characters** — may differ from `LEN(STR(text$))` in bytes.

## See Also

- `DOMparsemem` — DOM parser (builds tree in memory)
- `DOMcreate` — create a DOM document programmatically
- `CREATE` — create dynamic library objects
