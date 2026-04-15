# UFN: json_parse

A KCML User Defined Function (UFN) library that provides full JSON parsing from KCML 6.9 programs via a handle-based API built on cJSON 1.7.17.

## Background

KCML 6.9 has no built-in JSON support. KCML 7 includes a native JSON subsystem (visible in the `jsonparse.so` debug symbols) but this is not available in the 6.x line. This UFN back-ports the capability using [cJSON](https://github.com/DaveGamble/cJSON), a small MIT-licensed C JSON parser bundled directly into the shared library.

## Functions

| KCML Call | Purpose |
|-----------|---------|
| `CALL JSON_PARSE json$ TO handle` | Parse a JSON string; returns a handle (1–64) or 0 on parse error |
| `CALL JSON_GET_STR handle, "path" TO value$` | Navigate to a node and return its string value |
| `CALL JSON_GET_NUM handle, "path" TO nval` | Navigate to a node and return its numeric value (also works for booleans: true=1, false=0) |
| `CALL JSON_ARRAY_LEN handle, "path" TO count` | Return the number of elements in a JSON array at `path` |
| `CALL JSON_FREE handle` | Release the parsed JSON tree and free the handle slot |

## Path Syntax

Paths use dot notation with optional array index brackets:

| Path | Meaning |
|------|---------|
| `"key"` | Top-level key |
| `"key.subkey"` | Nested object key |
| `"key[0]"` | First element of a top-level array |
| `"key[0].subkey"` | Key within a specific array element |
| `""` | Root — useful for `JSON_ARRAY_LEN` when the top-level value is an array |

## Files

| File | Purpose |
|------|---------|
| `uf_json_parse.c` | C source — implements all five functions and the `uf_ext` entry point |
| `uf_pub.h` | KCML UFN public header — the 2014 version from `/usr/local/kcml/uf_pub.h` |
| `cJSON.c` / `cJSON.h` | cJSON 1.7.17 — bundled to avoid 32-bit shared library dependency issues |
| `uf_json_parse.mak` | Makefile — builds `uf_json_parse.so` |
| `uf_json_parse.exp` | Linker version script — exports `uf_ext@@VER_1.0` as required by KCML |

## Building

```bash
cd UFN/json_parse
make -f uf_json_parse.mak
```

Requires: `gcc-multilib` (for `-m32` on a 64-bit host). No external cJSON package needed — cJSON is bundled.

Output: `uf_json_parse.so`

Verify the export is correct before loading:

```bash
nm -D uf_json_parse.so | grep uf_ext
# Should show: T uf_ext@@VER_1.0
```

## KCML Usage

```bash
kcml -x /path/to/uf_json_parse.so -p myscript.kcml
```

The `-x` path can be absolute or relative. Multiple `-x` flags can be combined if you are also loading `uf_json.so` (JSON_ESCAPE).

## Example

```kcml
01000 REM JSON parse example
: DIM h, count, price, name$64, city$64, qty
: DIM json$512
: json$ = "{""customer"":{""name"":""Acme Ltd"",""city"":""Manchester""},""order"":{""total"":1234.56,""lines"":[{""item"":""Widget"",""qty"":10},{""item"":""Gadget"",""qty"":3}]}}"
: CALL JSON_PARSE json$ TO h
: PRINT "handle="; h
: IF h == 0 THEN PRINT "PARSE FAILED"
: IF h == 0 THEN $END
: CALL JSON_GET_STR h, "customer.name" TO name$
: PRINT "name=["; RTRIM(name$); "]"
: CALL JSON_GET_STR h, "customer.city" TO city$
: PRINT "city=["; RTRIM(city$); "]"
: CALL JSON_GET_NUM h, "order.total" TO price
: PRINT "total="; price
: CALL JSON_ARRAY_LEN h, "order.lines" TO count
: PRINT "lines="; count
: CALL JSON_GET_STR h, "order.lines[0].item" TO name$
: PRINT "line0 item=["; RTRIM(name$); "]"
: CALL JSON_GET_NUM h, "order.lines[1].qty" TO qty
: PRINT "line1 qty="; qty
: CALL JSON_FREE h
: PRINT "freed ok"
: $END
```

Expected output:

```
handle= 1
name=[Acme Ltd]
city=[Manchester]
total= 1234.56
lines= 2
line0 item=[Widget]
line1 qty= 3
freed ok
```

## Combining with JSON_ESCAPE

Use alongside `uf_json.so` (JSON_ESCAPE) for a complete JSON round-trip — escape when building outgoing JSON, parse when consuming incoming JSON:

```bash
kcml -x /path/to/uf_json.so -x /path/to/uf_json_parse.so -p myscript.kcml
```

## Handle Capacity

The library maintains a handle table of 64 slots. A handle is allocated on `JSON_PARSE` and freed on `JSON_FREE`. Always free handles when done; running out of slots causes `JSON_PARSE` to return 0.

## Notes

- String outputs (`JSON_GET_STR`) are truncated to the declared size of the receiving variable minus 1 byte for the null terminator. Size accordingly.
- `JSON_GET_NUM` returns `0.0` for missing or non-numeric nodes (including `null`). Boolean nodes return `1.0` (true) or `0.0` (false).
- `JSON_ARRAY_LEN` returns `0` for missing or non-array nodes.
- Path resolution is case-sensitive (uses `cJSON_GetObjectItemCaseSensitive`).
- The library is not thread-safe. KCML `-p` scripts are single-threaded so this is not a concern.
- This UFN targets KCML 6.9 (32-bit ELF). The `-m32` flag is mandatory; do not remove it.

## Further Reading

- `kcmlrefman_md/UFN.md` — full UFN interface reference
- `UFN/json_escape/README.md` — JSON_ESCAPE companion function
