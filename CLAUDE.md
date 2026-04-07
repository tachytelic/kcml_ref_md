# CLAUDE.md — KCML Reference Documentation

## Project Purpose

This repo is a Claude Code skill and reference system for **KCML** (Kerridge Computer Macro Language), a 4GL descended from Wang BASIC-2. The goal is to build a coding assistant that can write, test, and iteratively improve KCML code by executing it on a live KCML server over SSH.

The core workflow is:
1. User asks for KCML code help
2. Claude references the skill and reference docs to write correct code
3. Claude executes the code on the KCML server to verify it works
4. Claude updates the references when new patterns or behaviours are discovered

---

## Execution — Always Use SSH/SCP

The canonical method for running KCML code is SCP + SSH. This avoids all shell escaping issues.

```powershell
# Quickest: use the helper script
.\kcml_executor\run_kcml.ps1 -Code 'PRINT "Hello" : $END'
.\kcml_executor\run_kcml.ps1 -File .\mytest.kcml
```

Manual method (if needed):
```powershell
# 1. Write code to a temp file
[System.IO.File]::WriteAllText("$env:TEMP\test.kcml", 'DIM x : x = 42 : PRINT x : $END')

# 2. SCP to server
& "C:\Windows\System32\OpenSSH\scp.exe" -q -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa "$env:TEMP\test.kcml" interpartuk@10.1.1.213:/tmp/test.kcml

# 3. Execute
& "C:\Windows\System32\OpenSSH\ssh.exe" -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa interpartuk@10.1.1.213 "/usr/lib/kcml/kcml -p /tmp/test.kcml"
```

**Server:** `interpartuk@10.1.1.213` — Ubuntu 8.04, legacy SSH algorithms required, key auth (passwordless).

---

## Repository Structure

```
.github/skills/kcml-coding/
  SKILL.md                  # Main skill prompt — quick reference + execution guide
  references/               # Detailed topic references
    data-types.md
    arrays-variables.md
    control-flow.md
    string-functions.md
    numeric-functions.md
    date-functions.md
    file-io.md
    error-handling.md
    subroutines.md
    print-input.md
    operators.md
    screen-io.md            # Screen, windows, PRINT AT, KEYIN, menus
    com-chaining.md         # COM variables and LOAD/CHAIN program linking

kcmlrefman/                 # Full language reference (converted from HTML help)
kcml_executor/              # Python execution server + PowerShell helper scripts
kcml_source/PF/             # Real KCML business application source files (.Bre)
```

---

## Enriching the Skill

When Claude discovers new KCML behaviour through testing:

1. **Update the relevant reference file** in `.github/skills/kcml-coding/references/`
2. **Add patterns to SKILL.md** if they are common enough to include in the quick reference

When a tested code example reveals a quirk not in the docs, add it to the appropriate reference file with a comment like `REM Verified by execution`.

---

## Key KCML Rules (Never Get These Wrong)

- Strings **must** be DIM'd with a size: `DIM name$30` — never use a string without declaring it
- Strings are **fixed-length and space-padded** — `LEN()` returns content length excluding trailing spaces
- Arrays are **1-based**: `DIM arr(10)` gives elements 1 through 10
- Script mode (kcml -p): statements separated by `:`, continuation lines start with `: `
- Every script must end with `$END`
- Use `HEX(22)` for embedded quote characters — **not** `CHR$(34)`
- **Never put `:` in a REM statement** — KCML treats `:` as a statement separator even inside REM text, causing syntax errors. This includes URLs — `http://` breaks REM; write `http [colon] //` instead
- `DEFFN` (older syntax) and `DEFSUB`/`END SUB` (modern) both work; real source uses `DEFFN`
- Multiple assignment: `a$, b$, c$ = value` sets all variables to the same value
- `BOOL(x)` returns TRUE/FALSE from a numeric — used heavily in real code
- `ALL(HEX(xx))` fills a string with a repeated byte: `ALL(HEX(00))` = null-filled string
- `ZER` resets an array to all zeros: `arr() = ZER`
- `MAT REDIM arr(n)` resizes an array at runtime
- **DEFFORM: DEFEVENTs must be continuation lines INSIDE the DEFFORM block** — a DEFEVENT placed outside (as a separate numbered line) is not associated with the form; the form opens, does nothing, and closes silently. Use `+ DEFEVENT` with the `+` prefix inside the block. All DEFFORM blocks must be fully defined before any `.Open()` call.
- **DEFFORM: `.Open()` must assign a result** — `result = MyForm.Open()` not bare `MyForm.Open()`

---

## Source Code Reference

`kcml_source/PF/` contains real KCML business programs. Both the extensionless files and the `.Bre` files are source — they are not compiled/source pairs.

The `.Bre` extension relates to the `$SPECIAL` environment variable mechanism: when `$SPECIAL=Bre` is set for a customer, the KCML runtime loads `PROGRAM.Bre` instead of `PROGRAM` (the base version). This is how the ERP supports per-customer modifications — the `.Bre` file overrides the base program for that customer without touching the standard code. Reading both reveals real-world patterns that may not appear in the reference manual.

Key files studied:
- `MENU.Bre` — menu structure, LOAD, DATA statements, DEFFN, MAT REDIM
- `MUP.Bre` — full CRUD maintenance program, screen display, field definitions
- `DISP.Bre` — stock display, PRINT AT, KEYIN, BOX, window patterns
- `START.Bre` — COM declarations, PACK/UNPACK, program chaining

---

## What NOT to Do

- Do not use `CHR$(34)` — use `HEX(22)` for quotes in strings
- Do not use `INPUT` in scripts run with `kcml -p` — non-interactive, will hang
- Do not forget `$END` at the end of every script
- Do not use the HTTP server (`localhost:8765`) for complex code with subroutines — it may hang; prefer SSH
- **Never use blank lines in `kcml -p` scripts** — a blank line silently terminates execution. Use `: REM` lines for spacing. Bare `REM` (without `: ` prefix) also terminates the script mid-run.
- **Never use 4-param `KI_OPEN`** in KCML 6.x — `CALL KI_OPEN handle, stream, file$, mode$` causes an S24 panic. Use `CALL KI_OPEN handle, file$, mode$ TO status` (3 params).

## KISAM File Access (Verified Working Pattern)

Reading KISAM/KDB files from standalone scripts (KCML 06.00.88):

```kcml
: DIM ki_status, handle, ki_sym, ki_dataptr$6, ki_key$64, rec$512, count
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: CALL KI_OPEN handle, "/full/path/to/FILENAME", "R" TO ki_status
: IF ki_status <> 0 THEN $END
: CALL KI_START_BEG handle, 1 TO ki_status
: IF ki_status <> 0 THEN $END
: ki_sym = SYM(rec$)
: count = 0
: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status == 0 THEN DO
:     count++
:     PRINT "Key: ["; STR(ki_key$, 1, 20); "]"
:     PRINT "Rec: ["; STR(rec$, 1, 60); "]"
:   END DO
: UNTIL ki_status <> 0 OR count >= 10
: CALL KI_CLOSE handle TO ki_status
: $END
```

## Packed Date Format (OEHDR01 and likely all files)

Type `D`, 4-byte fields store dates as 4 binary-coded bytes that HEXUNPACK reveals as `YYYYMMDD`. To display as DD/MM/YYYY:

```kcml
: DIM hex$12, date$10
: HEXUNPACK STR(rec$, 82, 4) TO hex$
: date$ = STR(hex$, 7, 2) & "/" & STR(hex$, 5, 2) & "/" & STR(hex$, 1, 4)
```

## KISAM File Access (Verified Working Pattern)

Key facts:
- Connection 1 is auto-created as KISAM on script start — no `KI_ALLOC_CONNECT` needed
- `KI_ALLOC_HANDLE 0, 1` = auto-allocate handle on KISAM connection 1
- `ki_dataptr$` must be 6 bytes
- Pre-assign `ki_sym = SYM(rec$)` — do not pass `SYM()` inline to `KI_READ_NEXT`
- Status 2 = EOF (normal), 0 = success, 1 = not found
- `CALL KI_START handle, key$, path TO status` — key$ before path in KCML 6.x (libKI has them reversed)

## Conditional $END Pattern

`IF condition THEN action : $END` — the `:` is a TOP-LEVEL separator so `$END` fires unconditionally. Only one statement binds to `THEN`. Always use TWO separate IF lines:

```kcml
: IF ki_status <> 0 THEN PRINT "<error>"
: IF ki_status <> 0 THEN $END
```

When an operation between the error print and `$END` resets `ki_status` (e.g. `KI_CLOSE`), use a flag:

```kcml
: IF ki_status == 0 THEN read_ok = 1
: IF read_ok == 0 THEN PRINT "<error>"
: IF read_ok == 0 THEN CALL KI_CLOSE handle TO ki_status
: IF read_ok == 0 THEN $END
```
