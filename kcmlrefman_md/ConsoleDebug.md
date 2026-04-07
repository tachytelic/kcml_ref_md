# Debugging Programs from the Console

> Guide to debugging KCML programs in text terminal (non-Workbench) environments.

## Overview

For terminals that do not support the KCML Workbench, a line editor and immediate-mode debugger is available. When a runtime error halts a program, the error line and code are displayed. Execution can then be examined or resumed from the prompt.

---

## Halting Execution

### STOP

`STOP` halts the program and returns to immediate mode. Useful as an assertion guard:

```kcml
ON count GOTO 1000,2000,3000
STOP "Invalid option"
```

`RUN STOP` resolves the program and stops before any line executes (useful for catching resolve-time errors).

`STOP PANIC ON` / `STOP PANIC OFF` — makes all subsequent `STOP` statements behave as `PANIC`.

### PANIC

`PANIC` writes a snapshot of the program state to a file in the current directory, then exits KCML. The panic file contains screen contents, login name (Unix), terminal number, and output of `LIST RETURN`, `LIST DIM`, `LIST DT`.

File naming: `panicPPPP` (Unix, where PPPP = process ID) or `PANlllll` (DOS).

Override the output directory with the `PANICDIR` environment variable.

### TRAP

`TRAP` sets a breakpoint on a line/statement, variable, or subroutine label:

```
TRAP 100,5          — break before line 100 statement 5
TRAP name$          — break when variable name$ is executed
TRAP 'get_next_record  — break before subroutine runs
```

Re-issuing the same `TRAP` removes it (toggle). `TRAP OFF` removes all foreground traps; `@TRAP OFF` removes global traps; `TRAP ALL OFF` removes both.

Prefix with `@` for global partition traps:

```
@TRAP 100,5
@TRAP 'get_next_record
```

#### TRAP with conditional watchpoints

```
TRAP name$ : IF name$ = "Steve" THEN STOP
TRAP tp$ : IF tp$ = "A" THEN GOSUB 9000 : count++
```

Trailing statements execute whenever the trap fires; `STOP` is only reached if the condition is true.

`LIST TRAP` shows all active traps.

---

## Inspecting State

Once in immediate mode:

| Command | Purpose |
|---------|---------|
| `PRINT var` | Display a variable's current value |
| `LIST DIM` | List all variables and their contents |
| `LIST` | Display program text in memory |
| `LIST CALL` | Show all CALL references |
| `LIST DT` | Show device table |
| `LIST RETURN` | Show subroutine return stack |
| `$PROG` | Name of the last program loaded |
| `#LINE` | Line number currently executing |
| `#STAT` | Statement number within the current line |

---

## Resuming Execution

| Command | Effect |
|---------|--------|
| `CONTINUE` | Resume from the next statement |
| `CONTINUE LOAD` | Resume; break before first statement after next `LOAD` |
| `CONTINUE LOOP` | Resume; break before next `WEND`/`UNTIL` |
| `CONTINUE NEXT` | Resume; break before next `NEXT` |
| `CONTINUE RETURN` | Resume; break after next `RETURN` |
| `GOTO line` | Jump to a specific line and continue |

---

## See Also

- `STOP` — halt execution (resumable)
- `PANIC` — dump state and exit
- `TRAP` — set breakpoints
- `CONTINUE` (command) — resume execution
- `ERROR` / `ON ERROR` — trap recoverable runtime errors
