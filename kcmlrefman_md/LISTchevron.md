# LIST <<

> Lists all multi-language string definitions (strings enclosed in `<<` and `>>`).

## Syntax

```
[@]LIST [title] << [*]
```

With `*`: lists the full statements containing language strings.
Without `*`: lists only the line numbers.

```
LIST <<*
01010 :: lang$ = <<"Total">>
09000 :: $IMAGE = <<"$######.##">>

LIST <<
01010  09000
```

## See Also

- `LIST` — overview of LIST commands
- `KLANG` — environment variable for default language
