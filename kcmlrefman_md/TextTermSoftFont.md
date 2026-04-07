# Soft Font Boxes

> Using downloadable soft fonts for box graphics on Wyse and DEC terminals.

## Description

Modern Wyse and DEC terminals support downloadable soft fonts. KCML supplies fonts that reproduce the full character set and enable box graphics:

| Font file | Terminals |
|-----------|-----------|
| `wyfont1` | Wyse 60/99/120/160/325 (US character set) |
| `wyfont2` | Wyse 60/99/120/160/325 (overscored characters for box graphics) |
| `vt220font` | DEC VT220, VT320 |
| `vt420font` | DEC VT420, VT510 |

### Loading fonts at login

```sh
cat $KCMLADDR/wyfont1 $KCMLADDR/wyfont2   # Wyse terminals
cat $KCMLADDR/vt220font                    # VT220/320
```

The screen clears while the font loads. Loading time: up to 20 seconds.

### Enabling soft font box mode

Set `$BOXTABLE` byte 1 = `HEX(02)`:

```kcml
STR($BOXTABLE, 1, 1) = HEX(02)
```

TERMINFO `BoxStart` and `BoxEnd` sequences tell KCML how to switch fonts during box drawing. Bytes 2–9 of `$BOXTABLE` define the characters for vertical box segments.

### Limitations

- Horizontal box segments: reproduced with overscored characters.
- Vertical box segments: drawn as characters; not drawn in non-blank cells.
- Box segments above highlighted characters are also highlighted.
- No character compression — screen draw speed is slower than Wang terminals.

## See Also

- `TextTermBox` — box graphics overview
- `TextTermWy60box` — Wyse with soft fonts
- `TextTermVT220box` — VT220 with soft fonts
- `$BOXTABLE` — box character table
