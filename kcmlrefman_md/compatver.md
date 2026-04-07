# Compatibility Between KCML Versions

> How to target older KCML versions and what behaviour changes between releases.

## Description

KCML programs saved by earlier versions run on later versions with few exceptions. To develop on a newer KCML but deploy to an older version, set the appropriate `COMPAT` environment variable. `SAVE` will then warn if the program uses constructs not supported by the target version.

The compatibility flags affect both the **parser** (code generation) and the **runtime** (execution behaviour).

Setting `COMPAT40` implies `COMPAT32` — you do not need to set both.

## KCML 6.20 differences

- `LIBRARY` is a keyword (replaces `MODULE`; `MODULE` still accepted)
- `PRIVATE` and `PUBLIC` are now keywords
- Runtime lookup of library fields is now the default (byte 49 of `$OPTIONS RUN` = `HEX(03)`)
- `KI_FLD` no longer creates field variables — can only initialise existing ones
- `KI_DESCRIBE_COL` returns new `$PACK` text formats instead of 2-byte hex
- Some exotic `$PACK(F)` formats now require `$PACK(E)`
- SY8 pack format (KCML 6.0) renamed to `FP`
- Constants are enabled by default
- Direct telnet mode (`kcml -l`) removed
- Loading boot programs from platters (`kcml -w`) removed

## KCML 6 differences

There is no `COMPAT50` flag — differences must be coded around for cross-version compatibility. Notable changes from KCML 5.02 to 6.00:

- Some form properties are now read-only (e.g. `CursorRow`, `CursorCol`)
- Child forms cannot be opened in `.Enter()` or `.Exit()` events
- `MODULE` and `OBJECT` are now reserved words
- `$PSTAT` bytes `(43,2)`, `(45,2)`, `(47,2)` no longer maintained (no meaning with memory-mapped globals)
- OCX controls edited with KCML 6 Workbench will not show all properties/events in KCML 5

## COMPAT40 flags (KCML 4 compatibility)

Set with `COMPAT40` environment variable or byte 38 of `$OPTIONS RUN`:

| Byte 38 | Affects | Controls |
|---------|---------|----------|
| `HEX(01)` | Runtime | `SAVE` warns about constructs added after KCML 4.0 (including `0xNN` literals) |
| `HEX(02)` | Runtime | Suppress P41.6 error from `RETURN CLEAR` inside an arithmetic expression |
| `HEX(04)` | Parser | Save symbols in uppercase (KCML 4 convention) |
| `HEX(08)` | Parser | Disallow empty string literals (`""`) |

Other KCML 4→5 changes not covered by flags:
- `0x` hex prefix for numeric literals (new in KCML 5)
- `BYREF`, `RTRIM()`, `LTRIM()` are now reserved words
- `ENV()` assignments are exported to child processes by default (revert with byte 39 of `$OPTIONS RUN`)

## COMPAT32 flags (KCML 3.22 compatibility)

Set with `COMPAT32` environment variable or byte 16 of `$OPTIONS RUN`:

| Byte 16 | Affects | Controls |
|---------|---------|----------|
| `HEX(01)` | Runtime | `SAVE` warns about constructs after KCML 3.22 |
| `HEX(02)` | Runtime | Limit line length to 1900 bytes |
| `HEX(04)` | Parser | `LOCAL DIM` scoping matches KCML 3.2 (allows out-of-scope reference to returned `LOCAL DIM` strings) |
| `HEX(08)` | Parser | `FALSE` compiled for KCML 3.2 compatibility |
| `HEX(10)` | Parser | Disallow signed arguments in `$DECLARE` (P23.8 error) |
| `HEX(20)` | Parser | `SYM(*)$()` compiled for KCML 3.2 string array handling |
| `HEX(40)` | Parser | Generate `GOSUB` for subroutines (KCML 3.2 required it) |

## See Also

- `$OPTIONS` — runtime options byte array
- `$COMPLIANCE` — compliance level setting
- `compile` — compile utility
