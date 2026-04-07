# TRAP (debugging command)

> Sets a conditional breakpoint on a line, subroutine, or variable.

## Syntax

```
TRAP line [, stmt]
TRAP 'subroutine
TRAP variable
TRAP variable IF condition THEN statements
@TRAP ...           (trap in global/background partition)
TRAP OFF
@TRAP OFF
TRAP ALL OFF
```

## Description

`TRAP` sets a breakpoint. When the trap fires, KCML stops and displays the line before executing it. Execution can be resumed with `CONTINUE`, `CONTINUE LOAD`, `CONTINUE LOOP`, `CONTINUE NEXT`, `CONTINUE RETURN`, or by stepping.

Traps can have optional trailing statements (executed when the trap fires) — useful for conditional breakpoints:

```kcml
TRAP record$ IF record$ = "TST123" THEN STOP
```

All statements except `GOTO` can follow a TRAP condition. If a `STOP` or `PANIC` is executed inside a TRAP trailing statement, subsequent `CONTINUE` returns to the program.

`LIST TRAP` shows all currently active traps. Reissuing an active TRAP statement toggles it off.

## Examples

```kcml
TRAP 100                         : REM  break at line 100 (foreground)
@TRAP 1000, 5                    : REM  break at line 1000, stmt 5 (global)
TRAP 'merge                      : REM  break at subroutine 'merge
@TRAP 'new                       : REM  break at global subroutine 'new
TRAP new_var$()                  : REM  break when array is referenced
TRAP OFF                         : REM  remove all foreground traps
@TRAP OFF                        : REM  remove all global traps
TRAP ALL OFF                     : REM  remove both
```

```kcml
REM Conditional trap with action
TRAP 'open_file IF file$ = "STOCK" THEN GOSUB 'reorganise : ELSE PRINT file$
```

## Notes

- There is no limit to the number of active traps.
- Traps survive `LOAD` statements.
- `@TRAP` sets traps in the background (global) partition.
- The `TRAP` command is for interactive debugging only — not for use in deployed programs.

## See Also

- `TRACE` — execution tracing
- `STOP` — unconditional halt
- `LIST TRAP` — display active traps
- `CONTINUE` — resume after trap
