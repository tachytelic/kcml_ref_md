# LINPUT LIST

> Displays a position-based menu at specific screen coordinates and returns the selected option. Text-mode applications only.

## Syntax

```
LINPUT LIST alpha_receiver
```

The `alpha_receiver` must be at least 9 bytes long and **terminated with one or more `HEX(FF)` bytes**. It contains 6 control bytes followed by triplets defining menu positions.

## Description

`LINPUT LIST` places a selection block at specific screen positions (triplets). The user navigates with spacebar/backspace or first-letter matching, and presses RETURN to confirm.

### Control bytes (bytes 1–6)

| Byte | Direction | Description |
|------|-----------|-------------|
| 1 | IN | Initial triplet index (normally HEX(01) for first) |
| 2 | IN | Symbol for "selected" indicator (HEX(82) = right arrow, HEX(8B) = block) |
| 3 | IN | Symbol to erase the block (normally HEX(20) = space) |
| 4 | OUT | Index of selected triplet on exit |
| 5 | OUT | HEX(00) = RETURN/CANCEL; HEX(FD) = function key terminated |
| 6 | OUT | Character pressed (e.g. HEX(0D) = RETURN, HEX(7F) = SHIFT+TAB/FN) |

### Triplets (3 bytes each, starting at byte 7)

| Byte | Description |
|------|-------------|
| 1 | Column (0–79) |
| 2 | Row (0–23) |
| 3 | Tag character (usually first letter of menu text) |

End the triplet list with `HEX(FF)`.

### Navigation

- **Spacebar**: advance to next triplet (wraps)
- **Backspace**: reverse
- **Letter key**: jump to next triplet whose tag matches
- **RETURN / EXECUTE**: confirm; byte 4 = selected index
- **CANCEL**: abort; byte 4 = 0

### Mouse support (Windows / KClient)

| Action | Behaviour |
|--------|----------|
| Left click / double-click | Select |
| Left drag | Position and select |
| Right click / double-click | Abort |
| Right drag | Position then abort |

## Example

```kcml
DIM menu$100
PRINT HEX(0306)
menu$ = HEX(0182 2020 2020 0505 3105 0632 0507 33FF FFFF FF)
PRINT AT(5,7); "1st option"
PRINT AT(6,7); "2nd option"
PRINT AT(7,7); "3rd option"
LINPUT LIST menu$
REM byte 4 of menu$ = selected index (1, 2, or 3)
PRINT HEXOF(STR(menu$, 4, 1))
```

The control bytes specify:
- HEX(01): start at triplet 1
- HEX(82): use right-arrow as selector symbol
- HEX(20): space erases the block
- Triplet 1: column 5, row 5, tag `1` (HEX(31))
- Triplet 2: column 5, row 6, tag `2` (HEX(32))
- Triplet 3: column 5, row 7, tag `3` (HEX(33))

## Notes

- For text-mode applications only.
- `alpha_receiver` must be terminated with `HEX(FF)` — missing terminator causes unpredictable behavior.
- `LINPUT LINE` is simpler for horizontal word menus; `LINPUT LIST` is for menus at arbitrary positions.

## See Also

- `LINPUT LINE` — horizontal ring menu (simpler)
- `LINPUT` — full line input
- `PRINT AT` — position text at row/column
