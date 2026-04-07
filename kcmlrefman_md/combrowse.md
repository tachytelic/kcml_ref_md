# Browsing COM Objects

> How to inspect COM object methods, properties, and enumerations in KCML.

## Description

### Object Browser (KCML Workbench)

In the KCML Workbench IDE, `clientCOM` objects can be browsed using the Object Browser. The object must have been instantiated first (the program must have been run or executed as far as the `CREATE` statement).

The Object Browser displays a tree view of:
- Methods
- Properties
- Enumerations
- Collections and nested objects

Right-clicking an element shows associated help text from the object's type library.

### LIST OBJECT

The `LIST OBJECT` statement lists all objects in the current program in the console window, showing:

- Internal handle number
- Object type (`clientCOM`, `serverCOM`, etc.)
- Symbol name
- Object description from the type library

## Notes

- Only `clientCOM` objects can be browsed in the initial Object Browser implementation.
- The object must be instantiated before it appears in the browser.

## See Also

- `ObjCOM` — COM client overview
- `cominst` — instantiating objects
- `LIST OBJECT` — list objects in the current program
- `commethod` — object methods
- `comprops` — object properties
