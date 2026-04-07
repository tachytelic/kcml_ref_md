# Sorting Methods

> KCML provides two statements for sorting arrays and data files: `SORT` for in-memory arrays and `FSORT` for disk-based data files.

## Overview

Sorting is fundamental to any commercial programming language. KCML provides:

- **`SORT`** — sorts numeric or alpha arrays in place, with optional sub-field and descending-order control.
- **`FSORT`** — sorts disk files of fixed-length records (BU format) or DC-format sector files, optionally writing output to a separate file.
- **`MAT SORT`** — legacy compatibility with older BASIC-2 dialects; not recommended for new code.

---

## The SORT Statement

`SORT` rearranges the elements of an array in place. No temporary or pointer arrays are required.

### Syntax

```
SORT [−]array_name()[<[−]start,length>]
SORT [−]array_name()[<.field_var$>]
```

| Element | Description |
|---------|-------------|
| `array_name()` | The numeric or alpha array to sort. |
| `−` prefix | Sort in descending order (ascending is the default). |
| `<start,length>` | Sort on a sub-field: `start` is the 1-based start position within each element, `length` is the number of characters to use as the key. |
| `<.field_var$>` | Use a previously defined field variable to specify the sort sub-field. |
| `<−start,length>` | Negative start position — sort descending on the sub-field. |

### Sorting Numeric Arrays

Numeric arrays sort in ascending order by default. Prefix the array name with `−` for descending order.

```kcml
DIM abc(4)
READ abc(): 4,6,1,9
SORT abc()
MAT PRINT abc;
SORT -abc()
MAT PRINT abc;
```

**Output:**
```
 1
 4
 6
 9
 9
 6
 4
 1
```

### Sorting Alpha Arrays

By default, alpha arrays sort on the full content of each element in ascending lexicographic order. `PRINT array$()` prints all elements concatenated on one line.

```kcml
DIM records$(4)10
MAT READ records$()
DATA "Bill AB345","SteveAB535","Alan AB543","Fred AB135"
SORT records$()
PRINT records$()
```

**Output:**
```
Alan AB543Bill AB345Fred AB135SteveAB535
```

### Sorting on a Sub-field

To sort on a portion of each element, specify the start position and length within `<` and `>`. This is useful when elements contain packed fields (e.g., a name followed by a code).

```kcml
DIM records$(4)10
MAT READ records$()
DATA "Bill AB345","SteveAB535","Alan AB543","Fred AB135"
SORT records$()<6,5>
PRINT records$()
```

**Output** (sorted by characters 6–10, the code portion):
```
Fred AB135Bill AB345SteveAB535Alan AB543
```

To reverse the order:

```kcml
SORT records$()<-6,5>
```

### Sorting on a Sub-field Using a Field Variable

Field variables (defined with `.name$ = (start, length)`) can be used instead of an explicit `<start,length>`. This makes the code more readable and easier to maintain.

```kcml
DIM records$(4)10
.name$ = (1,5)
.code$ = (6,5)
MAT READ records$()
DATA "Bill AB345","SteveAB535","Alan AB543","Fred AB135"
SORT records$()<.code$>
PRINT records$()
```

**Output:**
```
Fred AB135Bill AB345SteveAB535Alan AB543
```

To sort descending using a field variable, define a new field with a negative start position:

```kcml
.reverse$ = (-6,5)
SORT records$()<.reverse$>
PRINT records$()
```

---

## The FSORT Statement

`FSORT` sorts data files held either in the native filesystem (UNIX/Windows) or within a platter image. Two formats are supported:

- **`FSORT BU`** — for files with fixed-length binary records (read with `DATA LOAD/SAVE BU`).
- **`FSORT DC`** — for DC-format sector files (read with `DATA LOAD/SAVE DC`). Largely obsolete; mainly used for sorting locator files.

Both variants can sort in place or write sorted output to a separate file using the `TO` clause. Sorts on platter images must always be done in place.

### FSORT BU Syntax

```
FSORT BU T#stream, "source_file" [TO "dest_file"] [,skip_bytes] <record_size[,num_records]> [KEY key_array()]
```

| Parameter | Description |
|-----------|-------------|
| `T#stream` | Stream number referencing the device or directory containing the file. |
| `"source_file"` | File to sort. |
| `TO "dest_file"` | Optional output file; source is left unchanged. Omit to sort in place. |
| `skip_bytes` | Bytes at the start of the file to leave unsorted (copied unchanged to the output file). |
| `<record_size>` | Size of each fixed-length record in bytes. |
| `<record_size, num_records>` | Record size and number of records to sort. |
| `KEY key_array()` | Two-dimensional array `(N,3)` specifying up to 10 sort key segments. |

**Key array layout** — each row `(n,1..3)` specifies one key segment:

| Column | Meaning |
|--------|---------|
| `akey(n,1)` | Direction: positive = ascending, negative = descending. |
| `akey(n,2)` | Start byte of the segment within the record (1-based). |
| `akey(n,3)` | Length of the segment in bytes. |

**Example:**

```kcml
FSORT BU T#3, "SRECS1" TO "TEMP-1", 200 <100,16>
```

Sorts `SRECS1`, skipping the first 200 bytes (copied unchanged to `TEMP-1`). Each record is 100 bytes; only 16 records are sorted.

**Full example — create, populate and sort a BU file:**

```kcml
DIM sort1$(20)10, akey(2,3)
akey() = CON
akey(1,3) = 3
akey(2,2) = 5
akey(2,3) = 3
SELECT #1 "/tmp"
DATA SAVE DC OPEN T#1,(80)"SORTFILE"
ERROR DO
    DATA LOAD DC OPEN T#1,"SORTFILE"
ENDDO
REPEAT
    count = 1
    REPEAT
        recchar = 1
        REPEAT
            STR(sort1$(count),recchar) = BIN(INT(RND(1)*58)+65)
        UNTIL recchar++ ==10
    UNTIL count++ ==20
    DATA SAVE BU T#1,(byte,byte)sort1$()
UNTIL se++ ==98
FSORT BU T#1,<10,200> KEY akey()
```

Key breakdown:
- `akey(1,1)=1` — first key sorts ascending.
- `akey(1,2)=1` — first key starts at byte 1 in each record.
- `akey(1,3)=3` — first key is 3 bytes long.
- `akey(2,1)=1` — second key sorts ascending.
- `akey(2,2)=5` — second key starts at byte 5.
- `akey(2,3)=3` — second key is 3 bytes long.

### FSORT DC Syntax

```
FSORT DC T#stream, "source_file" [TO "dest_file"] [,skip_sectors] [KEY key_array()]
```

| Parameter | Description |
|-----------|-------------|
| `skip_sectors` | Number of 256-byte sectors at the start of the file to skip (copied unchanged to output). |
| `KEY key_array()` | Same `(N,3)` format as FSORT BU. |

Record length is determined automatically from header information in the first sector. All sectors must have been written in the same array format. Multi-sector DC records cannot be sorted.

**Example:**

```kcml
FSORT DC T#12, "SRECS1" TO "TMP1", 10
```

Sorts `SRECS1` into `TMP1`, skipping the first 10 sectors.

---

## The WORKSPACE Environment Variable

When `FSORT` operates it creates a temporary work file at least as large as the file being sorted. By default this is placed in `/tmp` on UNIX, or in the directory nominated by `$TMP` or `$TEMP` on Windows.

If `/tmp` is space-constrained, set the `WORKSPACE` environment variable to redirect temporary files elsewhere:

```sh
WORKSPACE=/user1/tmp.fsort
export WORKSPACE
```

---

## Notes

- `SORT` on a numeric array always uses the full element value as the key; sub-field syntax applies only to alpha arrays.
- A negative start position in `<start,length>` or a field variable with a negative start triggers a descending sort on that sub-field.
- `FSORT` on a platter image must be done in place — specifying a `TO` destination for a platter sort is not supported.
- If no `KEY` clause is given to `FSORT`, the entire record is used as the key in ascending lexicographic order.
- `MAT SORT` is retained for compatibility with older BASIC-2 dialects and carries the restrictions of that dialect; use `SORT` for new code.
