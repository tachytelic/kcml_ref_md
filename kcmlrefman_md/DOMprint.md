# DOM Example: Printing (serializing) a DOM tree (DOM Level 2)

> Shows how to walk and print a DOM tree using DOM Level 2 methods — useful because DOM Level 2 has no built-in serializer.

## Description

DOM Level 2 has no standard serialization API. This example implements a recursive `'printnode` subroutine that walks the tree and prints each node type. It also demonstrates:

- Checking `NodeType` against predefined constants.
- Using `isWhiteSpace()` (a KCML extension) to skip whitespace text nodes between tags.
- Accessing element attributes via the `Attributes` `NamedNodeMap`.

For DOM Level 3 serialization (if available), see `DOM3print`.

## Node type constants

| Constant | Value | Meaning |
|----------|-------|---------|
| `_ELEMENT_NODE` | 1 | An element tag |
| `_TEXT_NODE` | 3 | Text content |
| `_CDATA_SECTION_NODE` | 4 | CDATA section |
| `_COMMENT_NODE` | 8 | XML comment |

## Example

```kcml
DIM OBJECT x, OBJECT p, OBJECT doc, OBJECT elm, count
DIM _ELEMENT_NODE=1, _TEXT_NODE=3, _CDATA_SECTION_NODE=4, _COMMENT_NODE=8

OBJECT x = CREATE "dynamic", "dyndom"
OBJECT p = x.CreateParser()
p.DoSchema = TRUE
p.DoNamespaces = TRUE
p.parse("books.xml")

OBJECT doc = p.Document
OBJECT elm = doc.DocumentElement
count = 'printnode(OBJECT elm, 0)
END


DEFSUB 'printnode(OBJECT n, level)
LOCAL DIM OBJECT e, t, count, i, acount, OBJECT alist, OBJECT a, b, nc
t = n.NodeType
SELECT CASE t
CASE _ELEMENT_NODE
    count = 1
    PRINT TAB(level); "<"; n.TagName$;
    OBJECT alist = n.Attributes
    IF (OBJECT alist <> NULL)
        acount = alist.length
        i = 0
        WHILE (i < acount) DO
            OBJECT a = alist.Item(i)
            PRINT " "; a.NodeName$; "='"; a.NodeValue$; "'";
            i++
        WEND
    END IF
    PRINT ">"
    OBJECT e = n.FirstChild
    WHILE (OBJECT e <> NULL) DO
        nc = 'printnode(OBJECT e, level+2)
        count = count + nc
        OBJECT e = e.NextSibling
    WEND
    PRINT TAB(level); "</"; n.TagName$; ">"
CASE _TEXT_NODE
    IF NOT n.isWhiteSpace()
        PRINT TAB(level); n.NodeValue$
    END IF
    count = 0
CASE _COMMENT_NODE
    PRINT TAB(level); "<!--"; n.NodeValue$; "-->"
    count = 0
CASE ELSE
    count = 0
END SELECT
RETURN = count
END SUB
```

## Notes

- `isWhiteSpace()` is a KCML extension. It returns TRUE if a text node contains only whitespace (tabs, spaces, newlines). This avoids printing blank lines between tags.
- `TAB(level)` indents output by `level` spaces.
- A more complete implementation would also handle `_CDATA_SECTION_NODE` and processing-instruction nodes.
- For DOM Level 3 serialization (much simpler), see `DOM3print`.

## See Also

- `DOM3print` — DOM3 serializer (simpler but experimental)
- `DOMcount` — basic node iteration
- `DOMattr` — attribute access
- `DEFSUB` — define a subroutine
- `SELECT CASE` — multi-way branch
