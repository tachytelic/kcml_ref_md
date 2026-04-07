# Sort Key Descriptors

> How to specify `KEY` clauses for `SORT` and `FSORT`.

## Description

The `SORT` and `FSORT` commands accept an optional `KEY` clause — a string expression containing a list of 4-byte key segment descriptors. The list terminates at the end of the string or at the first descriptor with a zero length.

## Segment descriptor layout

Each 4-byte descriptor contains:

| Byte | Content |
|------|---------|
| 1 | Length of the key segment (0 = end of list) |
| 2–3 | Start position of the segment (counted from 1) |
| 4 | Option bits (addable) |

### Option bits (byte 4)

| KCML constant | Bit value | Effect |
|---------------|-----------|--------|
| `_SORT_DESCENDING` | `HEX(20)` | Sort in descending order |
| `_SORT_COLLATESEQ` | `HEX(40)` | Use the active collating sequence |
| `_SORT_CASEINSENSITIVE` | `HEX(80)` | Case-insensitive sort |

**Note:** Case-insensitive sorting requires a collating sequence to be defined for the code page (see `collate`).

## Example

```kcml
REM Sort on bytes 1-5 ascending, then bytes 6-10 descending
DIM key$8
key$ = CHR$(5,1,0,0) & CHR$(5,6,0,HEX(20))
SORT arr$(), KEY key$
```

## See Also

- `SORT` — sort arrays in memory
- `FSORT` — sort data files
- `fsortutil` — fsort command-line utility
- `collate` — collating sequences
