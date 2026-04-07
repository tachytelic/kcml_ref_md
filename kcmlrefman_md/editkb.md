# editkb — $KEYBOARD Map Generator

> Windows utility for interactively building `$KEYBOARD` remapping strings.

## Description

`editkb.exe` is a Windows utility shipped with KCML. If found, it is automatically added to the Workbench menus. It provides an interactive GUI for building `$KEYBOARD` statement strings that remap keys.

## How to use

1. **Choose the key** to remap from the left-hand combo box.
2. **Check shift states** as required (Shift, Ctrl, Alt).
3. **Pick the KCML virtual key** that is the target of the mapping.
4. Click **Add** — the mapping is appended to the `$KEYBOARD` string displayed in the read-only text box at the top.
5. To remove a mapping, select it in the listbox and click **Remove**.
6. When done, select the `$KEYBOARD` string, copy with `Ctrl-C`, switch to the Workbench, and paste with `Ctrl-V`.

## See Also

- `$KEYBOARD` — keyboard remapping statement
- `keycodes` — KCML key codes reference
- `vkcodes` — Windows virtual key codes
