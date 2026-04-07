# tik — TERMINFO/GPDINFO Compiler

> Compile TERMINFO source files into terminal definition files.

## Syntax

```
tik [-vmb] [-p] [-t termname] source_file
```

## Description

`tik` converts a text source file into individual TERMINFO keyboard/screen definition files (or GPDINFO printer definition files) in the same directory as the source. The source file is free-format text, conventionally named `TERMINFO/src`.

Each section in the source starts with `[sectionname]`. The section name corresponds to the `KTERM` environment variable value used by KCML. Multiple names for the same terminal can be listed separated by `|`, e.g. `[wyse30|wyse50]`. UNIX symlinks are created for alternative names.

KCML searches its `PATH` for `TERMINFO/kterm_name` to find the compiled file.

## Typical usage

```sh
tik /usr/lib/kcml/TERMINFO/src
```

This compiles all sections and leaves the definition files in `/usr/lib/kcml/TERMINFO/`.

## Options

| Option | Description |
|--------|-------------|
| `-b` | Generate NPL-type `$KEYBOARD` files from source |
| `-m` | Merge descriptions from Unix `/usr/lib/terminfo` into the source |
| `-p` | Compile GPDINFO (printer) database instead of TERMINFO |
| `-v` | Verbose mode |
| `-t termname` | Export a minimal Unix terminfo description for `termname` to stdout, suitable for appending to a KCML TERMINFO/src file |

## Adding a new terminal type

```sh
tik -t $TERM >> /usr/lib/kcml/TERMINFO/src
tik /usr/lib/kcml/TERMINFO/src
```

This adds a minimal description from the Unix terminfo database. Missing capabilities can be added by hand with an editor.

## See Also

- `tiklist` — list a compiled TERMINFO file in ASCII
- `TextTermIntro` — text terminal overview
- `TextTermGrammar` — TERMINFO source file format
