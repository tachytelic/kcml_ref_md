# DOM Example: Creating an XML document from scratch

> Shows how to build an XML DOM tree programmatically using the `dyndom` DOM implementation object.

## Description

To create a new XML document (rather than parsing an existing one), use the `Implementation` object exposed by `dyndom`. The `createDocument()` method creates an empty document with a root element, and you can then attach child nodes to build the full tree.

## Key methods

| Method | Purpose |
|--------|---------|
| `imp.createDocument(ns, root_tag, dtd)` | Create a new document; pass `0` for no namespace, `NULL` for no DTD |
| `doc.DocumentElement` | Get the root element node |
| `doc.createElement("tag")` | Create a new element node |
| `doc.createTextNode("text")` | Create a text node |
| `doc.createComment("text")` | Create a comment node |
| `node.appendChild(OBJECT child)` | Append a child to a node |
| `node.insertBefore(OBJECT new, OBJECT ref)` | Insert before a reference node |
| `n.setAttribute("name", "value")` | Set an attribute on an element |

## Example

```kcml
DIM OBJECT x, OBJECT imp, OBJECT doc, OBJECT node, OBJECT a, OBJECT n, OBJECT dtd

OBJECT x = CREATE "dynamic", "dyndom"

REM get the DOM implementation
OBJECT imp = x.Implementation
OBJECT dtd = NULL

REM create an empty document with a root node
REM args: namespace (0=none), root element name, DTD (NULL=none)
OBJECT doc = imp.createDocument(0, "root", OBJECT dtd)

REM get the root node
OBJECT node = doc.DocumentElement

REM add a <one> element with text content
OBJECT n = doc.createElement("one")
node.appendChild(OBJECT n)
OBJECT a = doc.createTextNode("Hello world")
n.appendChild(OBJECT a)

REM add an empty <two> element with an attribute
OBJECT n = doc.createElement("two")
node.appendChild(OBJECT n)
n.setAttribute("namestring", "valuestring")

REM insert a comment before <two>
OBJECT a = doc.createComment("Commenting is good practice")
node.insertBefore(OBJECT a, OBJECT n)

REM serialize and print (using DOM3 writer or the DOMprint example)
OBJECT elm = doc.DocumentElement
count = 'printnode(OBJECT elm, 0)
```

Expected XML structure:
```xml
<root>
  <one>Hello world</one>
  <!-- Commenting is good practice -->
  <two namestring="valuestring"/>
</root>
```

## Notes

- `createDocument(0, "root", OBJECT dtd)` requires the `OBJECT` keyword before the DTD argument.
- Use `OBJECT NULL` or `OBJECT dtd` (pre-set to NULL) for the DTD argument when no DTD is needed.
- After building the tree, serialize it with the DOM3 writer (`DOM3print`) or the manual walker (`DOMprint`).
- Always set objects to `NULL` when done to release Xerces memory.

## See Also

- `DOM3print` — serialize a DOM tree to a string
- `DOMprint` — manual DOM2 tree walker/printer
- `DOMcount` — parsing an existing XML file
- `CREATE` — load dynamic libraries
