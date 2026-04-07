# Wyse with Soft Font Box Graphics

> KCML terminal configuration for Wyse 60/99/120/160/325 with soft font box graphics.

## Description

`KTERM=wynnnbox` (e.g. `wy60box`, `wy160box`)

Same as the standard Wyse 60 series but enables soft font box graphics. Requires two fonts to be loaded at login:

```sh
cat $KCMLADDR/wyfont1    # US 2336 character set
cat $KCMLADDR/wyfont2    # Box graphics (overscored characters)
```

Loading time: up to 20 seconds. The default `.profile` installed by `kcmladmin` sends the fonts automatically.

### Character cell size

If characters like p, g, y lose parts after font load, change the character cell size in the terminal setup menu to 10×16, then reload the font (log out and in again).

### Limitations

- Box segments above highlighted characters are also highlighted.
- No character compression → screen draw slower than Wang 2336.
- Some UNIX programs may not recognise `wynnnbox` as a TERM value — set `TERM=wynnn` for the shell.

### Setup

```sh
export TERM=wy160          # for UNIX programs
export KTERM=wy160box      # for KCML
```

If fonts cannot be used (clone without soft font support), remove the font loading from `.profile` and use plain `KTERM=wy160`.

## See Also

- `TextTermWy60` — Wyse 60 without soft fonts
- `TextTermSoftFont` — soft font box graphics overview
