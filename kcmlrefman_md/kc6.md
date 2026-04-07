# kc6 — KCML Library Compiler

> Compile multiple KCML source programs into a single library.

## Syntax

```
kc6 [-s] [-v] -o library [-i import] prog1 [prog2 ...]
```

## Description

`kc6` takes one or more KCML source file components and combines them into a generated library (equivalent to `SAVE <G>`). It is normally invoked by KMake, not directly.

`kc6` loads the KCML interpreter from `kserver.dll` (NT), `kserver.sl` (HP-UX), or `kserver.so` (Linux/Unix).

## Options

| Option | Description |
|--------|-------------|
| `-s` | Silent — suppress progress reports to stdout |
| `-v` | Print version number and exit |
| `-o library` | **Required.** Filename of the library to create |
| `-i import` | Import a dependency library (may be specified multiple times) |
| `-?` | Print usage message |

## `-i` import flag

Specifies another library that the new library depends on. The imported library must already exist and is loaded before the new library is resolved and saved, so constants and fields get their correct values. Multiple `-i` flags are processed in order. The list of imported libraries is saved in the new library's header.

## Notes

### Line numbers

Each source file has its own line number space. The combined library retains the original line numbers — a `GOTO` target must exist in the same source file. This means the Workbench can map a library line back to its source file.

### Source file information

Source file information is embedded in the library. From the Workbench, pressing a keystroke on a library line loads the corresponding source file with the cursor at the same location.

### Constructors

If any source file has a `'Constructor` subroutine, `kc6` renames each one and creates a new composite `'Constructor` that calls all of them. This is invoked automatically by `LIBRARY ADD`.

### Assumptions

- All libraries are created with `$COMPLIANCE 1`.
- All ASCII source files use text source conventions.
- Numeric variables with a leading `_` are treated as constants; dependent libraries are searched for definitions.

## See Also

- `kmake` — build utility that invokes `kc6`
- `compile` — compile individual programs
- `LIBRARY ADD` — load a library at runtime
