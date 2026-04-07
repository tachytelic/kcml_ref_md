# LIST V

> Finds all references to a variable (or all variables) in the program source.

## Syntax

```
[@]LIST [title] V[*] [variable | pattern]
[@]LIST [title] V COM [variable | pattern]
[@]LIST [title] V DIM [variable | pattern]
```

| Element | Description |
|---------|-------------|
| `@` | Search the selected global partition |
| `*` | List full statement text for each reference |
| `COM` | Only variables referenced in the foreground partition (COM form), in LIST DIM format |
| `DIM` | Same as COM form |

## Description

Without arguments, lists all variables. With a name, finds all references to that variable. With `*`, shows the full source line for each reference.

```
LIST V* new$
new$
     -  01010 ::'Create(new$)
     -  21000 :::MAT REDIM new$(256)nw

LIST V new$
NEW$
     -  01010 21000
```

For arrays, only the opening `(` is needed: `LIST V arr(`.

Accepts the same wildcard patterns as `LIST DIM`.

## Examples

```kcml
LIST V
@LIST V * new_variable$(
LIST V COM type$
```

## See Also

- `LIST DIM` — show variable values (pattern matching rules)
- `LIST P` — search by regex pattern
