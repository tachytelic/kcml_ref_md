# GOSUB

> Calls a subroutine at a specified line number, returning to the calling statement when `RETURN` is executed.

## Syntax

```
GOSUB line_number
```

Valid in interactive program mode (numbered lines). This is the legacy form — prefer `GOSUB'` / label-based subroutines in new code.

## Description

`GOSUB` transfers execution to the subroutine beginning at `line_number`. When a `RETURN` statement is reached, execution resumes at the statement immediately after the `GOSUB`.

Each `GOSUB` pushes an entry onto the RETURN stack. `RETURN` pops it. If a program jumps out of a subroutine without executing `RETURN`, the stack entry remains, and eventually causes an **A04 stack overflow** error.

The RETURN stack is cleared by:
- `CLEAR`
- `RETURN CLEAR`
- `LOAD`

## Example

```kcml
1000 GOSUB 2000
1010 PRINT "back from sub"
1020 END
2000 PRINT "in subroutine"
2010 RETURN
```

Conditional call:
```kcml
IF act_1 <> test_1 THEN GOSUB 2020
```

## Notes

- `GOSUB` with a line number is the original Wang BASIC-2 style. It works in numbered-line program mode only.
- Prefer `GOSUB'` (label form) — it is more readable and does not require knowing line numbers.
- Every `GOSUB` must have a matching `RETURN`. Jumping out of subroutines with `GOTO` without a `RETURN` leaks stack entries.

## See Also

- `GOSUB'` — preferred label-based subroutine call
- `RETURN` — return from subroutine
- `RETURN CLEAR` — return and clear the RETURN stack
- `DEFSUB` — define a named subroutine
- `ON ... GOSUB` — conditional multi-way subroutine dispatch
