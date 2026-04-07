# User Functions (UFN) — C Interface

> How to write external C functions callable from KCML with `CALL`.

## Description

UFNs (User Functions) are C functions in a shared library/DLL that can be called from KCML programs using the `CALL` statement. KCML automatically converts parameters between its internal formats (BCD number, fixed-size string) and standard C types (int, double, null-terminated string).

## Files provided

| File | Purpose |
|------|---------|
| `uf_samp.c` | Example C source; defines the UFN table |
| `uf_pub.h` | Header file for `uf_samp.c`; defines `UFN_Spec` typedef |
| `uf_samp.mak` | Makefile to build the sample |

## Initialisation

KCML calls `uf_ext()` during initialisation to get a pointer to the UFN table:

```c
UFN_Spec * UFN_API uf_ext(UFN_Subs *p) {
    return UFN_Table;
}
```

The argument `p` is obsolete but preserved for compatibility.

## Defining the UFN table

Each element of the table is of type `UFN_Spec`:

```c
typedef struct UFN_Spec {
    CONST char  name[UFN_NAMELEN];          /* KCML CALL name */
    UFN_RET     (UFN_API *function)(UFN_VALUE *);  /* C function pointer */
    unsigned char Param[MAXPARAMS];          /* parameter type list */
};
```

- `name` — the name used in KCML `CALL` statements
- `function` — pointer to the C implementation
- `Param` — array of parameter type codes

The table **must be in sorted order** by name. KCML performs a binary search on it at startup.

## Parameter type codes

High-order bits can be set to indicate:
- `RCVR()` macro — for parameters following `TO` in the `CALL` statement (receive back from C to KCML)
- Array parameters
- Optional parameters

## Dynamic linking

KCML is loaded with the `-x lib.so` command-line flag (Unix) to specify the shared library:

```sh
kcml -x myufns.so myprog
```

## See Also

- `CALL` — call a subroutine or external function
- `kcml` — interpreter command-line flags (`-x` for shared libraries)
