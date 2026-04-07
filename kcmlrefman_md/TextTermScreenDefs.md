# General TERMINFO Screen Definitions

> Common TERMINFO capability definitions for screen control.

## Key TERMINFO definitions

| Code | Description |
|------|-------------|
| `Above80` | Parameterized string to print characters `HEX(80)` or above; needed on 7-bit terminals (e.g. VT100) that require font switching for high characters |
| `ACSfix` | Boolean workaround for ACS terminal attribute/font change bug |
| `AttribOff` | Sequence to disable all attributes (no parameters) |
| `AttribOn` | Parameterized string to enable attributes; parameters: `%p1`=bold, `%p2`=blink, `%p3`=reverse, `%p4`=underline, `%p5`=always zero |
| `Below20` | Parameterized string to print characters below `HEX(20)`; needed for terminals that cannot directly print control characters |
| `BoxStart` | Sequence to switch to soft-font box drawing mode |
| `BoxEnd` | Sequence to restore normal font after box drawing |
| `Col132` | Sequence to switch to 132-column mode |

## Notes

- `Above80` and `Below20`: if not defined, KCML prints the character unaltered.
- `AttribOn` must be defined so that enabling any non-zero parameter enables the corresponding attribute.
- `AttribOff` on terminals without bold: use `dim` for normal, `normal` for bright.

## See Also

- `TextTermGrammar` — TERMINFO file format
- `TextTermAttrib` — text attributes
- `TextTermSoftFont` — soft font boxes
