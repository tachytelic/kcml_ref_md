# iskcml — KCML File Detection Utility

> Command-line utility that inspects a file and reports whether it is a compiled KCML program.

## Availability

`iskcml` was **removed in KCML 6.2**. It is not present in standard KCML 6.x installations. If you have it available, it has been copied from an earlier release (pre-6.2) and placed manually on the system (e.g. `/usr/local/kcml/iskcml`).

## Synopsis

```bash
iskcml <file>
iskcml -P <file>
```

## Modes

### Verbose mode (default)

```bash
iskcml /path/to/program
```

Prints a single line to stdout:

- If the file is a compiled KCML program:  
  `/path/to/program    06.00.88, Intel/DEC byte order`
- If it is not:  
  `/path/to/program is not a compiled KCML program`

The version shown (e.g. `06.00.88`) is the KCML version that compiled the program, not the version of the interpreter currently installed. The byte-order field indicates the CPU architecture used when the program was compiled.

### Silent mode (`-P`)

```bash
iskcml -P /path/to/program
```

Produces no output. The result is communicated entirely via the exit code:

| Exit code | Meaning |
|-----------|---------|
| `0` | File is a compiled KCML program |
| `1` | File is not a compiled KCML program |

Note: the flag is **`-P`** (capital P). Lowercase `-p` does not produce silent behaviour.

## Typical uses

**Check a single file:**
```bash
iskcml /user1/kopen/D40/SP/MANAG
# → /user1/kopen/D40/SP/MANAG    06.00.88, Intel/DEC byte order
```

**Scripted detection (silent):**
```bash
if /usr/local/kcml/iskcml -P "$file"; then
    echo "$file is a KCML program"
else
    echo "$file is not a KCML program"
fi
```

**Find all compiled KCML files under a directory:**
```bash
find /user1/kopen -type f | while read f; do
    /usr/local/kcml/iskcml -P "$f" && echo "$f"
done
```

## Notes

- Works on compiled (bytecode) KCML programs — it does not parse KCML source text.
- The version reported is embedded in the compiled file header at compile time.
- On systems running KCML 6.9, programs compiled under earlier versions (e.g. 6.0) will be detected correctly — `iskcml` reads the header, it does not depend on the installed interpreter version.
