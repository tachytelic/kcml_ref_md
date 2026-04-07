# Loop Constructs

> KCML provides three loop constructs — `FOR ... NEXT`, `REPEAT ... UNTIL`, and `WHILE ... WEND` — together with `BREAK` and `CONTINUE` for structured early exit and skip.

## Overview

There are three loop constructs available in KCML:

| Construct | When condition is tested | Minimum iterations |
|-----------|-------------------------|--------------------|
| `FOR ... NEXT` | After each iteration (counted) | 1 |
| `REPEAT ... UNTIL` | After each iteration (condition) | 1 |
| `WHILE ... WEND` | Before each iteration (condition) | 0 |

`BREAK` exits any loop immediately; `CONTINUE` skips the remaining loop body and proceeds to the next iteration.

---

## FOR ... NEXT Loops

`FOR ... NEXT` is used to create counted loops. The index variable is assigned an initial value and is incremented (or decremented) by the step on each pass. The loop continues while the index satisfies the termination condition.

**Each `FOR` statement must have a corresponding `NEXT` statement using the same index variable.** This pairing is verified at resolve time.

```kcml
FOR count = 1 TO 10
    PRINT count;
NEXT count
```

**Output:** `1  2  3  4  5  6  7  8  9  10`

### Counting down

Specify a negative `STEP` and reverse the start and end values:

```kcml
FOR count = 10 TO 1 STEP -1
    PRINT count;
NEXT count
```

**Output:** `10  9  8  7  6  5  4  3  2  1`

### BREAK and CONTINUE in FOR loops

Use `BREAK` to exit the loop cleanly and `CONTINUE` to skip the rest of the current iteration:

```kcml
FOR count = 1 TO 10
    IF count == 5 THEN CONTINUE
    PRINT count
    IF count == 7 THEN BREAK
NEXT count
```

**Output:** `1  2  3  4  6  7`

The value `5` is skipped by `CONTINUE`; the loop exits when `count` reaches `7` via `BREAK`.

### Rules for FOR loops

- Jumping **into** a `FOR ... NEXT` loop generates an error at the `NEXT` statement unless the loop has already been entered at least once. Use `BREAK` to exit loops cleanly instead.
- Jumping **out** of a loop with `GOTO` is permitted but leaves loop state on the return stack, which can eventually cause stack overflow. Always prefer `BREAK`.
- If a `FOR` loop is interrupted with `STOP`, `TRAP`, or the `HALT` key, `LIST RETURN` displays the return stack state. `CONTINUE NEXT` restarts the program and pauses just before the iteration that would complete the current loop.
- `RETURN CLEAR` clears the most recent return stack entry including `FOR ... NEXT` state; `RETURN CLEAR ALL` clears all return stack entries.

### See also (FOR loops)

`BREAK`, `CONTINUE`, `CONTINUE NEXT`, `FOR`, `RETURN CLEAR`

---

## REPEAT ... UNTIL and WHILE ... WEND Loops

Both `REPEAT ... UNTIL` and `WHILE ... WEND` evaluate a condition expression on every pass. The condition follows the same syntax as in `IF ... THEN` statements: a mix of numeric and alpha comparisons joined with `AND` and `OR` logical operators.

### Key difference

- **`WHILE ... WEND`** — tests the condition **before** the loop body. If the condition is false on entry, the body never executes.
- **`REPEAT ... UNTIL`** — tests the condition **after** the loop body. The body always executes at least once.

### REPEAT ... UNTIL example

```kcml
count = 0
REPEAT
    PRINT count
    count = count + 10
UNTIL count == 100
```

**Output:** `0  10  20  30  40  50  60  70  80  90`

### WHILE ... WEND example

```kcml
count = 0
WHILE count <> 100 DO
    PRINT count
    count = count + 10
WEND
```

**Output:** `0  10  20  30  40  50  60  70  80  90`

Both examples produce identical output in this case, because `count` starts at 0 (the `WHILE` condition is true on entry). If `count` were already 100, the `WHILE` loop body would not execute at all, while `REPEAT` would still run once.

### BREAK in condition-tested loops

BREAK and CONTINUE work in `WHILE` and `REPEAT` loops as well:

```kcml
WHILE count <> tmp DO
    'update()
    KEYIN char$
    IF char$ == exit_key$ THEN BREAK
    'write_screen()
WEND
```

The loop continues until `count == tmp` or until the exit key is pressed, whichever comes first.

### Infinite loops

Write an infinite loop using a condition that is always true, then use `BREAK` to exit:

```kcml
WHILE TRUE DO
    'get_next_record()
    IF FLD(rec$.accno$) == search$ THEN BREAK
WEND
```

The equivalent with `REPEAT ... UNTIL` requires a "never met" condition:

```kcml
REPEAT
    'get_next_record()
    IF FLD(rec$.accno$) == search$ THEN BREAK
UNTIL junk_var = 1E30
```

The `WHILE TRUE DO` form is generally clearer for infinite loops.

### Mixed condition example

```kcml
WHILE xpos < xt OR ypos < yt AND tmp$ <> " " DO
    REM loop body
WEND
```

Conditions may mix numeric and alpha comparisons in a single expression.

### Nesting and limits

Both `REPEAT ... UNTIL` and `WHILE ... WEND` may be nested. Each `REPEAT` must be paired with its `UNTIL`, and each `WHILE` must be paired with its `WEND`. Pairing is verified at resolve time. The nesting depth limit is typically 20.

The `LIST` statement automatically indents loop bodies for readability.

Neither `REPEAT` nor `WHILE` uses the return stack at execution time, so `LIST RETURN` does not show these loops.

---

## Notes

- Prefer `BREAK` over `GOTO` for early loop exit. `GOTO` out of a loop leaves state on the return stack.
- If early exit must set the index variable to force the loop to terminate via its normal condition, set it to the termination value and execute the `NEXT` statement.
- `CONTINUE LOOP` is available to skip to the next iteration of an *outer* enclosing loop when inside nested loops.
- The maximum nesting depth for `FOR` loops may vary by platform but is typically at least 20.

## See Also

- `FOR` — counted loop statement
- `REPEAT ... UNTIL` — post-condition loop
- `WHILE ... WEND` — pre-condition loop
- `BREAK` — exit a loop
- `CONTINUE` — skip to next iteration
- `CONTINUE LOOP` — skip to next iteration of outer loop
- `CONTINUE NEXT` — debugger resume tool for `FOR` loops
- `RETURN CLEAR` — clear return stack entries
- `LIST RETURN` — inspect the return stack
