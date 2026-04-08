# KCML Forms — Real-World Patterns

This chapter documents patterns drawn from `manag_form.kcml` — a working spool queue viewer form built with a grid, filter combos, context menu, and status bar. It is the primary reference for how production forms are structured.

---

## Program Structure

A form-based KCML program follows this layout:

```
[Line number] DIM declarations
[Line number] $DECLARE (for external functions)
[Line number] Initialisation code (file opens, env vars, etc.)
[Line number] - DEFFORM FormName()=\
                  {controls...}
              :   + DEFEVENT FormName.Enter() ... END EVENT
              :   + DEFEVENT FormName.control.Event() ... END EVENT
              : FORM END
[Line number] result = FormName.Open()
[Line number] Cleanup / close files
[Line number] $END

[Subroutine definitions with DEFFN]
```

---

## Complete Minimal Pattern — Grid List Form

This pattern is the foundation for almost all list/browse forms:

```kcml
: DIM handle, ki_status, ki_sym, ki_dataptr$6, ki_key$64
: DIM rec$1024, grid_idx(5001), sel_key$15
: DIM result
: REM
- DEFFORM StockBrowse()=\
    {.form,.form$,.Style=0x50c000c4,.Width=700,.Height=400,.Text$="Stock Browser",.Id=1024},\
    {.ok,.button$,.Style=0x50010001,.Left=580,.Top=360,.Width=80,.Height=14,.Text$="Close",.__Anchor=5,.Id=1,.Font=.SegoeUI},\
    {.grid,.KCMLgrid$,.Style=0x50010030,.Left=5,.Top=5,.Width=560,.Height=370,.Id=1000,.Rows=1,.Cols=3,.FixedRows=1,.Font=.Consolas},\
    {.pane1,.status$,.Width=200,.Style=0x50000000},\
    {.Consolas,.dlgfont$,.Name$="Consolas",.Size=10},\
    {.SegoeUI,.dlgfont$,.Name$="Segoe UI",.Size=10},\
    {.clrAlt,.color$,.Red=248,.Green=248,.Blue=252}
:   + DEFEVENT StockBrowse.Enter()
:       LOCAL DIM row, part$15, desc$30, qty
:       .grid.Cell(0,1).ColWidth = 80
:       .grid.Cell(0,1).Heading$ = "Part No"
:       .grid.Cell(0,2).ColWidth = 200
:       .grid.Cell(0,2).Heading$ = "Description"
:       .grid.Cell(0,3).ColWidth = 80
:       .grid.Cell(0,3).Heading$ = "On Hand"
:       CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
:       CALL KI_OPEN handle, "/data/S_STOK01", "R" TO ki_status
:       IF ki_status <> 0 THEN RETURN
:       CALL KI_START_BEG handle, 1 TO ki_status
:       ki_sym = SYM(rec$)
:       row = 1
:       REPEAT
:           CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:           IF ki_status == 0 THEN DO
:               row++
:               .grid.Rows = row
:               part$ = STR(rec$, 20, 15)
:               desc$ = STR(rec$, 36, 30)
:               UNPACK (#########.######) STR(rec$, 513, 8) TO qty
:               .grid.Cell(row,1).Text$ = RTRIM(part$)
:               .grid.Cell(row,2).Text$ = RTRIM(desc$)
:               .grid.Cell(row,3).Text$ = qty
:               .grid.Cell(row,1).LeftAction = &.Click
:               .grid.Cell(row,2).LeftAction = &.Click
:               .grid.Cell(row,3).LeftAction = &.Click
:               .grid.LeftSelect = &.Row
:               IF MOD(row,2)==0 THEN .grid.Cell(row,0).BackColor = &.clrAlt
:               IF MOD(row,2)<>0 THEN .grid.Cell(row,0).BackColor = &.Default
:           END DO
:       UNTIL ki_status <> 0
:       CALL KI_CLOSE handle TO ki_status
:       CALL KI_FREE_HANDLE handle TO ki_status
:       .pane1.Text$ = (row-1) & " records"
:   END EVENT
:   + DEFEVENT StockBrowse.grid.LeftClick()
:       LOCAL DIM r
:       r = ..CursorRow
:       IF r > 1 THEN sel_key$ = ..Cell(r, 1).Text$
:   END EVENT
: FORM END
: result = StockBrowse.Open()
: $END
```

---

## Filter Combos with Apply Button

From `manag_form.kcml` — the filter+search sidebar pattern:

```kcml
: REM Populate filter combos in Enter() event
+ DEFEVENT SpoolView.Enter()
    LOCAL DIM si
    .cmbStat.Delete()
    .cmbStat.Add("All")
    .cmbStat.Add("ON QUEUE")
    .cmbStat.Add("PRINTING")
    .cmbStat.Add("PRINTED")
    .cmbStat.SetSelection(0)
    .cmbUser.Delete()
    .cmbUser.Add("All")
    REM ... add users found while scanning records ...
END EVENT
```

```kcml
: REM Apply button re-scans and rebuilds grid with filters
+ DEFEVENT SpoolView.btnFind.Click()
    LOCAL DIM flt_s$10, flt_u$4, flt_d$30, row_match
    flt_s$ = RTRIM(.cmbStaty.Text$)
    flt_u$ = RTRIM(.cmbUser.Text$)
    flt_d$ = RTRIM(.txtFind.Text$)
    .grid.Rows = 1
    REM ... scan records, check row_match, add matching rows ...
END EVENT
```

The key insight: the filter apply button rebuilds the entire grid from scratch. This is simpler and more reliable than trying to show/hide individual rows.

---

## Search Within Grid Using MAT SEARCH

From `manag_form.kcml` — finding a substring in a field:

```kcml
: LOCAL DIM sv_desc$30, sv_nl, sv_found
: flt_d$ = $LOWER(RTRIM(.txtFind.Text$))
: sv_desc$ = $LOWER(STR(rec$, 17, 30))
: sv_nl = LEN(RTRIM(flt_d$))
: MAT SEARCH sv_desc$, == STR(flt_d$,,sv_nl) TO sv_found
: IF sv_found == 0 THEN row_match = 0
```

`MAT SEARCH` finds the position of a pattern within a string. Returns 0 if not found.

---

## Context Menu with Grid Right-Click

```kcml
: REM In Enter() — set right-click action on each data cell
: .grid.Cell(row, 1).RightAction = &.Click
: .grid.RightSelect = &.Row

+ DEFEVENT MyForm.grid.RightClick()
    LOCAL DIM r
    r = ..CursorRow
    IF r > 1 THEN DO
        sel_rclick_row = r
        sel_key$ = ..Cell(r, 1).Text$
        REM Enable/disable menu items based on selection state
        .ctxMenu.mnuDelete.Enabled = (sel_key$ <> " " ? 1 : 0)
        .ctxMenu.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top)
    END DO
END EVENT

+ DEFEVENT MyForm.ctxMenu.mnuDelete.Select()
    GOSUB 'DELETE_RECORD(sel_key$)
    REM Remove row from grid by rebuilding (or shift rows up)
    SpoolView.btnRefresh.Click()
END EVENT
```

---

## Refresh Pattern — Reuse Enter() Logic

Rather than duplicating the grid loading code, call the Enter() event handler directly from a Refresh button:

```kcml
+ DEFEVENT MyForm.btnRefresh.Click()
    MyForm.Enter()    : REM Re-run the entire initialisation
END EVENT
```

This works because DEFEVENT handlers are callable as methods. The Enter() event handler clears and repopulates the grid from scratch.

---

## Parallel Index Array for Row-to-Record Mapping

When rows may be filtered (not all records shown), maintain a separate array mapping grid row numbers to record positions:

```kcml
: DIM grid_idx(5001)    : REM maps grid row → file record position
```

```kcml
: REM While loading grid:
: row++
: grid_idx(row) = file_record_number    : REM store mapping
```

```kcml
: REM In click handler:
: file_rec = grid_idx(..CursorRow)
: DATA LOAD BU T#gb_h(213),(file_rec * 128) sp_rec$
```

---

## Tagged Combo for Code/Description Pairs

Store a display name in the combo and retrieve the code via tag:

```kcml
: REM Populate
: .cboPrinter.Add("Laser (Reception)", "LP01")
: .cboPrinter.Add("Inkjet (Workshop)", "IP02")
: .cboPrinter.SetSelection(0)

: REM Read selected code
: printer_code$ = RTRIM(.cboPrinter.GetTag$())
```

---

## Status Bar for Item Count and Messages

```kcml
: .pane1.Text$ = sv_disp & " items"          : REM count
: .pane1.Text$ = "Saved OK"                  : REM confirmation
: .pane1.Text$ = "Error: " & RTRIM(err_msg$) : REM error
```

---

## Collecting Unique Values While Scanning

From `manag_form.kcml` — building filter combo content from the data:

```kcml
: DIM staty_str$500, staty_cnt
: staty_str$ = ALL(HEX(00))
: staty_cnt = 0
: REM In scan loop:
: sty_tmp$ = RTRIM(STR(rec$, 47, 10))
: sty_found = 0
: FOR si = 1 TO staty_cnt
:     IF RTRIM(STR(staty_str$,(si-1)*10+1,10)) == sty_tmp$ THEN sty_found = 1
: NEXT si
: IF sty_found == 0 AND staty_cnt < 50 THEN DO
:     staty_cnt++
:     STR(staty_str$,(staty_cnt-1)*10+1,10) = sty_tmp$
: END DO
: REM After scan — populate combo from collected values:
: .cmbStaty.Add("All")
: FOR si = 1 TO staty_cnt
:     sty_tmp$ = RTRIM(STR(staty_str$,(si-1)*10+1,10))
:     .cmbStaty.Add(sty_tmp$)
: NEXT si
```

This packs unique values into a fixed-length string buffer used as a simple array. Each slot is 10 bytes. The same pattern works for any fixed-width string collection.

---

## Conditional Menu Item Enable

Enable a menu option only when it makes sense:

```kcml
: .ctxMenu.mnuPrint.Enabled = (sv_sel_printer$ <> " " ? 1 : 0)
```

The ternary `(condition ? true_val : false_val)` is a compact way to set boolean properties.

---

## $DECLARE for Windows API / Clipboard

When the form needs to call a Windows DLL function (e.g. write to clipboard):

```kcml
: $DECLARE 'KCMLWriteClipboard(STR())
```

Then call it from an event handler:

```kcml
+ DEFEVENT MyForm.btnCopyGrid.Click()
    LOCAL DIM grid_text$65000, r, c, line$500
    grid_text$ = ALL(HEX(00))
    FOR r = 2 TO .grid.Rows
        line$ = ""
        FOR c = 1 TO 7
            line$ = line$ & RTRIM(.grid.Cell(r,c).Text$) & HEX(09)
        NEXT c
        grid_text$ = grid_text$ & RTRIM(line$) & HEX(0D) & HEX(0A)
    NEXT r
    CALL 'KCMLWriteClipboard(grid_text$)
END EVENT
```

---

## Opening a Child Form for Detail View

From a grid click or context menu, open a detail form that shows/edits the selected record:

```kcml
+ DEFEVENT MyForm.ctxMenu.mnuView.Select()
    result = DetailForm.Open()
END EVENT
```

The child form can access parent variables (they share the same variable scope in the same program). When `DetailForm.Open()` returns, the parent can check `result` and refresh if needed.

---

## Common Mistakes to Avoid

| Mistake | Effect | Fix |
|---------|--------|-----|
| Bare `FormName.Open()` without `result =` | Form opens then immediately closes silently | Always assign: `result = FormName.Open()` |
| DEFEVENT placed after FORM END (without `+`) | Event never fires | Use `+` prefix inside the DEFFORM block |
| Missing `LeftAction = &.Click` on cells | Click events not sent | Set per-cell or per-column action |
| Colons inside REM statements | Syntax error | Remove colons from REM text |
| Blank lines in -p scripts | Silent early termination | Use `: REM` lines for spacing |
| Updating `grid.Rows` without clearing old cells | Stale data in new rows | Clear with `grid.Rows = 1` before repopulating |
