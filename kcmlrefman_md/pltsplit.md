# pltsplit (Unix)

> Extract program or data files from a platter image into the filesystem.

## Syntax

```
pltsplit [-psd] [-f mask] platter directory
```

## Description

`pltsplit` is the reverse of `pltglue`. It copies programs or data files from a platter image into a Unix directory.

- KCML programs: BASIC-2 headers and trailers are removed before creating the file.
- Data files and BASIC-2 programs: copied without modification.

## Options

| Option | Description |
|--------|-------------|
| `-d` | Convert data files only |
| `-f mask` | Limit to files matching mask (limited pattern matching) |
| `-p` | Convert program files only (use `deatom` for KCML >= 2.06.08 programs) |
| `-s` | Also convert scratched files |

## Example

```sh
pltsplit -dsv -f 'GB*' D11.2200 D11.tmp
```

Converts all data files (including scratched) from `D11.2200` to the directory `D11.tmp`, only files matching `GB*`. Verbose output.

## See Also

- `pltglue` — add files to a platter
- `pltlist` — list platter contents
- `ucompile` — batch decompile from platter
- `kat` — decompile individual programs
