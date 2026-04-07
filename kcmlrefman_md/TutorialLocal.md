# Local Variables in Subroutines

> How to write subroutines with their own private variable scope using DEFSUB and LOCAL DIM.

## Overview

By default, all variables in a KCML program are global — a subroutine shares the same variable namespace as the code that calls it. Local variables change this: any variable declared as local inside a subroutine gets its own private copy. When the subroutine returns, local variables are discarded and the original values of any variables whose names were reused are automatically restored.

There are two mechanisms for local variables:

1. **`DEFSUB`** — declares a named subroutine whose parameter variables are automatically local, and which establishes a local scope for the entire routine.
2. **`LOCAL DIM`** — declares additional local variables inside either a `DEFSUB` or a `DEFFN` subroutine.

## DEFSUB Subroutines

`DEFSUB` is the named-subroutine declaration with local scope. It is similar to `DEFFN` except that it provides full variable isolation.

### Naming rules

- Must start with an alpha character, up to 128 alphanumeric characters total.
- Underscores allowed as word separators: `get_next_record` is valid.
- Integer labels are **not** allowed (unlike `DEFFN`).
- Append `$` if the subroutine returns a string: `DEFSUB 'get_record$(...)`

### Parameters are automatically local

Variables listed in the `DEFSUB` parameter list are declared as local variables. They receive the dimensions of the corresponding arguments from the call site. The call site's existing variables with the same names are saved and restored on `RETURN`.

You can also explicitly declare dimensions in the `DEFSUB` signature, which acts as a size check — if the caller passes an array of different dimensions, KCML reports an error rather than silently accepting a mismatched array:

```kcml
DIM tmp$1000, .name$, .zyx$(10)4, abc

REM call the subroutine
name$ = FLD('get_record$(1,tmp$,zyx$()).name$)

REM subroutine definition - dimensions on zyx$ are checked against the call
DEFSUB 'get_record$(abc, def$256, ghi$(10)4)
    REM ... body ...
RETURN result$
```

### Dynamic parameter sizing

Parameter dimensions can reference other parameters, evaluated at call time:

```kcml
DEFSUB 'get_next_record$(n, def$n)
    REM def$ is declared as n bytes long, where n is the first argument
    REM ...
RETURN result$
```

### Recursion

`DEFSUB` subroutines can call themselves recursively. Each recursive call gets a fresh set of local variables. The return stack limit is 42 levels deep.

```kcml
DEFSUB 'factorial(n)
RETURN (n == 1 ? 1 : n * 'factorial(n-1))
```

**Example call:**
```kcml
PRINT 'factorial(6)
```

**Output:**
```
720
```

## LOCAL DIM

`LOCAL DIM` declares additional local variables inside either a `DEFSUB` or a `DEFFN` subroutine. It follows the same syntax as `DIM` except that explicit scalar initialization is not allowed.

If a variable declared with `LOCAL DIM` already exists in the outer scope, its value is saved and restored on `RETURN`.

### Example

The following table shows the value of `zyx$` at each step when `LOCAL DIM` is used to shadow an existing variable:

| Code | Value of zyx$ |
|------|---------------|
| `DIM zyx$ = "AABBCC"` | `zyx$6 = "AABBCC"` |
| `GOSUB 'abc()` | `zyx$6 = "AABBCC"` (saved) |
| `DEFFN 'abc()` | — |
| `LOCAL DIM zyx$9` | `zyx$9 = "         "` (fresh local) |
| `zyx$ = "ZZZYYYXXX"` | `zyx$9 = "ZZZYYYXXX"` |
| `RETURN` | restored: `zyx$6 = "AABBCC"` |
| `STOP` | `zyx$6 = "AABBCC"` |

**Key point:** `LOCAL DIM` creates a new local variable of the declared size. The original variable (with its original size and content) is invisible inside the subroutine and is fully restored on `RETURN`.

### Restrictions

- `LOCAL DIM` cannot be used outside a `DEFSUB` or `DEFFN` subroutine — an error is reported.
- `LOCAL DIM` cannot be used after a jump into the middle of a subroutine — the context for local variables is not established.
- It is recommended to place `LOCAL DIM` immediately after the `DEFFN`/`DEFSUB` line.
- Locally dimensioned string variables **cannot** be returned from a subroutine.
- `MAT REDIM` cannot expand a locally dimensioned variable.

## Inspecting Local Variables

### LIST DIM

`LIST DIM`, when executed inside a subroutine with local variables, marks local variables with an `L` in the type column:

```
LIST DIM
C type$1        "."
C new_var$16    "                "
D status$(5)1   "A","A","A","A","B"
D .name$
D .total$       (1,0x6002)
L table$(2)10   "          ","          "
L count         45
L .balance      (0,0000)
```

Only the local form of a shadowed variable is shown — the outer (saved) value does not appear.

### LIST LOCAL

`LIST LOCAL` shows only the local variables for the current subroutine. Output format is the same as `LIST DIM`. Outside a subroutine with local variables it returns nothing.

### LIST LOCAL RETURN

`LIST LOCAL RETURN` augments the `LIST RETURN` output (the call stack) with local variable contents at each stack frame. It also shows the original saved values at the end:

```
:list local return
Program at line 30, statement 6
...
Return stack contents
Top    00030 :::FOR d = 1 TO n , varying D now 1, by 1, until 10
 -     00010 ::GOSUB 'get(10)
 L N                 10
 L AB$16             "................"
 L BA$16             "................"
 -     00010 :FOR b = 1 TO 10 , varying B now 1, by 1, until 10
Bottom 00010 FOR a = 0 TO 9 STEP 2, varying A now 0, by 2, until 9
Original values of local variables
 C N                 0
 C AB$40             "TEST1                                   "
 D BA$25             "TEST2                    "
```

## Jumping In and Out of Subroutines

- **Jumping out** (`GOTO` past `RETURN`) is allowed but strongly discouraged. Local variables will not be cleaned up properly.
- **`RETURN CLEAR`** and **`RETURN CLEAR ALL`** restore the original values of shadowed global variables when unwinding.
- **Jumping into** the middle of a `DEFSUB` or a subroutine using `LOCAL DIM` is allowed, but all variables in that subroutine are then treated as ordinary global variables. `LOCAL DIM` statements encountered after such a jump will cause an error.

## Notes

- The return stack is limited to **42 levels**. Deep recursion will overflow it.
- `DEFSUB` is preferred over `DEFFN` for any subroutine with complex variable usage, as `DEFFN` does not establish local scope automatically.
- See also: `DEFSUB`, `DEFFN`, `GOSUB'`, `LIST LOCAL`, `LIST RETURN`, `LOCAL DIM`
