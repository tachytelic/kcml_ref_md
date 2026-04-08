# KCML Forms — Dynamic Forms and Inheritance

## Form Inheritance

A form can inherit all controls and event handlers from a parent (template) form. Only the new controls unique to the child need to be defined.

### Syntax

```kcml
- DEFFORM ChildForm(ParentForm)=\
    {.form,.form$,...},\
    {.extraButton,.button$,...}
:   + DEFEVENT ChildForm.extraButton.Click()
:       REM only the new handler needed
:   END EVENT
: FORM END
```

- The parent form name goes in the parentheses after the child form name
- The parent form must already be compiled (its `DEFFORM` block must have been processed) before `ChildForm.Open()` is called
- Inherited controls appear in the designer with a red cross marker (read-only)
- The child can add new controls and new event handlers but cannot modify inherited ones

### Use Case

Template forms for consistent layout — e.g. a standard footer with OK/Cancel/Help buttons defined once in a `BaseForm`, inherited by all application forms.

---

## Dynamic Control Creation

### Duplicate()

Clone an existing control at runtime. Used to create a variable number of controls:

```kcml
+ DEFEVENT MyForm.Enter()
    LOCAL DIM i, new_btn
    FOR i = 1 TO 5
        new_btn = .btnTemplate.Duplicate()
        new_btn.Top = 20 + (i * 20)
        new_btn.Text$ = "Option " & i
    NEXT i
END EVENT
```

`Duplicate()` returns a reference to the new control. The new control is a copy of the template including style, size, and position. Move/resize it after duplication.

### Import()

Add controls defined as a property string (the same format used in DEFFORM):

```kcml
: control_def$ = "{.dynEdit,.KCMLedit$,.Left=100,.Top=50,.Width=150,.Height=14}"
: .form.Import(control_def$)
```

### Create() Event

The `Create()` event fires on the server **before** the form definition is sent to the client. Use it to modify the form definition programmatically — add or remove controls based on user permissions, configuration, etc.:

```kcml
+ DEFEVENT MyForm.Create()
    IF NOT user_is_admin THEN DO
        REM remove the admin-only button from the definition
        .btnAdmin.Visible = FALSE
    END DO
END EVENT
```

### EditForm()

Allows the user to rearrange and customise controls at runtime. The customised layout can be saved and restored:

```kcml
: .form.EditForm()   : REM opens layout editor for end-user customisation
```

---

## Object Notation (KCML 5.02+)

`OBJECT` variables hold references to form objects (controls). Useful for passing controls to subroutines or iterating over collections.

### Declaring and Assigning

```kcml
LOCAL DIM OBJECT ctrl
OBJECT ctrl = .grid                 : REM reference to the grid
OBJECT ctrl = .grid.Cell(1, 1)      : REM reference to a specific cell
```

### Passing to Subroutines

```kcml
GOSUB 'FORMAT_CONTROL(.btnSave)

01500 DEFFN 'FORMAT_CONTROL(OBJECT btn)
    btn.Enabled = TRUE
    btn.Text$ = RTRIM(btn.Text$) & " *"
    RETURN
```

### Iterating Controls

```kcml
LOCAL DIM OBJECT c
FOR OBJECT c IN .form
    c.Enabled = FALSE    : REM disable all controls
NEXT OBJECT c
```

### NULL Check

```kcml
: OBJECT ctrl = .grid.Cell(..CursorRow, 1)
: IF OBJECT ctrl == NULL THEN ...
: OBJECT ctrl = NULL    : REM release reference when done
```

---

## Idle Processing

While a form is displayed and no events are being processed, the `Idle()` event can fire at a regular interval. Useful for background monitoring, progress updates, or polling:

```kcml
+ DEFEVENT MyForm.Enter()
    .form.IdleTimer = 10000    : REM Idle() fires every 10 seconds
END EVENT

+ DEFEVENT MyForm.Idle()
    GOSUB 'POLL_STATUS()
    .pane1.Text$ = "Last checked: " & $TIME
END EVENT
```

`IdleTimer` is in milliseconds. Set to `-1` to disable. The event will not fire while another event handler is executing.

---

## Positioning Forms

Forms can be positioned relative to the screen or parent:

```kcml
: .form.Placement = &.MiddleCenter     : REM centre on screen
: .form.Placement = &.RelativeToParent : REM offset from parent form
: .form.Left = 200                     : REM explicit Left/Top (DLUs)
: .form.Top = 100
```

Common `Placement` values:

| Value | Meaning |
|-------|---------|
| `&.MiddleCenter` | Centred on screen |
| `&.TopLeft` | Top-left of screen |
| `&.RelativeToParent` | Offset from parent form's position |

---

## Multi-Language Strings

For multi-national systems, string literals can have language variants:

```kcml
: .btnSave.Text$ = <<"Save", "Speichern", "Enregistrer">>
```

The language is determined by the system setting (`STR($OPTIONS, 20, 1)`). The first string is the default (English), followed by alternatives in language order.

This also applies to `PRINT` statements and any string expression.
