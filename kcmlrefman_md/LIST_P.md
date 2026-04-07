# LIST P

> Searches for text matching a regular expression in the program source. Case-sensitive.

## Syntax

```
[@]LIST [title] P[*] "pattern"
```

## Description

Uses Unix regex pattern matching (ed/sed/vi style). Case-sensitive; spaces are significant. `@` searches the selected global partition.

With `*`: lists full statement text with leading `:` markers showing position within multi-statement lines.

```
LIST P* "F*R"
00010 FOR count=1 TO length
09000 :::FOR z=1 TO 50
09000 ::::FOR y=2 TO 20 STEP 2

LIST P "F*R"
00010 09000
```

Special regex characters (`.`, `$`, etc.) can be escaped with `\`.

**Not supported on DOS.**

## Examples

```kcml
LIST P "Fred?"
LIST P* AARDVARK$(1)
@LIST P "NAME[23]"
```

## Notes

- For case-insensitive search, use `LIST T`.
- For variable references, use `LIST V`.
- Best done via the Workbench search dialog.

## See Also

- `LIST T` — case-insensitive text search
- `LIST V` — find variable references
