# LIST T

> Searches for text in the program source. Case-insensitive; spaces in the pattern are ignored.

## Syntax

```
[@]LIST [title] T[*] "text"
```

## Description

Case-insensitive text search. Embedded spaces in the pattern are ignored. `@` searches the selected global partition. Only one text string per search.

With `*`: lists full statement text.

```
LIST T* "FOR"
00010 FOR count=1 TO length
09000 :::FOR z=1 TO 50

LIST T "FOR"
00010 09000 09000
```

## Examples

```kcml
LIST T "Fred"
LIST T AARDVARK$(1)
@LIST T* "Returning"
```

## Notes

- For case-sensitive regex search, use `LIST P`.
- Best done via the Workbench search dialog.

## See Also

- `LIST P` — case-sensitive regex search
- `LIST V` — find variable references
