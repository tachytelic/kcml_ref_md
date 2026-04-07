# LINPUT+

> Enhanced text input supporting multi-line editing, scrolling, word wrap, and CUA-style keyboard handling. Text-mode applications only.

## Syntax

```
LINPUT+ alpha_receiver$, proplist$
```

| Element | Description |
|---------|-------------|
| `alpha_receiver$` | Variable to receive the entered text |
| `proplist$` | 64-byte control structure (initialise to `HEX(00)`) |

## Description

`LINPUT+` is the modern replacement for `LINPUT`, adding:
- Multi-line editing (`ed_depth > 1`)
- Horizontal and vertical scrolling
- Word wrap
- CUA-style editing (no overwrite mode)
- Remote execution via Windows control (when using KClient / WDW)

The `proplist$` structure governs all behaviour. Initialise it to `ALL(HEX(00))` and set only the fields you need.

### Control structure fields

| Field name | Bytes | Dir | Format | Description |
|------------|-------|-----|--------|-------------|
| `.ed_resultlen` | 1–4 | OUT | B4 | Length of returned string |
| `.ed_returnkey$` | 5 | OUT | 1 | Terminating key (HEX(0D)=RETURN, HEX(7E)=TAB) |
| `.ed_returnpf` | 6 | OUT | B1 | 1 = PF key terminated, 0 = RETURN |
| `.ed_width` | 7 | IN | B1 | Width of edit area (0 = full size of variable) |
| `.ed_depth` | 8 | IN | B1 | Height in rows (0 or 1 = single line) |
| `.ed_attribute$` | 9 | IN | 1 | Attribute: HEX(08)=underline, HEX(20)=bright, HEX(40)=reverse |
| `.ed_color$` | 10 | IN | 1 | Reserved |
| `.ed_wordwrap` | 11 | IN | B1 | 0=no wrap, 1=word wrap (multi-line only) |
| `.ed_vscrollbar` | 12 | IN | B1 | 0=none, 1=vertical scrollbar (Windows only) |
| `.ed_hscrollbar` | 13 | IN | B1 | 0=none, 1=horizontal scrollbar (Windows only) |
| `.ed_delimiter` | 14 | IN | 1 | Paragraph delimiter (default HEX(0D)) |
| `.ed_markrows` | 15 | IN | B1 | 0=none, 1=add delimiter at each row end |
| `.ed_displayonly` | 16 | IN | B1 | 0=normal, 1=display and return, 2=display no-edit |
| `.ed_selectonentry` | 17 | IN | B1 | 0=select all, 1=no initial selection |
| `.ed_remoteexec` | 18 | IN | B1 | 0=local, 1=use Windows control |

### Single-line mode

- `ed_depth` = 0 or 1
- Auto-horizontal scroll if `ed_width < LEN(STR(alpha_receiver$))`
- RETURN or any non-editing function key terminates
- `ed_width = 0` → control width equals variable size
- `ed_width > LEN(STR(variable))` → X70 error

### Multi-line with word wrap

```kcml
LOCAL DIM text$640, lines$(8)80, prop$64
prop$ = ALL(HEX(00))
FLD(prop$.ed_delimiter) = HEX(0D)
FLD(prop$.ed_markrows) = 1
FLD(prop$.ed_wordwrap) = 1
FLD(prop$.ed_depth) = 5
LINPUT+ text$, prop$
$UNPACK(D=HEX(010D)) text$ TO lines$()
```

## Examples

### Simple single-line input

```kcml
DIM name$40, prop$64
prop$ = ALL(HEX(00))
FLD(prop$.ed_attribute$) = HEX(08)    REM underline
LINPUT+ name$, prop$
PRINT "Entered: "; name$
```

### Display-only (no editing)

```kcml
FLD(prop$.ed_displayonly) = 1
LINPUT+ message$, prop$
REM message$ is displayed; returns immediately
```

## Notes

- `LINPUT+` uses CUA-style editing (Insert mode only; no overwrite).
- Function keys `'00`–`'31`, GL, Shift GL, TAB, SHIFT+TAB do not edit — they terminate the control.
- Clicking outside the editable area also terminates (if a mouse is available).
- `Ctrl+BREAK` during `LINPUT+` is deferred until the statement ends.
- For text-mode applications only; not required in graphical forms environments (use form controls).

## See Also

- `LINPUT` — simpler single-line input
- `LINPUT LINE` — ring menu
- `$UNPACK` — split a delimited string into array elements
- `DEFEVENT` — event-driven form input (GUI alternative)
