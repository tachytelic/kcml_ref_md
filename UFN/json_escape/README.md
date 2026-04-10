# UFN: json_escape

A KCML User Defined Function (UFN) library that provides safe JSON string escaping from KCML programs.

## Background: Why a UFN?

KCML has no built-in function for escaping strings for JSON output. When building JSON from KCML — for example, exporting ERP data to a REST API or writing a `.json` file — any string value that might contain double-quotes, backslashes, or control characters will produce malformed JSON if embedded literally.

The problem arises with real-world data like part descriptions:

```
100MM X 33M (4" X 36yds)
```

Embedding this directly into a JSON string produces invalid JSON:

```json
{ "desc": "100MM X 33M (4" X 36yds)" }
                           ^ breaks JSON here
```

KCML's `HEX(22)` / `""` quoting mechanisms handle quotes within KCML string literals, but they cannot transform arbitrary runtime data. A UFN written in C is the correct solution.

## What JSON_ESCAPE Does

Takes a string and returns a version safe for embedding inside a JSON double-quoted string value. The caller emits the surrounding `"` characters; the UFN escapes the content.

Characters handled:

| Input | Output |
|-------|--------|
| `"` | `\"` |
| `\` | `\\` |
| newline (0x0A) | `\n` |
| carriage return (0x0D) | `\r` |
| tab (0x09) | `\t` |
| other control chars (< 0x20) | `\u00XX` |
| all other characters | passed through unchanged |

## Files

| File | Purpose |
|------|---------|
| `uf_json.c` | C source — implements `JSON_ESCAPE` and the `uf_ext` entry point |
| `uf_pub.h` | KCML UFN public header (defines `UFN_Spec`, parameter type macros, etc.) |
| `uf_json.mak` | Makefile — builds `uf_json.so` |

## Building

```bash
cd UFN/json_escape
make -f uf_json.mak
```

Output: `uf_json.so`

On a 64-bit host building for a 32-bit KCML, the makefile detects the architecture and adds `-m32` automatically.

## KCML Usage

Load the library with the `-x` flag and call `JSON_ESCAPE` in your script:

```bash
kcml -x /path/to/uf_json -p myscript.kcml
```

```kcml
: DIM raw$256, escaped$512, q$1
: q$ = HEX(22)
: raw$ = "100MM X 33M (4" & q$ & " X 36yds)"
: CALL JSON_ESCAPE raw$ TO escaped$
: PRINT $PRINTF("  ""desc"": ""%s""", escaped$)
```

Output:
```json
  "desc": "100MM X 33M (4\" X 36yds)"
```

**Important:** size the output (`escaped$`) at least 2x the input in the worst case where every character is a quote or backslash. Control characters expand to 6 bytes (`\u00XX`), so 6x input is the theoretical maximum. In practice 2x is sufficient for descriptive text.

If the output buffer is too small, `JSON_ESCAPE` returns `UFN_BADARGS`, which raises an S24 error in KCML.

## Example: Part description to JSON

```kcml
01000 REM Export part to JSON
: DIM ki_status, handle, ki_sym, ki_dataptr$6, ki_key$64
: DIM rec$512, desc$64, escaped_desc$256, q$1
: q$ = HEX(22)
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: CALL KI_OPEN handle, "/erp/data/S_PART01", "R" TO ki_status
: IF ki_status <> 0 THEN PRINT "open failed"
: IF ki_status <> 0 THEN $END
: CALL KI_START_BEG handle, 1 TO ki_status
: ki_sym = SYM(rec$)
: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status == 0 THEN DO
:     desc$ = RTRIM(STR(rec$, 1, 64))
:     CALL JSON_ESCAPE desc$ TO escaped_desc$
:     PRINT "{" & q$ & "part" & q$ & ": " & q$ & RTRIM(ki_key$) & q$ & ", "
:     PRINT " " & q$ & "desc" & q$ & ": " & q$ & RTRIM(escaped_desc$) & q$ & "}"
:   END DO
: UNTIL ki_status <> 0
: CALL KI_CLOSE handle TO ki_status
: $END
```

## Notes

- `JSON_ESCAPE` uses `CSTR` parameter types — KCML strips trailing blanks from the input before passing it to C. This is correct behaviour for fixed-length KCML string variables.
- The function does **not** add surrounding double-quotes — emit those yourself (e.g. with `HEX(22)` or `$PRINTF`).
- This UFN is UNIX/Linux only (uses `-DUNIX` and produces a `.so`). A Windows build would require a separate makefile using the Windows DLL toolchain.

## Further Reading

- `kcmlrefman_md/UFN.md` — full UFN interface reference (parameter types, macros, return codes)
- `kcmlrefman_md/$PRINTF.md` — formatted string output, useful for building JSON lines
