# DEFFORM

> Defines a form (GUI window) with its controls and event handlers.

## Syntax

```
DEFFORM formname()
    [form definition lines prefixed with +]
    + DEFEVENT formname.controlname.eventname()
    +     ...
    + END EVENT
FORM END
```

## Description

`DEFFORM` defines a GUI form for the KCML client/server forms system. It is a declarative block processed at resolve time. The form is opened at runtime with:

```kcml
result = formname.Open()
```

### CLAUDE.md Critical Rules

- **All DEFFORM blocks must be fully defined before any `.Open()` call.**
- **`.Open()` must assign a result**: use `result = MyForm.Open()`, not bare `MyForm.Open()`.
- **DEFEVENT blocks must be continuation lines inside the DEFFORM block** — prefixed with `+`. A `DEFEVENT` placed outside the `DEFFORM` block (as a separate top-level statement) is not associated with the form; the form opens, does nothing, and closes silently.

### Structure

- `DEFFORM formname()` — opens the form definition
- `+ DEFEVENT ...` — defines event handlers as continuation lines (the `+` prefix is mandatory)
- `FORM END` — closes the form definition

## Example

```kcml
DEFFORM Form1()
    + DEFEVENT Form1.btnOK.Click()
    +     PRINT "OK was clicked"
    + END EVENT
    + DEFEVENT Form1.btnCancel.Click()
    +     PRINT "Cancel clicked"
    + END EVENT
FORM END

...

result = Form1.Open()
```

## Syntax example

```kcml
DEFFORM Form1()
```

## Notes

- Forms are designed using the KCML Workbench forms designer; the generated `DEFFORM` code is embedded in the program.
- The form definition is typically generated code — hand-editing is unusual.
- All form methods (`.Open()`, `.Close()`, `.Enter()`, etc.) are called on the form name as if it were an object.

## See Also

- `DEFEVENT` — define an event handler inside a DEFFORM block
- `DEFOBJ` — bind a data-aware database table to form controls
