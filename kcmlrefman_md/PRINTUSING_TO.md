# PRINTUSING TO

> Formats values using a print image and stores the result in an alpha variable (string buffer).

## Syntax

```
PRINTUSING TO buffer$, image, expr [, expr ...]
```

## Description

Works identically to `PRINTUSING` except output goes into `buffer$` instead of the print device.

The first two bytes of `buffer$` hold a binary count of bytes stored. Each `PRINTUSING TO` appends to the existing content (using the count to find the insertion point). Initialise with `buffer$ = HEX(0000)` before the first call. If the buffer fills, output is truncated and the count is clamped to the buffer length.

### Modified behaviour via `$OPTIONS RUN` byte 47

| Byte 47 value | Effect |
|---------------|--------|
| `HEX(01)` | No count prefix; output starts at byte 1; no `HEX(0D)` appended; string blank-filled |
| `HEX(02)` | Tab (`HEX(09)`) inserted at column boundaries; leading/trailing spaces stripped (for listbox column data) |

## Examples

```kcml
DIM buf$200
buf$ = HEX(0000)             : REM init count
PRINTUSING TO buf$, "-$###,###.###", 11123.46
PRINT STR(buf$, 3, LEN(STR(buf$,3)))   : REM print the formatted content
```

```kcml
REM Build a listbox row with tab-separated columns
REM Set $OPTIONS RUN byte 47 = HEX(02) for tab mode
DIM row$100
row$ = HEX(0000)
PRINTUSING TO row$, "######", partno
PRINTUSING TO row$, "####################", desc$
PRINTUSING TO row$, "####.##", price
```

```kcml
REM Using a variable for the image
DIM img$20, out$80
img$ = "####.###"
out$ = HEX(0000)
PRINTUSING TO out$, img$, 3.14159
```

## Notes

- `buf$ = HEX(0000)` is essential before the first call — an uninitialised count gives garbage results.
- The count bytes are always big-endian 16-bit.
- To extract the formatted text: `STR(buf$, 3, VAL(STR(buf$, 1, 2)))` (skip the 2-byte count header).
- Tab mode (`HEX(02)`) is designed for populating multi-column listboxes with proportional fonts.

## See Also

- `PRINTUSING` — format to the print device
- `PRINT TO` — unformatted print to buffer
- `$OPTIONS RUN` — byte 47 for PRINTUSING TO mode
