# ucompile (Unix)

> Decompile an entire directory or platter image of KCML programs to ASCII source.

## Syntax

```
ucompile [-vcnu] [-w in_platter] [-e sectors] [-i sectors] [-W out_platter]
         [-d find_list] [-f mask] [-x extension] [-p find_pred] [directory] [ascii-directory]
```

## Description

`ucompile` is a Bourne shell script that uses `kat` to decompile an entire directory (including subdirectories) or a platter image of compiled KCML programs into ASCII source files (`.asc` extension by default).

It operates in two modes:
- **Directory mode**: reads programs from native filesystem directories.
- **Platter mode**: reads programs from a platter image (`-W platter`).

## Options (both modes)

| Option | Description |
|--------|-------------|
| `-c` | Generate KCML < 2.00 compatible source (`==` → `=`) |
| `-e sectors` | With `-w`: add sectors before placing file on output platter |
| `-f mask` | Restrict decompilation to files matching mask (filename is the part after the last `/`) |
| `-i sectors` | With `-w`: create output platter with specified index sectors |
| `-n` | NPL output format (implies `-c -x SRC`); no KCML extension checking |
| `-u` | Unconditionally overwrite existing output files |
| `-v` | Verbose: list program names as processed |
| `-w platter` | Output to a BASIC-2 compatible platter in release 2 atomised form |
| `-x extension` | Use this extension instead of `asc` |

## Options (directory mode only)

| Option | Description |
|--------|-------------|
| `-p find_pred` | Insert additional `find` options after `-p` (e.g. filter by date) |
| `-d find_list` | Pathnames to descend into (default: `* .??*`) |

If `ascii-directory` is omitted, ASCII files are created alongside the originals.

## Options (platter mode only, with -W)

Use `-W platter` to read from a platter image. Combined with `-f mask` to select files.

## See Also

- `kat` — decompile individual programs
- `compile` — compile ASCII source to binary
- `pltlist` — list platter contents
- `pltsplit` — extract files from a platter
