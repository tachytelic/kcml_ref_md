# Object Lifetimes

> How KCML manages the lifecycle of objects.

## Description

Objects have an independent existence outside the KCML process. KCML tracks object references internally using reference counting.

### Automatic release

- `LOCAL DIM OBJECT` variables are automatically released when the subroutine returns (reference count decremented; object destroyed if count reaches zero).
- Objects with global scope (non-LOCAL) are released on `LOAD` or `CLEAR` (for non-common objects).

### Explicit release

An object can be released at any time by assigning `NULL`:

```kcml
OBJECT TempObj = NULL
```

If no other references exist, the object is immediately destroyed.

### Multiple references

`OBJECT a = b` does **not** copy the object — it creates a second reference to the same object. Both `a` and `b` must be set to `NULL` before the object is destroyed:

```kcml
OBJECT a = b         : REM  both a and b reference the same object
OBJECT a = NULL      : REM  object still alive — b still holds it
OBJECT b = NULL      : REM  now object is destroyed
```

### Word and Excel

Word and Excel do **not** terminate automatically when the last KCML reference is dropped. You must explicitly call `.Quit()` and then set all references to `NULL`.

## Examples

```kcml
DIM OBJECT app
OBJECT app = CREATE "clientCOM", "Excel.Application"
app.Visible = TRUE
REM ... use Excel ...
app.Quit()
OBJECT app = NULL
```

## See Also

- `comdecl` — declaring object variables
- `cominst` — creating objects
- `comref` — object references
- `comsubs` — objects in subroutines
- `comautomation` — Word/Excel specific notes
