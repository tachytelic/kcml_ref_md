# SORT

> Sorts a numeric or alpha array in place.

## Syntax

```
SORT numeric_arr()          (ascending)
SORT -numeric_arr()         (descending)
SORT alpha_arr$()           (ascending, full element)
SORT alpha_arr$() <start, length>   (ascending, by subfield)
SORT alpha_arr$() <.field_var>      (ascending, by field variable)
SORT alpha_arr$() <-start, length>  (descending, by subfield)
SORT alpha_arr$() KEY segs$()       (multi-segment sort with collation)
```

## Description

Sorts the array elements in place.

- **Numeric**: ascending by default; prefix with `-` for descending.
- **Alpha**: ascending by default; specify a subfield to sort by part of each element; negative start for descending.
- **KEY form**: supports multi-segment keys and collating sequences (KCML 6.0+). Each element of `segs$()` is a 4-byte segment descriptor.

### KEY segment descriptor format

Each 4-byte segment: `<length(1)><start(1)><flags(2)>`. Flag `0xC0` in flags = descending.

Example: sort on 8 bytes at offset 2, descending:
```kcml
segs$(1) = HEX(0800 02C0)
```

## Examples

```kcml
DIM numbers(5)
numbers(1) = 3 : numbers(2) = 1 : numbers(3) = 4 : numbers(4) = 1 : numbers(5) = 5
SORT numbers()
FOR i = 1 TO 5
  PRINT numbers(i);
NEXT i
REM  1 1 3 4 5
```

```kcml
DIM names$(4)
MAT READ names$()
DATA "John","Steve","Alan","Paul"
SORT names$()
FOR i = 1 TO 4
  PRINT names$(i)
NEXT i
REM  Alan  John  Paul  Steve
```

```kcml
REM Sort by character positions 21-25 of each element
SORT records$() <21, 5>
```

```kcml
REM Sort by a field variable subfield
SORT records$() <.name$>
```

```kcml
REM Case-insensitive sort using KEY
DIM segs$(1)4
segs$(1) = HEX(0800 02C0)    : REM 8 bytes at offset 2, descending
SORT a$() KEY segs$()
```

## Notes

- Sorts the array **in place** — elements are reordered, not copied.
- 1-based indexing; sorts all elements from 1 to the array's declared size.
- For sorting fixed-record native files, see `FSORT_BU`.

## See Also

- `FSORT_BU` — sort a native (fixed-record) file
- `MAT SEARCH` — search a sorted array
- `DIM` — array declaration
