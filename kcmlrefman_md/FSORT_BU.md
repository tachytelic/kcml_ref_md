# FSORT BU

> Sorts the contents of a native operating-system file with a fixed record length.

## Syntax

```
FSORT BU #stream, [file1 [TO file2]] [, skip_bytes] <reclen [, num_records]> [KEY array | string_expr]
```

| Element | Description |
|---------|-------------|
| `#stream` | Stream number for temporary workspace |
| `file1` | Source file path |
| `TO file2` | Optional destination file (in-place sort if omitted) |
| `skip_bytes` | Number of bytes at the start of the file to skip (copied unchanged) |
| `reclen` | Record length (required, inside angle brackets `< >`) |
| `num_records` | Number of records to sort (default: whole file) |
| `KEY array` | Numeric array `(N,3)` specifying sort segments |
| `KEY string_expr` | String expression listing key segment descriptors |

## Description

`FSORT BU` sorts a fixed-record-length native file in ascending lexicographic order by default.

- **In-place sort**: `FSORT BU #stream, "MYFILE" <16>` — sorts and overwrites the same file.
- **Copy-and-sort**: `FSORT BU #stream, "SOURCE" TO "DEST" <16>` — leaves source unchanged.
- **Skip bytes**: An optional byte count at the start of the file (e.g. a header) is copied unchanged to the output without being sorted.
- **Temporary files**: The `WORKSPACE` environment variable specifies the directory for temporary work files created during sorting.

### KEY clause

Without `KEY`, the entire record is used as the sort key (forward lexicographic).

With `KEY numeric_array`, the array has dimensions `(N, 3)` where N is the number of key segments. For each segment:

| Array element | Meaning |
|---------------|---------|
| `key(i,1)` | Direction: negative = descending, positive = ascending |
| `key(i,2)` | Start byte of segment (1-based) |
| `key(i,3)` | Length of segment in bytes |

With `KEY string_expr`, the expression is a string of key descriptors (alternative format).

## Examples

### Simple in-place sort, 16-byte records

```kcml
FSORT BU #3, "SRECS-1" TO "TEMP-1", 1 <16>
```
Sorts `SRECS-1` into `TEMP-1`, skipping the first 256 bytes (copied as-is). Records are 16 bytes.

### Sort with skip and explicit record count

```kcml
FSORT BU #7, "SORTFILE", skip_1 <120, file_size>
```

### Copy-sort to output file

```kcml
FSORT BU #33, "SORT-IN" TO "SORT-OUT", 5 <RecLen>
```

### Sort on the current stream's platter (no filename)

```kcml
FSORT BU #71
```

### Multi-key sort using array

```kcml
DIM key(2,3)
key(1,1)=1   : key(1,2)=1  : key(1,3)=10    REM first 10 bytes ascending
key(2,1)=-1  : key(2,2)=11 : key(2,3)=4     REM bytes 11-14 descending
FSORT BU #5, "ORDERS" <80> KEY key()
```

## Notes

- Platter-image files must be sorted in-place (no `TO` clause).
- FSORT BU operates on **native OS files** with fixed-length records. KISAM/KSAM file sorting is handled differently.
- Up to 10 key segments can be specified in the legacy array form.
- The `WORKSPACE` environment variable determines where temporary work files are created.

## See Also

- `FSORT` — sort a KSAM or stream file
- `OPEN#` — open a stream
- `ENV(` — read the WORKSPACE environment variable
