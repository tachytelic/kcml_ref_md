# DOM Example: Counting and printing nodes

> A simple example of loading an XML file into a DOM tree and iterating its nodes.

## Description

This example shows the basic pattern for using the Xerces DOM object in KCML:

1. Load the `dyndom` library via `CREATE "dynamic"`.
2. Create a `Parser` object and call `.parse()` to load an XML file into a DOM tree.
3. Use `getElementsByTagName()` to get a `NodeList` of matching nodes.
4. Iterate the list with `FOR OBJECT ... IN`.
5. Navigate the tree (`.FirstChild`, `.NodeValue$`) to extract data.
6. Set objects to `NULL` when done to free memory.

Any parsing error (file not found, XML syntax error) raises an **O30** runtime error.

## Example

```kcml
DIM OBJECT x, OBJECT p, OBJECT nodelist, OBJECT node, count, n

REM load the Xerces DOM library
OBJECT x = CREATE "dynamic", "dyndom"

REM create a parser object
OBJECT p = x.CreateParser()
REM optional: p.DoSchema = TRUE / p.DoNamespaces = TRUE

REM parse the XML file into a DOM tree
p.parse("books.xml")

REM get all <title> elements as a NodeList
OBJECT nodelist = p.Document.getElementsByTagName("title")
count = nodelist.length
PRINT "Found "; count; " title nodes"

REM iterate and print each title's text content
FOR OBJECT node IN nodelist
    PRINT node.FirstChild.NodeValue$
NEXT OBJECT node

REM free memory
OBJECT p = NULL
OBJECT x = NULL
```

## Notes

- `dyndom` and the Xerces library must be on the system `PATH` for `CREATE "dynamic", "dyndom"` to succeed.
- `getElementsByTagName("*")` returns all elements in the document.
- A `NodeList`'s `.length` property gives the element count.
- A text node's value is accessed via `.FirstChild.NodeValue$` (the text node is the first child of an element node).
- The `Parser` object owns all DOM memory. Setting it to `NULL` releases everything.

## See Also

- `FOR OBJECT` — iterate a collection
- `CREATE` — instantiate a dynamic or built-in object
- `DOMattr` — accessing element attributes
- `DOMparsemem` — parsing XML from a string buffer
- `DOMprint` — printing (serializing) a DOM tree
