# pltglue (Unix)

> Copy files into a platter image.

## Syntax

```
pltglue [-vru] [-e sectors] [-i sectors] platter source_files...
```

## Description

`pltglue` copies Unix files into a platter image. It can glue KCML programs, Wang programs, and data files.

- KCML programs: a Wang BASIC-2 header and trailer are added before copying.
- Data files and Wang BASIC-2 programs: copied directly without modification.

If the specified platter does not exist, it is created with a default index of 43 sectors (unless `-i` is specified).

## Options

| Option | Description |
|--------|-------------|
| `-e sectors` | Add `sectors` extra sectors to each file before gluing |
| `-i sectors` | Create platter with this many index sectors |
| `-r` or `-u` | Overwrite files that already exist on the platter |
| `-v` | Verbose mode |

## Example

```sh
pltglue -v -i 101 -e 40 D40.bin ACCPROG
```

Creates platter `D40.bin` with a 101-sector index. Places `ACCPROG` on the platter with 40 extra sectors.

## See Also

- `pltsplit` — extract files from a platter
- `pltlist` — list platter contents
- `compile` — compile programs onto a platter
