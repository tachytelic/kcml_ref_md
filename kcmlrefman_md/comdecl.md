# Declaring Object Variables

> How to declare KCML object variables with `DIM OBJECT`.

## Syntax

```
DIM OBJECT objname [, OBJECT objname2, ...]
LOCAL DIM OBJECT objname
```

## Description

Objects are declared using `DIM` or `LOCAL DIM` with the `OBJECT` keyword prefix on the variable name. This creates a placeholder symbol; the object is **not** instantiated at declaration time. The initial value is `NULL`.

```kcml
DIM s$100, OBJECT Range, OBJECT Cell
```

Object variables look like scalar numeric symbols (`Range`, `Document`, `abc`) — KCML distinguishes them from regular numerics by context or the `OBJECT` prefix. Declaring with `DIM OBJECT` ensures correct scoping.

## Scope

| Declaration | Scope |
|-------------|-------|
| `DIM OBJECT` | Global to the program (or library) |
| `LOCAL DIM OBJECT` | Local to the current subroutine |

`LOCAL DIM OBJECT` objects are automatically released when the subroutine returns (reference count decremented; object destroyed if count reaches zero).

## Notes

- DIM is not strictly mandatory yet but is strongly recommended for clarity and scoping.
- An undeclared object variable behaves as global numeric scope.
- To instantiate the object after declaration, use `CREATE`.

## Examples

```kcml
DIM OBJECT app, OBJECT doc
OBJECT app = CREATE "clientCOM", "Word.Application"
OBJECT doc = app.Documents.Add()
```

```kcml
DEFSUB 'processSheet(OBJECT ws)
LOCAL DIM OBJECT cell
OBJECT cell = ws.Range("A1")
PRINT cell.Value$
OBJECT cell = NULL
END SUB
```

## See Also

- `cominst` — instantiating objects with `CREATE`
- `comlife` — object lifetime and `NULL`
- `comsubs` — passing objects to subroutines
- `comintro` — distributed objects overview
