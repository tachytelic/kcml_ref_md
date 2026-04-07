# WINDOW

> Opens and closes overlay windows on the text screen, saving and restoring the underlying content.

## Syntax

```
WINDOW OPEN [#n,] ["title",] depth, width [AT(row, col)]
WINDOW CLOSE [#n]
WINDOW CLOSE ALL
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `#n` | Window number 0–9 (default: 0) |
| `"title"` | Optional centred title (up to 78 chars); if absent, no border is drawn |
| `depth` | Height in rows |
| `width` | Width in columns |
| `AT(row, col)` | Top-left corner position (0-based) |

## Description

`WINDOW OPEN` draws a framed window on the screen. The content behind the window is saved (in terminal memory on KCML terminals, otherwise by KCML itself). Up to 10 windows can be open simultaneously.

After opening:
- The window area is cleared to the background color.
- The cursor is positioned at the top-left of the window and hidden.
- The cursor is **not** constrained to the window — text can be written anywhere on the physical screen.
- Windows do **not** scroll when text is written past the last line.

`WINDOW CLOSE #n` removes the window and restores the hidden content and cursor.

`WINDOW CLOSE ALL` closes all windows in descending order (#9 to #0).

**Windows must be closed in reverse order of opening.**

### KClient 5.03+

KClient can display text windows as floating GUI popup forms (enabled by default in client preferences).

## Examples

```kcml
REM Open a titled window at top-left
WINDOW OPEN #1, "Customer Details", 15, 40 AT(2, 10)
PRINT AT(3, 12); "Name: "; cust_name$
PRINT AT(4, 12); "Acct: "; account$
REM ... interact ...
WINDOW CLOSE #1
```

```kcml
REM Window without border
WINDOW OPEN 5, 30 AT(5, 20)
PRINT AT(6, 21); "Loading..."
WINDOW CLOSE
```

```kcml
REM Close all windows (e.g. on error exit)
WINDOW CLOSE ALL
```

## Notes

- Window numbers 0–9; each concurrent window needs a different number.
- The color palette is **not** restored on `WINDOW CLOSE` — only text, boxes, cursor, and screen attribute are restored.
- Overlapping windows must be closed in the reverse order they were opened.

## See Also

- `PRINT AT(` — position cursor for output inside window
- `PRINT BOX(` — draw boxes
- `INPUT SCREEN` — capture screen region
- `PRINT SCREEN` — restore screen region
