# END

> Halts execution and displays an "END PROGRAM" message (interactive mode).

## Syntax

```
END
```

## Description

`END` halts execution and displays an "END PROGRAM" message. It is primarily an interactive-mode statement. After `END`, the program remains in memory but cannot be resumed with `CONTINUE`.

**`END` should not be used in application software** — users will not want to be dropped into the development environment. Use `$END` to exit the KCML session early, or `STOP` for debugging breakpoints.

`$END` terminates the KCML session itself. In `-p` (batch/script) mode, the interpreter exits naturally when it runs out of statements — `$END` is not required at the end of a script but is used to exit early (e.g. on an error condition).

The keyword `END` is also used in these compound contexts (which are unrelated to this statement):

| Context | Meaning |
|---------|---------|
| `END IF` | Close an `IF ... END IF` block |
| `END DO` | Close a `DO ... END DO` group |
| `END SUB` | Close a `DEFSUB` block |
| `END RECORD` | Close a `DEFRECORD` block |
| `END EVENT` | Close a `DEFEVENT` block |
| `END SECTION` | Close a `DEFSECTION` block |
| `IF (END)` | Test end-of-file after `READ #` |

## Notes

- `$END` exits the KCML session — useful for early exit, not required at the natural end of a `-p` script.
- Use `STOP` for debugging breaks (resumable with `CONTINUE`).
- `END` in a condition (`IF (END)`) tests EOF after `READ #` — it is unrelated to this statement.

## See Also

- `$END` — exit the KCML session (early exit from scripts)
- `STOP` — halt execution (resumable)
- `CONTINUE` (command) — resume after STOP (not after END)
