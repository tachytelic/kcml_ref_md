# KCML Forms — Introduction and Architecture

## Overview

KCML Forms adds a Win32 GUI layer to KCML programs. Instead of terminal-based screen I/O (`PRINT AT`, `KEYIN`, `BOX`), forms programs produce standard Windows dialogs, grids, menus, and common controls rendered natively by the Windows client.

The key point: **this is not a web framework or a report renderer**. The forms run as genuine Win32 windows on the user's desktop. They look and behave like any other Windows application — resizable, scrollable, with standard keyboard navigation, drag-and-drop, context menus, clipboard support.

## Thin Client Architecture

```
[KCML Server — Linux/Unix/Windows]          [Windows Client — KClient]
  KCML program runs here                       Renders the form
  Business logic executes here                 Handles mouse/keyboard
  DEFFORM definition sent to client            Sends events back to server
  Event handler runs on server                 Updates controls from server
```

The KCML program runs on the server. When `FormName.Open()` is called:
1. The complete form definition (from `DEFFORM`) is sent to the client
2. KClient assembles the Win32 window and its controls
3. The user interacts with the form; events are sent back to the server
4. The server runs the appropriate DEFEVENT handler
5. Changes to controls (text, state, rows added) are sent back to the client
6. `Open()` returns when the form closes (OK/Cancel/Terminate)

This means **all KCML code runs on the server** — even event handlers. The client is a pure renderer. Network latency affects responsiveness, which is why the `Flush()` method exists (force an update mid-handler) and why `DataPending` / `RowRequest()` exist (defer loading large grids).

## What Forms Replace

| Old (character-based) | New (forms) |
|-----------------------|-------------|
| `PRINT AT row, col, "text"` | Static label control |
| `KEYIN` / `KEYSTR` | Edit control in event handler |
| `BOX` / `WINDOW` | Group box or tab control |
| `SELECT PRINT` / menu loops | Menu bar or combo box |
| Character-mode grid (PRINT AT loops) | KCMLgrid control |
| `MESS_BOX` subroutine | Nested form or MessageBox |

The transition is incremental — existing character-based screens and new form-based screens coexist in the same ERP system.

## The Form Lifecycle

```
1. DEFFORM block compiled (at program load time)
2. FormName.Open() called
   a. Code between DEFFORM and FORM END runs (initialisation)
   b. Form definition sent to client → window appears
   c. Enter() event fires → populate controls
3. User interacts → events fire on server → server updates controls
4. User clicks OK/Cancel or code calls Terminate()
5. Exit() event fires (if defined)
6. Open() returns: 1 (OK), 0 (Cancel), or custom value from Terminate()
7. Form variables and LOCAL DIM vars destroyed
```

## Form Return Values

```kcml
: DIM result
: result = MyForm.Open()
: IF result == 0 THEN PRINT "Cancelled"
: IF result == 1 THEN PRINT "OK"
: IF result == 2 THEN PRINT "Custom return from Terminate(2)"
```

- `0` — user clicked a Cancel button (button with Type=Cancel / Id=2) or closed the window
- `1` — user clicked an OK button (button with Type=OK / Id=1)
- Any other value — returned by `.form.Terminate(n)` called in code

## Nesting Forms

Forms can open other forms. The inner form blocks until it closes:

```kcml
+ DEFEVENT MyForm.btnDetail.Click()
    LOCAL DIM detail_result
    detail_result = DetailForm.Open()
    IF detail_result == 1 THEN DO
        REM user confirmed in detail form
    END DO
END EVENT
```

The outer form remains displayed but inactive while the inner form is open.

## KClient Version Notes

| Feature | Minimum version |
|---------|----------------|
| Basic forms | KCML 5.x |
| OBJECT notation, default params | KCML 5.02 |
| Graph control, Label$ on edit | KCML 5.03 |
| AutoEdit grid, ServerText fixed | KCML 6.00 |
| EditGroup multi-column | KClient 6.20 |
