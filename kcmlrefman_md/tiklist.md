# tiklist — TERMINFO File Lister

> List the contents of a compiled TERMINFO file in ASCII text form.

## Syntax

```
tiklist keyfile
```

## Description

`tiklist` lists a compiled TERMINFO file in human-readable ASCII text. The output can be used as input to `tik` for editing or conversion.

`keyfile` is the full path to the compiled TERMINFO file (typically in `/usr/lib/kcml/TERMINFO/`).

## Example

```sh
tiklist /usr/lib/kcml/TERMINFO/vt220
```

Displays the TERMINFO information for the `vt220` terminal type.

## See Also

- `tik` — TERMINFO/GPDINFO compiler
- `TextTermGrammar` — TERMINFO source format
