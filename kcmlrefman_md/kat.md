# kat (Unix utility)

> Decompile compiled KCML programs into ASCII source listings.

## Syntax

```
kat [-acfhlrskunxv3] [-p filename] [-P filename] [-e sectors] [-i sectors]
    [-m mask] [-W inplatter] [-w outplatter] filename [, filename ...]
```

## Description

`kat` produces readable ASCII listings from compiled KCML programs. It is the inverse of `compile`. Programs can reside on a platter image (via `-W`) or as Unix files. Output goes to standard output.

Without options, output is formatted for loading into KCML with `LOAD ASCII` — one line per program line, containing the line number and all statements without formatting.

`kat` provides backward compatibility with BASIC-2 and BASIC-2C.

Use `ucompile` to decompile entire directories or platter images in batch mode.

## Options

| Option | Description |
|--------|-------------|
| `-3` | Generate KCML 3.00 compatible code |
| `-a` | Force all symbols to lowercase (default prior to KCML 5) |
| `-c` | Generate KCML < 2.00 source (e.g. `==` → `=`) |
| `-e sectors` | With `-w`: add sectors before placing file on platter (+ BASIC-2 header/trailer) |
| `-f` | Format output like KCML `LIST` (one statement per line) |
| `-h` | Prefix each line with the filename (useful with `grep`) |
| `-i sectors` | With `-w`: create platter with specified index sectors |
| `-k` | Prefix decomposed listing with line and statement number |
| `-l` | Read filenames from standard input |
| `-m mask` | With `-W`: only list files matching this mask |
| `-n` | Produce BASIC-2C compatible output (implies `-c -f`) |
| `-p filename` | Same as `iskcml` |
| `-P filename` | Same as `iskcml -p` |
| `-r` | Remove text from REM statements |
| `-r30` | Check for KCML 3.0x compatibility |
| `-r31` | Check for KCML 3.1x compatibility |
| `-r32` | Check for KCML 3.2x compatibility |
| `-r40` | Check for KCML 4.0x compatibility |
| `-R n` | Report lines with more than n p-code operators |
| `-s` | Suppress system error messages |
| `-u` | Unconditionally overwrite existing output files |
| `-v` | Display version number |
| `-w plat` | Generate BASIC-2 compatible file in release 3 atomised form on platter |
| `-W plat` | Read programs from platter image |
| `-x` | With `-W`: produce extended format output |

## Examples

```sh
kat -f MENU                    # List MENU with one statement per line
kat -h *.bin | grep "PRINT"    # Search for PRINT across all programs
kat -W D10.plt -m 'SORT*'      # List programs matching SORT* from platter
```

## See Also

- `compile` — compile ASCII source to binary programs
- `ucompile` — batch decompile entire directories
- `LOAD ASCII` — load ASCII source into KCML
