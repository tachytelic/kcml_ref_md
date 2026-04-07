# The SELECT CASE Statement

> An efficient, readable alternative to cascaded IF/ELSE chains for multi-way branching on a single value.

## Overview

`SELECT CASE` evaluates an expression or condition once and then tests it against a series of `CASE` clauses in order. When a match is found, the statements following that clause execute and control passes to the statement after `END SELECT`. If no match is found and a `CASE ELSE` clause is present, its statements execute instead.

`SELECT CASE` can span any number of program lines. The `LIST` command automatically indents the body for readability.

**Performance tip:** Put the most frequently matched `CASE` clauses first, especially in long statements. KCML tests clauses in order and stops at the first match.

## Structure

```kcml
SELECT CASE expr
CASE value1 [, value2, ...]
    REM statements executed when expr matches value1 or value2
CASE value3
    REM statements executed when expr matches value3
CASE ELSE
    REM statements executed when no CASE matched
END SELECT
```

| Clause | Purpose |
|--------|---------|
| `SELECT CASE expr` | Evaluates `expr` (numeric or alpha) and begins matching |
| `CASE v1 [, v2 ...]` | Matches if expr equals any listed value - comma-separated list |
| `CASE ELSE` | Catch-all executed when no earlier CASE matched |
| `END SELECT` | Closes the statement |

**Type consistency:** The type (numeric vs. alpha) of expressions in `CASE` clauses must match the type in `SELECT CASE`. A mismatch produces an `X74` error.

**CASE ELSE placement:** Any `CASE` clauses written after `CASE ELSE` are silently ignored.

## Numeric SELECT CASE

Match a numeric variable against specific values. Multiple values in a single `CASE` are comma-separated.

```kcml
REM example of numeric CASE
WHILE TRUE DO
    READ test_number
    SELECT CASE test_number
    CASE 1,2
        PRINT "test_number is either 1 or 2"
        CONTINUE
    CASE 3
        PRINT "test_number is now 3"
        CONTINUE
    CASE 4,5,6,7,8,9,10
        PRINT "test_number is now either 4,5,6,7,8,9,10"
        CONTINUE
    CASE ELSE
        PRINT "Number out of range"
        BREAK
    CASE 98,97,96,95
        REM this case is never reached - it follows CASE ELSE
    END SELECT
    REM only reached when CASE does not match and no CASE ELSE executed BREAK
    PRINT "test_number not found in CASE"
WEND
DATA 1,2,3,4,5,6,7,8,9,10,99
```

**Output:**
```
test_number is either 1 or 2
test_number is either 1 or 2
test_number is now 3
test_number is now either 4,5,6,7,8,9,10
test_number is now either 4,5,6,7,8,9,10
test_number is now either 4,5,6,7,8,9,10
test_number is now either 4,5,6,7,8,9,10
test_number is now either 4,5,6,7,8,9,10
test_number is now either 4,5,6,7,8,9,10
test_number is now either 4,5,6,7,8,9,10
Number out of range
```

Note that `CONTINUE` jumps to the end of the enclosing `WHILE`/`FOR` loop — useful here to skip past `PRINT "test_number not found in CASE"` at the bottom of the loop. `BREAK` exits the loop entirely.

## Alpha SELECT CASE

Match a string variable against literal strings or expressions. Expressions (including function calls) are fully supported in `CASE` clauses.

```kcml
REM example of string CASE
astring$ = "XXXXSteveXXXX"
WHILE TRUE DO
    READ test_string$
    PRINT """";test_string$;"""",
    SELECT CASE test_string$
    CASE "END"
        BREAK
    CASE "Peter","Bill"
        PRINT "test_string$ is now either Peter or Bill"
        CONTINUE
    CASE STR(test_string$,5,5)
        REM matches if chars 5-9 of test_string$ equal the whole of test_string$
        REM i.e. when test_string$ is exactly 5 chars starting at position 5
        PRINT "test_string$ is now Steve"
        CONTINUE
    CASE "Alan","Graham","Dave","Fred",STR(astring$,4,5)
        REM STR(astring$,4,5) extracts "Steve" from "XXXXSteveXXXX" - not used here
        PRINT "test_string$ is now Alan, Fred or Dave"
        CONTINUE
    END SELECT
    PRINT "test_string$ not found in CASE"
WEND
DATA "Bill","Steve","Alan","Fred","Dave","Peter","Rob","END"
```

**Output:**
```
"Bill"          test_string$ is now either Peter or Bill
"Steve"         test_string$ is now Steve
"Alan"          test_string$ is now Alan, Fred or Dave
"Fred"          test_string$ is now Alan, Fred or Dave
"Dave"          test_string$ is now Alan, Fred or Dave
"Peter"         test_string$ is now either Peter or Bill
"Rob"           test_string$ not found in CASE
"END"
```

## Conditional SELECT CASE (Boolean)

When `SELECT CASE TRUE` is used, each `CASE` clause specifies a condition rather than a value. The first clause whose condition evaluates to true executes. This is equivalent to an if/else-if chain but often more readable.

Any expression that could appear in an `IF ... THEN` can be used as a condition in a `CASE` clause.

```kcml
REM example of logical CASE
FOR loop_value = -2 TO 2
    PRINT "(";loop_value;")",
    SELECT CASE TRUE
    CASE loop_value<0
        PRINT "loop_value is < 0"
    CASE loop_value==0
        PRINT "loop_value is = 0"
    CASE loop_value>0
        PRINT "loop_value is > 0"
    END SELECT
NEXT loop_value
```

**Output:**
```
(-2 )           loop_value is < 0
(-1 )           loop_value is < 0
( 0 )           loop_value is = 0
( 1 )           loop_value is > 0
( 2 )           loop_value is > 0
```

`SELECT CASE TRUE` could be replaced with any expression — the `CASE` conditions are then tested for equality against that expression's value rather than testing the conditions themselves as booleans.

## Notes

- **Clause ordering matters.** Clauses are tested top to bottom; the first match wins. Put common cases early for performance.
- **Dead code after CASE ELSE.** Any `CASE` clause following `CASE ELSE` is ignored — KCML does not warn about this.
- **CONTINUE inside SELECT CASE** acts on the enclosing loop (WHILE, FOR, REPEAT), not on the SELECT CASE itself.
- **Type mismatch** between the `SELECT CASE` expression and a `CASE` expression produces an `X74` error at runtime.
- **Expressions in CASE are re-evaluated each pass.** If the CASE expression calls a function or references a variable, that call/reference happens each time the clause is tested.
