# LOAD ASCII

> Workbench command: loads and compiles an ASCII source file into memory, merging it with the current program.

## Syntax

```
LOAD ASCII strexpr
```

## Description

`LOAD ASCII` is an **immediate-mode command** (not programmable). It reads an ASCII source file and merges it into the program in memory, executing any immediate-mode statements in the file line by line as it reads them.

File is searched in the current working directory. Full Unix/DOS paths may be used.

The command is roughly equivalent to redirecting keyboard input from a file (`SELECT CI`). Useful for running rename/edit scripts against the program in memory.

Do **not** use `RUN`, `LOAD` (of another ASCII program), `$COMPILE`, or `LOAD ASCII` inside such scripts.

## Example

Script file `map`:
```
RENAME EACH$ TO RECORD$
RENAME QUICK$ TO WORK$
RENAME '100 TO 'GET_NEXT_RECORD
```

Then in the Workbench:
```
LOAD ASCII "map"
```

This executes each RENAME command against the currently loaded program.

## Notes

- Since KCML 3.0, `LOAD` itself can load ASCII source files directly — `LOAD ASCII` is largely obsolete.
- Cannot be used programmatically.

## See Also

- `LOAD` — load a program (also handles ASCII source since KCML 3.0)
- `SAVE ASCII` — save a program as ASCII source
