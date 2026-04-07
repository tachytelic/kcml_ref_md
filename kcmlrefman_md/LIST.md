# LIST

> Displays the source code of the program currently in memory. Also the root of many Workbench diagnostic commands.

## Syntax

```
[@]LIST [title] [S][D] [start_line [,]] [, end_line]
```

| Element | Description |
|---------|-------------|
| `@` | List from the currently selected global partition |
| `title` | Optional heading (string literal or variable) |
| `S` | Unstructured format (multi-statement lines not split) |
| `D` | Combined with S: unstructured without highlighting |
| `start_line` | List from this line |
| `, end_line` | List up to this line |

## Description

`LIST` with no parameters lists the entire program in **structured form**: loops are indented (default 4 spaces, controlled by `KINDENT`), and each statement of a multi-statement line is printed on its own line.

Output can be redirected with `SELECT LIST`.

### Line range forms

| Syntax | Lists |
|--------|-------|
| `LIST` | Entire program (structured) |
| `LIST 1000` | Only line 1000 |
| `LIST 1000,` | From line 1000 to end |
| `LIST ,900` | From start to line 900 |
| `LIST 1000,5000` | Lines 1000 to 5000 |
| `LIST S 10,50` | Lines 10–50, unstructured |

## Examples

```kcml
LIST 1000
@LIST 1000,5000        REM list from global partition
LIST ,900
@LIST "test" 1000      REM with title
LIST S 10,50           REM unstructured
```

## Notes

- The KCML Workbench provides all LIST functions through its editor interface.
- `SELECT LIST` redirects output to a printer or file.
- The `@` prefix reads from the selected global partition (see `SELECT @PART`).

## Related LIST commands

| Command | Purpose |
|---------|---------|
| `LIST ADD` | Lines added/modified since load |
| `LIST CALL` | References to CALL routines |
| `LIST DC` | Directory listing |
| `LIST DIM` | All dimensioned variables |
| `LIST DT` | Device table |
| `LIST E` | ENV( variables |
| `LIST FROM'` | From start of a subroutine |
| `LIST L` | Lint/warnings (unmatched loops) |
| `LIST LOAD` | Programs currently in memory |
| `LIST LOCAL` | Local variables |
| `LIST M` | Loaded libraries/globals |
| `LIST OBJECT` | Active objects |
| `LIST P` | Regex text search |
| `LIST R` | DEFRECORD fields |
| `LIST RETURN` | Return stack / execution info |
| `LIST SPACE` | Memory usage |
| `LIST T` | Case-insensitive text search |
| `LIST TRAP` | Active TRAP breakpoints |
| `LIST U` | Available CALL routines |
| `LIST V` | Variable references |

## See Also

- `SELECT LIST` — redirect list output
- `SELECT @PART` — select a global partition
