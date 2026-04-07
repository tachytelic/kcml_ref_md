# REPEAT ... UNTIL

> Repeats a block of statements until a condition becomes true, testing the condition after each iteration so the body always executes at least once.

## Syntax

```
REPEAT
    ...
UNTIL condition
```

| Element | Description |
|---------|-------------|
| `condition` | A boolean expression evaluated at the end of each iteration. The loop exits when this is true. |

## Description

`REPEAT ... UNTIL` forms a post-condition loop. The body executes first, then `condition` is evaluated. If the condition is false, the loop repeats. If it is true, execution continues with the statement after `UNTIL`.

**The body always executes at least once**, regardless of the initial state of the condition. This is the key distinction from `WHILE ... WEND`, which tests the condition before the first iteration and may skip the body entirely.

Each `REPEAT` must be paired with a `UNTIL` statement. Pairing is verified at resolve time. The KCML editor automatically indents the loop body. REPEAT loops may be nested to a depth of at least 20.

The return stack is not used at execution time, so `LIST RETURN` does not list these loops.

## Parameters / Clauses

### condition

The condition is any valid KCML boolean expression using the same rules as `IF` conditions: numeric comparisons, string comparisons, logical operators (`AND`, `OR`, `XOR`), and the special `END` keyword for end-of-file detection.

The condition is evaluated after each iteration. Post-increment or post-decrement operators inside the condition are common:

```kcml
UNTIL count++ < 100
```

### BREAK and CONTINUE

Jumping into or out of `REPEAT` loops with `GOTO` is permitted but is very poor practice. Use the structured alternatives:

| Statement | Effect |
|-----------|--------|
| `BREAK` | Exits the loop immediately; execution continues after `UNTIL` |
| `CONTINUE` | Skips the rest of the loop body and jumps to re-evaluate the `UNTIL` condition |

## Examples

### Loop with BREAK and CONTINUE

```kcml
REPEAT
    IF (count == temp)
        BREAK
    END IF
    IF (MOD(count,5) == 0)
        CONTINUE
    END IF
    'Adjust(count)
UNTIL count++ < 100
```

- `'Adjust(count)` is called only when `count` is not a multiple of 5.
- The loop exits early if `count` equals `temp`.
- Otherwise the loop exits when `count` reaches or exceeds 100 (checked after the post-increment).

### Read until end of file

```kcml
REPEAT
    READ #stream, record$
    IF (END)
        BREAK
    END IF
    'Process(record$)
UNTIL FALSE
```

Reads records continuously until end of file is detected. `UNTIL FALSE` makes the condition always false so the loop only exits via `BREAK`.

### Simple prompt loop

```kcml
REPEAT
    INPUT "Enter a value (0 to quit): ", val
UNTIL val == 0
```

Always prompts at least once. Exits when the user enters 0.

## Notes

- Unlike `WHILE ... WEND`, the body of a `REPEAT ... UNTIL` loop always executes at least once.
- The condition at `UNTIL` exits the loop when **true** — the opposite of `WHILE`, which continues while true.
- Operators like `++` and `--` in the `UNTIL` condition are evaluated as part of the condition check, after the loop body.
- The return stack is not involved, so no `RETURN CLEAR` is needed after breaking out of a `REPEAT` loop.
- Nesting depth is at least 20.

## See Also

- `WHILE ... WEND` — pre-condition loop (body may be skipped if condition is initially false)
- `BREAK` — exit a loop early
- `CONTINUE` — skip to the `UNTIL` condition re-evaluation
- `FOR ... NEXT` — counted loop
- `CONTINUE LOOP` — skip to the next iteration of an outer loop
