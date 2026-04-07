# PRINT AT(

> Positions the cursor to a row/column before printing; optionally erases characters at that position.

## Syntax

```
PRINT AT(row, col [, erase_length]); output ...
PRINT AT(row, col,); output ...    (erase to end of screen)
```

`AT(` can appear anywhere in a `PRINT` statement, mixed with other print functions (`BOX(`, `TAB(`, `HEXOF(`).

## Parameters

| Parameter | Description |
|-----------|-------------|
| `row` | Row (0-based; 0–23 on standard 24-line screen) |
| `col` | Column (0-based; 0–79 on standard 80-column screen) |
| `erase_length` | Characters to erase at the new position (optional) |
| `,` (trailing) | If present with no erase length: erase from cursor to bottom of screen |

## Description

Moves the cursor to (`row`, `col`) on the text screen before printing the values that follow. Only relevant for text-mode (terminal) applications — ignored when printing to a file.

`TERMINFO` `Lines` and `Columns` settings can override the 24×80 defaults.

## Examples

```kcml
REM Print at top-right corner
PRINT AT(0, 74); "hello"
```

```kcml
REM Print with field erase
PRINT AT(5, 10, 20); name$     : REM erase 20 chars then print name$
```

```kcml
REM Erase to bottom of screen from row 10
PRINT AT(10, 0,);               : REM trailing comma, no erase_length
```

```kcml
REM Multiple AT( calls in one PRINT
PRINT AT(0, 0); title$; AT(23, 0); "Press ENTER to continue"
```

```kcml
REM Common screen update pattern (from real KCML source)
row = 5
PRINT AT(row, 10, 30); custname$    : REM clear 30 cols then show name
PRINT AT(row+1, 10, 30); address$
```

## Notes

- Rows and columns are **0-based**.
- `AT(` is a PRINT function — it must appear inside a `PRINT` statement, not standalone.
- When printing to a file (`PRINT #stream`), `AT(` is silently ignored.
- `erase_length` erases characters *at* the cursor position before printing the subsequent text.

## See Also

- `PRINT` — base print statement
- `PRINT BOX(` — draw a box on the screen
- `PRINT TAB(` — tab to a column
- `INPUT SCREEN` — capture screen content
