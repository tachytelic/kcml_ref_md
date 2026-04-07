# fsort (Unix utility)

> Sort KCML data files in BA, BU, or DC format from the command line.

## Syntax

```
fsort [options] -f start end ... -r start end ... in_file out_file
fsort [options] ... -o in_file
```

## Description

`fsort` sorts KCML data files in BA, BU, or DC format. BA and DC modes are supported for backward compatibility; the KCML `FSORT` statement provides the same functionality from within a program.

- `in_file` — input file to be sorted
- `out_file` — output file name
- `-o in_file` — sort in place (overwrite input file)

## Parameters

| Parameter | Description |
|-----------|-------------|
| `start_sec` | Sector number at which sorting starts (0 = beginning) |
| Record size | (BA mode) Bytes per record; must be an exact sub-multiple of 256 |
| Sectors to sort | (BA mode) Number of sectors; 0 = sort to end of file |
| `-f start end` | Forward sort key: bytes `start` to `end` (1-based), ascending |
| `-r start end` | Reverse sort key: bytes `start` to `end`, descending |

Up to 10 key specifications (`-f` or `-r`) may be given. Default: forward sort on entire record.

## DC sort notes

- Administrative information is preserved.
- Array structure is maintained: if two 20-element string arrays were saved, two 20-element arrays can be loaded from the output.
- Elements may be redistributed between arrays after sorting.
- Only string arrays of the same length should be in a file to be sorted DC. Use `SORT` for numeric data.

## Workspace

Temporary sort workspace is created in `/tmp` unless the `WORKSPACE` environment variable specifies an alternative directory.

## Examples

```sh
fsort -f 1 10 accounts.ba accounts_sorted.ba
fsort -f 1 5 -r 6 10 -o data.bu
```

## See Also

- `FSORT` — sort a KCML data file from within a program
- `SORT` — sort an array in memory
- `sortdesc` — sort key descriptor format
