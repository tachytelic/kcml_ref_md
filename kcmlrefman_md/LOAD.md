# LOAD

> Loads a KCML program segment into memory and executes it. Clears non-common variables and the return stack.

## Syntax

```
LOAD [#stream | /device,] program_name [start_line [, end_line]] [BEG line]
LOAD [#stream | /device,] <num_expr> program_names$
LOAD [#stream | /device,] <str_expr> program_names$
```

| Element | Description |
|---------|-------------|
| `program_name` | Name of program to load |
| `start_line`, `end_line` | Range of lines to clear before loading |
| `BEG line` | Start execution at this line (default: first line) |
| `<num_expr>` | Number of programs to load (names are 8-char space-padded in the variable) |
| `<str_expr>` | Delimiter character for multi-program names (KCML 6.0+) |

## Description

`LOAD` clears non-common variables and the return stack, loads the specified program, and begins execution.

### Line range clearing

| Syntax | Lines cleared before load |
|--------|--------------------------|
| `LOAD "PROG"` | All lines |
| `LOAD "PROG" 5000` | Lines from 5000 to end |
| `LOAD "PROG" 1000,2000` | Lines 1000–2000 |

If `end_line < start_line`, no lines are cleared.

If no device is specified, the directory selected to stream `#0` is used.

### Multi-program load

```kcml
COM programs$16
programs$ = "PROG001 PROG002"
LOAD #27, <2> programs$       REM load 2 programs; names are 8-char padded

LOAD <","> "file1,../specials/file2"   REM delimiter form (KCML 6.0+)
```

The whole merged program is resolved only after all segments are loaded. Error recovery only works during the first program load.

### $OPTIONS RUN behaviour

`$OPTIONS RUN` byte 46 controls whether `.src` extension is appended and whether source or compiled files are preferred.

## Examples

```kcml
LOAD "MAINMENU"
LOAD #27, "SL/pmenu" 10000,19999
LOAD "STARTUP" BEG 1000
```

## Notes

- `LOAD` is the primary mechanism for program chaining in KCML — equivalent to `CHAIN` in some BASICs.
- COM variables survive a `LOAD`; all other variables are cleared.
- For clean start, use `LOAD RUN`.

## See Also

- `LOAD RUN` — clear everything and load/run
- `LOAD ASCII` — load an ASCII script file
- `SAVE` — save a program
- `COM` — common variables that survive LOAD
