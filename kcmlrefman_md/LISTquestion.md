# LIST ?

> Lists non-common variables that appear only once in the program — likely unused or misspelled.

## Syntax

```
[@]LIST [title] ? [*]
```

With `*`: shows the full statement for each single-occurrence variable.

```
LIST ?*
NEW_RECORD$
     -  01010 :: GOSUB'create(new_record$)

LIST ?
NEW_RECORD$  -  01010
```

## Notes

Single-occurrence non-common variables are either genuinely unused (dead code) or misspellings of another variable name. Reviewing this list helps catch bugs.

## See Also

- `LIST V` — find all references to a variable
- `LIST DIM` — list all dimensioned variables
