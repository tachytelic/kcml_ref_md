# FOR ... TO ... NEXT

> Executes a block of statements a fixed number of times, counting an index variable from a start value to an end value with an optional step.

## Syntax

```
FOR index_variable = expression_1 TO expression_2 [STEP expression_3]
    ...
NEXT index_variable
```

| Element | Description |
|---------|-------------|
| `index_variable` | Numeric variable used as the loop counter |
| `expression_1` | Initial value assigned to `index_variable` when the loop starts |
| `expression_2` | The limit value; the loop continues while `index_variable <= expression_2` (or `>=` for negative step) |
| `expression_3` | Optional step increment; defaults to `1` if omitted. May be negative for counting down. |

## Description

When the `FOR` statement is first executed, `index_variable` is set to the value of `expression_1`. The loop body executes. When the corresponding `NEXT` is reached, `index_variable` is incremented by the step (default `1`) and compared to `expression_2`:

- If the step is positive and `index_variable <= expression_2`, the loop repeats.
- If the step is negative and `index_variable >= expression_2`, the loop repeats.
- Otherwise execution continues with the statement after `NEXT`.

**The loop body is always executed at least once**, even if `index_variable` already exceeds `expression_2` when the `FOR` is first reached.

Multiple `NEXT` statements can be listed after a comma to close nested loops in a single statement (see examples).

FOR loops may be nested. The KCML editor automatically indents the body of `FOR` loops, provided every `FOR` has a paired `NEXT` at resolve time.

## Parameters / Clauses

### STEP

When `STEP expression_3` is included, `index_variable` is incremented (or decremented) by `expression_3` each iteration instead of by `1`. A negative step causes the loop to count down:

```kcml
FOR Count = 10 TO 1 STEP -1
    ...
NEXT Count
```

A fractional step is also valid:

```kcml
FOR Loop2 = first_5 TO last_5 STEP 0.5
```

### BREAK and CONTINUE

Jumping out of a `FOR` loop with `GOTO` is permitted but is poor practice and can cause stack overflow errors. Use the structured alternatives instead:

| Statement | Effect |
|-----------|--------|
| `BREAK` | Exits the loop immediately; execution continues after `NEXT` |
| `CONTINUE` | Skips the rest of the loop body and moves to the next iteration |

## Examples

### Nested loops with combined NEXT

```kcml
FOR Count1 = 10 TO 1 STEP -1
    FOR Count2 = 1 TO 100
        CONVERT INT(RND(1)*1000) TO Abc$,(####)
        .KCMLGrid1.MoveCell(Count2, Count1)
        .KCMLGrid1.Cell.Text$ = Abc$
    NEXT Count2, Count1
```

Counts `Count1` from 10 down to 1 and `Count2` from 1 to 100 in the inner loop. The `NEXT Count2, Count1` closes both loops.

### Using BREAK and CONTINUE

```kcml
FOR Count = pos1 TO pos2
    CONVERT Count TO Text$,(####)
    .static1.Text$ = Text$
    IF Count>50 AND Count<80 THEN CONTINUE
    IF Count>100 THEN BREAK
    'Update_Record()
NEXT Count
```

The subroutine `'Update_Record` is called only when `Count` is not between 51 and 79. When `Count` exceeds 100 the loop exits entirely.

### Simple counting loop

```kcml
FOR Loop = 1 TO last_record
    ...
NEXT Loop
```

### Counting down with step

```kcml
FOR Count = last TO first STEP -5
    ...
NEXT Count
```

## Notes

- The loop body always executes at least once, regardless of whether the initial value already exceeds the limit.
- Jumping **into** a `FOR` loop with `GOTO` causes an error at the `NEXT` statement if the loop has not previously been entered at least once.
- Jumping **out** of a `FOR` loop with `GOTO` leaves the loop state on the stack; use `BREAK` to exit cleanly.
- Every `FOR` must have exactly one matching `NEXT` using the same index variable; mismatches are detected at resolve time.
- Multiple nested loops can share a single `NEXT` by listing index variables separated by commas: `NEXT inner, outer`.

## See Also

- `BREAK` — exit a loop early
- `CONTINUE` — skip the rest of the current loop iteration
- `WHILE ... WEND` — condition-tested loop
- `REPEAT ... UNTIL` — post-condition loop
- `RETURN CLEAR` — clear the return stack
