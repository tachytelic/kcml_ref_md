# GOSUB

> Calls a subroutine by line number or label, returning control after RETURN.

## Syntax

```
GOSUB line_number
GOSUB 'label [([BYREF] arg [, ...])]
result = 'label([arg [, ...]])
ON expr GOSUB label1 [, label2, ...]
```

## Description

`GOSUB` transfers execution to a subroutine and pushes a return address onto the RETURN stack. When the subroutine executes `RETURN`, control passes back to the statement immediately after the `GOSUB`.

**Two calling styles:**

- **Line number** — `GOSUB 2000` — traditional, jumps to a numbered line
- **Label (tick-apostrophe)** — `GOSUB 'ProcessRecord()` — modern, readable, preferred

The tick-apostrophe form also doubles as a function call when the subroutine returns a value:
```kcml
result = 'calculate(x, y)    REM numeric return
name$ = 'lookup$(key$)       REM string return (DEFSUB with $ suffix)
```

**Computed dispatch:** `ON expr GOSUB` calls one of several subroutines depending on the numeric value of `expr`.

## Examples

### Example 1 — Basic GOSUB with line number
```kcml
01000 REM Call a subroutine by line number
: DIM result
: GOSUB 02000
: PRINT "Back from subroutine, result = " ; result
: GOSUB 02000
: PRINT "Called again, result = " ; result
: $END
02000 REM Subroutine
: result++
: PRINT "In subroutine, result = " ; result
: RETURN
```
**Output:**
```
In subroutine, result =  1 
Back from subroutine, result =  1 
In subroutine, result =  2 
Called again, result =  2
```

### Example 2 — GOSUB with named label (DEFFN)
```kcml
01000 REM Accumulate a total by calling a named subroutine
: DIM total, i
: FOR i = 1 TO 3
:   GOSUB 'add_ten()
: NEXT i
: PRINT "Total after 3 calls: " ; total
: $END
02000 DEFFN 'add_ten()
: total = total + 10
: RETURN
```
**Output:**
```
Total after 3 calls:  30
```

### Example 3 — Subroutine returning a string value
```kcml
01000 REM DEFSUB returning a string via tick-apostrophe
: DIM s$30
: s$ = 'greet$("Paul")
: PRINT RTRIM(s$)
: $END
02000 DEFSUB 'greet$(name$)
: DIM r$50
: r$ = "Hello " & RTRIM(name$)
: RETURN r$
: END SUB
```
**Output:**
```
Hello Paul
```

### Example 4 — Computed dispatch with ON GOSUB
```kcml
01000 REM Dispatch to different routines based on a value
: DIM option
: FOR option = 1 TO 3
:   ON option GOSUB 'do_one(), 'do_two(), 'do_three()
: NEXT option
: $END
02000 DEFFN 'do_one()
: PRINT "Option 1"
: RETURN
03000 DEFFN 'do_two()
: PRINT "Option 2"
: RETURN
04000 DEFFN 'do_three()
: PRINT "Option 3"
: RETURN
```
**Output:**
```
Option 1
Option 2
Option 3
```

## Notes

- Prefer the tick-apostrophe style (`'label()`) — it supports local variables (via `DEFSUB`), is readable, and works identically as both a call and a function.
- Never jump out of a subroutine with `GOTO` — always `RETURN`. Orphaned stack entries cause **A04 stack overflow** eventually.
- All RETURN stack entries are cleared by `CLEAR`, `RETURN CLEAR`, or `LOAD`.
- The global partition is searched for labels before the foreground partition (unless `KEEPSHARED` env var is set).
- Parameter without explicit size in DEFSUB (`name$` not `name$30`) — KCML sizes the local copy to match the caller's string.

## See also

[RETURN](RETURN.md), [DEFFN](DEFFN.md), [DEFSUB](DEFSUB.md), [GOTO](GOTO.md)
