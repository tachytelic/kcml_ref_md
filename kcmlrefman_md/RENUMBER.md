# RENUMBER (immediate mode command)

> Renumbers the program lines of the program in memory.

## Syntax

```
RENUMBER
RENUMBER start_line
RENUMBER start_line, end_line
RENUMBER start_line, end_line TO new_start [STEP increment]
```

## Description

**Immediate mode only** — cannot be used inside a running program.

Renumbers program lines in memory. All cross-references (`GOTO`, `GOSUB`, `RESTORE`, etc.) are updated automatically to match the new line numbers.

| Form | Effect |
|------|--------|
| `RENUMBER` | All lines, starting at 10, step 10 |
| `RENUMBER start` | From `start` to end of program, step 10; lines before are unchanged |
| `RENUMBER ,end` | Lines 0 to `end`, step 10; lines after are unchanged |
| `RENUMBER start, end` | Lines from `start` to `end`, step 10 |
| `RENUMBER start, end TO new_start STEP n` | Renumber range starting at `new_start` with step `n` |

## Examples

```kcml
RENUMBER                        : REM  all lines → 10, 20, 30, ...
RENUMBER 100-500 TO 1000 STEP 5 : REM  lines 100–500 → 1000, 1005, 1010, ...
RENUMBER 10000, 12000 TO 25000  : REM  lines 10000–12000 → 25000, 25010, ...
```

## Notes

- Line numbers must be in range 1–32000.
- `STEP` defaults to 10.
- All `GOTO`, `GOSUB`, `RESTORE`, and other line-number references are patched automatically.
- With the new text format (`NEWASCII`), line numbers are optional and `RENUMBER` is less relevant.

## See Also

- `RENAME` — rename variables and labels
- `NEWASCII` — source format without mandatory line numbers
