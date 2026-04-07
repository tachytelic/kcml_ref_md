# SELECT PASSWORD

> Sets a password to scramble/encrypt a KCML program saved with `SAVE <!>`.

## Syntax

```
SELECT PASSWORD
SELECT PASSWORD ! [challenge$]
```

## Description

**Immediate mode command** — prompts for a password (echoing suppressed) twice for confirmation. The password is then used for all subsequent `SAVE <!>` operations until a `CLEAR` is issued.

### Challenge/response support

`SELECT PASSWORD !` — displays a random challenge string. The program author can use `SELECT PASSWORD ! challenge$` to generate the response (prompting for the master password). This allows temporary access to scrambled programs without revealing the master password.

### Scrambled programs

- All listing, editing, and tracing is disabled.
- `Ctrl+BREAK` stops execution but only `CLEAR` and `LOAD RUN` are available.
- The workbench shows "Protected Program".
- To un-scramble: `SELECT PASSWORD` immediately after loading, entering the original password.

## Examples

```kcml
REM Set password then save scrambled
SELECT PASSWORD          : REM  prompts for password twice
SAVE <!> "MYPROG"        : REM  save encrypted
```

```kcml
REM Scripted (no prompt — next input line is the password)
REM  (via SELECT CI from a file)
```

## Notes

- The password is stored with the scrambled program file.
- `CLEAR` resets the password.
- Scrambling prevents casual inspection but is not strong cryptography.

## See Also

- `SAVE` — save a program (use `<!>` flag to scramble)
- `RESAVE` — resave with `<!>` flag
- `SELECT` — overview
