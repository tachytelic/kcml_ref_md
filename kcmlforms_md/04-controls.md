# KCML Forms — Controls Reference

All controls share a common addressing pattern: `.controlName.Property` and `.controlName.Method()` within a DEFEVENT on the same form. Outside a DEFEVENT, use `FormName.controlName.Property`.

---

## Push Button (`.button$`)

The standard clickable button.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Text$` | string | Button caption |
| `Enabled` | boolean | Enable / disable |
| `Visible` | boolean | Show / hide |

### Events

| Event | Description |
|-------|-------------|
| `Click()` | Fired on click or accelerator key |

### Notes

- `Id=1` makes the button the default (Enter key triggers it) — conventional OK button
- `Id=2` makes the button the Cancel button (Esc key triggers it)
- Prefix a letter in `Text$` with `&` to create an accelerator key: `"&Save"` → Alt+S

### Example

```kcml
{.btnSave,.button$,.Style=0x50010000,.Left=200,.Top=240,.Width=80,.Height=14,.Text$="&Save",.Id=2010}
```

```kcml
+ DEFEVENT MyForm.btnSave.Click()
    GOSUB 'SAVE_RECORD()
END EVENT
```

---

## Edit Control (`.edit$` / `.KCMLedit$`)

Single-line text input. Prefer `.KCMLedit$` (KCML enhanced edit) for new work — it supports labels, data binding, and validation.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Text$` | string | Current content |
| `Enabled` | boolean | Enable / disable |
| `Visible` | boolean | Show / hide |
| `Label$` | string | Auto-placed label (KCML 5.03+) |
| `Type$` | string | Data type (`"D"` = date, `"B4"` = 4-byte binary integer, etc.) |
| `DropDown` | boolean | Enable dropdown list |
| `DropStyle` | enumeration | Dropdown style |
| `DropDownFilled` | boolean | Dropdown already populated |
| `ValidateText$` | string | Proposed new content (read in `Validate()` event) |
| `DataSource` | string | Variable name for data binding |
| `DataField` | reference | Field variable for data binding |
| `Help$` | string | Shown in status bar when focused |
| `ReadOnly` | boolean | Prevent editing |

### Events

| Event | Description |
|-------|-------------|
| `Click()` | Clicked |
| `Validate()` | User finished editing — `ValidateText$` holds new content, `Text$` holds old |
| `DropDown()` | Dropdown list opened |
| `MaxText()` | Maximum text length reached |

### Setting and Getting Text

```kcml
.txtName.Text$ = "Smith"          : REM set
name$ = .txtName.Text$            : REM get
```

### Validation Pattern

```kcml
+ DEFEVENT MyForm.txtQty.Validate()
    LOCAL DIM n
    CONVERT ValidateText$ TO n
    IF n < 0 THEN DO
        .pane1.Text$ = "Quantity must be positive"
        REM to reject: leave Text$ unchanged, or use Terminate/beep
    END DO
END EVENT
```

---

## Combo Box (`.combobox$`)

A dropdown list, optionally editable. Use for selecting from a known set of values.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Text$` | string | Currently selected / typed text |
| `Index` | numeric | Zero-based index of selected item |
| `Enabled` | boolean | Enable / disable |
| `Visible` | boolean | Show / hide |
| `Sort` | boolean | Auto-sort items alphabetically |
| `Help$` | string | Status bar help |

### Methods

| Method | Description |
|--------|-------------|
| `Add(string$)` | Add item to list |
| `Add(string$, tag$)` | Add item with an associated tag value |
| `Delete()` | Clear all items |
| `GetString$(index)` | Return item text at given index |
| `GetTag$()` | Return tag of currently selected item |
| `SetSelection(index)` | Select item by zero-based index |

### Events

| Event | Description |
|-------|-------------|
| `Click()` | Selection changed |
| `DblClick()` | Double-click |
| `GetFocus()` | Gained focus |
| `LoseFocus()` | Lost focus |
| `DropDown()` | Dropdown opened |

### Combo Box Style (`.Style` flag)

| Style | Behaviour |
|-------|-----------|
| `0x50210003` | Drop-down with editable field |
| `0x50210002` | Drop-down list (no editing) |
| `0x50210001` | Simple (list always visible) |

### Typical Pattern — Populate and Read

```kcml
+ DEFEVENT MyForm.Enter()
    .cmbStatus.Delete()
    .cmbStatus.Add("All")
    .cmbStatus.Add("Active")
    .cmbStatus.Add("Inactive")
    .cmbStatus.SetSelection(0)
END EVENT

+ DEFEVENT MyForm.btnApply.Click()
    LOCAL DIM status$10
    status$ = RTRIM(.cmbStatus.Text$)
    IF status$ == "All" THEN ...
END EVENT
```

### Tagged Items (key + display text)

```kcml
: .cboPrinter.Add("Laser (Main Office)", "LP1")
: .cboPrinter.Add("Inkjet (Workshop)", "IP2")
: REM later, get the tag of selected item:
: printer_code$ = RTRIM(.cboPrinter.GetTag$())
```

---

## List Box (`.listbox$`)

A scrollable list for displaying and selecting items.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Enabled` | boolean | Enable / disable |
| `Visible` | boolean | Show / hide |
| `Sort` | boolean | Auto-sort items |
| `Selection` | enumeration | Single / multiple / extended |
| `MultiColumn` | boolean | Multi-column layout |
| `UseTabs` | boolean | Expand tab characters |
| `TabStops$` | string | Tab stop positions (DLUs) |

### Methods

| Method | Description |
|--------|-------------|
| `Add(string$)` | Append item |
| `Add(string$, tag$)` | Append item with tag |
| `Delete()` | Clear all items |
| `GetTag$()` | Return tag of selected item |

### Events

| Event | Description |
|-------|-------------|
| `Click()` | Selection changed |
| `DblClick()` | Double-click — typically triggers action |
| `GetFocus()` / `LoseFocus()` | Focus events |

### Tab-Separated Columns

Use `HEX(09)` (tab) to separate columns within a single list item, combined with `UseTabs=TRUE`:

```kcml
+ DEFEVENT MyForm.Enter()
    LOCAL DIM line$100
    line$ = "Smith" & HEX(09) & "John" & HEX(09) & "London"
    .lstCustomers.Add(line$)
END EVENT
```

---

## Checkbox (`.checkbox$`)

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Text$` | string | Caption text |
| `State` | boolean (0/1) or 3-state | Checked state |
| `ThreeState` | boolean | Enable indeterminate state |
| `LeftText` | boolean | Caption on left side |
| `Enabled` | boolean | Enable / disable |

### Events

| Event | Description |
|-------|-------------|
| `Click()` | State changed |

```kcml
+ DEFEVENT MyForm.chkActive.Click()
    LOCAL DIM checked
    checked = .chkActive.State
    IF checked THEN GOSUB 'SHOW_ACTIVE_ONLY()
END EVENT
```

---

## Radio Button (`.radiobutton$`)

Radio buttons must be grouped. Only one in a group can be selected at a time.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Text$` | string | Caption |
| `State` | boolean | Selected (1) or not (0) |
| `LeftText` | boolean | Caption on left |
| `Enabled` | boolean | Enable / disable |

### Events

| Event | Description |
|-------|-------------|
| `Click()` | Selection changed |

---

## Static Text / Label (`.static$`)

Display-only text. Not interactive.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Text$` | string | Label content |
| `Visible` | boolean | Show / hide |

Use `&` in `Text$` to define an accelerator key that focuses the next control in tab order.

---

## Group Box (`.groupbox$`)

A labelled border that visually groups controls.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Text$` | string | Border title |
| `Enabled` | boolean | Enables/disables all contained controls |
| `Visible` | boolean | Shows/hides the group and its contents |

---

## Tab Control (`.tabbed$`)

Multi-page container. Each page is a separate tab.

**Important:** The correct type token is `.tabbed$`, **not** `.tabcontrol$`. The `.tabcontrol$` entry in the type token table is incorrect.

### DEFFORM Definition

Pages are defined inline as named sub-properties of the tab control. Controls within pages use `.Parent` and `.Page` to specify placement, with **form-absolute** coordinates (not tab-relative).

```kcml
{.tabMain,.tabbed$,.Style=0x500100C0,.Left=5,.Top=23,.Width=858,.Height=443,.__Anchor=15,.Id=1025,\
    .Summary={.Text$="Summary"},\
    .Details={.Text$="Details"},\
    .BOM={.Text$="Bill of Materials"}}
```

Controls placed on a specific tab page:

```kcml
{.btnOK,.button$,.Left=200,.Top=250,.Width=80,.Height=14,...,.Parent=.tabMain,.Page=.Summary,.Id=1010}
{.grid,.KCMLgrid$,.Left=8,.Top=41,.Width=844,.Height=418,...,.Parent=.tabMain,.Page=.BOM,.Id=1300,...}
```

Key points:
- Page names (`Summary`, `BOM` etc.) must be valid KCML identifiers — no spaces
- `.Left` / `.Top` on tab child controls are **form-absolute** coordinates, not relative to the tab
- The tab header takes approximately 18 DLU, so content starts at roughly `Tab.Top + 18`

### Tab Page Events

Each tab page has `Enter()` and `Exit()` events — the page name from DEFFORM is used directly:

```kcml
+ DEFEVENT MyForm.tabMain.BOM.Enter()
    GOSUB 'LOAD_BOM_DATA()
END EVENT

+ DEFEVENT MyForm.tabMain.Summary.Enter()
    REM user switched back to Summary
END EVENT
```

### Changing the Selected Tab Programmatically

```kcml
: .tabMain.CurrentTab = 2    : REM switch to page index 2 (0-based)
```

### Real-World Example (from Disp_form.kcml)

```kcml
{.tabMain,.tabbed$,.Style=0x500100C0,.Left=5,.Top=23,.Width=858,.Height=443,.__Anchor=15,.Id=1025,\
    .Summary={.Text$="Summary"},\
    .BOM={.Text$="Bill of Materials"},\
    .Locations={.Text$="Locations"}}

REM Controls on Summary page (form-absolute coordinates):
{.lblActual,.static$,.Left=100,.Top=48,.Width=80,.Height=13,...,.Parent=.tabMain,.Page=.Summary}
{.gridBOM,.KCMLgrid$,.Left=8,.Top=41,.Width=844,.Height=418,...,.Parent=.tabMain,.Page=.BOM,...}

REM DEFEVENT uses the page name from DEFFORM:
+ DEFEVENT StockDisp.tabMain.BOM.Enter()
    GOSUB 'dp_populate_bom()
END EVENT
```

---

## Status Bar (`.status$`)

Displays text in a panel at the bottom of the form. Define one `.status$` entry per pane.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Text$` | string | Displayed text |
| `Width` | numeric | Pane width (DLUs) |
| `Visible` | boolean | Show / hide pane |

### Usage

```kcml
: .pane1.Text$ = "Ready"
: .pane1.Text$ = count & " records loaded"
```

When a control has a `Help$` property set, its text is automatically shown in the status bar when that control has focus.

---

## Picture / Picture Button

### Picture Button Properties

| Property | Type | Description |
|----------|------|-------------|
| `Visible` | boolean | Show / hide |
| `Enabled` | boolean | Enable / disable |
| `MouseX` | numeric | X coordinate of last click (relative to control) |
| `MouseY` | numeric | Y coordinate of last click (relative to control) |

### Events

| Event | Description |
|-------|-------------|
| `Click()` | Clicked |
| `RightClick()` | Right-click (used to launch popup menus) |

### Popup from Picture Button

```kcml
+ DEFEVENT MyForm.picIcon.RightClick()
    .ctxMenu.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top)
END EVENT
```

---

## Gauge / Progress Bar

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Position` | numeric | Current value |
| `Min` | numeric | Minimum value |
| `Max` | numeric | Maximum value |

### Usage

```kcml
: .gauge1.Min = 0
: .gauge1.Max = 100
: .gauge1.Position = 50    : REM 50%
: .form.Flush()            : REM update display immediately
```

---

## RTF Control (`.rtf$`)

Rich text editor with formatting toolbar.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `RichText$` | string | RTF-formatted content |
| `ToolFont` | boolean | Show font toolbar |
| `ToolColor` | boolean | Show colour toolbar |
| `SelectionBar` | boolean | Show selection bar |

### Events

| Event | Description |
|-------|-------------|
| `Modified()` | Content changed |
| `RightClick()` | Right-click |
| `PrintStatus()` | Print operation status |

---

## Graph / Chart Control (`.graph$`)

2D and 3D pie and bar charts.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Type` | enumeration | Chart type (pie 2D/3D, bar 2D/3D, etc.) |
| `Text$` | string | Chart title |
| `Legend` | boolean | Show legend |
| `XLabel` | string | X-axis label |
| `ClickSet` | numeric | Dataset index of last click |
| `ClickIndex` | numeric | Data point index of last click |

### Methods

| Method | Description |
|--------|-------------|
| `Data(dataset, index, value)` | Set a data point |
| `Data(index, value)` | Pie chart variant |
| `Reset()` | Clear all data |
| `Explode(index)` | Explode a pie slice |

### Events

| Event | Description |
|-------|-------------|
| `Click()` | User clicked a data point — read `ClickSet` and `ClickIndex` |

### Example

```kcml
+ DEFEVENT MyForm.Enter()
    .chart.Reset()
    .chart.Data(1, 1, 42)    : REM dataset 1, point 1, value 42
    .chart.Data(1, 2, 58)
    .chart.Data(2, 1, 30)
    .chart.Text$ = "Sales by Region"
END EVENT
```

---

## Tree Control (`.tree$`)

Hierarchical list, like Windows Explorer.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `HasButtons` | boolean | +/- expand buttons |
| `HasLines` | boolean | Connector lines |
| `LinesAtRoot` | boolean | Lines at root level |
| `HasPictures` | boolean | Use icons |
| `ShowSelAlways` | boolean | Keep highlight when unfocused |

### Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `Add(text$, type)` | item ID | Add root item (type 0=leaf, 3=folder) |
| `Item(id).Add(text$, type)` | item ID | Add child item |
| `Item(id).Expand()` | — | Expand node |
| `Item(id).Collapse()` | — | Collapse node |
| `Item(id).Select()` | — | Select item |
| `Item(id).Delete()` | — | Remove item |
| `Item(id).Text$` | string | Get/set item text |
| `Item(id).Bold` | boolean | Bold formatting |

### Events

| Event | Description |
|-------|-------------|
| `Expand()` | First expand of a node — populate children here |
| `ExpandChange()` | Any expand or collapse |

### Deferred Population Pattern

```kcml
+ DEFEVENT MyForm.treeFiles.Expand()
    LOCAL DIM parent_id, child_id
    parent_id = ..ExpandItem
    REM populate children of parent_id
    child_id = ..Item(parent_id).Add("Child A", 0)
END EVENT
```

### OBJECT Notation for Tree Traversal

```kcml
LOCAL DIM OBJECT node
OBJECT node = .treeFiles.Item(root_id)
WHILE OBJECT node <> NULL
    PRINT node.Text$
    OBJECT node = node.Next
WEND
```

---

## Edit Group (`.editgroup$`)

A container that auto-aligns KCML edit controls and their labels at runtime.

### How it Works

1. Place KCML edit controls inside an edit group at design time
2. At runtime, the group finds the longest label among its children
3. All labels are left-aligned; all edit fields start at the same X position
4. The group may shift controls rightward to avoid label text being clipped

### Notes

- Only aligns `.KCMLedit$` controls that are members of the group
- No vertical spacing adjustments — the designer must space rows manually
- Multi-column support from KClient 6.20 (tab order goes left-to-right across columns)
