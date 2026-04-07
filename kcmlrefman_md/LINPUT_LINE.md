# LINPUT LINE

> Displays a horizontal ring menu and returns the index of the selected option. Text-mode applications only.

## Syntax

```
LINPUT LINE alpha_expression, num_receiver [, alpha_receiver]
```

| Element | Description |
|---------|-------------|
| `alpha_expression` | Space-separated list of option words |
| `num_receiver` | Receives the index of the selected word (1-based); set to 0 on CANCEL/SHIFT+TAB |
| `alpha_receiver` | Optional: receives the function key used to terminate |

## Description

`LINPUT LINE` prints the space-separated words and reverse-videos the current selection. The user navigates with cursor keys or first-letter jumps, then confirms with RETURN/EXECUTE.

Navigation:
- **Space** or **right arrow**: advance to next word (wraps)
- **Backspace** or **left arrow**: move backwards
- **First letter of any word**: jump to the next matching word
- **RETURN / EXECUTE**: confirm selection; `num_receiver` = selected index
- **CANCEL / SHIFT+TAB**: abort; `num_receiver` = 0

If `alpha_receiver` is omitted, only RETURN/EXECUTE can terminate. If `alpha_receiver` is specified, any function key also terminates and the key value is returned.

Pre-setting `num_receiver` to a non-zero value causes the initial highlight to start at that word.

Words with embedded underscore characters are displayed with spaces instead of underscores.

### Mouse support (Windows / KClient)

| Action | Behaviour |
|--------|----------|
| Left click / double-click | Select item |
| Left drag | Position and select |
| Right click / double-click | Abort |
| Right drag | Position then abort |

## Examples

```kcml
DIM index, key$4
LINPUT LINE "Exit Next Prev Select", index
PRINT "Selected: "; index

REM With function key capture:
LINPUT LINE menu$, position, fnkey$

REM With field variable:
LINPUT LINE FLD(men$.master$), position, key1$
```

## Notes

- For text-mode applications only.
- The `num_receiver` can be used both as input (initial selection) and output (result).
- `LINPUT LIST` is the alternative for position-based menus on specific screen coordinates.

## See Also

- `LINPUT LIST` — position-based menu with explicit screen coordinates
- `LINPUT` — line input with editing
- `LINPUT+` — enhanced multi-line input
