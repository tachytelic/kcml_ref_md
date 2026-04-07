# CONTINUE (loop statement)

> Skips the remaining statements in the current loop iteration and jumps to the start of the next iteration.

## Syntax

```
CONTINUE
```

## Description

`CONTINUE` is the loop equivalent of `BREAK`: instead of exiting the loop, it abandons the rest of the current iteration and re-evaluates the loop condition (for `WHILE` and `REPEAT`) or increments the counter and tests the limit (for `FOR`).

`CONTINUE` must be physically inside the body of the loop. It cannot be inside a subroutine called from within the loop. The pairing of `CONTINUE` with its enclosing loop is checked at resolve time.

**Note:** In immediate (interactive) mode, `CONTINUE` is treated as the `CONTINUE` command (resume a stopped program) rather than this loop statement.

## Example

```kcml
WHILE in_loop < 10 DO
    IF ++in_loop = 5 THEN CONTINUE
    'Update()
WEND
```

Iteration 5 skips `'Update()` and re-tests the `WHILE` condition.

### Skipping odd numbers in FOR loop

```kcml
FOR i = 1 TO 10
    IF (i MOD 2 = 1) THEN CONTINUE
    PRINT i
NEXT i
```

Prints only even numbers: 2, 4, 6, 8, 10.

## Notes

- `CONTINUE` panics (S-series error) in KCML 06.00.88 when run via `-p` script mode. It is intended for use in the interactive Workbench / compiled program environment. If you need to skip iterations in script mode, use a flag variable and `IF` instead:

```kcml
: FOR i = 1 TO 10
:   IF i = 3 THEN GOTO skip_body
:   PRINT i
:   REM (rest of loop body)
:   skip_body:
: NEXT i
```

Or restructure with an `IF ... END IF` around the body:

```kcml
: FOR i = 1 TO 5
:   IF i <> 3
:     PRINT i
:   END IF
: NEXT i
```

## See Also

- `BREAK` — exit the loop entirely
- `FOR ... NEXT` — counted loop
- `REPEAT ... UNTIL` — post-condition loop
- `WHILE ... WEND` — pre-condition loop
- `CONTINUE` (command) — resume a stopped program (different)
