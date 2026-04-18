# CLAUDE.md — KCML Reference Documentation

## Project Purpose

This repo is a Claude Code skill and reference system for **KCML** (Kerridge Computer Macro Language), a 4GL descended from Wang BASIC-2. The goal is to build a coding assistant that can write, test, and iteratively improve KCML code by executing it on a live KCML server over SSH.

The core workflow is:
1. User asks for KCML code help
2. Claude references the skill and reference docs to write correct code
3. Claude executes the code on the KCML server to verify it works
4. Claude updates the references when new patterns or behaviours are discovered

---

## Execution — Local KCML

KCML runs locally. Always run tests in the **foreground** — background processes leak the single-user licence (exit 107/144).

```bash
# Write script to a temp file, then run:
/usr/lib/kcml/kcml -p /tmp/test.kcml
```

No environment variables required — this is a fully licensed system.

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

kcmlrefman_md/              # Full language reference — 393 markdown files (primary reference source)
kcml_executor/              # Python execution server + PowerShell helper scripts
```

---

## Enriching the Skill

When Claude discovers new KCML behaviour through testing:

1. **Update the relevant markdown file** in `kcmlrefman_md/` — this is the primary reference source (393 files covering the full language)
2. **Update the relevant reference file** in `.github/skills/kcml-coding/references/` if the topic is covered there
3. **Add patterns to SKILL.md** if they are common enough to include in the quick reference

When a tested code example reveals a quirk not in the docs, add it to the appropriate `kcmlrefman_md/` file with a comment like `REM Verified by execution`.

---

## Key KCML Rules (Never Get These Wrong)

- Strings **must** be DIM'd with a size: `DIM name$30` — never use a string without declaring it
- Strings are **fixed-length and space-padded** — `LEN()` returns content length excluding trailing spaces
- Arrays are **1-based**: `DIM arr(10)` gives elements 1 through 10
- Script mode (kcml -p): statements separated by `:`, continuation lines start with `: `
- `$END` terminates the KCML session — in `-p` scripts the interpreter exits naturally when it runs out of statements, so `$END` is not required at the end but is used to exit early
- Use `HEX(22)` or `""` (double double-quote) for embedded quote characters — **not** `CHR$(34)`. `""` is often cleaner when building structured text like JSON: `msg$ = "say ""hello"""` → `say "hello"`
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

## What NOT to Do

- Do not use `R7_DATE2J` or `R7_J2DATE` — these are Kerridge Rev7-era compatibility routines removed in KCML 6.9. They are officially obsolete (Y2K issues) and will fail on upgraded systems. Replace with manual ISO string rearrangement + `CONVERT DATE` (see date-functions.md for the exact pattern)
- Do not use `CHR$(34)` — use `HEX(22)` or `""` (double double-quote) for quotes in strings
- Do not use `INPUT` in scripts run with `kcml -p` — non-interactive, will hang
- Do not forget `$END` at the end of every script
- **Never background KCML processes** — they exhaust the single-user licence; always run foreground
- **Never use blank lines in `kcml -p` scripts** — a blank line silently terminates execution. Use `: REM` lines for spacing. Bare `REM` (without `: ` prefix) also terminates the script mid-run.
- **`-p` scripts: put ALL code under a numbered line** — unnumbered `: ` lines are treated as immediate mode. `GOSUB`/`RETURN` only work correctly when the calling code is inside a numbered block (e.g. `01000 REM main`). Use `01000 REM main` at the top of every script that uses subroutines.
- **`RETURN` inside `IF...THEN` causes A07** — use a flag variable instead: `IF condition THEN sv_ok = 0` then `IF sv_ok == 1 THEN DO ... END DO : RETURN`
- **`& numeric` concatenation unreliable in PRINT** — use semicolons: `PRINT "status="; ki_status` not `PRINT "status=" & ki_status`
- **`LOCAL DIM` not supported in DEFFN `-p` mode** — declare all subroutine variables in the outer DIM block
- **Never use 4-param `KI_OPEN`** in KCML 6.x — `CALL KI_OPEN handle, stream, file$, mode$` causes an S24 panic. Use `CALL KI_OPEN handle, file$, mode$ TO status` (3 params).
- **`HEX(22)` cannot be used with `&` in PRINT** — using `HEX(22)` as a `&` operand in a PRINT statement causes a syntax error because the embedded `"` confuses the parser. Assign it to a variable first: `q$ = HEX(22)` then use `;` separators: `PRINT q$; "field"; q$; ": "; q$; value$; q$`
- **`IF ... THEN x ELSE y` single-line ELSE not supported** — KCML's `IF ... THEN` form does not support an inline `ELSE`. Use two separate IF statements or a DO block structure instead.

## KISAM File Access (Verified Working Pattern)

Reading KISAM/KDB files from standalone scripts (KCML 06.00.88):

**CRITICAL**: Start the script with a numbered line (`01000 REM ...`). Unnumbered `: ` lines are "immediate mode" — GOSUB/RETURN only work correctly inside numbered blocks.

```kcml
01000 REM Read KISAM file
: DIM ki_status, handle, ki_sym, ki_dataptr$6, ki_key$64, rec$512, count
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: CALL KI_OPEN handle, "/full/path/to/FILENAME", "R" TO ki_status
: IF ki_status <> 0 THEN PRINT "open failed"
: IF ki_status <> 0 THEN $END
: CALL KI_START_BEG handle, 1 TO ki_status
: IF ki_status <> 0 THEN PRINT "start failed"
: IF ki_status <> 0 THEN $END
: ki_sym = SYM(rec$)
: count = 0
: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status == 0 THEN DO
:     count++
:     PRINT "Rec: ["; STR(rec$, 1, 60); "]"
:   END DO
: UNTIL ki_status <> 0 OR count >= 10
: CALL KI_CLOSE handle TO ki_status
: $END
```

## String-to-Numeric Conversion

**`VAL(str$, n)` in KCML reads `n` bytes of a string as a binary integer** (inverse of `BIN(`) — it is NOT a string-to-numeric parser. `VAL("300")` = 48 (binary value of ASCII byte '0' with default n=1), not 300.

Use `CONVERT str$ TO num` to parse an ASCII number string into a numeric variable:

```kcml
: DIM s$20, n
: s$ = "300.50"
: CONVERT s$ TO n
: PRINT n
```

`CONVERT` stops at the first non-numeric character, so trailing spaces in fixed-length string variables are safe.

## Packed Date Format (OEHDR01 and likely all files)

Type `D`, 4-byte fields store dates as 4 binary-coded bytes that HEXUNPACK reveals as `YYYYMMDD`. To display as DD/MM/YYYY:

```kcml
: DIM hex$12, date$10
: HEXUNPACK STR(rec$, 82, 4) TO hex$
: date$ = STR(hex$, 7, 2) & "/" & STR(hex$, 5, 2) & "/" & STR(hex$, 1, 4)
```

To **write** a packed date from a `YYYYMMDD` string, use `HEXPACK`:

```kcml
: DIM date_packed$4
: HEXPACK date_packed$ FROM "20260418"   REM treats string as 8 hex chars -> 4 bytes
```

## IBM Packed Decimal (type K / type I in DD files, verified on S_STOK01)

Type K (`DECIMAL` in SQL, type `I` in legacy DD files) stores packed BCD numbers. Use `UNPACK` directly — it handles IBM BCD format:

```kcml
: REM 8-byte field, 6 decimal places (15 total digits = 9 integer + 6 decimal)
: DIM packed$8, val
: packed$ = STR(rec$, 513, 8)
: UNPACK (#########.######) packed$ TO val
```

The image string must match: `(field_bytes*2 - 1 - scale)` `#` chars + `.` + `scale` `#` chars. For fallback/inspection using HEXUNPACK: 8 bytes = 16 hex chars = 15 BCD digits + sign nibble (last char, C=pos, D=neg). Build decimal string: `STR(hex$, 1, 9) & "." & STR(hex$, 10, 6)` then `CONVERT valstr$ TO val`.

**PACK statement is broken in KCML 06.00.88** — `PACK "image", val TO dest$` gives S12 syntax error. To **write** packed BCD, build the hex string manually and use `HEXPACK`:

```kcml
: REM Write value=9.99 into an 8-byte #########.###### packed field
: DIM val, bcd_val, n_s$12, pad_s$32, hex_s$16, packed$8
: val = 9.99
: bcd_val = ROUND(val * 1000000, 0)
: n_s$ = $PRINTF("%d", bcd_val)
: pad_s$ = "000000000000000" & RTRIM(n_s$)
: hex_s$ = STR(RTRIM(pad_s$), LEN(RTRIM(pad_s$)) - 14, 15) & "C"
: HEXPACK packed$ FROM hex_s$
: REM hex_s$ = "000000009990000C", packed$ = 8 binary bytes
```

Sign nibble: use `C` for OEENT01 #########.###### fields; use `0` for integer-only PACK(#######) fields (e.g. PFN8 counter).

For PACK(#######) 7-digit integer fields (4 bytes):
```kcml
: DIM n_s$12, pad_s$16, hex_s$8, packed$4
: n_s$ = $PRINTF("%d", val)
: pad_s$ = "0000000" & RTRIM(n_s$)
: hex_s$ = STR(RTRIM(pad_s$), LEN(RTRIM(pad_s$)) - 6, 7) & "0"
: HEXPACK packed$ FROM hex_s$
```

## KISAM File Access (Verified Working Pattern)

Key facts:
- Connection 1 is auto-created as KISAM on script start — no `KI_ALLOC_CONNECT` needed
- `KI_ALLOC_HANDLE 0, 1` = auto-allocate handle on KISAM connection 1
- `ki_dataptr$` must be 6 bytes
- Pre-assign `ki_sym = SYM(rec$)` — do not pass `SYM()` inline to `KI_READ_NEXT`
- Status 2 = EOF (normal), 0 = success, 1 = not found
- `CALL KI_START handle, key$, path TO status` — key$ before path in KCML 6.x (libKI has them reversed)

**KI_REWRITE signature (verified from libKI source):**

```kcml
CALL KI_REWRITE h, ki_dataptr$, ki_sym TO ki_status
```

Used after `KI_READ_HOLD` to write back a modified locked record. The ERP wrapper `GOSUB 'KI_REWRITE(handle, ki_dataptr$, ki_sym)` auto-stamps USER_AMEND/DATE_AMEND fields; the direct CALL does not.

**KI_WRITE signature for new records:**

```kcml
CALL KI_WRITE h, SYM(rec$), 0 TO ki_status, ki_dataptr$
```

The third argument (path=0 = key path 1) tells KISAM which key path to use for the insert.

## ERP Wrapper ki_start_beg Bug (after EOF)

After reading a KISAM file to EOF, the ERP global wrapper `GOSUB 'ki_start_beg(handle, 1)` fails to reposition — it returns a non-zero status. The fix: capture the first real part key before any EOF reads, then use `GOSUB 'ki_start(handle, first_part$, 1)` instead.

```kcml
: REM Capture before any full-file scan
: GOSUB 'ki_start(gb_h(51), ps_null_key$, 1)
: GOSUB 'ki_read_next(gb_h(51), 1, SYM(ps_srec$))
: IF ki_status == 0 THEN ps_first_part$ = RTRIM(STR(ps_srec$, pf_m1(1), pf_m2(1)))
: REM Later, to restart from beginning (works even after EOF):
: GOSUB 'ki_start(gb_h(51), ps_first_part$, 1)
```

`CALL KI_START_BEG handle, 1 TO ki_status` (direct, not ERP wrapper) works fine after EOF.

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
