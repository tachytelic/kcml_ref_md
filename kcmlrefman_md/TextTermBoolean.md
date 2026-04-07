# TERMINFO Boolean Flags

> Boolean capability flags in KCML TERMINFO entries.

## Description

Boolean flags in the TERMINFO source file control terminal behaviour. Unset flags default to FALSE.

| Flag | Description |
|------|-------------|
| `ACSfix` | Workaround for attribute problems on ACS terminals |
| `AutoWrap` | TRUE if terminal auto-issues LF when it receives CR |
| `CS8bits` | Enable 8-bit character set; auto-set for KClient/WDW |
| `CuaMode` | Remap Esc, TAB, SHIFT-TAB to `0x7F`, `0x7B`, `0x7E` |
| `DefaultScreen` | TRUE = terminal understands native KCML sequences (KClient, WDW) |
| `Editor` | Enable KCML 4 editor support |
| `FastClear` | Use clear-to-EOL/EOS sequences for `PRINT AT(,,n)` — faster but incompatible with box graphics |
| `Ideographic` | Taiwanese 2236 only; suppresses `HEX(0202040F)` |
| `MultiScreen` | Suppress screen switching in editor (do not use) |
| `RobustFlow` | Send FDF6 on CLEAR (for Redhaw Wyse 50 only) |
| `SpecTerm` | Spectrix terminal flow control workaround |

## See Also

- `TextTermGrammar` — TERMINFO file format
- `TextTermKybDefs` — keyboard key definitions
