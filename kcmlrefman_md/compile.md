# compile (Unix utility)

> Compile KCML ASCII source files into binary programs.

## Syntax

```
compile [options] source... destination
```

On Unix, `compile` is a symlink to the `kcml` executable. On other systems: `kcml -c`.

## Description

`compile` converts ASCII KCML source files (`.asc` or `.SRC` extensions) into compiled binary programs. It can output to a directory on the native filesystem or to a platter image file.

Source specifiers may be a file, a wildcard (`*.SRC`), or a directory. If a directory is given, the destination must also be a directory (or platter with `-w`). Directory hierarchies are reproduced in the output. Output directories are created as needed.

Only files named `base.asc` or `base.SRC` are compiled; output is named `base`.

## Options

| Option | Description |
|--------|-------------|
| `-b maxexp` | Clamp exponents: expressions > `1E{maxexp}` become `1E{maxexp}`. For older processors (VAX, Pyramid, CCI 6/32) that cannot hold floats > 1E34. |
| `-d` | Delete source file after successful compilation |
| `-e sectors` | With `-w`: add `sectors` extra sectors + Wang BASIC-2 header/trailer to each file |
| `-i index` | With `-w`: create platter with `index` index sectors (default 43) |
| `-r` | Overwrite existing output files (default: don't overwrite) |
| `-s` | Strip REM text from compiled programs (same as `SAVE <R>"PROG1"` inside KCML) |
| `-v` | Verbose: display filenames as compiled |
| `-w platter` | Create/write to named platter image file |
| `!` | Prompt for a password to scramble programs (see `SELECT PASSWORD`) |

## Examples

```sh
compile -vs ACCOUNTS/SOURCE ACCOUNTS/PROGS
```
Compile all `.asc`/`.SRC` files under `ACCOUNTS/SOURCE` into `ACCOUNTS/PROGS`, stripping REMs, verbose output. Existing files not overwritten.

```sh
compile -v -w D11.bs2 -i 253 *.SRC >/tmp/log 2>&1
```
Compile all `.SRC` files in the current directory onto platter `D11.bs2` (253-sector index). Existing platter files not overwritten. Log to `/tmp/log`.

## Compatibility

Platter compilation was introduced in KCML 3.00.00.

## See Also

- `$COMPILE` — compile within a running KCML program
- `kcml` — KCML interpreter
- `SAVE` — save a program from within KCML
- `SELECT PASSWORD` — program scrambling
