# MAT assignment (array = array)

> Copies one array into another, automatically adjusting the receiver's dimensions.

## Syntax

```
receiver_array() = source_array()
```

The legacy `MAT receiver = source` form is also accepted but automatically rewritten by KCML to the modern form.

## Description

Copies each element of `source_array` into `receiver_array`. For numeric arrays, the receiver is automatically resized to match the source. For string arrays, no automatic resizing occurs unless `REDIM` is used.

## Examples

```kcml
first() = second()          REM copy numeric array

p$() = q$()                 REM copy string array (no auto-resize)
REDIM p$() = q$()           REM copy and resize string array
```

## Notes

- KCML rewrites `MAT A = B` to `A() = B()` automatically.
- String array copy is just a special case of LET assignment — no dimension change unless `REDIM` is used.

## See Also

- `MAT COPY` — copy with optional reversal and subfield selection
- `MAT REDIM` — resize an array
- `LET` — assignment
