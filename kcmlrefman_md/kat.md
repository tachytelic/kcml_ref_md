# kat — KCML Decompiler / ASCII Listing Utility

> Produces readable ASCII listings from compiled KCML programs; it is in some ways the inverse of the compile utility.

## Availability

`kat` was **removed in KCML 6.2**. It is not present in standard KCML 6.x installations. If you have it available, it has been copied from an earlier release (pre-6.2) and placed manually on the system (e.g. `/usr/local/kcml/kat`).

The version bundled on this system is `06.00.88.13214`.

## Synopsis

```bash
kat [-acfhlrskunxv3] [-p filename] [-P filename] [-e sectors] [-i sectors] \
    [-m mask] [-W inplatter] [-w outplatter] filename [, filename ...]
```

Program files can be UNIX/DOS files, or files on a platter image (via `-W`). Output is written to stdout.

Use `iskcml -P` to verify a file is a compiled KCML program before passing it to `kat`.

## Default behaviour (no options)

```bash
kat /path/to/program
```

Produces output suitable for loading back into KCML with `LOAD ASCII`. Each output line contains a line number followed by all statements for that line, with no formatting — everything on one line per KCML line number:

```
01000 REM % Main program:DIM items(3000),buf$1000,...:IF x THEN DO:...
01005 IF ENV("X")<>" " THEN DO:...
```

## Formatted output (`-f`)

```bash
kat -f /path/to/program
```

Produces output similar to the KCML `LIST` command — one statement per line, with continuation lines indented and prefixed with `    : `:

```
01000 REM % Main program
    : DIM items(3000),buf$1000,...
    : IF x THEN DO
    : ...
```

This is the most human-readable form and is recommended for code review and inspection.

## Options

### Output format

| Option | Purpose |
|--------|---------|
| `-f` | Formatted output: one statement per line, similar to the KCML `LIST` command |
| `-h` | Prefix each line with the source filename — useful when piping output to `fgrep` or other UNIX tools. Combining `-f` and `-h` is not particularly useful |
| `-k` | Prefix each statement in a decomposed listing with the line number and statement number |
| `-x` | Produce a symbol cross-reference only (no source listing) |
| `-r` | Remove text from REM statements |
| `-a` | Force all symbols to lowercase (this was the default prior to KCML 5) |

### Compatibility / version targeting

| Option | Purpose |
|--------|---------|
| `-3` | Generate release 3.00 compatible code |
| `-c` | Generate source code for KCML versions prior to release 2.00 (e.g. `==` becomes `=`). Only valid if no release 2 or release 3 statements are present in the program |
| `-n` | Produce output formatted for BASIC-2C. Implies `-c` and `-f`. No checking for KCML extensions is performed |
| `-r30` | Check for KCML 3.0x compatibility |
| `-r31` | Check for KCML 3.1x compatibility |
| `-r32` | Check for KCML 3.2x compatibility |
| `-r40` | Check for KCML 4.0x compatibility |
| `-R n` | Report lines containing more than `n` p-code operators |

### iskcml-equivalent options

| Option | Purpose |
|--------|---------|
| `-p filename` | Performs the same function as the `iskcml` utility (verbose: prints version and byte order) |
| `-P filename` | Performs the same function as `iskcml -P` (silent: exit 0 if KCML, exit 1 if not) |

### Platter (BASIC-2) options

| Option | Purpose |
|--------|---------|
| `-W plat` | Use a platter image file as input; files are looked up in its catalogue |
| `-m mask` | Only list files matching this mask — can only be used with `-W` |
| `-w plat` | Write output as a BASIC-2 compatible file in release 3 atomised form into the named platter image |
| `-e sectors` | Only used with `-w`. Add the specified number of sectors to the file before placing it on the platter. Also adds a BASIC-2 header and trailer |
| `-i sectors` | Only used with `-w`. Create the platter with the specified number of index sectors before copying any files. Default is 43 index sectors |

### Miscellaneous

| Option | Purpose |
|--------|---------|
| `-l` | Read filenames from stdin rather than the command line |
| `-s` | Suppress system error messages (permission errors, protection errors, KEYIN and `$GIO` warnings, etc.) |
| `-u` | Unconditionally overwrite existing output files |
| `-v` | Display the version number of `kat` and exit |

## Typical uses

**Inspect a compiled program (formatted, readable):**
```bash
/usr/local/kcml/kat -f /user1/kopen/D40/SP/MANAG | less
```

**Check a file is KCML before decompiling:**
```bash
if /usr/local/kcml/iskcml -P "$file"; then
    /usr/local/kcml/kat -f "$file"
fi
```

**Decompile all KCML files in a directory to text files:**
```bash
find /user1/kopen/D40/SP -type f | while read f; do
    if /usr/local/kcml/iskcml -P "$f"; then
        /usr/local/kcml/kat -f "$f" > "${f}.src"
    fi
done
```

**Search for a symbol across multiple compiled programs:**
```bash
/usr/local/kcml/kat -h /user1/kopen/D40/SP/MANAG /user1/kopen/D40/SP/OTHER | fgrep "ki_status"
```

**Cross-reference all symbols in a program:**
```bash
/usr/local/kcml/kat -x /user1/kopen/D40/SP/MANAG
```

**Decompile all files on a platter image:**
```bash
/usr/local/kcml/kat -f -W /path/to/platter.img
```

## Notes

- `kat` also provides backward compatibility with BASIC-2 and BASIC-2C (see `-n`, `-c`, `-3` options).
- The `ucompile` script (also in `/usr/local/kcml/`) can be used to run `kat` across entire directories or platter images in batch mode.
- When producing output for `LOAD ASCII`, use the default mode (no `-f`). The formatted output produced by `-f` is for human reading and may not load correctly.
- See also: [`iskcml`](iskcml.md) for file type detection.
