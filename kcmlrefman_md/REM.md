# REM

> Inserts a comment into a KCML program. Ignored at runtime.

## Syntax

```
REM text
REM % text     (skip a line, then print text below)
REM ? stmt     (hide a KCML statement from other BASIC-2 dialects)
// comment     (end-of-line comment; KCML 6.20+)
```

## Description

`REM` marks a comment. Execution skips the `REM` statement entirely. The comment extends from `REM` to the next **colon** or the end of the line (whichever comes first).

### CRITICAL WARNING

**Never put `:` inside a REM comment.** KCML treats `:` as a statement separator even inside REM text. A colon in a REM terminates the comment and the remaining text is parsed as another statement. This includes URLs — `http://` breaks the REM; write `http [colon] //` instead.

```kcml
: REM Bad: see http://example.com for details  ← WRONG — breaks at //
: REM Good: see http [colon]//example.com      ← OK
```

### Special forms

- `REM %` — skips a line and prints the following text in the listing.
- `REM ?` — the `REM ?` itself is ignored; the statement after `?` is executed. Used to hide KCML-specific statements from older BASIC-2 dialects.

### End-of-line comments (KCML 6.20+)

The `//` form starts a comment that extends to the end of the line including any colons. Best used with the new text format (one statement per line):

```kcml
DIM _BUFSIZE=4096    // size of input buffer
DIM buf$_BUFSIZE     // the input buffer
```

The workbench aligns `//` comments to column 40 by default (configurable via `$OPTIONS LIST` byte 6).

## Examples

```kcml
REM Beginning of program
PRINT "Hello"   : REM  this comment ends at the next colon
```

```kcml
REM % Main routine
REM  (the line above prints "Main routine" below a blank line in listings)
```

```kcml
REM ? LINPUT LINE "Exit one two three", abc
REM  (above: other dialects see REM and skip; KCML executes the LINPUT)
```

```kcml
REM In -p script mode, use REM for spacing (not blank lines)
: REM ---- section break ----
: PRINT "Next section"
```

## Notes

- In `-p` (script) mode, **blank lines silently terminate execution** — use `: REM` lines for spacing instead.
- A bare `REM` at the start of a `:` continuation line also terminates the script — always write `: REM text`.
- The `;` character can also start an end-of-line comment (NPL compatibility) but is not recommended.

## See Also

- `NEWASCII` — new text format where `//` comments work best
- `$KEEPREMS` — keep REM statements when compiling (NPL compat)
