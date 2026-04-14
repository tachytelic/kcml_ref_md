# UFN — User Defined Functions

> Extends KCML with external C functions loaded at runtime as a shared library, callable via `CALL` like any built-in KCML function.

## Overview

The UFN interface connects KCML with compiled C code. KCML handles type conversion between its internal formats (BCD numbers, fixed-length strings) and standard C types (int, double, null-terminated strings). Once a UFN library is loaded, its functions are indistinguishable from built-in `CALL` targets.

UFNs are the correct tool when:
- A task is impractical in KCML (e.g. bitwise manipulation, binary protocol encoding, complex string transformation)
- Performance is critical for a tight loop over large data
- An existing C library can be wrapped rather than reimplemented

## Loading a UFN Library

Pass the shared library to KCML with the `-x` flag. The `.so` extension is added automatically:

```bash
kcml -x /path/to/uf_json.so -p myscript.kcml
# or without extension:
kcml -x /path/to/uf_json -p myscript.kcml
```

Multiple `-x` flags may be used to load multiple libraries.

## KCML Call Syntax

```
CALL function_name param1 [, param2 ...] TO return1 [, return2 ...]
```

The function name is the string defined in the `UFN_Spec` table (see below).

**Example:**

```kcml
: DIM raw$256, escaped$512
: raw$ = "Hello ""World"" and C:\path"
: CALL JSON_ESCAPE raw$ TO escaped$
: PRINT escaped$
```

## Listing Available Functions

```
LIST U
```

Lists all built-in CALLs and any UFNs loaded in the current session, with their parameter signatures.

```
LIST CALL
```

Lists all `CALL` statements in the current program by line number.

## Building a UFN Library

### Required files

| File | Purpose |
|------|---------|
| `uf_pub.h` | KCML-supplied public header — defines all types, macros, and the `UFN_Spec` struct |
| `uf_xxx.c` | Your C source file |
| `uf_xxx.mak` | Makefile (based on the KCML-supplied `uf_samp.mak`) |

### Compile

```bash
make -f uf_xxx.mak
```

Produces `uf_xxx.so` (Linux/UNIX) or the platform equivalent.

### Compiler flags (Linux)

```makefile
CFLAGS  = -O -DUNIX -fPIC -Wall
LDFLAGS = -shared
```

Add `-m32` on 64-bit hosts if KCML is a 32-bit build.

## C Implementation

### Entry point

KCML calls this function once on library load to obtain the function table:

```c
UFN_Spec * UFN_API uf_ext(UFN_Subs *p)
{
    return UFN_Table;
}
```

### UFN_Spec table

Defines the functions exported to KCML. **Must be sorted alphabetically by name** — KCML uses binary search for lookup. Terminate with a zero-name sentinel entry.

```c
static UFN_Spec UFN_Table[] = {
    { "DOUBLEIT",    0, doubleit,    { INT,  RCVR(INT),  0 } },
    { "JSON_ESCAPE", 0, json_escape, { CSTR, RCVR(CSTR), 0 } },
    { "REVERSEIT",   0, reverseit,   { CSTR, RCVR(CSTR), 0 } },
    { "", 0, 0, { 0 } },   /* end marker */
};
```

### Parameter types

| Constant | Description |
|----------|-------------|
| `CSTR` | C string (null-terminated, no embedded NULs). Trailing blanks stripped before passing in. When returned to KCML the result is blank-padded to fill the receiver variable. |
| `KSTR` | KCML string (pointer + length, may contain NULs). Used for binary/structured data. |
| `INT` | 4-byte signed integer. Fractional values are truncated (987.654 → 987). |
| `DOUBLE` | 8-byte double. |
| `RCVR(x)` | Wraps any type to mark it as an output (receiver) parameter. |
| `OPTPAR(x)` | Marks a parameter as optional. |
| `ARRAY(x)` | Marks a parameter as an array of the given type. |

Maximum parameters: 12 (`MAXPARAMS`). Maximum function name length: 23 characters (`UFN_NAMELEN`).

### Parameter access macros

Inside a UFN C function, access parameters via the `pb` pointer (expanded from `UFN_ARGS`):

| Macro | Access |
|-------|--------|
| `NVAL(n)` | Numeric value (double) of parameter n |
| `IVAL(n)` / `NINT(n)` | Integer value of parameter n |
| `SVAL(n)` | `unsigned char *` pointer to string data of parameter n |
| `SLEN(n)` | Length (bytes) of string parameter n |
| `SATTR(n)` | String attribute flags of parameter n |
| `SYPTR(n)` | Symbol pointer for `SYMPTR`-type parameter n |

### Function signature and return codes

```c
static UFN_RET UFN_API my_function(UFN_ARGS)
{
    /* UFN_ARGS expands to: UFN_Value *pb */
    ...
    return UFN_SUCCESS;
}
```

| Return value | KCML error raised |
|---|---|
| `UFN_SUCCESS` (0) | None — success |
| `UFN_BADARGS` (1) | S24 — wrong parameters supplied |
| `UFN_ERROR` (2) | P46 — recoverable error from user function |
| `UFN_FATAL` (3) | S22 — unrecoverable error |

### Memory allocation

`UFN_Subs` passes KCML's internal `malloc`/`realloc`/`free` pointers (via `UFN_MALLOC`, `UFN_REALLOC`, `UFN_FREE` macros). In KCML 4 and later these are no longer needed — call the standard C runtime functions directly.

## Example: DOUBLEIT (integer in, integer out)

```c
static UFN_RET UFN_API doubleit(UFN_ARGS)
{
    IVAL(1) = IVAL(0) * 2;
    return UFN_SUCCESS;
}
```

KCML usage:
```kcml
: DIM x, y
: x = 27
: CALL DOUBLEIT x TO y
: PRINT y   REM prints 54
```

## Example: REVERSEIT (string in, string out)

```c
static UFN_RET UFN_API reverseit(UFN_ARGS)
{
    const char *in  = (const char *)SVAL(0);
    char       *out = (char *)SVAL(1);
    int         len = strlen(in);
    int         i;
    for (i = 0; i < len; i++)
        out[i] = in[len - 1 - i];
    out[len] = '\0';
    return UFN_SUCCESS;
}
```

KCML usage:
```kcml
: DIM from$30, to$30
: from$ = "quick brown fox"
: CALL REVERSEIT from$ TO to$
: PRINT to$   REM prints "xof nworb kciuq"
```

## Notes

- Function names in `UFN_Spec` are matched exactly as declared — use uppercase by convention to match KCML call-site style.
- The `UFN_Table` **must** end with a zero-name sentinel `{ "", 0, 0, { 0 } }` — a missing sentinel causes a crash.
- `CSTR` input parameters have trailing blanks stripped automatically by KCML before the C function is called; this is usually correct for fixed-length KCML string variables.
- Output `RCVR(CSTR)` buffers are blank-padded by KCML after return to fill the declared receiver variable size.
- Declare all C functions before the `UFN_Table` to avoid forward-reference errors.
- The library name given to `-x` does not need the `.so` extension — KCML appends the OS default automatically.

## See Also

- `CALL` — invokes built-in and UFN functions
- `LIST U` — lists loaded UFNs and their parameter signatures
- `LIST CALL` — lists all CALL statements in the current program by line number
