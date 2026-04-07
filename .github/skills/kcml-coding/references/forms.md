# KCML Forms Reference

KCML forms are GUI dialog boxes rendered on the KCML Windows client. The control definitions
map directly onto Win32 dialog box styles — the style integers are genuine `WS_` flags.

---

## DEFFORM — Define a Form

```kcml
01011 - DEFFORM FormName()=\
          {.form,.form$,.Style=0x50c000c4,.Width=640,.Height=480,.Text$="Title",.Id=1024},\
          {.ok,.button$,.Style=0x50010001,.Left=582,.Top=5,.Width=50,.Height=14,.Text$="Close",.__Anchor=5,.Id=1,.Font=.SegoeControl},\
          {.lblTitle,.static$,.Style=0x50000000,.Left=5,.Top=5,.Width=200,.Height=14,.Text$="Hello",.Id=1001,.Font=.SegeoLabel},\
          {.SegoeControl,.dlgfont$,.Size=10}
    :     + DEFEVENT FormName.Enter()
    :         .lblTitle.Text$ = "Loaded"
    :     END EVENT
    :     REM
    : FORM END FormName
01012 result = FormName.Open()
```

**Critical rules:**
- Every `DEFEVENT` must be a **continuation line inside** the `DEFFORM...FORM END` block, prefixed with `+`
- `FORM END FormName` closes the block — it does not open the form
- All DEFFORM blocks must appear before any `.Open()` call
- `.Open()` must always assign a result: `result = FormName.Open()`

---

## Control Types

| Type string | Win32 class | Description |
|-------------|-------------|-------------|
| `.form$` | DIALOG | The form container itself (always first) |
| `.button$` | BUTTON | Push button |
| `.static$` | STATIC | Label / non-interactive text |
| `.edit$` | EDIT | Single-line text input |
| `.listbox$` | LISTBOX | Scrollable list |
| `.combobox$` | COMBOBOX | Drop-down list |
| `.KCMLgrid$` | KCMLgrid | Kerridge grid control |
| `.groupbox$` | BUTTON (BS_GROUPBOX) | Frame/group box with title |
| `.status$` | status bar pane | Status bar pane (one per pane) |
| `.Menu$` | — | Context menu container |
| `.dlgfont$` | — | Named font definition (not a visible control) |

---

## Common Control Properties

| Property | Type | Description |
|----------|------|-------------|
| `.Style` | hex int | Win32 window style flags |
| `.Left` | int | X position in dialog units |
| `.Top` | int | Y position in dialog units |
| `.Width` | int | Width in dialog units |
| `.Height` | int | Height in dialog units |
| `.Id` | int | Control ID (must be unique per form) |
| `.Text$` | string | Initial caption/text |
| `.Font` | font ref | Named font (e.g. `.SegoeControl`) |
| `.__Anchor` | int | Resize anchor: 0=top-left, 5=top-right |
| `.Enabled` | 0/1 | 0=greyed/disabled, 1=enabled (default 1) |
| `.Visible` | 0/1 | 0=hidden, 1=visible (default 1) |
| `.BackColor` | color ref | Background colour — any control, grid row, or grid cell (see BackColor below) |

### Common Style Values

| Hex | Meaning |
|-----|---------|
| `0x50000000` | Visible, child window |
| `0x50000001` | Visible, child, BS_DEFPUSHBUTTON (default button, responds to Enter) |
| `0x50010000` | Visible, child, WS_TABSTOP (normal button) |
| `0x50010001` | Visible, child, WS_TABSTOP, BS_DEFPUSHBUTTON |
| `0x50210003` | Combobox: CBS_DROPDOWNLIST, CBS_HASSTRINGS, WS_TABSTOP |
| `0x50310000` | Listbox: LBS_NOINTEGRALHEIGHT, LBS_HASSTRINGS, WS_TABSTOP |
| `0x50c000c4` | Form: WS_CAPTION, WS_SYSMENU, WS_THICKFRAME (resizable) |
| `0x50000007` | Groupbox: BS_GROUPBOX |
| `0x50810080` | Edit box: ES_AUTOHSCROLL, WS_TABSTOP |

---

## BackColor — Background Colour (Generic Property)

`BackColor` is a generic property available on **any** form control — buttons, labels, edit boxes,
listboxes, comboboxes, groupboxes, grid cells, grid rows, and the form itself. It accepts a
reference to a named colour defined with `.color$` in the DEFFORM control list, or a stock colour.

### Defining custom colours

Add `.color$` entries to the DEFFORM control list (conventionally at the end with fonts):

```kcml
{.clrAlt,.color$,.Red=250,.Green=248,.Blue=248}
```

Assign with `&.colourName` at runtime or at design time via the control definition:

```kcml
REM - Any control type:
.lblTitle.BackColor = &.clrAlt
.txtSearch.BackColor = &.clrAlt
.btnApply.BackColor = &.Yellow
.form.BackColor = &.clrAlt

REM - Individual grid cell:
.grid.Cell(sv_row, 1).BackColor = &.clrAlt

REM - Entire grid row (col=0 means all cells in that row):
.grid.Cell(sv_row, 0).BackColor = &.clrAlt

REM - Entire grid column (row=0 means all cells in that column):
.grid.Cell(0, sv_col).BackColor = &.clrAlt

REM - Entire grid (row=0, col=0):
.grid.Cell(0, 0).BackColor = &.clrAlt
```

### Stock colours

These named colours are available without defining a `.color$` entry:

| Name | Name | Name |
|------|------|------|
| `Black` | `Gray` | `DarkGray` |
| `Blue` | `DarkBlue` | `Cyan` |
| `DarkCyan` | `Green` | `DarkGreen` |
| `Magenta` | `DarkMagenta` | `Red` |
| `DarkRed` | `White` | `Yellow` |
| `Default` | | |

`Default` restores the control's default background — use it to reset alternating rows back to
the grid's normal colour without needing a second custom colour definition.

```kcml
.lblWarning.BackColor = &.Yellow
```

### Alternating row colours on a KCMLgrid (verified pattern)

Use `Cell(row, 0)` (column 0 = all cells in that row) — one line per row rather than one line
per cell. Use `Default` for the reset so only one `.color$` definition is needed:

```kcml
REM - In DEFFORM control list (one colour only needed):
{.clrAlt,.color$,.Red=250,.Green=248,.Blue=248}

REM - In the grid fill loop:
IF MOD(sv_row,2)==0 THEN .grid.Cell(sv_row,0).BackColor = &.clrAlt
IF MOD(sv_row,2)<>0 THEN .grid.Cell(sv_row,0).BackColor = &.Default
```

Both branches must be explicit — omitting the odd-row reset leaves rows at whatever colour they
had previously (e.g. after a Refresh that reuses existing row slots).

---

## Font Definitions (dlgfont$)

Define named fonts at the end of the control list:

```kcml
{.ConsolasGrid,.dlgfont$,.Name$="Consolas",.Size=10},\
{.SegoeHeading,.dlgfont$,.Name$="Segoe UI",.Size=14,.Bold=1},\
{.SegeoLabel,.dlgfont$,.Name$="Segoe UI",.Size=11},\
{.SegoeControl,.dlgfont$,.Size=10}
```

Reference a named font on any control with `.Font=.FontName`.

---

## DEFEVENT — Event Handlers

### Standard events

| Event | Fires when |
|-------|-----------|
| `FormName.Enter()` | Form opens — use this to load data, set control state |
| `FormName.btnName.Click()` | Button clicked |
| `FormName.cboName.Click()` | Combobox item selected |
| `FormName.lstName.Click()` | Listbox item clicked |
| `FormName.grid.LeftClick()` | Grid cell left-clicked |
| `FormName.grid.RightClick()` | Grid cell right-clicked |
| `FormName.ctxMenu.mnuItem.Select()` | Context menu item selected |

### LOCAL DIM in DEFEVENTs

Variables declared `LOCAL DIM` inside a DEFEVENT are scoped to that event invocation.
They are **not** reset between calls — always explicitly initialise before use:

```kcml
+ DEFEVENT MyForm.btnOK.Click()
    LOCAL DIM sv_i, sv_result$80
    sv_result$ = " "    : REM always initialise - LOCAL DIM does not reset
    FOR sv_i = 1 TO 10
        REM ...
    NEXT sv_i
END EVENT
```

### Dot notation inside events

Inside a DEFEVENT, controls are accessed with a leading dot:

```kcml
+ DEFEVENT MyForm.btnApply.Click()
    .lblStatus.Text$ = "Processing..."
    .btnApply.Enabled = 0
END EVENT
```

For grid events, `..` (double dot) accesses the grid's own properties:

```kcml
+ DEFEVENT MyForm.grid.LeftClick()
    LOCAL DIM sv_row
    sv_row = ..CursorRow
    sel_desc$ = ..Cell(sv_row, 2).Text$
END EVENT
```

---

## Button

```kcml
{.btnOK,.button$,.Style=0x50010001,.Left=450,.Top=5,.Width=80,.Height=14,.Text$="OK",.__Anchor=5,.Id=1,.Font=.SegoeControl}
```

- `.Id=1` is the standard "OK/Close" button ID — pressing Enter on a form with a default button triggers Id=1
- `.__Anchor=5` anchors to top-right so button stays in position when form is resized

Enable/disable at runtime:
```kcml
.btnPrint.Enabled = 0    : REM grey out
.btnPrint.Enabled = 1    : REM re-enable
```

---

## Static Label

```kcml
{.lblTitle,.static$,.Style=0x50000000,.Left=5,.Top=5,.Width=400,.Height=16,.Id=1001,.Font=.SegoeHeading}
```

Update text at runtime:
```kcml
.lblTitle.Text$ = RTRIM(some_variable$)
```

---

## Edit Box

```kcml
{.txtSearch,.edit$,.Style=0x50810080,.Left=5,.Top=5,.Width=200,.Height=14,.Id=2001,.Font=.SegoeControl}
```

Read value:
```kcml
LOCAL DIM sv_input$50
sv_input$ = RTRIM(.txtSearch.Text$)
```

---

## Listbox

```kcml
{.lstContent,.listbox$,.Style=0x50310000,.Left=5,.Top=24,.Width=627,.Height=427,.Id=1000,.Font=.ConsolasGrid}
```

### Listbox methods

| Method | Description |
|--------|-------------|
| `.lstName.Add(str$)` | Append an item |
| `.lstName.Delete()` | Clear all items |
| `.lstName.Delete(idx)` | Remove item at index |

```kcml
REM Populate listbox
.lstContent.Delete()
FOR sv_i = 1 TO line_count
    .lstContent.Add(lines$(sv_i))
NEXT sv_i
```

---

## Combobox

```kcml
{.cboPrinter,.combobox$,.Style=0x50210003,.Left=708,.Top=194,.Width=125,.Height=150,.Id=2016,.Font=.SegoeControl}
```

The `.Height` of a combobox defines the **dropdown height**, not the control height. Set it large enough to show all items without scrolling.

### Combobox methods and properties

| Method/Property | Description |
|-----------------|-------------|
| `.Add(str$)` | Add item (display text only) |
| `.Add(str$, tag$)` | Add item with associated tag (use for codes) |
| `.Delete()` | Clear all items |
| `.Delete(idx)` | Remove item at index |
| `.SetSelection(idx)` | Select item by 0-based index |
| `.SetSelection()` | Clear selection |
| `.Index` | 0-based index of currently selected item |
| `.GetString$(idx)` | Return display text for item at index |
| `.GetTag$(idx)` | Return tag for item at index |
| `.Text$` | Display text of selected item (read) |

### Pattern: code/name pairs using tags

Store the 3-char printer code as the tag, display name as the string:

```kcml
REM Populate
FOR sv_pi = 1 TO 100
    sv_ac$ = printer_addr$(sv_pi)
    IF sv_ac$ <> " " THEN DO
        sv_nm$ = RTRIM(printer_name$(sv_pi))
        .cboPrinter.Add(sv_nm$, sv_ac$)
    END DO
NEXT sv_pi

REM Read back selected code on Click()
+ DEFEVENT MyForm.cboPrinter.Click()
    sv_sel_printer$ = .cboPrinter.GetTag$(.cboPrinter.Index)
END EVENT
```

---

## Groupbox (Frame)

```kcml
{.frameFilter,.groupbox$,.Left=644,.Top=10,.Width=198,.Height=167,.Style=0x50000007,.Text$="Filter and Search",.Id=1027}
```

Visual grouping only — no functional behaviour. Controls positioned inside the groupbox bounds appear visually grouped but are not child controls of it in KCML's event model.

---

## Status Bar

Each status bar pane is a separate control with type `.status$`:

```kcml
{.pane1,.status$,.Width=100,.Style=0x50000000,.Text$="Ready"},\
{.pane2,.status$,.Width=200,.Style=0x50000000,.Text$=""}
```

Update at runtime:
```kcml
.pane1.Text$ = sv_disp & " items"
```

---

## Context Menu

```kcml
{.ctxMenu,.Menu$,.Style=0x01,.Id=2020,\
    .mnuView={.Text$="View"},\
    .mnuSep={.Flag=2048},\
    .mnuDelete={.Text$="Delete"},\
    .mnuSep2={.Flag=2048},\
    .mnuPrint={.Text$="Print"}}
```

- `.Flag=2048` creates a separator line
- Show the menu at the mouse position from inside a RightClick event:

```kcml
+ DEFEVENT MyForm.grid.RightClick()
    LOCAL DIM sv_row
    sv_row = ..CursorRow
    IF sv_row > 1 THEN DO
        sel_rclick_row = sv_row
        sel_spool_idx = grid_idx(sv_row)
        .ctxMenu.mnuPrint.Enabled = (sv_sel_printer$ <> " " ? 1 : 0)
        .ctxMenu.TrackPopup(..MouseX+..Left,..MouseY+..Top)
    END DO
END EVENT
```

### Menu item properties

| Property | Description |
|----------|-------------|
| `.Text$` | Display label |
| `.Enabled` | 0=greyed, 1=active |
| `.Visible` | 0=hidden, 1=shown |
| `.Checked` | 0=unchecked, 1=checked (tick) |

---

## KCMLgrid

```kcml
{.grid,.KCMLgrid$,.Style=0x50010030,.Left=5,.Top=10,.Width=636,.Height=431,.Id=1000,.Rows=1,.Cols=8,.FixedRows=1,.Font=.ConsolasGrid}
```

- `.Rows=1` — just the header row initially; set to `sv_disp+1` in Enter() after counting records
- `.Cols=8` — total columns including any hidden columns
- `.FixedRows=1` — number of non-scrolling header rows

### Cell() addressing

`Cell(row, col)` moves the programming cell to a position. Subsequent property accesses on `.Cell`
(without arguments) then operate on that position. Both row and col can be 0 to mean "all":

| row | col | Scope |
|-----|-----|-------|
| n | n | Single cell |
| n | 0 | All cells in row n |
| 0 | n | All cells in column n |
| 0 | 0 | Entire grid |

```kcml
REM - Single cell
.grid.Cell(4,2).Text$ = "hello"

REM - All cells in row 4 (e.g. set row background colour)
.grid.Cell(4,0).BackColor = &.clrAlt

REM - All cells in column 3 (e.g. set column width)
.grid.Cell(0,3).ColWidth = 80

REM - IMPORTANT: cannot use Cell() twice in one statement
REM   WRONG:  .grid.Cell(r1,c1).Text$ = .grid.Cell(r2,c2).Text$
REM   RIGHT:  a$ = .grid.Cell(r1,c1).Text$ : .grid.Cell(r2,c2).Text$ = a$
```

### Grid properties and methods

| Property/Method | Description |
|-----------------|-------------|
| `.Rows` | Total row count (read/write) |
| `.CursorRow` | Currently highlighted row (1-based; row 1 = header) |
| `.LeftSelect` | Event binding for left-click row selection |
| `.RightSelect` | Event binding for right-click row selection |
| `.Cell(row,col).Text$` | Cell text (read/write) |
| `.Cell(row,col).BackColor` | Cell/row/column/grid background colour |
| `.Cell(row,col).ColWidth` | Column width in pixels |
| `.Cell(row,col).Heading$` | Column heading (row=0) |
| `.Cell(row,col).LeftAction` | Left-click action binding |
| `.Cell(row,col).RightAction` | Right-click action binding |

### Binding cells to click events

```kcml
REM In Enter() — bind each data row cell to the click event
.grid.LeftSelect = &.Row
.grid.RightSelect = &.Row
FOR sv_i = 1 TO sv_disp
    sv_row = sv_i + 1
    .grid.Cell(sv_row,1).LeftAction = &.Click
    .grid.Cell(sv_row,2).LeftAction = &.Click
    .grid.Cell(sv_row,1).RightAction = &.Click
    .grid.Cell(sv_row,2).RightAction = &.Click
NEXT sv_i
```

### CRITICAL: never store per-row data in a grid cell via a local loop variable

Grid cells store a reference to the variable, not its value. After the loop, all cells point to the same variable (holding its final value). Use a form-level numeric array to map rows to record indices:

```kcml
REM Form level:
DIM grid_idx(500)

REM In Enter():
grid_idx(sv_row) = sv_i    : REM numeric array assignment — always correct

REM In LeftClick():
sv_spool_idx = grid_idx(..CursorRow)
```

### Grid events

`LeftClick()` and `RightClick()` both work. `DblClick()` does **not** fire on the KCML grid control.

### Hidden column pattern

Use a narrow hidden column (ColWidth=1) to carry a file key or other identifier without display:

```kcml
.grid.Cell(0,8).ColWidth = 1
.grid.Cell(0,8).Heading$ = ""
REM ... in the fill loop:
.grid.Cell(sv_row,8).Text$ = RTRIM(STR(sp_rec$,5,12))   : REM spool filename
```

Check column 8 is non-blank to detect populated rows in btnCopyGrid etc.

---

## Form-level vs LOCAL DIM

- **Form-level DIM** (at program top, outside any DEFEVENT) — persists for the lifetime of the program, accessible from all DEFEVENTs and DEFSUBs
- **LOCAL DIM** (inside a DEFEVENT or DEFSUB) — scoped to that invocation, but values are **not** reset between calls

Use form-level variables to pass data between DEFEVENTs:

```kcml
REM Form-level — set in RightClick, used in menu Select():
DIM sel_rclick_row, sel_spool_idx, sel_file$12, sel_stat$10
```

---

## DEFSUB called from DEFEVENT

DEFSUBs placed between `FORM END FormA` and `DEFFORM FormB` are accessible from DEFEVENTs in both forms:

```kcml
FORM END SpoolView
: DEFSUB 'sv_print_spool_file()
:     REM shared between SpoolView and SpoolFileView events
: END SUB
01012 - DEFFORM SpoolFileView()=...
```

Call with `GOSUB 'sv_print_spool_file()` from any DEFEVENT.

---

## Printing from a DEFEVENT (SELECT PRINT)

See [print-input.md](print-input.md) for the full `SELECT PRINT` / `$REWIND` reference.

```kcml
+ DEFEVENT MyForm.btnPrint.Click()
    SELECT PRINT <sv_sel_printer$>(0)
    REM ... PRINT lines ...
    $REWIND <sv_sel_printer$>
END EVENT
```

---

## $DECLARE — Calling Windows DLLs from Forms

See [declare.md](declare.md) for the full reference.

```kcml
REM Inside a DEFEVENT or DEFSUB:
$DECLARE 'sv_shell(INT(),STR(),STR(),STR(),STR(),INT())=".ShellExecute"
'sv_shell(0,"open",sv_tmp_path$,HEX(00),HEX(00),1)
```
