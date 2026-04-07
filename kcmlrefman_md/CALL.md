# CALL

> Invokes a built-in or user-written external function (UFN) from a shared C library loaded into the KCML runtime.

## Syntax

```
CALL ufn_name [variable_list [TO receiver_list]]
```

| Element | Description |
|---------|-------------|
| `ufn_name` | Name of the external function to call |
| `variable_list` | Optional comma-separated list of input arguments |
| `TO receiver_list` | Optional comma-separated list of output variables to receive results |

## Description

`CALL` invokes user-written functions (UFNs) compiled into a shared library (`.so` on Linux) and loaded into KCML at startup with the `-x` switch:

```
kcml -x uf_samp.so START
```

This allows performance-critical or system-level code written in C (or another compiled language) to be called from KCML. It is the lower-overhead alternative to `$DECLARE`.

### Compared to $DECLARE

- `$DECLARE` is the standard way to call external functions on Windows and most Unix systems. It has more overhead but is more flexible and generally easier to use.
- `CALL` provides lower overhead and is preferred when performance is critical and the developer can write the UFN to KCML's SDK conventions.
- On Windows, `CALL` is **not** available — use `$DECLARE`.

### Memory management

If the UFN makes extensive use of `malloc()`, invoke KCML with the `-y` flag or set the `USEMALLOC` environment variable to force KCML to use the same heap manager as the C runtime.

### Built-in CALL functions

Several KCML subsystems use `CALL` syntax for built-in functions, most notably the KISAM/KDB database access layer:

```kcml
CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
CALL KI_OPEN handle, "/path/to/FILE", "R" TO ki_status
CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
CALL KI_CLOSE handle TO ki_status
```

See the [KISAM file access pattern in CLAUDE.md] for the full verified working example.

## Example

```kcml
CALL READ_NEXT handle, buffer$, length TO status
```

## See Also

- `$DECLARE` — declare and call external library functions (more portable)
- `LIST CALL` — list all loaded UFN entries
- `LIST U` — list UFN library details
- `KI_OPEN`, `KI_READ_NEXT` etc. — built-in KISAM/KDB CALL functions
