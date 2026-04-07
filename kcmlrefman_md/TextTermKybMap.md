# Remapping the Keyboard

> Three methods for remapping keys in KCML text-mode sessions.

## Method 1 — TERMINFO map entries

Best for fixing terminal-specific character mappings. Add `map` entries to the terminal's TERMINFO section:

```
map(\x7C) = \xF6
```

This maps the character sent by the terminal (`HEX(F6)`) to `HEX(7C)` before KCML sees it. Fixed per terminal type; applies to all sessions of that terminal type.

## Method 2 — `$TRAN`

For single-key runtime remapping. `$TRAN /001` is a 256-byte translation table for simple (single-character) keys:

```kcml
STR($TRAN /001, VAL(HEX(F6))+1, 1) = HEX(7C)
```

Does not affect multi-character sequences (function keys). Use `$KEYBOARD` for those.

## Method 3 — `$KEYBOARD`

For runtime remapping of function keys and complex key sequences under program control. A utility `editkb` generates the mapping string for KClient (mapping Windows Virtual Key codes to KCML equivalents).

The older DOS `$KEYBOARD` format used a 576-byte table (still supported for compatibility).

## Notes

- TERMINFO remapping: affects all programs for that terminal type.
- `$TRAN`: affects only the running program.
- `$KEYBOARD`: most flexible for KClient; KClient-specific in its extended form.

## See Also

- `TextTermGrammar` — TERMINFO file format
- `$TRAN` — translation table
- `$KEYBOARD` — keyboard remapping
