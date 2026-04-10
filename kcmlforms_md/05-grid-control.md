# KCML Forms — Grid Control

The grid is the most powerful control in the forms library. It displays tabular data with clickable, selectable, and editable cells. It is the standard way to show lists of records in KCML forms.

## DEFFORM Definition

```kcml
{.grid,.KCMLgrid$,.Style=0x50010030,\
    .Left=5,.Top=10,.Width=636,.Height=431,\
    .Id=1000,.Rows=1,.Cols=8,.FixedRows=1,.Font=.ConsolasGrid}
```

Key DEFFORM properties:

| Property | Description |
|----------|-------------|
| `Rows` | Initial row count (including fixed heading rows) |
| `Cols` | Number of columns |
| `FixedRows` | Number of heading rows (don't scroll, not selectable) |
| `FixedCols` | Number of heading columns (fixed on left) |
| `Font` | Font for all cells (overridden per-cell if needed) |

### Inline Column Widths and Headings

The Forms Designer also supports defining column widths and heading text directly in the DEFFORM control block using named sub-properties. This avoids the need to set them in the `Enter()` event:

```kcml
{.gridPartSearch,.KCMLgrid$,.Style=0x50010030,.Left=6,.Top=58,.Width=434,.Height=214,\
    .Id=1033,.Rows=1,.Cols=3,.FixedRows=1,.Font=.MonoFont,\
    .Col1={.ColWidth=76,.Col=1},\
    .Col2={.ColWidth=180,.Col=2},\
    .Col3={.ColWidth=100,.Col=3}}
```

Named sub-properties:
- `.ColN={.ColWidth=nnn,.Col=N}` — sets width of column N
- `.AnyName={.Row=1,.Col=N,.Text$="Heading"}` — sets heading text for column N (row 1 = fixed heading row)

You can still override these in `Enter()` if needed — set in DEFFORM and set again in code are not exclusive.

## Cell Addressing

Cells are addressed `Cell(row, col)` — both are **1-based** for data rows/columns. Row 0 and column 0 refer to the heading row and the row-selector column respectively.

```kcml
.grid.Cell(0, 1).Heading$ = "Part No"   : REM heading for column 1
.grid.Cell(0, 2).Heading$ = "Description"
.grid.Cell(1, 1).Text$ = "ABC123"       : REM data in row 1, column 1
```

## Core Properties

### Grid-level

| Property | Type | Description |
|----------|------|-------------|
| `Rows` | numeric | Current row count (set to resize grid) |
| `Cols` | numeric | Column count |
| `FixedRows` | numeric | Fixed heading rows |
| `FixedCols` | numeric | Fixed side columns |
| `CursorRow` | numeric | Currently selected row |
| `CursorCol` | numeric | Currently selected column |
| `DataPending` | boolean | TRUE = more rows available (triggers `RowRequest()`) |
| `AutoEdit` | boolean | Click a row to enter auto-edit mode (KCML 6.00+) |
| `TabThrough` | boolean | Tab key navigates within a row during edit |

### Cell-level (accessed via `Cell(row, col)`)

| Property | Type | Description |
|----------|------|-------------|
| `Text$` | string | Cell content |
| `Heading$` | string | Column heading (row 0 only) |
| `ColWidth` | numeric | Column width (DLUs) |
| `RowHeight` | numeric | Row height (DLUs) |
| `LinesPerRow` | numeric | Lines for multi-line text |
| `Type$` | string | Cell data type (`"D"` = date, etc.) |
| `BackColor` | colour ref | Background colour |
| `ForeColor` | colour ref | Text colour |
| `LeftAction` | enumeration | Left-click action (`&.Default`, `&.Ignore`, `&.Down`, `&.Click`, `&.ClickAndDblClick`, `&.DisableCursor`) |
| `RightAction` | enumeration | Right-click action |
| `LeftSelect` | enumeration | Left-click selection mode (`&.Row`, `&.Cell`, etc.) |
| `RightSelect` | enumeration | Right-click selection mode |
| `DropDown` | reference | Dropdown list |
| `DropStyle` | enumeration | Dropdown style |
| `Enabled` | boolean | Enable / disable cell editing |
| `ReadOnly` | boolean | Prevent editing |

## Setting Up the Grid

### Configure headings and column widths

```kcml
+ DEFEVENT MyForm.Enter()
    .grid.Cell(0, 1).ColWidth = 60
    .grid.Cell(0, 1).Heading$ = "Part No"
    .grid.Cell(0, 2).ColWidth = 200
    .grid.Cell(0, 2).Heading$ = "Description"
    .grid.Cell(0, 3).ColWidth = 80
    .grid.Cell(0, 3).Heading$ = "On Hand"
END EVENT
```

### Populate rows from a KISAM file

```kcml
+ DEFEVENT MyForm.Enter()
    LOCAL DIM ki_status, ki_sym, ki_dataptr$6, ki_key$64
    LOCAL DIM rec$1024, row, part$15, desc$30, qty
    REM ... open KISAM handle ...
    CALL KI_START_BEG handle, 1 TO ki_status
    ki_sym = SYM(rec$)
    .grid.Rows = 1        : REM start with just the heading row
    row = 1
    REPEAT
        CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
        IF ki_status == 0 THEN DO
            row++
            .grid.Rows = row
            part$ = STR(rec$, 20, 15)
            desc$ = STR(rec$, 36, 30)
            UNPACK (#########.######) STR(rec$, 513, 8) TO qty
            .grid.Cell(row, 1).Text$ = RTRIM(part$)
            .grid.Cell(row, 2).Text$ = RTRIM(desc$)
            .grid.Cell(row, 3).Text$ = qty
        END DO
    UNTIL ki_status <> 0
END EVENT
```

## Click Handling

To detect which row the user clicked, configure `LeftAction` and `LeftSelect` on the cells, then handle the `LeftClick()` event.

**`LeftAction` values:**
- `&.Click` — fires `LeftClick()` on single click
- `&.ClickAndDblClick` — fires `LeftClick()` on single click AND `LeftDblClk()` on double-click
- `&.Down` — fires `LeftClick()` on mouse-down (immediate, before release)
- `&.Ignore` — no click events

### Configure cells to be clickable (do this in Enter())

```kcml
: FOR sv_row = 2 TO .grid.Rows
:     .grid.Cell(sv_row, 1).LeftAction = &.Click
:     .grid.Cell(sv_row, 2).LeftAction = &.Click
:     .grid.Cell(sv_row, 3).LeftAction = &.Click
: NEXT sv_row
: .grid.LeftSelect = &.Row    : REM whole row highlighted on click
```

### Handle click

```kcml
+ DEFEVENT MyForm.grid.LeftClick()
    LOCAL DIM row
    row = ..CursorRow
    IF row > 1 THEN DO      : REM ignore heading row (row 1 = first heading)
        sel_part$ = ..Cell(row, 1).Text$
        sel_desc$ = ..Cell(row, 2).Text$
    END DO
END EVENT
```

### Handle double-click (use `&.ClickAndDblClick` and `LeftDblClk()`)

Note: the event name is `LeftDblClk` — **not** `LeftDblClick`. Using `&.Click` alone will NOT fire the double-click event.

```kcml
: FOR sv_row = 2 TO .grid.Rows
:     .grid.Cell(sv_row, 1).LeftAction = &.ClickAndDblClick
:     .grid.Cell(sv_row, 2).LeftAction = &.ClickAndDblClick
: NEXT sv_row

+ DEFEVENT MyForm.grid.LeftDblClk()
    LOCAL DIM row
    row = ..CursorRow
    IF row > 1 THEN result = DetailForm.Open()
END EVENT
```

## Alternating Row Colours

A common pattern for readability:

```kcml
: IF MOD(row, 2) == 0 THEN .grid.Cell(row, 0).BackColor = &.clrAlt
: IF MOD(row, 2) <> 0 THEN .grid.Cell(row, 0).BackColor = &.Default
```

Where `clrAlt` is a named colour defined in DEFFORM:
```kcml
{.clrAlt,.color$,.Red=250,.Green=248,.Blue=248}
```

`&.Default` restores the system default background.

## Right-Click and Context Menus

```kcml
: REM In Enter() — configure right-click on each data cell
: .grid.Cell(row, 1).RightAction = &.Click
: .grid.RightSelect = &.Row

+ DEFEVENT MyForm.grid.RightClick()
    LOCAL DIM row
    row = ..CursorRow
    IF row > 1 THEN DO
        sel_part$ = ..Cell(row, 1).Text$
        .ctxMenu.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top)
    END DO
END EVENT
```

## Cell Precedence

When a property (colour, font, type, etc.) is set at multiple levels, the most specific wins:

```
individual cell > row > column > grid > default
```

Set a column-wide type by setting it on row 0:
```kcml
.grid.Cell(0, 3).Type$ = "D"    : REM column 3 = date type throughout
```

Override for a specific cell:
```kcml
.grid.Cell(5, 3).Type$ = ""     : REM row 5 col 3 = plain text
```

## Large Datasets — RowRequest()

For tables too large to load at once, use deferred loading:

```kcml
+ DEFEVENT MyForm.Enter()
    GOSUB 'LOAD_NEXT_BLOCK()
END EVENT

+ DEFEVENT MyForm.grid.RowRequest()
    GOSUB 'LOAD_NEXT_BLOCK()
END EVENT

01500 DEFFN 'LOAD_NEXT_BLOCK()
    LOCAL DIM i, start_row
    start_row = .grid.Rows
    FOR i = 1 TO 50
        REM load next record from file
        CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
        IF ki_status <> 0 THEN DO
            .grid.DataPending = FALSE
            RETURN
        END DO
        .grid.Rows = .grid.Rows + 1
        .grid.Cell(.grid.Rows, 1).Text$ = ...
    NEXT i
    .grid.DataPending = TRUE    : REM more data remains
    RETURN
```

## AutoEdit Mode (KCML 6.00+)

When `AutoEdit=TRUE`, clicking a row enters edit mode automatically. The user can tab between cells in the row and press Enter to commit:

```kcml
{.grid,.KCMLgrid$,...,.AutoEdit=1,.TabThrough=1}
```

Events in AutoEdit mode:

| Event | Description |
|-------|-------------|
| `EditRowNotify()` | Row changed (user moved to a different row) |
| `EditValidate()` | Cell being validated — `ValidateText$` holds new value, `Text$` holds original |
| `EndEdit()` | Edit session finished — `EditReason` indicates why |

```kcml
+ DEFEVENT MyForm.grid.EditRowNotify()
    LOCAL DIM row
    row = ..CursorRow
    GOSUB 'SAVE_ROW(row)
END EVENT
```

## Programmatic Editing (KCML 5 / Legacy)

These methods pre-date AutoEdit and are still valid:

| Method | Description |
|--------|-------------|
| `EditCell(row, col)` | Edit a single cell |
| `EditRow(row, col)` | Edit a full row starting at col |
| `EditGrid(row, col)` | Edit the whole grid starting at position |

## CursorRow and CursorCol

Read these during click/edit events to identify position:

```kcml
+ DEFEVENT MyForm.grid.LeftClick()
    LOCAL DIM r, c, val$50
    r = ..CursorRow
    c = ..CursorCol
    val$ = ..Cell(r, c).Text$
END EVENT
```

## Useful Patterns

### Clear and repopulate

```kcml
: .grid.Rows = 1    : REM shrink to just the heading row
: REM then re-add data rows as normal
```

### Store hidden data per row (hidden column)

Use a column with `ColWidth=1` (effectively invisible) to store a key or index:

```kcml
{.grid,.KCMLgrid$,...,.Cols=8,...}
```

```kcml
: .grid.Cell(0, 8).ColWidth = 1      : REM hidden column 8
: .grid.Cell(row, 8).Text$ = spool_key$   : REM store key per row
```

Then in click handler:
```kcml
: key$ = ..Cell(..CursorRow, 8).Text$
```

### Parallel index array

When you need to map grid rows back to file records (especially after filtering), maintain a parallel numeric array:

```kcml
: DIM grid_idx(5001)
: grid_idx(row) = file_record_number
```

Then in click handler:
```kcml
: file_rec = grid_idx(..CursorRow)
```
