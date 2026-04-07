# RESAVE

> Saves the program currently in memory, overwriting an existing file.

## Syntax

```
RESAVE ["<" flags ">"] [#stream,] filename [start_line] [, end_line]
```

### Flags (optional, inside `< >`)

| Flag | Meaning |
|------|---------|
| `S` | Save selected lines only |
| `R` | Strip REM comments from saved output |
| `!` | Scramble (encrypt) using current SELECT PASSWORD |

## Description

`RESAVE` overwrites an existing file with the in-memory program. Unlike `SAVE`, it does not ask for confirmation if the file already exists.

Commonly used with `$PROG` to resave the last loaded program:

```kcml
RESAVE $PROG
```

Line range parameters save only the specified portion of the program.

## Examples

```kcml
RESAVE "TESTPROG"
RESAVE #10, prog$(3)           : REM  save to stream 10, filename in array
RESAVE $PROG 400, 9000         : REM  resave last loaded program, lines 400–9000
RESAVE "<R>" "MYPROG"          : REM  save without REM comments
```

## Notes

- **Immediate mode** or **program mode** — can be used in both.
- When used in program mode with overlaid programs (multiple LOAD'd), the combined program is saved into one file — use with caution.
- `$PROG` holds the filename of the last program loaded.
- The `!` scramble flag works with `SELECT PASSWORD` to produce a non-listable binary.

## See Also

- `SAVE` — save (may prompt if file exists)
- `REMOVE` — delete a file
- `$PROG` — last loaded program name
- `SELECT PASSWORD` — set encryption password
