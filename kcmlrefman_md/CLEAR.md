# CLEAR

> Clears program text, variables, and/or device table from memory; resets the KCML environment to a known state.

## Syntax

```
CLEAR [V | N | P [start_line] [, end_line]]
```

| Form | Effect |
|------|--------|
| `CLEAR` | Full reset — clears everything (see below) |
| `CLEAR V` | Clears all variables only; program text and device table unchanged |
| `CLEAR N` | Clears non-common variables only; COM variables preserved |
| `CLEAR P` | Clears program text only; variables and device table unchanged |
| `CLEAR P start` | Removes lines from `start` to end of program |
| `CLEAR P ,end` | Removes lines from beginning up to and including `end` |
| `CLEAR P start,end` | Removes lines `start` through `end` inclusive |

Line numbers must be in the range 0–32000.

## Description

### Full CLEAR

`CLEAR` with no parameters performs a complete environment reset:

- All program text and variables are cleared from memory
- All open devices are closed
- Device table entries are cleared and reset to defaults
- `TRACE` and `TRAP` modes are turned off
- Pending `$ALARM`s are cleared
- Selected global partitions are deselected
- Trigonometric mode reverts to RADIANS
- `$PROG` variable and the program history buffer are cleared
- Screen is cleared; copyright message and KCML release number are displayed

### CLEAR V — Variables only

Removes all variables without touching the program or device table. Useful when you want to re-run a program with a fresh variable state but keep the loaded program.

### CLEAR N — Non-common variables only

Removes non-common variables (those declared with `DIM`). Variables declared with `COM` are preserved. Has no effect on the program or device table.

### CLEAR P — Program text only

Removes the specified range of program lines without affecting variables or the device table.

| Example | Effect |
|---------|--------|
| `CLEAR P` | Remove entire program |
| `CLEAR P 1020` | Remove lines 1020 and above |
| `CLEAR P ,9000` | Remove lines up to and including 9000 |
| `CLEAR P 20,900` | Remove lines 20 through 900 |

## Notes

- `CLEAR` is primarily an interactive/Workbench command. In a running program, `COM CLEAR` is the equivalent for clearing common variables.
- Be careful with bare `CLEAR` — it closes all open files and resets the whole environment.

## See Also

- `COM CLEAR` — clear common variables from within a program
- `RUN` — restart the current program (also reinitialises DIM variables)
- `TRACE`, `TRAP` — debug modes turned off by full `CLEAR`
- `$ALARM` — timed events cleared by full `CLEAR`
