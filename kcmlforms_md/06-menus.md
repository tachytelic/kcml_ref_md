# KCML Forms — Menus

## Menu Types

KCML forms support two types of menus:

1. **Menu bar** — attached to the top of a form (standard Windows menu bar)
2. **Context / popup menu** — displayed at a mouse position in response to a right-click

Both are defined in the `DEFFORM` block as `.Menu$` controls.

## Defining a Context Menu

Context menus have `.Style=0x01`:

```kcml
{.ctxMenu,.Menu$,.Style=0x01,.Id=2020,\
    .mnuView={.Text$="View"},\
    .mnuSep={.Flag=2048},\
    .mnuSetOnQ={.Text$="Set Status: On Queue"},\
    .mnuSetPrinted={.Text$="Set Status: Printed"},\
    .mnuSep2={.Flag=2048},\
    .mnuPrint={.Text$="Print"},\
    .mnuDelete={.Text$="Delete"}}
```

- `Flag=2048` creates a separator line
- Each named sub-property (`.mnuView`, `.mnuPrint`, etc.) becomes an addressable menu item object

## Defining a Menu Bar

A menu bar groups top-level menus and their items:

```kcml
{.menuBar,.Menu$,.Style=0x00,.Id=100,\
    .mnuFile={.Text$="&File",\
        .mnuNew={.Text$="&New"},\
        .mnuOpen={.Text$="&Open"},\
        .mnuSep={.Flag=2048},\
        .mnuExit={.Text$="E&xit"}},\
    .mnuEdit={.Text$="&Edit",\
        .mnuCopy={.Text$="&Copy"},\
        .mnuPaste={.Text$="&Paste"}}}
```

Note: menu items are nested within their parent using the same `{...}` property syntax.

## Displaying a Popup Menu — TrackPopup()

To display a context menu at the mouse position, call `TrackPopup(x, y)` with screen coordinates:

```kcml
+ DEFEVENT MyForm.grid.RightClick()
    LOCAL DIM row
    row = ..CursorRow
    IF row > 1 THEN DO
        sel_row = row
        REM MouseX/MouseY are relative to the grid control
        REM Add Left/Top to convert to form coordinates
        .ctxMenu.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top)
    END DO
END EVENT
```

The `..MouseX` and `..MouseY` properties are available on grid cells and picture button click events. They give the mouse position **relative to the control's top-left corner**. Add the control's own `.Left` and `.Top` to get form coordinates, which is what `TrackPopup` expects.

## Handling Menu Item Selection

Each menu item fires a `Select()` event when chosen:

```kcml
+ DEFEVENT MyForm.ctxMenu.mnuView.Select()
    result = DetailForm.Open()
END EVENT

+ DEFEVENT MyForm.ctxMenu.mnuSetOnQ.Select()
    GOSUB 'SET_STATUS(sel_spool_idx, "1")
    .grid.Cell(sel_rclick_row, 4).Text$ = "ON QUEUE"
END EVENT

+ DEFEVENT MyForm.ctxMenu.mnuDelete.Select()
    GOSUB 'DELETE_RECORD(sel_spool_idx)
END EVENT
```

## Enabling / Disabling Menu Items

```kcml
: .ctxMenu.mnuDelete.Enabled = TRUE
: .ctxMenu.mnuPrint.Enabled = (printer_code$ <> " " ? 1 : 0)
```

## Checked Menu Items (Toggle)

```kcml
+ DEFEVENT MyForm.menuBar.mnuView.mnuShowAll.Select()
    IF ..mnuShowAll.Checked THEN DO
        ..mnuShowAll.Checked = FALSE
        GOSUB 'FILTER_ON()
    END DO
    ELSE DO
        ..mnuShowAll.Checked = TRUE
        GOSUB 'FILTER_OFF()
    END DO
END EVENT
```

## Popup Menus from Other Controls

Popup menus can be triggered from any control that has a right-click event. Common cases:

### From a picture button

```kcml
+ DEFEVENT MyForm.picActions.RightClick()
    .ctxMenu.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top)
END EVENT
```

### From a grid cell (see grid chapter for detail)

```kcml
+ DEFEVENT MyForm.grid.RightClick()
    .ctxMenu.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top)
END EVENT
```

## Accelerator Keys

Prefix a letter with `&` in menu item `Text$` to create an accelerator:
- `"&File"` → Alt+F opens the File menu
- `"&Save"` → Alt+S when menu is open

Standard conventions: `&File`, `&Edit`, `&View`, `&Help`.
