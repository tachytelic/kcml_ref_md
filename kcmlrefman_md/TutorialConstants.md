# Constants in KCML

> Numeric variables whose names begin with an underscore are treated as compile-time constants: their values are set once at resolve time and cannot be changed during execution.

## Overview

A **constant** in KCML is a numeric variable whose name begins with an underscore (`_`). Constants are initialized in a `DIM` or `COM` statement at resolve time and their values cannot be reassigned during program execution. Because constants are resolved before the program runs, they can be used in other resolve-time expressions such as array dimension specifications.

---

## Declaring Constants

Constants are declared with `DIM` using the underscore-prefix naming convention, with an optional initializer expression:

```kcml
DIM _BUFSIZE = 8 * 1024
DIM buffer$(_BUFSIZE)
```

The second `DIM` uses `_BUFSIZE` (which was just resolved to `8192`) as the array dimension. This is legal because both declarations are processed at resolve time and `_BUFSIZE` is available by the time `buffer$` is dimensioned.

**The following are not legal:**

```kcml
_BUFSIZE = 1024          REM error: assignment during execution, not at resolve time
DIM _SomeConstant        REM error: no initializer — constant has no value
```

---

## Enabling Constant Behaviour

For compatibility with programs that already use underscore-prefix variable names as ordinary variables, constant functionality can be enabled or disabled at compile time via **byte 59 of `$OPTIONS RUN`**. The `HEX(01)` bit must be set for constant behaviour to be active.

As of **KCML 6.10**, constant behaviour is enabled by default.

---

## Constants in LOCAL DIM

As a convenience, constant definitions can appear in `LOCAL DIM` statements when their value will not be known until runtime:

```kcml
DEFSUB 'calc_buffer(n)
    LOCAL DIM _LOCAL_SIZE = n * 512
    DIM work$(_LOCAL_SIZE)
    REM ...
RETURN result$
```
<!-- UNTESTED -->

---

## Constants in Libraries

Constants can be defined in a [library](TutorialModules.md) and referenced from the foreground program or from other libraries. They are initialized during the resolve phase, so:

- The library defining the constant **must be loaded** (visible) when the referencing program is resolved.
- Other libraries that reference constants from a defining library should have the defining library loaded when they are saved.
- **Recompile dependent libraries** if the value of a constant in a defining library changes — dependent libraries cache the resolved value.

### PRIVATE constants in libraries

Constants declared with `PRIVATE` in a library's `DIM` statement are visible only within that library:

```kcml
PRIVATE DIM _INTERNAL_LIMIT = 256
```
<!-- UNTESTED -->

`_INTERNAL_LIMIT` can be used in functions defined inside the library but cannot be referenced from another library or from the foreground program.

---

## Predefined System Constants

Starting with **KCML 6.10**, a set of commonly used constants are predefined and do not require a `DIM` declaration. When a constant is not found in the foreground program, KCML searches loaded libraries and then a built-in constant list.

Predefined constants include values such as maximum array sizes, common buffer sizes, and encoding-related limits. The full list is available in the Workbench Function Browser.

---

## Constants from DEFRECORD

The `DEFRECORD` statement automatically creates a constant whose name is the record name prefixed with an underscore. This constant holds the total size of the record in bytes and can be used to dimension string variables that will hold record instances:

```kcml
DEFRECORD Fred
    FLD a
    FLD b
END RECORD

DIM FredRec$ _Fred
```

After this, `_Fred` equals the byte size of the record (`Fred`) and `FredRec$` is dimensioned exactly large enough to hold one instance.

---

## Notes

- Constants must be **initialized** in their `DIM` statement. A `DIM _Name` without `= expr` is an error.
- Constants **cannot be re-assigned** at execution time. Any attempt to write to a constant variable causes an error.
- Initializer expressions in constant `DIM` statements are evaluated at resolve time, not at execution time. Only other constants and simple numeric literals are valid in these expressions.
- `DIM` and `COM` may both be used to declare constants, though `DIM` is more common.
- The underscore prefix is a naming **convention** enforced by the runtime; there is no separate keyword like `CONST`.

## See Also

- `DIM` — variable and constant declaration
- `COM` — common (persistent) variable declaration
- `LOCAL DIM` — local variable declaration inside subroutines
- `DEFRECORD` — record type definition (creates `_RecordName` size constant)
- `LIBRARY ADD` — load a library (required before resolving programs that reference library constants)
- `$OPTIONS RUN` byte 59 — enable/disable constant behaviour (`HEX(01)` bit)
