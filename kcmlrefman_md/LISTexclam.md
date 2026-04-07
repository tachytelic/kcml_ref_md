# LIST !

> Lists line numbers (or full text) of lines that contain syntax errors.

## Syntax

```
LIST [title] ! [*]
```

With `*`: lists the erroneous lines in full.
Without `*`: lists only line numbers.

```
LIST !*
00010 PRINT"TESTING

LIST !
00010
```

Programs can be saved with syntax errors. When the program is LISTed, erroneous lines are not structured and have a `!` prefix on the line number.

## See Also

- `LIST L` — check for structural/loop errors
- `LIST` — list program source
