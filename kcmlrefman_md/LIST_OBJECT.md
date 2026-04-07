# LIST OBJECT

> Lists all active (non-NULL) objects in the current program with their types and descriptions.

## Syntax

```
LIST [title] OBJECT [obj | pattern]
```

## Description

Without arguments, lists all non-NULL objects showing:
- Internal handle number
- Object type (ClientCOM, SOAP, serverCOM, etc.)
- Symbol name
- Description from the type library

```
:LIST OBJECT
    2 ClientCOM    Rows (_RecordSet)
    8 ClientCOM    Cols (Field)
   10 SOAP         s    (http://www.kcml.com/soap/test.wsdl)
```

With a specific object or pattern, also lists the methods and properties of the matching objects. Pattern matching uses the same wildcards as `LIST DIM`.

## See Also

- `OBJECT` — object reference declaration
- `CREATE` — instantiate an object
- `LIST DIM` — pattern matching rules
