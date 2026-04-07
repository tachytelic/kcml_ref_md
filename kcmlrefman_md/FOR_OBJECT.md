# FOR OBJECT ... IN ... NEXT OBJECT

> Iterates over all elements of a collection object, assigning each element in turn to an object reference variable.

## Syntax

```
FOR OBJECT object_ref IN collection_object
    ...
NEXT OBJECT object_ref
```

| Element | Description |
|---------|-------------|
| `object_ref` | An `OBJECT` variable that receives each element |
| `collection_object` | Any object that provides `First()` and `Next()` methods |

## Description

`FOR OBJECT ... IN` iterates over a collection. On each iteration, `object_ref` is set to the next object in the collection. The loop ends when there are no more objects.

**Key difference from `FOR...NEXT`:** If the collection is empty, the loop body is **never executed** (unlike classic `FOR...NEXT` which always executes at least once).

The collection expression is evaluated **once** when the `FOR OBJECT` statement is first reached — it is not re-evaluated on subsequent iterations.

Jumping into a `FOR OBJECT ... IN` loop causes an error at the first use of the index object.

### Loop control

| Statement | Effect |
|-----------|--------|
| `BREAK` | Exit the loop immediately |
| `CONTINUE` | Skip to the next iteration |

```kcml
FOR OBJECT c IN countries
    IF c.source == 1 THEN BREAK
    IF c.language <> "En" THEN CONTINUE
    EnSpeakers += c.population
NEXT OBJECT c
```

## Examples

### Iterate a Rowset field collection

```kcml
FOR OBJECT col IN Rowset.Fields()
    PRINT col.name$, col.precision
NEXT OBJECT col
```

### Iterate controls on a form

```kcml
DIM f=2
FOR OBJECT i IN Form1
    i.Height = i.Height * f
NEXT OBJECT i
```

### XML DOM: iterate nodes by tag

```kcml
OBJECT x = CREATE "dynamic", "dyndom"
OBJECT p = x.CreateParser()
p.parse("books.xml")
FOR OBJECT i IN p.Document.getElementsByTagName("book")
    OBJECT a = i.Attributes
    IF (a.getNamedItem("cat").NodeValue$ == "classics")
        PRINT a.getNamedItem("isbn").NodeValue$
    END IF
NEXT OBJECT i
OBJECT a = NULL
OBJECT p = NULL
OBJECT x = NULL
```

## Notes

- Both `FOR OBJECT` and `NEXT OBJECT` must use the same `object_ref` variable.
- The KCML editor auto-indents `FOR OBJECT` loops when the program is resolved with exactly one corresponding `NEXT OBJECT`.
- Do not jump into or out of `FOR OBJECT` loops with `GOTO`; use `BREAK` to exit cleanly.
- To avoid an object reference evaluating twice (e.g. when checking attributes), assign it to a local `OBJECT` variable first.

## See Also

- `FOR` — classic numeric loop
- `BREAK` — exit a loop early
- `CONTINUE` — skip to next iteration
- `OBJECT` — object reference declaration
- `CREATE` — create an object instance
