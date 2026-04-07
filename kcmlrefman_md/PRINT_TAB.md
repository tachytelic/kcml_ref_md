# PRINT TAB(

> Positions the cursor to a specific column before printing the next value.

## Syntax

```
PRINT TAB(col); output ...
PRINT TAB(strexpr, width); ...
```

`TAB(` can appear anywhere in a `PRINT` statement alongside `AT(`, `BOX(`, `HEXOF(`.

## Description

**Form 1** — `TAB(col)`: moves the cursor to column `col` on the current line. Columns are 1-based. If the cursor is already past `col`, the `TAB(` is ignored. If `col` exceeds the line width, the cursor moves to column 1 on the next line.

**Form 2** — `TAB(strexpr, width)`: prints `strexpr` in a fixed-width field of `width` characters. If `strexpr` is longer than `width`, it is right-truncated. If shorter, the field is space-padded. Useful in multilanguage apps where string length may vary.

## Examples

```kcml
FOR count = 1 TO 5
  PRINT TAB(4 * count); count;
NEXT count
REM Output:     1   2   3   4   5
```

```kcml
REM Column headings
PRINT TAB(7); "Name"; TAB(30); "Amount"; TAB(45); "Date"
```

```kcml
REM Fixed-width string fields
PRINT TAB(desc$, 30); TAB(price$, 10); TAB(qty$, 6)
```

## Notes

- `TAB(` overwrites intervening characters with spaces on the screen.
- Only relevant for text-mode (terminal) output — ignored when printing to a file.
- Columns in `TAB(` are **1-based** (unlike `AT(` which is 0-based).

## See Also

- `PRINT` — base print statement
- `PRINT AT(` — absolute row/column positioning
- `PRINTUSING` — formatted numeric output
