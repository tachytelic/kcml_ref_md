# MAT SEARCH

> Scans an alpha variable or array for substrings matching a relational condition, returning their positions.

## Syntax

```
MAT SEARCH [ELEMENT] search_var, operator search_string TO pointer_var [STEP step]
```

| Element | Description |
|---------|-------------|
| `ELEMENT` | Return element number instead of byte position |
| `search_var` | Alpha variable, literal, or array to scan |
| `operator` | One of: `<`, `<=`, `==`, `<>`, `!=`, `>=`, `>` |
| `search_string` | String to compare against |
| `pointer_var` | Alpha array (2-byte binary entries) or numeric array for results |
| `STEP` | Bytes to skip between comparisons (default: 1) |

## Description

Scans `search_var` for substrings matching the condition. Each found position is stored in `pointer_var`.

- **Alpha pointer**: each location stored as a 2-byte binary value (relative byte position). Limits search to 64kb — now discouraged.
- **Numeric pointer**: positions stored as decimal. Supports arrays >64k. Last entry set to 0.

`STEP` specifies the stride — typically set to the element length when searching an array as a flat buffer.

`ELEMENT` returns the array element number instead of the byte offset; only meaningful when `STEP` equals the element size.

**Important:** KCML uses `LEN()` internally to determine substring length. Trailing spaces matter — use `STR(` to be explicit about the comparison length.

The comma after `search_var` is mandatory.

## Examples

```kcml
DIM source$(5)6, point$2
source$(1) = "steve" : source$(2) = "fred"
source$(3) = "alan" : source$(4) = "john" : source$(5) = "bill"
name$ = "alan"

MAT SEARCH source$(), == STR(name$,, 6) TO point$ STEP 6
PRINT "Byte position: "; VAL(point$, 2)   REM 13

MAT SEARCH ELEMENT source$(), == STR(name$,, 6) TO point$ STEP 6
PRINT "Element number: "; VAL(point$, 2)  REM 3
```

More examples:
```kcml
MAT SEARCH temp$(), == STR(string$,, 5) TO pointer$ STEP 5
MAT SEARCH FLD(fi$().nl$), == FLD(fq$.name$) TO log
MAT SEARCH file$(), == STR(string$,, 5) TO point()   REM numeric pointer
```

## Notes

- Use numeric pointer arrays for large data sets (avoids 64kb limit).
- Use `STR(` to pad the search string to a fixed length to avoid trailing-space issues.
- The zero terminator in numeric pointer arrays marks the end of results.

## See Also

- `MAT MOVE` — move elements (can use locator from MAT SEARCH)
- `STR(` — substring with explicit length
- `LEN(` — content length
