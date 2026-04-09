# $ARG(

> Returns a command-line argument passed to KCML at startup.

## Syntax

```
alpha_receiver = $ARG(param_num)
```

## Description

`$ARG(` returns command-line parameters that were passed when KCML was launched. `param_num` is zero-based:

- `$ARG(0)` — the first non-switch parameter (typically the program name or script path)
- `$ARG(1)` — the second parameter, and so on

KCML absorbs its own switches (parameters starting with `-`) before counting, so `$ARG(0)` is always the first user-visible parameter regardless of how many KCML switches precede it.

```bash
kcml -g START 'DIR=/user1/data'
```

In this example:
- `$ARG(0)` → `START`
- `$ARG(1)` → `DIR=/user1/data`

Negative numbers or indices beyond the number of supplied parameters return a blank string.

`$ARG(` is valid wherever an alpha function is legal.

## Examples

### Example 1 — Read script path (ARG 0)
```kcml
01000 REM Show the script path passed as ARG(0)
: DIM arg0$100
: arg0$ = $ARG(0)
: PRINT "Script: " ; RTRIM(arg0$)
: $END
```
**Output** (when run as `kcml -p /tmp/test.kcml`):
```
Script: /tmp/test.kcml
```

### Example 2 — Read a named parameter
```kcml
01000 REM Parse a DIR= parameter from command line
: DIM param$100, dir$80
: param$ = $ARG(1)
: IF RTRIM(param$) == "" THEN PRINT "No parameter supplied"
: IF RTRIM(param$) <> "" THEN PRINT "Param 1: " ; RTRIM(param$)
: $END
```
**Output** (when run with no extra args):
```
No parameter supplied
```

### Example 3 — Use ARG to select a mode at startup
```kcml
01000 REM Launch program in batch or interactive mode based on arg
: DIM mode$20
: mode$ = $ARG(1)
: IF RTRIM($UPPER(mode$)) == "BATCH" THEN PRINT "Running in batch mode"
: IF RTRIM($UPPER(mode$)) <> "BATCH" THEN PRINT "Running interactively"
: $END
```

## Notes

- `$ARG(0)` when using `-p` script mode returns the script path, not a program name.
- KCML treats `$ARG(0)` as the initial program to run when starting normally (not `-p`). The first parameter is interpreted by KCML itself; subsequent ones are for the program.
- Returns blank (not an error) for out-of-range indices.
