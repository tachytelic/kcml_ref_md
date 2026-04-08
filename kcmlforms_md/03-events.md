# KCML Forms — Events

## Overview

Events are the mechanism by which forms communicate user actions back to KCML code on the server. A `DEFEVENT` block defines a handler that runs when a specific event occurs on a specific control.

Events are **only sent to the server if a handler exists** for them. This minimises network traffic — a click on a button with no `Click()` handler produces no server round-trip.

## DEFEVENT Syntax

```
+ DEFEVENT FormName.ControlName.EventName()
    [code]
END EVENT
```

The `+` prefix places the DEFEVENT **inside** the DEFFORM block — this is the correct pattern. DEFEVENTs without `+` (standalone, placed after FORM END) are not associated with the form and will be silently ignored when the form opens.

```kcml
- DEFFORM MyForm()=\
    {.form,.form$,...},\
    {.btnSave,.button$,...}
:   + DEFEVENT MyForm.btnSave.Click()
:       REM this runs when btnSave is clicked
:       GOSUB 'SAVE_RECORD()
:   END EVENT
:   + DEFEVENT MyForm.Enter()
:       REM this runs when the form opens
:       .btnSave.SetFocus()
:   END EVENT
: FORM END
```

## Standard Events by Control Type

### Form-level events

| Event | When it fires |
|-------|--------------|
| `Enter()` | Form has opened and is ready — use this to populate controls |
| `Exit()` | Form is about to close — cleanup |
| `Idle()` | Fires periodically when form is inactive (requires `IdleTimer` property set) |

### Button

| Event | When it fires |
|-------|--------------|
| `Click()` | Button clicked or accelerator key pressed |

### Edit / KCML Edit

| Event | When it fires |
|-------|--------------|
| `Click()` | Control clicked |
| `DropDown()` | Dropdown list opened |
| `Validate()` | User has finished editing the field — validate content |
| `MaxText()` | Maximum text length reached |

### Combo Box

| Event | When it fires |
|-------|--------------|
| `Click()` | Selection changed |
| `DblClick()` | Double-click on selection |
| `GetFocus()` | Control gained focus |
| `LoseFocus()` | Control lost focus |
| `DropDown()` | Dropdown opened |

### List Box

| Event | When it fires |
|-------|--------------|
| `Click()` | Selection changed |
| `DblClick()` | Double-click on item |
| `GetFocus()` | Focus gained |
| `LoseFocus()` | Focus lost |

### Grid

| Event | When it fires |
|-------|--------------|
| `LeftClick()` | Left mouse click on a cell |
| `RightClick()` | Right mouse click on a cell |
| `LeftDblClick()` | Left double-click on a cell |
| `RightDblClick()` | Right double-click on a cell |
| `RowRequest()` | User has scrolled to last row and `DataPending` is TRUE |
| `EditRowNotify()` | Row has changed in AutoEdit mode |
| `EditValidate()` | Cell content is being validated during edit |
| `EndEdit()` | Edit session has ended |
| `CursorMove()` | Cursor moved to different row/column |

### Menu item

| Event | When it fires |
|-------|--------------|
| `Select()` | Menu item chosen |

### Tab control

| Event | When it fires |
|-------|--------------|
| `Enter()` | Tab page activated |
| `Exit()` | Tab page deactivated |

### Tree control

| Event | When it fires |
|-------|--------------|
| `Expand()` | Tree node first expanded (deferred population) |
| `ExpandChange()` | Node expanded or collapsed |

### Checkbox / Radio button

| Event | When it fires |
|-------|--------------|
| `Click()` | State changed |

### RTF control

| Event | When it fires |
|-------|--------------|
| `Modified()` | Content changed |
| `PrintStatus()` | Print operation status update |
| `RightClick()` | Right mouse click |

## Self-Reference: `..` (Double-Dot)

Inside a DEFEVENT, `..` refers to the control that owns the event ("self"):

```kcml
+ DEFEVENT MyForm.grid.LeftClick()
    LOCAL DIM row, col
    row = ..CursorRow       : REM grid's own CursorRow property
    col = ..CursorCol
    PRINT ..Cell(row, col).Text$
END EVENT
```

```kcml
+ DEFEVENT MyForm.ctxMenu.mnuView.Select()
    REM .. here refers to mnuView
END EVENT
```

## Sibling Control Reference: `.controlName`

Within any DEFEVENT on the same form, sibling controls are referenced with a single leading dot:

```kcml
+ DEFEVENT MyForm.btnLoad.Click()
    LOCAL DIM key$20
    key$ = .txtKey.Text$         : REM read from sibling edit control
    .grid.Rows = 0               : REM clear sibling grid
    GOSUB 'LOAD_DATA(key$)
END EVENT
```

## LOCAL DIM — Event-local Variables

Variables declared with `LOCAL DIM` inside a DEFEVENT exist only during that event call. They are destroyed when the event handler returns. Use them for temporary working variables to avoid polluting the outer program's namespace.

```kcml
+ DEFEVENT MyForm.grid.LeftClick()
    LOCAL DIM row, col, cell_text$50
    row = ..CursorRow
    col = ..CursorCol
    cell_text$ = ..Cell(row, col).Text$
    PRINT "Clicked: "; cell_text$
END EVENT
```

`LOCAL DIM` supports the same types as regular `DIM`:

```kcml
LOCAL DIM i, total
LOCAL DIM name$30, code$10
LOCAL DIM items(50)
LOCAL DIM OBJECT obj
```

## Calling Event Handlers as Subroutines

A DEFEVENT handler can be called explicitly as if it were a method. This is useful for triggering initialisation logic from multiple places:

```kcml
+ DEFEVENT MyForm.btnRefresh.Click()
    LOCAL DIM i
    REM ... populate grid ...
END EVENT

+ DEFEVENT MyForm.Enter()
    REM Reuse the refresh logic on form open
    MyForm.btnRefresh.Click()
END EVENT
```

The return value (if the event handler uses `Terminate()` or similar) can be captured:

```kcml
: result = MyForm.btnHelp.Click()
```

## Idle Processing

The `Idle()` event fires at a configurable interval while the form is displayed and no other event is processing. Use it for background polling or animation:

```kcml
+ DEFEVENT MyForm.Enter()
    .form.IdleTimer = 5000    : REM fire Idle() every 5 seconds
END EVENT

+ DEFEVENT MyForm.Idle()
    GOSUB 'CHECK_QUEUE()
END EVENT
```

Set `IdleTimer` to `-1` to disable idle processing.

## Flush() — Force Intermediate Updates

Event handlers run to completion before the client is updated. If a long handler needs to show progress:

```kcml
+ DEFEVENT MyForm.btnProcess.Click()
    LOCAL DIM i
    FOR i = 1 TO 1000
        .pane1.Text$ = "Processing " & i
        .form.Flush()          : REM send update to client now
        GOSUB 'PROCESS_ROW(i)
    NEXT i
END EVENT
```

Without `Flush()`, the status bar update would only appear after the entire loop completes.

## EventPending() — Check for Queued Events

During a long handler, check if the user has clicked something else:

```kcml
+ DEFEVENT MyForm.btnLoad.Click()
    LOCAL DIM i, abort
    abort = 0
    FOR i = 1 TO large_count
        IF .form.EventPending() THEN abort = 1
        IF abort THEN BREAK
        GOSUB 'LOAD_ROW(i)
    NEXT i
END EVENT
```

## Terminating a Form from Code

```kcml
+ DEFEVENT MyForm.btnCustomClose.Click()
    .form.Terminate(42)    : REM Open() will return 42
END EVENT
```

Standard button IDs:
- `Id=1` — OK button (Open() returns 1)
- `Id=2` — Cancel button (Open() returns 0)
- Any other Id combined with `Terminate(n)` — Open() returns n
