# GOTO

> Unconditionally transfers program execution to a specified line number.

## Syntax

```
GOTO line_number
ON expr GOTO line1 [, line2, ...]
IF condition THEN GOTO line_number
```

## Description

`GOTO` immediately transfers control to the specified line number. Any statements after the `GOTO` on the same line are ignored.

`GOTO` is allowed in immediate mode provided the program is still resolved — `CONTINUE` will then restart execution at the new line.

**Computed GOTO:** `ON expr GOTO` jumps to one of several line numbers depending on the integer value of `expr`. Empty entries (consecutive commas) fall through to the next statement after the `ON GOTO` line.

In modern KCML, `GOTO` is mostly used for:
- Early exit from a loop or block
- Error-handling jumps
- Legacy code maintenance

Structured alternatives (`IF/ENDIF`, `DO/WHILE`, `BREAK`) are generally preferred over `GOTO`.

## Examples

### Example 1 — Basic loop with GOTO
```kcml
01000 REM Manual loop using GOTO
: DIM i
: i = 0
01100 REM Loop start
: i++
: PRINT "i = " ; i
: IF i < 3 THEN GOTO 01100
: PRINT "Done"
: $END
```
**Output:**
```
i =  1 
i =  2 
i =  3 
Done
```

### Example 2 — Early exit on error
```kcml
01000 REM Skip processing if value is negative
: DIM x
: x = -5
: IF x < 0 THEN GOTO 01900
: PRINT "Processing: " ; x
01900 REM End
: PRINT "Finished (x=" ; x ; ")"
: $END
```
**Output:**
```
Finished (x= -5 )
```

### Example 3 — Computed GOTO dispatch
```kcml
01000 REM Jump to different section based on value
: DIM mode
: FOR mode = 1 TO 3
:   ON mode GOTO 02000, 03000, 04000
02000 REM Mode 1
:   PRINT "Mode: Read"
:   GOTO 05000
03000 REM Mode 2
:   PRINT "Mode: Write"
:   GOTO 05000
04000 REM Mode 3
:   PRINT "Mode: Delete"
05000 REM Continue
: NEXT mode
: $END
```
**Output:**
```
Mode: Read
Mode: Write
Mode: Delete
```

## Notes

- Prefer `IF/ENDIF`, `FOR`, `WHILE`, `DO/LOOP`, and `BREAK` over `GOTO` in new code.
- `GOTO` out of a `GOSUB` subroutine without `RETURN` leaves orphaned RETURN stack entries — eventually causing **A04 stack overflow**.
- In `ON expr GOTO`, a blank entry (e.g. `ON n GOTO 100, , 300`) skips that index and falls through to the next statement.

## See also

[GOSUB](GOSUB.md), [IF](IF.md), [FOR](FOR.md)
