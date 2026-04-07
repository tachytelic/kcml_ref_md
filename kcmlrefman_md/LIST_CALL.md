# LIST CALL

> Finds all references to `CALL` routines (user-written C functions) in the program.

## Syntax

```
[@]LIST [title] CALL [*] [callname]
```

| Element | Description |
|---------|-------------|
| `@` | Search in the currently selected global partition |
| `*` | List full statement text (not just line numbers) |
| `callname` | Specific CALL to search for; omit to list all |

## Description

Without `*`, outputs just the line numbers where the CALL appears. With `*`, outputs the full line with leading colons marking the CALL's position within multi-statement lines.

```
LIST CALL * KI_CLOSE
KI_CLOSE    - 00010 CALL KI_CLOSE handle TO ki_status
            - 00900 ::CALL KI_CLOSE f_hndl TO ret

LIST CALL KI_CLOSE
KI_CLOSE    - 00010 00900
```

## Examples

```kcml
LIST CALL
@LIST CALL *
LIST CALL * GETDATE
@LIST CALL NEWSUB
```

## See Also

- `CALL` — call a user-written C routine
- `LIST U` — list available CALL routines
