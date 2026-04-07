# SELECT LIBRARY

> Selects a library for use with `@LIST` statements.

## Syntax

```
SELECT LIBRARY
SELECT LIBRARY "library_name"
```

## Description

Sets the library that will be used for all subsequent `@LIST` (library list/call) statements. The selected library is also automatically set when a library is loaded.

`SELECT LIBRARY` without an argument reverts to the traditional global `@` library.

## Examples

```kcml
SELECT LIBRARY              : REM  revert to global @ library
SELECT LIBRARY "MyLib"      : REM  use MyLib for @LIST operations
```

## Notes

- Introduced alongside KCML's shared library/module system.
- The library file must have been loaded (via `MODULE` or `LIBRARY ADD`) before selecting it.

## See Also

- `MODULE` — library management (LIBRARY ADD/REMOVE)
- `SELECT` — overview
