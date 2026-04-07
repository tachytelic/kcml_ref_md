# GOTO

> Transfers program execution unconditionally to a specified line number.

## Syntax

```
GOTO line_number
```

Valid in numbered-line program mode. Any statements between the `GOTO` and the target line are skipped.

## Description

`GOTO` causes execution to jump immediately to `line_number`. Statements following a `GOTO` on the same line (or logically after it) are never reached.

`GOTO` is also permitted in **immediate mode** (the KCML Workbench command line), provided the program is still resolved. Issuing `CONTINUE` after an immediate-mode `GOTO` restarts the program at the new line.

## Example

```kcml
1000 IF x > 10 THEN GOTO 1050
1010 PRINT "x is small"
1020 GOTO 1060
1050 PRINT "x is large"
1060 REM continue here
```

Unconditional jump:
```kcml
GOTO 9999
```

## Notes

- `GOTO` with a line number is the legacy Wang BASIC-2 style. In modern KCML, prefer structured control flow: `IF...END IF`, `FOR...NEXT`, `REPEAT...UNTIL`, `WHILE...WEND`.
- Jumping into a `FOR...NEXT` or `FOR OBJECT` loop is not recommended and can cause stack/runtime errors.
- `GOTO` is not available in `-p` (script) mode since scripts have no line numbers.

## See Also

- `ON ... GOTO` — computed multi-way branch
- `IF ... THEN` — conditional branch
- `GOSUB` — call a subroutine at a line number (with RETURN)
- `BREAK` — exit a loop cleanly
