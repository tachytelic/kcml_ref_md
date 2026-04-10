# DEFFORM Syntax

## Overview

`DEFFORM` declares a form and all its controls as a single KCML statement. It is followed by `DEFEVENT` blocks (using `+` prefix) and terminated by `FORM END`. The entire block must appear before `Open()` is called.

## Basic Structure

```kcml
- DEFFORM FormName()=\
    {.form,.form$,.Style=0x50c000c4,.Width=400,.Height=300,.Text$="My Form",.Id=1024},\
    {.btn1,.button$,.Style=0x50010001,.Left=150,.Top=240,.Width=80,.Height=14,.Text$="OK",.Id=1},\
    {.btn2,.button$,.Style=0x50010000,.Left=240,.Top=240,.Width=80,.Height=14,.Text$="Cancel",.Id=2}
:   + DEFEVENT FormName.Enter()
:       REM initialisation code here
:   END EVENT
: FORM END
```

Key formatting rules:
- The `-` prefix on the `DEFFORM` line marks it as a continuation-style block opener
- Each control definition is a `{...}` comma-separated property list
- Lines are joined with `\` (backslash continuation)
- `DEFEVENT` blocks use `+` prefix to place them **inside** the DEFFORM block
- `FORM END` terminates the block

## Control Definition Syntax

Each control is defined as:

```
{.name, .typetoken$, .Property1=value, .Property2=value, ...}
```

`.name` — the identifier used to reference this control in code (e.g. `.btn1`, `.grid`)

`.typetoken$` — the control type (see table below)

## Control Type Tokens

| Token | Control type |
|-------|-------------|
| `.form$` | The form window itself (must be first entry) |
| `.button$` | Push button |
| `.edit$` | Edit control (standard) |
| `.KCMLedit$` | KCML enhanced edit control |
| `.combobox$` | Combo box (dropdown or list) |
| `.listbox$` | List box |
| `.static$` | Static text label |
| `.groupbox$` | Group box (border + title) |
| `.KCMLgrid$` | Grid control (table of cells) |
| `.checkbox$` | Check box |
| `.radiobutton$` | Radio button |
| `.tabbed$` | Tab control (multiple pages) — note: NOT `.tabcontrol$` |
| `.status$` | Status bar pane |
| `.Menu$` | Menu bar or context menu |
| `.rtf$` | Rich text (formatted text editor) |
| `.graph$` | Graph/chart control |
| `.tree$` | Tree view control |
| `.gauge$` | Gauge / progress bar |
| `.picture$` | Picture (image display) |
| `.picturebutton$` | Picture button |
| `.dlgfont$` | Font definition (named font for use by controls) |
| `.color$` | Colour definition (named colour for use by controls) |

## Common Properties in DEFFORM

| Property | Type | Purpose |
|----------|------|---------|
| `.Left` | numeric | X position (dialog units) |
| `.Top` | numeric | Y position (dialog units) |
| `.Width` | numeric | Width (dialog units) |
| `.Height` | numeric | Height (dialog units) |
| `.Text$` | string | Caption / label text |
| `.Id` | numeric | Windows control ID (OK button = 1, Cancel = 2) |
| `.Style` | hex numeric | Win32 style flags (see below) |
| `.Font` | reference | Named font (e.g. `.Font=.MyFont`) |
| `.__Anchor` | numeric | Anchoring behaviour on resize (5 = bottom-right) |
| `.Rows` | numeric | Grid: initial row count |
| `.Cols` | numeric | Grid: column count |
| `.FixedRows` | numeric | Grid: number of heading rows |
| `.FixedCols` | numeric | Grid: number of heading columns |

## Style Flags

The `.Style` property is a Win32 `DWORD` combining window style bits. The most common values seen in practice:

| Hex value | Meaning |
|-----------|---------|
| `0x50c000c4` | Standard resizable form with title bar, min/max/close |
| `0x50010001` | OK button (default button with Enter key) |
| `0x50010000` | Standard push button |
| `0x50210003` | Combo box, drop-down with list |
| `0x50810080` | Edit control, left-aligned |
| `0x50000002` | Static text, right-aligned |
| `0x50000007` | Group box |
| `0x50010030` | Grid control |
| `0x01` | Context menu (popup, not attached to menu bar) |

In practice, use the Forms Designer to set styles visually — it generates the correct hex values.

## Defining Fonts

Named fonts are defined within the DEFFORM as `.dlgfont$` entries and referenced by controls:

```kcml
- DEFFORM MyForm()=\
    {.form,.form$,...},\
    {.lblTitle,.static$,...,.Font=.TitleFont},\
    {.grid,.KCMLgrid$,...,.Font=.GridFont},\
    {.TitleFont,.dlgfont$,.Name$="Segoe UI",.Size=14,.Bold=1},\
    {.GridFont,.dlgfont$,.Name$="Consolas",.Size=10}
```

The `.dlgfont$` entries can appear anywhere in the control list. Reference them with `.Font=.FontName`.

## Defining Colours

Named colours are defined with `.color$` entries:

```kcml
{.clrAlt,.color$,.Red=250,.Green=248,.Blue=248}
```

Reference in code: `&.clrAlt` — the `&.` prefix creates a reference to a named object within the form.

## Reference Operator `&.`

`&.Name` creates a reference to a named form object. Used for:

```kcml
.grid.Cell(row,0).BackColor = &.clrAlt      : REM reference to named colour
.grid.LeftSelect = &.Row                     : REM reference to selection mode constant
.grid.Cell(row,1).LeftAction = &.Click       : REM reference to action constant
```

## Inline Menu Definition

Menus (including context menus) are defined inline in the DEFFORM:

```kcml
{.ctxMenu,.Menu$,.Style=0x01,.Id=2020,\
    .mnuView={.Text$="View"},\
    .mnuSep={.Flag=2048},\
    .mnuDelete={.Text$="Delete"}}
```

`Flag=2048` creates a separator line. The menu items become sub-properties of the menu object (`.ctxMenu.mnuView`, `.ctxMenu.mnuDelete`).

## Real-World Example (from manag_form.kcml)

```kcml
01011 - DEFFORM SpoolView()=\
          {.form,.form$,.Style=0x50c000c4,.Width=848,.Height=457,.Text$="Spool Queue Viewer",.Id=1024},\
          {.ok,.button$,.Style=0x50010001,.Left=708,.Top=287,.Width=125,.Height=14,.Text$="Exit",.__Anchor=5,.Id=1,.Font=.SegoeControl},\
          {.btnRefresh,.button$,.Style=0x50010000,.Left=708,.Top=248,.Width=125,.Height=14,.Text$="Refresh",.__Anchor=5,.Id=2011,.Font=.SegoeControl},\
          {.lblFUser,.static$,.Style=0x50000002,.Left=655,.Top=71,.Width=49,.Height=13,.Id=2005,.Text$="User:",.Font=.SegeoLabel},\
          {.cmbUser,.combobox$,.Style=0x50210003,.Left=708,.Top=69,.Width=125,.Height=100,.Id=2006,.Font=.SegoeControl},\
          {.grid,.KCMLgrid$,.Style=0x50010030,.Left=5,.Top=10,.Width=636,.Height=431,.Id=1000,.Rows=1,.Cols=8,.FixedRows=1,.Font=.ConsolasGrid},\
          {.ctxMenu,.Menu$,.Style=0x01,.Id=2020,.mnuView={.Text$="View"},.mnuSep={.Flag=2048},.mnuDelete={.Text$="Delete"}},\
          {.frameFilter,.groupbox$,.Left=644,.Top=10,.Width=198,.Height=167,.Style=0x50000007,.Text$="Filter and Search",.Id=1027},\
          {.pane1,.status$,.Width=100,.Style=0x50000000},\
          {.ConsolasGrid,.dlgfont$,.Name$="Consolas",.Size=10},\
          {.SegoeControl,.dlgfont$,.Size=10},\
          {.clrAlt,.color$,.Red=250,.Green=248,.Blue=248}
```

## Positioning and Units

Control positions use **Dialog Units (DLUs)**, not pixels. DLUs scale with the system font, making forms resolution-independent. The Forms Designer displays and edits in DLUs.

To position a form on screen at runtime:
```kcml
: .form.Placement = &.MiddleCenter    : REM centre on screen
: .form.Left = 100                    : REM explicit position (DLUs from parent)
: .form.Top = 50
```
