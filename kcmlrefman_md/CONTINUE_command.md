# CONTINUE (command)

> Resumes execution of a program that was stopped by `STOP`, `TRAP`, or a Ctrl+Break interrupt.

## Syntax

```
CONTINUE
```

## Description

The `CONTINUE` command restarts a halted program from where it stopped. The program must be in a stopped (but resolved) state — caused by:
- A `STOP` statement
- A `TRAP` statement
- A Ctrl+Break interrupt

It is not possible to resume execution of an unresolved program.

In the KCML Workbench, `CONTINUE` can be executed as a single keystroke or from the toolbar.

**Note:** `CONTINUE` entered within an immediate-mode loop (inside a `FOR`, `WHILE`, or `REPEAT`) is treated as this command rather than the loop-control `CONTINUE` statement.

## Variants

| Command | Effect |
|---------|--------|
| `CONTINUE` | Resume from the next statement after the stop point |
| `CONTINUE LOAD` | Resume and stop again just before the first statement after the next `LOAD` |
| `CONTINUE LOOP` | Resume and stop before the next `WEND` or `UNTIL` |
| `CONTINUE NEXT` | Resume and stop before the `NEXT` at the end of the current `FOR` loop |
| `CONTINUE RETURN` | Resume and stop after the next `RETURN` from the current `GOSUB` |

These variants are debugging stepping aids, typically used from the Workbench.

## See Also

- `STOP` — halt program execution (resumable)
- `TRAP` — error-trap that stops execution
- `CONTINUE LOAD` — resume and break before next LOAD
- `CONTINUE LOOP` — resume and break before next WEND/UNTIL
- `CONTINUE NEXT` — resume and break before next NEXT
- `CONTINUE RETURN` — resume and break after next RETURN
