# KCML Language Basics

> The core structural rules of KCML: program lines, variable types and naming, arrays, constants, initialization, and the READ/DATA mechanism.

## Program Structure

A KCML program is a sequence of numbered lines. Line numbers are integers in the range 0–32000 and are assigned by the developer. They serve two purposes:

1. **Reference points** for branching (`GOTO`, `GOSUB`).
2. **Overlay anchors** for merging programs or loading overlays at specific positions.

Each line can contain one or more statements separated by colons (`:`). There is no hard limit on line length, so an entire program can technically live on a single line — this is the style used internally by the KCML Workbench, which hides line numbers by default.

Loop constructs (`FOR`/`NEXT`, `REPEAT`/`UNTIL`, `WHILE`/`WEND`) and subroutine boundaries can span multiple line numbers.

## Statements, Functions, and Operators

KCML provides three categories of instruction:

| Category | Description |
|----------|-------------|
| **Statement** | A programmable instruction that performs an action (`PRINT`, `LOAD`, `IF … THEN`, etc.). |
| **Function** | Used inside expressions; most operate on the value in the parentheses immediately following the function name (`STR(`, `LEN(`, `ABS(`, etc.). |
| **Operator** | Performs operations on alpha operands (string concatenation, comparison, etc.). |

## Variables

KCML has two primary variable types:

| Type | Description | Example names |
|------|-------------|---------------|
| **Numeric** | Fixed-size real numbers, initialized to zero. | `i`, `counter`, `sales_total` |
| **String (alpha)** | Variable-size character data, initialized to spaces. Name ends with `$`. | `name$`, `result$` |

String variables do not have a fixed size built into the language. If you do not declare one with `DIM`, `COM`, `LOCAL DIM`, or `DEFSUB'`, KCML automatically allocates 16 bytes. For anything larger, declare explicitly.

### Variable Name Rules

- 1–120 characters long.
- Characters: `A-Z`, `a-z`, `0-9`, underscore `_`.
- Must start with a letter (`_` prefix is reserved for constants).
- `@` prefix marks a global variable (shared across partitions).
- `.` prefix marks a field variable (sub-string descriptor).
- `$` suffix marks a string variable.
- Parentheses mark an array: `sales(10)`.
- Array names cannot start with the letters `fn`.
- Case is insignificant in names; KCML displays keywords in upper case and variable names in lower case.
- `var$` and `var$(1)` are different variables — the opening parenthesis is part of the array name.

### Typical Variable Names

```
Numerics:   i
            counter
            days_in_the_month(12)
            sales_by_division(25,1024)
            @partitions_in_use
            @lock_table(256)

Strings:    q6$
            surname$
            color_palette$(7)
            @message_of_the_day$
            @lock_records$(32)

Fields:     .color$
            .salary
            .name$(100)
            .counters(100)
            .@position
            .@title$(960)
```

For global field variables, the period precedes the `@` sign: `.@title$`.

## Array Variables

Arrays may have up to two dimensions and must be declared with `DIM`, `COM`, or `LOCAL DIM`. Elements are automatically initialized (zero for numerics, spaces for strings).

A useful pattern is to declare an array with zero dimensions and extend it with `MAT REDIM` to exactly the size needed at runtime:

```kcml
COM references(0,0)
MAT REDIM references(rows, columns)
```

This avoids pre-allocating a fixed worst-case size. When the data is no longer needed, `MAT REDIM references(0,0)` frees the memory. `MAT REDIM` can also change the number of dimensions.

## Common vs. Non-Common Variables

By default, all variables are cleared when a new program is loaded. To preserve a variable's value across `LOAD` statements, declare it with `COM` instead of `DIM`:

```kcml
DIM sales(10)
COM junk$20, new$
```

- `COM` variables survive `LOAD` but are cleared by `CLEAR`, `CLEAR V`, or `LOAD RUN`.
- `DIM` variables (and implicitly declared variables) are always cleared on `LOAD`.
- `COM CLEAR` can demote trailing `COM` variables to non-common status.

If no length is given for a `COM` string, 16 bytes are allocated:

```kcml
COM junk$20, new$    REM junk$ gets 20 bytes, new$ gets 16 bytes
```

## Local Variables

`LOCAL DIM` and `DEFSUB'` parameters create variables scoped to the subroutine they are declared in. When the subroutine exits, the local variables are destroyed and any shadowed outer variables are restored. Local variables make subroutines safer by eliminating accidental side-effects on global state.

## Initializing Variables

Variables do not need to be declared before use (though it is good practice). Undeclared variables in the KCML Workbench are underlined as a reminder.

**Scalar initialization in DIM/COM:**

```kcml
DIM title$ = "Number 1", esc$ = HEX(1B)
```

The size of the literal determines the size of the string variable. Numeric initializers may be any expression resolvable at load time.

**Assignment in code:**

```kcml
total = 0
result = new_val / old_val
```

**Multiple variables set to the same value:**

```kcml
total, count, value = 100
first$, last$, next$, previous$ = "ABCDEFG"
```

**Initializing entire arrays:**

```kcml
figures() = ZER      REM all elements to 0
totals()  = CON      REM all elements to 1
contents$() = ALL("A")  REM every byte set to "A"
```

## Constants

There are two kinds of constant in KCML:

**Literals:** numeric (`2`, `3.14`, `1.5E10`) or string (`"hello"`).

**Named constants:** variables whose name begins with an underscore. They must be declared and initialized in a `DIM` or `COM` statement and cannot be modified after that.

```kcml
DIM _BUFSIZE = 8 * 1024
DIM buffer$(_BUFSIZE)
```

The following are errors:

```kcml
_BUFSIZE = 2048          REM error - cannot assign to a constant
DIM _SomeConstant        REM error - constant must be initialized
```

The special constant `#PI` holds `3.14159265359` and requires no declaration.

Constant functionality is controlled by byte 59 of `$OPTIONS RUN` and is enabled by default as of KCML 6.10.

## The READ and DATA Statements

`DATA` statements embed static values directly in a program. `READ` assigns the next unread value to a variable, advancing a data pointer:

```kcml
READ name$, score
DATA "Alice", 95
```

- The data pointer starts at the first `DATA` statement on program resolution.
- `RESTORE` resets the pointer to a named `DATA` label.
- Reading past the end of available data produces an error.

## Pointers

The `SYM(` function returns a symbol-table index for a variable. That index can later be used to access the variable generically, enabling subroutines that operate on any variable without needing to know its name:

```kcml
DIM abc$110
var1 = SYM(abc$)
SYM(*var1)$ = "HELLO WORLD"
PRINT SYM(*var1)$
```

**Output:**
```
HELLO WORLD
```

Pointers work for alpha, numeric, and field variables, including arrays. They allow more general subroutines and can improve performance by avoiding copying large strings into and out of subroutine arguments.

## Reserved Words and Spaces

Because KCML supports multi-character variable names, spaces are significant. Reserved words like `PRINT`, `READ`, `LOAD`, `SELECT INPUT` must be separated from identifiers by spaces. Without spaces, the compiler cannot distinguish between a variable name and a keyword:

```kcml
SELECT INPUT name$    REM correct - SELECT INPUT with variable name$
SELECTINPUTNAME$      REM error - ambiguous, no spaces
```

When displaying stored code, KCML inserts spacing automatically and renders keywords in upper case, variables in lower case.

## Using Double Quotes

Double quotes delimit string literals in print statements, assignments, and file commands:

```kcml
PRINT "This is a test!"
tmp$ = "Testing"
SAVE "File99"
```

To include a literal double-quote character in a string, double it:

```kcml
PRINT "The double quote "" character!"
```

**Output:**
```
The double quote " character!
```

This also applies in comparisons and sub-string operations:

```kcml
IF abc$ == """" THEN GOSUB 'Get_Next_Record
STR(zyx$, 99, 2) = """"""
```

The first example tests whether `abc$` equals a single `"`. The second sets a 2-byte sub-string to `""`.

## Notes

- String variables implicitly declared (never dimensioned) receive 16 bytes. This is often too small; always `DIM` strings that may hold more.
- `var$` and `var$(1)` are entirely separate variables. Arrays and scalars of the same base name occupy different name spaces.
- The `_` prefix on variable names enables constant semantics only when byte 59 of `$OPTIONS RUN` has the `HEX(01)` bit set (the default since KCML 6.10). In older programs that use `_`-prefixed variables as ordinary variables, this byte should be cleared.
- See also: `COM`, `DIM`, `LOCAL DIM`, `MAT REDIM`, `SYM(`, `$OPTIONS RUN`
