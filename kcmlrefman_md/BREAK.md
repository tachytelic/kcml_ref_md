# BREAK

> Exits a `FOR`, `WHILE`, or `REPEAT` loop immediately, transferring control to the statement after the loop's closing keyword.

## Syntax

```
BREAK
```

## Description

`BREAK` provides an early exit from the innermost enclosing loop. Control transfers to the first statement after `NEXT` (for `FOR` loops), `WEND` (for `WHILE` loops), or `UNTIL` (for `REPEAT` loops).

`BREAK` must be physically inside the body of the loop — it cannot be inside a subroutine that is called from within the loop. The pairing of `BREAK` with its enclosing loop is checked at resolve time.

## Examples

### Exit FOR loop early

```kcml
: DIM i
: FOR i = 1 TO 10
:   IF i = 5 THEN BREAK
:   PRINT i
: NEXT i
: PRINT "after loop i="; i
: $END
```

Output:
```
 1
 2
 3
 4
after loop i= 5
```

The loop variable `i` retains the value it had when `BREAK` fired.

### Exit when condition found in WHILE loop

```kcml
WHILE new_loop < 10 DO
    IF (++new_loop = 5)
        BREAK
    END IF
    'Update()
WEND
```

### Exit on error in REPEAT loop

```kcml
: DIM status
: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO status, ki_dataptr$, ki_key$
:   IF status <> 0 THEN BREAK
:   'ProcessRecord()
: UNTIL FALSE
: $END
```

## Notes

- `BREAK` exits only the **innermost** loop. For nested loops, use a flag variable to propagate the exit outward.
- `BREAK` cannot be used inside a subroutine that is called from within the loop it is meant to exit.
- The loop variable in a `FOR` loop keeps the value it had when `BREAK` was executed.

## See Also

- `CONTINUE` — skip the rest of the current iteration and go to the next
- `FOR ... NEXT` — counted loop
- `REPEAT ... UNTIL` — post-condition loop
- `WHILE ... WEND` — pre-condition loop
