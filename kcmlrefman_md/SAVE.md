# SAVE

> Saves the in-memory program to a file in compiled binary format.

## Syntax

```
SAVE ["<" flags ">"] [#stream,] filename [, start_line [, end_line]]
```

### Flags (inside `< >`)

| Flag | Meaning |
|------|---------|
| `R` | Strip REM comments before saving |
| `G` | Create a global library (deprecated — use `kmake`/`kc6` instead) |
| `!` | Scramble/encrypt (requires `SELECT PASSWORD`) |
| `S` | BASIC-2 compatibility (ignored) |

## Description

Saves the program in compiled binary form for efficient loading. The file must not already exist — use `RESAVE` to overwrite an existing file.

Line range parameters save only the specified portion:
- `SAVE name, 100` — save from line 100 to end.
- `SAVE name, 100, 500` — save lines 100–500.

To save as text (ASCII source), use `SAVE ASCII` or configure `$OPTIONS RUN` byte 46.

## Examples

```kcml
SAVE "PROGONE"
SAVE #16, "GBPROG"                : REM  save to directory on stream 16
SAVE <R> "/tmp/TEMP", 4000        : REM  save from line 4000, strip REMs
SAVE file$ 1000, 4000             : REM  save lines 1000–4000
SAVE <!> "TESTPROG"               : REM  scramble with current password
```

## Notes

- Raises `D83 File already exists` if the file is present — use `RESAVE` to overwrite.
- The compiled binary is not portable between different KCML versions.
- `SAVE <G>` global library creation is **deprecated** in favour of `kmake` and `kc6`.
- For source control, keep programs as text and use `SAVE ASCII` or `$OPTIONS RUN` byte 46 = `HEX(05)`.

## See Also

- `RESAVE` — overwrite an existing file
- `SAVE ASCII` — save as text source
- `LOAD` — load a program
- `NEWASCII` — new text source format
- `SELECT PASSWORD` — set scramble password
