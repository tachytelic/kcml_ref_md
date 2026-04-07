# DOM Example: Accessing element attributes

> Shows how to access XML element attributes using a `NamedNodeMap` collection.

## Description

Element nodes expose an `Attributes` property that returns a `NamedNodeMap`. The `getNamedItem()` method retrieves a named attribute node; its `.NodeValue$` property gives the attribute's string value.

**Tip:** Assign the `Attributes` collection to a local `OBJECT` variable before calling it twice — this avoids evaluating the expression twice and is more efficient.

## Example

Using this XML (books.xml):
```xml
<library>
  <book cat="classics" isbn="978-0-14-028329-7">
    <title>Moby Dick</title>
  </book>
  <book cat="fiction" isbn="978-0-7432-7356-5">
    <title>The Great Gatsby</title>
  </book>
</library>
```

```kcml
DIM OBJECT x, OBJECT p, OBJECT i, OBJECT a

OBJECT x = CREATE "dynamic", "dyndom"
OBJECT p = x.CreateParser()
p.parse("books.xml")

REM iterate all <book> nodes
FOR OBJECT i IN p.Document.getElementsByTagName("book")
    OBJECT a = i.Attributes        REM assign once — avoid double evaluation
    IF (a.getNamedItem("cat").NodeValue$ == "classics")
        PRINT a.getNamedItem("isbn").NodeValue$
    END IF
NEXT OBJECT i

OBJECT a = NULL
OBJECT p = NULL
OBJECT x = NULL
```

Output:
```
978-0-14-028329-7
```

## Notes

- `i.Attributes` returns a `NamedNodeMap`, not an array — use `getNamedItem("name")` to look up by name.
- Assign the `Attributes` object to a variable (`OBJECT a = i.Attributes`) before using it more than once to avoid re-evaluating the property expression.
- If the named attribute does not exist, `getNamedItem()` returns `NULL` — accessing `.NodeValue$` on a NULL object raises a runtime error.
- All attribute values are returned as strings via `.NodeValue$`.

## See Also

- `FOR OBJECT` — iterate a collection
- `DOMcount` — simple node iteration example
- `DOMprint` — tree serialization / printing
- `DOMcreate` — creating a DOM document from scratch
