# pltlist (Unix/DOS)

> List the catalogue of a platter image.

## Syntax

```
pltlist [-cdnp] [-f mask] platter
```

## Description

`pltlist` lists the catalogue of a platter image to standard output, similar to the `LIST DCT` command within KCML.

## Options

| Option | Description |
|--------|-------------|
| `-c` | Display index size, end catalogue area, and current end position |
| `-d` | List data files only |
| `-n` | List file names only, one per line |
| `-p` | List program files only |
| `-f mask` | Limit output to files matching the mask (limited pattern matching) |

## Example

```sh
pltlist -dc -f 'SORT*' D10.plt
```

Lists the names, sizes, and start positions of all files beginning with `SORT` in `D10.plt`, along with the platter's index and catalogue information.

## See Also

- `pltglue` — add files to a platter
- `pltsplit` — extract files from a platter
- `kat` — decompile programs from a platter
