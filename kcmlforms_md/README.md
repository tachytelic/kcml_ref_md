# KCML Forms Reference Documentation

KCML Forms provides a Win32 GUI layer on top of the KCML 4GL. Forms run on a Windows client (KClient) connected to a KCML server over TCP/IP. The system produces standard Win32 windows, dialogs, grids, menus, and common controls — programmed entirely in KCML without any separate resource files or GUI designer code generation beyond the `DEFFORM` block.

This is a primary development area: forms replace the legacy character-based terminal UI with a modern Windows interface while keeping all business logic in KCML.

## Files

| File | Contents |
|------|---------|
| [01-introduction.md](01-introduction.md) | Architecture, thin client model, how forms work |
| [02-defform-syntax.md](02-defform-syntax.md) | DEFFORM block syntax, control type tokens, style flags, fonts, colors |
| [03-events.md](03-events.md) | DEFEVENT, event lifecycle, LOCAL DIM, calling events as subroutines |
| [04-controls.md](04-controls.md) | All control types — properties, methods, events |
| [05-grid-control.md](05-grid-control.md) | Grid control in depth — cells, headings, editing, large datasets |
| [06-menus.md](06-menus.md) | Menu bars, popup/context menus, TrackPopup |
| [07-data-binding.md](07-data-binding.md) | DataSource/DataField, bespoke data awareness, DataBind |
| [08-dynamic-inheritance.md](08-dynamic-inheritance.md) | Form inheritance, Duplicate(), dynamic control creation |
| [09-patterns.md](09-patterns.md) | Real-world patterns from manag_form.kcml — annotated reference |

## Minimal Working Form

```kcml
: DIM result
: REM
- DEFFORM Hello()=\
  {.form,.form$,.Style=0x50c000c4,.Width=300,.Height=150,.Text$="Hello"},\
  {.ok,.button$,.Style=0x50010001,.Left=90,.Top=80,.Width=100,.Height=14,.Text$="OK",.Id=1}
:   + DEFEVENT Hello.Enter()
:       .ok.SetFocus()
:   END EVENT
: FORM END
: result = Hello.Open()
: $END
```

## Key Rules

- `DEFFORM` must be complete before `Open()` is called — all `DEFEVENT` blocks must be inside the DEFFORM using the `+` prefix
- `result = FormName.Open()` — **must assign the return value**; bare `FormName.Open()` silently fails
- DEFEVENTs placed outside the DEFFORM block (without `+`) are not associated with the form
- Within a DEFEVENT, `.controlName` refers to a sibling control on the same form; `..PropertyName` refers to the event's own control ("self")
- `LOCAL DIM` inside DEFEVENTs declares variables that exist only during that event call
- Event handlers are not called until `Open()` is executing; any code between DEFFORM and FORM END runs at Open() time as initialisation
- Forms can be nested — `ChildForm.Open()` inside a parent event handler blocks until child closes
