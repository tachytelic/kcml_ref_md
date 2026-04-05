# KCML Forms - Grid Control Snippets

Verified working patterns for grid controls in KCML forms (KCML 06.00.88).

---

## Making Grid Cells Clickable

Grid cells do NOT respond to clicks by default. You must set `LeftAction = &.Click` on each cell and `LeftSelect` on the grid itself.

```kcml
REM In Enter() event, after filling cells:
.grid.LeftSelect = &.Row        : REM clicking selects whole row
FOR row = 2 TO last_row
  .grid.Cell(row,1).LeftAction = &.Click
  .grid.Cell(row,2).LeftAction = &.Click
  REM repeat for each column that should be clickable
NEXT row
```

Then handle the event with `LeftClick()` - NOT `Click()` or `SelChange()`:

```kcml
DEFEVENT MyForm.grid.LeftClick()
  DIM sel_row
  sel_row = ..CursorRow
  IF sel_row > 1 THEN DO
    REM Row 1 is the fixed header - ignore clicks on it
    sel_value$ = ..Cell(sel_row, 2).Text$
  END DO
END EVENT
```

---

## Correct Grid Event Names

From the forms designer property list:
- `LeftClick()` - left mouse button click (use this for row selection)
- `RightClick()` - right mouse button click
- `LeftDblClk()` - left double-click
- `SelChange()` - selection changed (keyboard or mouse)
- `RowRequest()` - user scrolled past last row (for paginated data)
- `EndEdit()` - editing session ended
- `EditValidate()` - validate cell before leaving

**No plain `Click()` event exists on grids.**

---

## Storing Hidden Data in a Narrow Column

Use an extra column with `ColWidth = 1` to store a key value (e.g. filename) without it being visible:

```kcml
REM In form definition:
{.grid,.kcmlgrid$,...,.Cols=7,...}

REM In Enter() event:
.grid.Cell(0,7).ColWidth = 1
.grid.Cell(0,7).Heading$ = ""

REM When filling rows:
.grid.Cell(row,7).Text$ = hidden_key$

REM In LeftClick() event:
key$ = ..Cell(..CursorRow, 7).Text$
```

---

## Column Headings and Widths

Use `Heading$` and `ColWidth` on `Cell(0, col)` — row 0 = column selector:

```kcml
.grid.Cell(0,1).ColWidth = 40
.grid.Cell(0,1).Heading$ = "Entry"
.grid.Cell(0,2).ColWidth = 160
.grid.Cell(0,2).Heading$ = "Description"
```

`Cell(row, 0)` = row selector (for row-level properties).
`Cell(0, col)` = column selector (for column-level properties including headings).

---

## Enabling a Button on Row Selection

```kcml
REM In form definition - start disabled:
{.btnView,.button$,...,.Enabled=0,...}

REM In LeftClick() event:
IF ..CursorRow > 1 THEN .btnView.Enabled = 1
```

---

## DEFEVENT Naming

- `DEFEVENT FormName.Enter()` - form initialisation (NOT `FormName.form.Enter()`)
- `DEFEVENT FormName.control.Event()` - control event
- No `RETURN` inside DEFEVENT - causes P41.003 error; use nested `IF ... THEN DO` blocks instead

---

## Clipboard Copy from a Form

Use `'KCMLWriteClipboard` to copy text to the Windows clipboard. Requires a
`$DECLARE` at script level (outside any DEFFORM/DEFEVENT):

```kcml
$DECLARE 'KCMLWriteClipboard(STR())
```

Then call it from a button event:

```kcml
DEFEVENT MyForm.btnCopy.Click()
  LOCAL DIM clip_result
  clip_result = 'KCMLWriteClipboard(text_to_copy$)
END EVENT
```

Notes:
- The leading apostrophe is required - it denotes a KClient-side function
- Returns TRUE on success, FALSE on failure
- String limit is 65535 bytes (KCML string constraint, not a clipboard limit)
- Available since KCML 5.00

---

## Listbox - Adding Items and Reading File Line by Line

`READ #fh, var$` reads a **fixed number of bytes** equal to `var$`'s declared size,
NOT a line. To read a text file line by line into a listbox, read one byte at a time
and split on LF (`HEX(0A)`):

```kcml
REM At top level - declare 1-byte read buffer and line accumulator
LOCAL DIM ch$1, line_acc$300, la_pos, bytes
la_pos = 1
REPEAT
  bytes = READ #6, ch$
  IF ch$ == HEX(0A) THEN DO
    IF la_pos > 1 THEN .lstContent.Add(STR(line_acc$, 1, la_pos - 1))
    IF la_pos == 1 THEN .lstContent.Add(" ")
    la_pos = 1
  END DO
  IF ch$ <> HEX(0A) AND ch$ <> HEX(0D) THEN DO
    STR(line_acc$, la_pos, 1) = ch$
    la_pos = la_pos + 1
  END DO
UNTIL END
IF la_pos > 1 THEN .lstContent.Add(STR(line_acc$, 1, la_pos - 1))
CLOSE #6
```

Use `listbox$` with `Style=0x50310000` for both vertical and horizontal scrollbars.
Listbox items never wrap - each item is one line regardless of length.

---

## Complete Working Example

See `kcml_executor/spool_view.kcml` - a two-form application:
1. `SpoolView` - grid listing all SPOOLMAST entries with clickable rows
2. `SpoolFileView` - listbox showing contents of the selected spool file with Copy button

Demonstrates: DATA LOAD BU file reading, grid fill, hidden column, LeftClick event,
button enable on selection, passing data between forms via shared DIM variables,
OPEN # text file reading into a listbox, KCMLWriteClipboard clipboard copy.
