# SAVE ASCII

> Saves the in-memory program as a text (ASCII) source file.

## Syntax

```
SAVE ASCII filename [, start_line [, end_line]]
```

## Description

**Immediate mode command** — saves the program in a human-readable text format (similar to `LIST D` output). The file is always overwritten if it already exists (no `D83` error, unlike `SAVE`).

Files are created in the current working directory regardless of any `SELECT #0` or `SELECT DISK` setting, but full paths are allowed.

The output can be loaded back with `LOAD ASCII`.

Line range parameters save only the specified lines.

## Examples

```kcml
SAVE ASCII "/tmp/PROG.asc"
SAVE ASCII "temp_file.asc"
SAVE ASCII "myprog.src", 100, 5000   : REM  lines 100–5000 only
```

## Notes

- `SAVE ASCII` always overwrites — unlike `SAVE` which errors if the file exists.
- The text format includes line numbers, colons as statement separators, and REM statements.
- For the newer `.src` format (optional line numbers, optional colons), configure `$OPTIONS RUN` byte 46 — see `NEWASCII`.
- Use `SAVE ASCII` for exporting to source control or text editors.

## See Also

- `LOAD ASCII` — load and execute an ASCII command/program file
- `SAVE` — save in compiled binary format
- `NEWASCII` — new text source format (`.src`)
