# LIST #

> Cross-references line numbers — shows which lines reference a given line number.

## Syntax

```
[@]LIST [title] # [*] [start_line [,]] [, end_line]
```

## Description

Shows each referenced line followed by the lines that reference it. Non-existent lines are shown in parentheses.

```
LIST #
 2020 - 04000 05000 07000 09020
 5000 - 00010 00050
(6000)- 00090 00010 00050
```

With `*`: also shows the full statement text for each reference.

```
LIST # * 1000
01000 REM Main routine
        - 00040 IF count==new_count THEN GOSUB 1000
        - 00100 ON test GOSUB 1000,2000,3000
```

### Line range

| Syntax | Behaviour |
|--------|-----------|
| `LIST #` | Cross-reference all lines |
| `LIST # 310` | Lines that reference line 310 |
| `LIST # 300,400` | Cross-reference lines 300–400 |
| `LIST # ,200` | All lines up to 200 |
| `LIST # 300,` | All lines from 300 |

## See Also

- `LIST` — overview of LIST commands
- `LIST V` — find variable references
