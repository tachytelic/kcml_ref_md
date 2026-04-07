# LIST DC

> Lists files in a platter image or native OS directory, with optional wildcard filtering.

## Syntax

```
LIST [title] DC [#stream] [pattern] [W]
```

| Element | Description |
|---------|-------------|
| `#stream` | Stream number; defaults to `#0` |
| `pattern` | Optional filename pattern with `*`, `?`, `[...]` wildcards |
| `W` | Wide format: filenames in columns |

## Description

Lists files similar to `ls -alR` on Unix. For native OS files the output matches `ls -alR` (can be changed with the `LISTDCT` environment variable). For DOS/Windows, `LISTDCT` is ignored.

### Wildcards

| Pattern | Matches |
|---------|---------|
| `*` | Any string (including empty) |
| `?` | Any single character |
| `[abc]` | Any of a, b, c |
| `[1-9]` | Any digit 1–9 |

## Examples

```kcml
LIST DC "SL/P*"          REM files in SL/ starting with P
LIST DC "??/FILE2"       REM FILE2 in any two-char subdirectory
LIST DC "ABC/DEF[1-9]"   REM ABC/DEF1 through DEF9
LIST DC #14 W            REM stream 14, wide format
```

## See Also

- `SELECT LIST` — redirect output
- `LIST` — list program source
