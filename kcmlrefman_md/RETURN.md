# RETURN

> Ends a subroutine and returns control (and optionally a value) to the caller.

## Syntax

```
RETURN
RETURN expr
RETURN CLEAR
```

## Description

`RETURN` marks the end of a subroutine started with `GOSUB` or `GOSUB 'label`. Control passes back to the statement immediately after the calling `GOSUB`.

**Returning a value:** When a subroutine is called as a function (e.g. `x = 'calculate(n)`), `RETURN expr` passes the value back to the expression. The type of the returned value must match the function type (numeric function returns a number, `$`-suffixed function returns a string).

**Terminating FOR loops:** `RETURN` also closes any open `FOR...NEXT` loops that were entered within the subroutine.

**Local variables:** Any variables declared with `LOCAL DIM` or `DEFSUB` parameters are destroyed on `RETURN`.

**`RETURN CLEAR`:** Clears the entire RETURN stack — use when you want to abort back to the top level without unwinding normally.

**Function key context:** If a `RETURN` is encountered in a routine triggered by a function key, it returns to immediate mode or to the statement after the interrupted `LINPUT`.

## Examples

### Example 1 — Basic RETURN from subroutine
```kcml
01000 REM RETURN sends control back to caller
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

### Example 2 — RETURN with numeric value
```kcml
01000 REM DEFFN returning a computed value
: DIM n
: n = 'double(5)
: PRINT "double(5) = " ; n
: n = 'double(21)
: PRINT "double(21) = " ; n
: $END
02000 DEFFN 'double(x)
: RETURN x * 2
```
**Output:**
```
double(5) =  10
double(21) =  42
```

### Example 3 — RETURN with string value from DEFSUB
```kcml
01000 REM DEFSUB returning a string
: DIM s$30
: s$ = 'greet$("Paul")
: PRINT RTRIM(s$)
: s$ = 'greet$("World")
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
Hello World
```

## Notes

- **`RETURN` inside `IF...THEN` causes A07** in `-p` script mode. Use a flag variable instead:
  ```kcml
  : IF condition THEN ok = 0
  : IF ok == 0 THEN RETURN
  ```
- Every `GOSUB` must eventually reach a `RETURN` — jumping out via `GOTO` leaves orphaned stack entries leading to A04 stack overflow.
- `RETURN CLEAR` wipes the entire stack — use only when aborting completely (e.g. fatal error recovery).
- `END SUB` at the end of a `DEFSUB` block acts as an implicit `RETURN`.

## See also

[GOSUB](GOSUB.md), [DEFFN](DEFFN.md), [DEFSUB](DEFSUB.md)
