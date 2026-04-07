# RENAME (immediate mode command)

> Renames all occurrences of a label, variable, or object name in the program currently in memory.

## Syntax

```
RENAME label1 TO label2
RENAME variable1 TO variable2
RENAME OBJECT object1 TO object2
```

## Description

**Immediate mode only** — cannot be used inside a program.

Globally renames all occurrences of the specified label, variable, or DEFFORM/object name in the in-memory program. KCML updates all references (GOTO, GOSUB, variable uses, etc.) automatically.

`RENAME OBJECT` handles `DEFFORM` names and handle objects declared with `DIM OBJECT`.

## Examples

```kcml
REM Rename a subroutine label
RENAME '66 TO 'open_file

REM Rename a variable
RENAME a1$ TO lock1$

REM Rename an array
RENAME k$() TO variable$()

REM Rename a DEFFORM
RENAME OBJECT Form1 TO OrderForm

REM Rename a SOAP object handle
RENAME OBJECT s TO SOAPsession
```

## Batch rename (multiple files)

To rename across multiple files:
1. Create an ASCII file containing the RENAME commands (one per line).
2. `LOAD` each program.
3. `LOAD ASCII filename` to execute the rename commands.

## Notes

- After `RENAME` on a halted program in the Workbench, the program is marked *unresolved* — execution cannot be resumed with CONTINUE; re-run from the start.
- Both old and new variable values are reset to defaults after a rename, even if the variable was COM-declared.
- `RENAME` will error if an attempt is made to change the variable type (e.g. global to normal variable).
- The new name must not already exist in the program (for RENAME OBJECT).
- The Workbench Search and Replace function can also perform renames.

## See Also

- `LOAD ASCII` — load and execute an ASCII command file
- `RENUMBER` — renumber program lines
