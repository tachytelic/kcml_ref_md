# Objects in Forms (OCX Controls)

> How to use OCX/ActiveX controls and object notation in KCML forms.

## Description

### OCX controls

KCML 6.00+ implements the full OCX96 specification. OCX controls are treated as standard COM objects — the form's `Open()` method automatically instantiates them within the form container. Property and method specifications are no longer stored inside the form definition (as they were in KCML 5.02 and earlier); KCML discovers them at runtime from the type library.

Old KCML 5 forms are accepted by the KCML 6 designer; the old property/method specifications are ignored for OCX controls accessed as objects.

```kcml
DIM OBJECT myOCX
OBJECT myOCX = form1.controlOCX
myOCX.Redraw()
```

### Object notation in event handlers

Inside event handlers, object notation simplifies access to controls, grid cells, tabs, listbox items, and tree nodes:

```kcml
REM Access a grid cell as an object
DIM OBJECT thiscell
OBJECT thiscell = .grdDB.Cell(row, col)
thiscell.Text$ = "Hello"
```

```kcml
REM Access an entire grid control
DIM OBJECT grid
OBJECT grid = Form1.gridControl1
'InitGrid(OBJECT grid)
```

### Enumerating form controls

`FOR OBJECT` iterates over all controls on a form:

```kcml
DIM OBJECT ctrl
FOR OBJECT ctrl IN Form1
    REM Process each control
NEXT OBJECT ctrl
```

### Special collection properties

For listbox items, tabs, and tree nodes:

| Property | Description |
|----------|-------------|
| `First` | First element |
| `Next` | Next element |
| `SelectedFirst` | First selected element |
| `SelectedNext` | Next selected element |
| `Index` | Element index |
| `TabFirst` | First tab |
| `TabNext` | Next tab |
| `Parent` | Parent tree node |
| `Child` | Child tree node |

## See Also

- `comintro` — distributed objects overview
- `comenum` — `FOR OBJECT` enumeration
- `commethod` — object methods
- `ObjCOM` — COM client reference
