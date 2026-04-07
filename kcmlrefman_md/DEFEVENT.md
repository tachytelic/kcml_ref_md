# DEFEVENT

> Defines an event handler subroutine that is called when a form control fires an event (e.g. a button click).

## Syntax

```
DEFEVENT eventname([argument [, argument] ...])
    ...
END EVENT
```

| Element | Description |
|---------|-------------|
| `eventname` | Dotted name: `FormName.ControlName.EventName` (e.g. `Form1.btnOK.Click`) |
| `argument` | Optional string or numeric receiver variables for event data |

## Description

`DEFEVENT` marks the start of an event handler subroutine. It is called automatically by the KCML forms runtime whenever the specified event is signalled from the client.

Event names are dotted: `FormName.ControlName.EventName`. The form name and control name identify which control on which form, and the event name identifies the specific action (e.g. `Click`, `Change`).

When KCML opens a form with `.Open()`, it scans the program for relevant `DEFEVENT` blocks and registers them with the client. The client then calls back to KCML when those events fire.

Most events have no arguments, but some pass data (e.g. key events may pass the key value). Arguments must match the event definition in type and count.

`DEFEVENT` can appear anywhere in the program — inside or outside a `DEFFORM` block — as long as the dotted name specifies the correct form.

Control returns to the form when a `RETURN` statement is executed inside the handler.

**Important from CLAUDE.md:** DEFEVENT blocks must be **inside** a `DEFFORM` block as continuation lines (prefixed with `+`). A DEFEVENT placed outside or as a top-level numbered line is not associated with the form and will be silently ignored.

## Example

```kcml
DEFFORM Form1()
    + DEFEVENT Form1.btnOK.Click()
    +     PRINT "OK clicked"
    + END EVENT
FORM END
```

## Syntax example

```kcml
DEFEVENT Form1.btnOK.Click()
```

## Notes

- Events with no arguments are by far the most common.
- If the event has arguments, they must be declared as receiver variables in the `DEFEVENT` line.
- Use `RETURN` (not `END EVENT` alone) to return control to the form after handling the event.

## See Also

- `DEFFORM` — define a form structure
- `RETURN` — return from an event handler
