# LINPUT

> Displays a prompt and accepts a line of text from the keyboard into an alpha variable, with full cursor-editing support. Text-mode applications only.

## Syntax

```
LINPUT [literal_string[,]] [?] [-] alpha_variable [, [mask] [, cursor_pos]]
```

| Element | Description |
|---------|-------------|
| `literal_string` | Optional prompt text (followed by a space and the current variable contents) |
| `?` | Start in Text Entry mode (default is Edit mode) |
| `-` | Underline the entire input field |
| `alpha_variable` | The variable to receive input |
| `mask` | Reserved |
| `cursor_pos` | Initial cursor position within the field (1-based) |

## Description

When executed, `LINPUT`:
1. Displays the optional prompt on the `CO` device.
2. Recalls and displays the current contents of `alpha_variable` at the cursor position.
3. Positions the cursor at `cursor_pos` (default: 1 = start of field).
4. Accepts keyboard input, confined to the field width.

Input is limited to the defined size of `alpha_variable` (up to 1900 bytes). Attempting to move outside the field causes an alarm beep.

### Edit mode vs Text Entry mode

| Mode | Behaviour |
|------|-----------|
| **Edit mode** (default) | Function keys perform cursor movement / editing. Cursor blinks if terminal supports it. |
| **Text Entry mode** (`?` flag) | Function keys execute `DEFFN'` functions or subroutines. |

Press the `EDIT` key to toggle between modes.

### Restoring original contents

If `RETURN` has not yet been pressed: press `ERASE` then `RECALL` (Edit mode) or `ERASE` then `EDIT RECALL` (Text Entry mode).

### Mouse support (Windows / KClient)

| Action | Behaviour |
|--------|----------|
| Left click | Position cursor |
| Left double-click | Carriage return |
| Left drag | Position cursor |
| Right click / double-click | Abort then execute `'127` subroutine |
| Right drag | Position cursor, then abort and execute `'127` |

### Redirected input

`LINPUT` reads from the `INPUT` device, which can be redirected with `SELECT INPUT`:

```kcml
DIM act$64
SELECT INPUT "date ^"    REM pipe from Unix date command
LINPUT act$
SELECT INPUT /001         REM restore keyboard
```

An `X70` error occurs if `LINPUT` reads past the end of a redirected file.

## Examples

```kcml
DIM temp$20
temp$ = "ABCDEFGHIJKLMNOP"
LINPUT "Enter Text  : " -temp$,, 5
REM Displays: "Enter Text  : ABCDEFGHIJKLMNOP" with cursor at position 5 (under E)
```

Underlined field:
```kcml
LINPUT "Name: " -name$
```

With field variable:
```kcml
LINPUT "Enter field =", FLD(temp$.name$),, 12
```

## Notes

- `LINPUT` is for **text-mode** applications. For graphical forms, use form controls with `DEFEVENT`.
- Prefer `LINPUT+` for new code — it supports multi-line, word wrap, CUA-style editing, and more.
- The `-` underscore flag is used to visually indicate the input field boundaries.

## See Also

- `LINPUT+` — enhanced version with multi-line, scroll, word wrap
- `LINPUT LINE` — ring menu selection
- `LINPUT LIST` — position-based menu
- `INPUT` — legacy single-value input (obsolete)
- `KEYIN` — single character input
- `SELECT INPUT` — redirect input device
