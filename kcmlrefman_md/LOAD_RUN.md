# LOAD RUN

> Clears all program text and variables from memory, then loads and executes the specified program.

## Syntax

```
LOAD RUN [#stream,] [program_name]
```

If `program_name` is omitted, defaults to `START`.

## Description

`LOAD RUN` is a complete reset: clears both the program in memory and all variables (including COM variables, unlike `LOAD`), then loads and runs the named program. It is typically used to launch the initial application entry point.

## Examples

```kcml
LOAD RUN
LOAD RUN "PROG1"
```

## Notes

- Unlike `LOAD`, `LOAD RUN` also clears COM variables.
- The `START` environment variable can specify a default program to run when KCML starts.

## See Also

- `LOAD` — load preserving COM variables
- `START` — environment variable for auto-start program
