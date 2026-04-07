# WHILE ... WEND

> Repeats a block of statements as long as a condition remains true, testing the condition before each iteration.

## Syntax

```
WHILE condition DO
    ...
WEND
```

| Element | Description |
|---------|-------------|
| `condition` | Any KCML boolean expression. Evaluated before each iteration. |
| `DO` | Required keyword that ends the `WHILE` clause and begins the loop body. |
| `WEND` | Marks the end of the loop body. Must be paired with the corresponding `WHILE`. |

## Description

The `WHILE` statement tests `condition` before each pass through the loop. If the condition is true, the body executes and the condition is re-evaluated at `WEND`. If the condition is false when first reached, the body is skipped entirely — unlike `REPEAT ... UNTIL`, which always executes at least once.

Each `WHILE` must be paired with a `WEND`. Pairing is verified at resolve time. The KCML editor automatically indents the loop body. `WHILE` loops may be nested to a depth of at least 20.

The `WHILE ... WEND` loop does **not** use the return stack at execution time, so `LIST RETURN` does not show these loops.

## Parameters / Clauses

### Condition

The condition follows the same rules as conditions in `IF` statements. It can be:

- A simple comparison: `a < 100`, `x == y`, `name$ <> ""`
- A compound expression using `AND`, `OR`, `XOR`, and parentheses
- The special keyword `TRUE` (for an infinite loop)
- The special keyword `NOT END` (loop until end of file)
- A subroutine call result: `'counter <> 45`

### BREAK and CONTINUE

Jumping into or out of `WHILE` loops with `GOTO` is permitted but is very poor practice. Use the structured alternatives:

| Statement | Effect |
|-----------|--------|
| `BREAK` | Exits the loop immediately; execution continues after `WEND` |
| `CONTINUE` | Skips the remaining loop body and jumps back to re-evaluate the `WHILE` condition |

## Examples

### Basic loop with BREAK and CONTINUE

```kcml
WHILE a < 100 DO
    IF (++a = b)
        BREAK
    END IF
    IF (MOD(a,5)==0)
        CONTINUE
    END IF
    'Calculate()
WEND
```

`'Calculate()` is skipped whenever `a` is a multiple of 5. The loop exits early if `a` equals `b`.

### Infinite loop (event loop pattern)

```kcml
WHILE TRUE DO
    'Read_keyboard
    IF (char$ == exit_key$)
        BREAK
    END IF
    'UpdateForm()
WEND
```

Runs forever until `char$` matches `exit_key$`, then `BREAK` exits.

### Syntax variations

```kcml
WHILE NOT END DO
WHILE x<9 OR P<>6 AND Y<>100 DO
WHILE 'counter<>45 AND a9$="FN" DO
```

## Notes

- The condition is checked **before** the first iteration. If it is false initially, the loop body never executes.
- Contrast with `REPEAT ... UNTIL`, which checks the condition **after** each iteration and always executes at least once.
- The `DO` keyword is required as part of the `WHILE` clause syntax.
- The return stack is not used, so stack overflow from nested `WHILE` loops is not a concern; however the nesting depth limit is at least 20.
- Using `++` (pre/post increment) inside the condition is valid and common.

## See Also

- `WEND` — closes a `WHILE` loop
- `BREAK` — exit a loop early
- `CONTINUE` — skip to the next loop iteration
- `REPEAT ... UNTIL` — post-condition loop (body always executes at least once)
- `CONTINUE LOOP` — skip to the next iteration of an outer loop
- `FOR ... NEXT` — counted loop
