# Character Boxes ($BOXTABLE layout)

> How KCML uses character substitution to simulate box graphics on non-native terminals.

## Description

When a terminal does not support native KCML box drawing (`$BOXTABLE` first byte = `HEX(01)`), KCML uses characters to simulate boxes. The 16 bytes following the mode byte in `$BOXTABLE` define which character to use for each combination of box segments.

Box segments extend from the centre of a character cell in N/S/E/W directions. Each of the 16 combinations is a bitmask:

| Bit | Segment |
|-----|---------|
| 3 (MSB) | North (↑) |
| 2 | South (↓) |
| 1 | East (→) |
| 0 (LSB) | West (←) |

### $BOXTABLE byte index to segment combination

| Byte | N | S | E | W | Character needed |
|------|---|---|---|---|-----------------|
| 2 | — | — | — | — | (empty/space) |
| 3 | — | — | — | W | left end |
| 4 | — | — | E | — | right end |
| 5 | — | — | E | W | horizontal bar |
| 6 | — | S | — | — | top end |
| 7 | — | S | — | W | top-right corner |
| 8 | — | S | E | — | top-left corner |
| 9 | — | S | E | W | T (top) |
| 10 | N | — | — | — | bottom end |
| 11 | N | — | — | W | bottom-right corner |
| 12 | N | — | E | — | bottom-left corner |
| 13 | N | — | E | W | T (bottom) |
| 14 | N | S | — | — | vertical bar |
| 15 | N | S | — | W | T (right) |
| 16 | N | S | E | — | T (left) |
| 17 | N | S | E | W | cross (+) |

## Example ($BOXTABLE for VT100 graphics)

```kcml
REM VT100 uses ACS (Alternate Character Set) graphics characters
REM Set $BOXTABLE to use VT100 ACS characters
```

## See Also

- `TextTermBox` — box graphics overview
- `$BOXTABLE` — set/get the box character table
- `PRINT BOX(` — draw boxes
