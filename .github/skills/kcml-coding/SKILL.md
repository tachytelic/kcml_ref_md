---
name: kcml-coding
description: 'Generate and test KCML code. Use when: writing KCML programs, creating KCML examples, debugging KCML syntax, learning KCML language features. KCML is a BASIC-derived language from Wang BASIC-2 used for business applications.'
argument-hint: 'Describe the KCML program or feature you need'
---

# KCML Code Generation and Testing

Generate working KCML (Kerridge Computer Macro Language) code snippets and verify them by execution.

## When to Use

- Writing KCML programs or subroutines
- Creating working code examples from documentation
- Debugging KCML syntax errors
- Learning KCML language features
- Converting algorithms to KCML

## KCML Language Quick Reference

### Program Structure

KCML programs consist of numbered lines (0-32000) containing statements separated by colons:

```kcml
10 DIM name$30, count
20 FOR i = 1 TO 10
30    PRINT "Iteration: "; i
40 NEXT i
```

Modern style (used by Workbench) omits line numbers - statements are separated by newlines.

### Variable Types

| Type | Suffix | Example | Notes |
|------|--------|---------|-------|
| Numeric | (none) | `count`, `total` | Real numbers, auto-initialized to 0 |
| String | `$` | `name$`, `buffer$` | Must be DIM'd with size, auto-init to spaces |
| Array | `()` | `items(10)`, `grid(5,5)` | Up to 2 dimensions, 1-based indexing |
| Field | `.` prefix | `.name$`, `.amount` | Sub-records within strings |
| Global | `@` prefix | `@counter`, `@shared$` | Shared across partitions |
| Constant | `_` prefix | `_MAXSIZE` | Cannot be modified after DIM |

### Essential Statements

```kcml
REM Comment or ' Comment
DIM variable$100          : REM Declare string of 100 chars
DIM array(10,5)           : REM 2D numeric array
COM persistent$50         : REM Survives LOAD
LET x = expression        : REM Assignment (LET optional)
PRINT "text"; variable    : REM Output (semicolon=no space)
PRINT "A","B"             : REM Comma = tab to column 16
INPUT "Prompt: "; var$    : REM Read from user
```

### Control Flow

```kcml
REM IF-THEN-ELSE (single line)
IF condition THEN statement ELSE statement

REM IF-ENDIF (multi-line)
IF condition THEN
   statements
ELSE
   statements
ENDIF

REM FOR loop
FOR i = 1 TO 100 STEP 2
   statements
NEXT i

REM WHILE loop  
WHILE condition
   statements
WEND

REM DO-LOOP (REPEAT-UNTIL style)
DO
   statements
LOOP UNTIL condition

REM SELECT CASE
SELECT CASE expression
   CASE value1
      statements
   CASE value2, value3
      statements
   CASE ELSE
      statements
END SELECT
```

### Common Functions

```kcml
REM String functions
LEN(string$)              : REM Length
STR$(number)              : REM Number to string
VAL(string$)              : REM String to number
STR(s$, start, len)       : REM Substring (1-based)
POS(haystack$ = needle$)  : REM Find position (0 if not found)
$UPPER(string$)           : REM Uppercase
$LOWER(string$)           : REM Lowercase

REM Numeric functions
INT(x)                    : REM Truncate to integer
ABS(x)                    : REM Absolute value
RND(1)                    : REM Random 0-1
SQR(x)                    : REM Square root
MOD(a, b)                 : REM Modulo

REM Date/Time
$TODAY                    : REM Current date (YYYYMMDD)
$TIME                     : REM Current time (HHMMSS)
```

### Operators

| Type | Operators |
|------|-----------|
| Arithmetic | `+`, `-`, `*`, `/`, `^` (power) |
| Comparison | `=`, `<>`, `<`, `>`, `<=`, `>=` |
| Logical | `AND`, `OR`, `NOT`, `XOR` |
| String | `&` (concatenate), comparison operators |

### Output Formatting

```kcml
REM PRINT USING for formatted output
PRINT USING "(###.##)", number
PRINT USING "($$###.##)", amount      : REM Currency
PRINT USING "(LLLLLLLLLL)", name$     : REM Left-justified
PRINT USING "(RRRRRRRRRR)", name$     : REM Right-justified

REM CONVERT for formatting to string
CONVERT number TO result$, (###.##)
```

## Code Execution

### Local Execution (Recommended — Linux with KCML installed)

KCML is installed locally at `/usr/lib/kcml/kcml`. Write code to a temp file and run directly:

```bash
# Write script to temp file
cat > /tmp/test.kcml << 'EOF'
DIM x : x = 42 : PRINT x : $END
EOF

# Run with required env vars
export MAC_ADDRESS="00:0c:44:88:7a:4c"
export SPOOF_HOSTNAME="640UK"
export LD_PRELOAD=/usr/lib/kcml/ioctl_preload.so
/usr/lib/kcml/kcml -p /tmp/test.kcml
```

Or as a one-liner:
```bash
export MAC_ADDRESS="00:0c:44:88:7a:4c" && export SPOOF_HOSTNAME="640UK" && export LD_PRELOAD=/usr/lib/kcml/ioctl_preload.so && /usr/lib/kcml/kcml -p /tmp/test.kcml
```

### SSH/SCP Method (Legacy — Windows development only)

This was the previous method when developing on Windows. No longer needed on Linux.

```powershell
# Use the helper script
.\kcml_executor\run_kcml.ps1 -Code 'PRINT "Hello World" : $END'
```

**Server Details (legacy):**
- Host: 10.1.1.213 (Ubuntu 8.04 - requires legacy SSH algorithms)
- User: interpartuk (key auth configured, passwordless sudo)
- KCML path: `/usr/lib/kcml/kcml -p`

### CGI Method (Alternative)

Execute KCML via Apache CGI. The helper script auto-wraps code with Content-type headers:

```powershell
.\kcml_executor\run_kcml.ps1 -Code 'PRINT "Hello" : $END' -Method cgi
```

Or access directly via browser: `http://10.1.1.213/hello.kcml?param=value`

CGI scripts can use `ENV("QUERY_STRING")` to read URL parameters.

**Key CGI notes:**
- Use `HEX(22)` for quote character in JSON (NOT `CHR$(34)`)
- **Never put `:` in a REM statement** — KCML parses `:` as a statement separator even inside REM text (syntax error). Use a dash instead of a colon in REM text.
- Must output `Content-type:` header + blank line before content
- Cannot use `$END` inside IF blocks to exit early

For complete Apache setup instructions, see [CGI_SETUP.md](../../kcml_executor/CGI_SETUP.md).

### HTTP Server (Legacy)

An HTTP server on port 8765 can accept code via POST, but may hang on complex code (subroutines):

```bash
curl -X POST http://10.1.1.213:8765/execute \
  -H "Content-Type: application/json" \
  -d '{"code": "PRINT \"Hello World\""}'
```

Response:
```json
{
  "success": true,
  "stdout": "Hello World\n",
  "stderr": "",
  "exit_code": 0
}
```

## Writing KCML for Script Execution

When writing code to run with `kcml -p` (non-interactive):

1. **Colons separate statements** - Use `:` between statements (newlines alone don't work)
2. **Two styles work:**
   - Single line: `DIM x : x = 1 : PRINT x : $END`
   - Continuation: Start each new line with `: ` prefix
3. **Use PRINT for output** - Output goes to stdout
4. **End with $END** - Cleanly terminates the script
5. **Avoid INPUT** - Non-interactive mode cannot prompt users
6. **Never use `:` in REM text** - KCML parses `:` as a statement separator even inside REM; this causes syntax errors. Use `-` instead (e.g. `REM Target - /some/path`)

### Script Template (Continuation Style)

```kcml
REM Script description
: DIM result$100
: REM Your code here
: result$ = "Computed value"
: PRINT result$
: $END
```

### Script Template (Single Line)

```kcml
DIM result$100 : result$ = "Hello" : PRINT result$ : $END
```

### Script Template (Line Numbers - Traditional)

```kcml
10 REM Script description
20 DIM result$100
30 result$ = "Computed value"
40 PRINT result$
50 $END
```

## Procedure for Generating KCML

1. **Understand the requirement** - What should the code do?
2. **Check documentation** - Reference files in `kcmlrefman/` for syntax
3. **Write initial code** - Use patterns from this skill
4. **Execute and verify** - Send to execution server
5. **Iterate if needed** - Fix errors based on output

## Common Patterns

### String Processing

```kcml
DIM input$100, word$20
: input$ = "Hello World Example"
: PRINT "Input: "; input$
: PRINT "Length: "; LEN(input$)
: PRINT "Upper: "; $UPPER(input$)
: $END
```

### Numeric Calculations

```kcml
DIM values(10), sum, avg, i
: REM Initialize array
: FOR i = 1 TO 10
: values(i) = i * 2
: NEXT i
: REM Calculate sum and average
: sum = 0
: FOR i = 1 TO 10
: sum = sum + values(i)
: NEXT i
: avg = sum / 10
: PRINT "Sum: "; sum; " Average: "; avg
: $END
```

### Date Formatting

```kcml
REM Using $TODAY (YYYYMMDD string)
DIM today$8
: today$ = $TODAY
: PRINT STR(today$,7,2); "/"; STR(today$,5,2); "/"; STR(today$,1,4)
: $END
```

```kcml
REM Using CONVERT DATE (recommended for date arithmetic)
DIM julian, iso$12
: CONVERT DATE "2026-04-04" TO julian
: PRINT "Julian: "; julian
: CONVERT DATE julian + 30 TO iso$
: PRINT "30 days later: "; iso$
: $END
```

See [date-functions.md](./references/date-functions.md) for R7_DATE2J, R7_J2DATE, and Excel date conversion.

## Error Handling

KCML errors include line number and error description. Common errors:

| Error | Cause | Fix |
|-------|-------|-----|
| `Undefined variable` | Variable not DIM'd | Add DIM statement |
| `Type mismatch` | Wrong variable type | Check $ suffix |
| `Subscript error` | Array index out of bounds | Check array dimensions |
| `Syntax error` | Invalid statement | Check spelling and punctuation |

## Detailed Reference Files

For in-depth coverage of specific topics, see the reference files:

| Topic | File | Coverage |
|-------|------|----------|
| Date Functions | [date-functions.md](./references/date-functions.md) | CONVERT DATE, R7_DATE2J/R7_J2DATE, Julian dates, date arithmetic |
| String Functions | [string-functions.md](./references/string-functions.md) | STR(), LEN(), POS(), $UPPER/$LOWER, concatenation |
| Control Flow | [control-flow.md](./references/control-flow.md) | IF/ELSE, FOR, WHILE, DO-LOOP, SELECT CASE, GOSUB |
| Arrays & Variables | [arrays-variables.md](./references/arrays-variables.md) | DIM, COM, arrays, MAT operations, constants, globals |
| File I/O | [file-io.md](./references/file-io.md) | OPEN#, READ#, WRITE#, DATA LOAD DC, buffered chunk reads, sockets, pipes |
| Error Handling | [error-handling.md](./references/error-handling.md) | TRY/CATCH, THROW ERR, ERR function, error codes |
| Subroutines | [subroutines.md](./references/subroutines.md) | DEFSUB, GOSUB, RETURN, BYREF, LOCAL DIM, CALL |
| Numeric Functions | [numeric-functions.md](./references/numeric-functions.md) | INT, ABS, math functions, CONVERT, operators |
| Print & Input | [print-input.md](./references/print-input.md) | PRINT, PRINTUSING, LINPUT, KEYIN, SELECT PRINT, $REWIND, PACK/UNPACK |
| Screen I/O | [screen-io.md](./references/screen-io.md) | PRINT AT, KEYIN, BOX, WINDOW, menus, control codes, grid patterns |
| Forms | [forms.md](./references/forms.md) | DEFFORM, DEFEVENT, all control types, combobox, grid, context menus, $DECLARE |
| $DECLARE | [declare.md](./references/declare.md) | Windows DLL calls, parameter types, ShellExecute, clipboard, file I/O |
| COM & Chaining | [com-chaining.md](./references/com-chaining.md) | COM variables, LOAD, program linking, DATA statements |
| Global Partitions | [global-partitions.md](./references/global-partitions.md) | SELECT @PART, @LOCK/@UNLOCK, libraries, KI_ database routines, SYM() |
| Field Variables | [field-variables.md](./references/field-variables.md) | DEFRECORD, FLD(), dot notation, packed numeric fields, record layouts |

## Real-World Patterns (from Source Code)

These patterns are drawn from actual KCML business applications and reflect idioms not always visible in the reference manual.

### DEFFN vs DEFSUB

Older code (and most real programs) use `DEFFN` with a line number. `DEFSUB`/`END SUB` is the modern equivalent:

```kcml
REM Older style (DEFFN) - very common in real programs
02000 DEFFN 'FIND()
    : REM ... code ...
    : RETURN

REM Modern style (DEFSUB)
DEFSUB 'find()
:   REM ... code ...
: END SUB
```

Both styles are valid and can be called with `GOSUB 'FIND()`.

### Multiple Assignment

Assign the same value to several variables at once:

```kcml
: a$, b$, c$ = " "           : REM Clear three strings
: nextok, prevok = TRUE       : REM Set two flags
: x, y, z = 0                : REM Zero three numerics
: pf_dataptr$ = ALL(HEX(00)) : REM Fill with null bytes
```

### BOOL() — Boolean Coercion

`BOOL()` converts a numeric to a proper TRUE/FALSE. Used extensively in real code:

```kcml
: IF BOOL(quick_add) THEN DO ... END DO
: IF NOT BOOL(file_open) THEN ...
: eko_do_uploads = BOOL(eko_realtimeupload_stk)
```

### ALL() — Fill String with Byte

`ALL(HEX(xx))` fills a string with a repeated byte value:

```kcml
: pf_dataptr$ = ALL(HEX(00))     : REM Null-fill (uninitialised pointer)
: pf_srch_acc$ = ALL(HEX(FF))    : REM Fill with 0xFF (match-all sentinel)
```

### ZER — Zero an Array

```kcml
: arr() = ZER         : REM Zero all elements
: bxpos() = ZER       : REM Common before rebuilding position arrays
```

### MAT REDIM — Resize Array at Runtime

```kcml
: MAT REDIM pf_pre_rec$ LEN(STR(pf_rec$))  : REM Resize to match another string
: MAT REDIM BS_LOG(4)                        : REM Change array dimension
```

### Computed GOSUB / GOTO

```kcml
REM Dispatch to one of several functions based on option number
: ON option GOSUB 'FIND, 'NEXT, 'PREV, 'DISPLAY_RECORD, 'ADD, 'CHANGE, 'DELETE
: GOTO 1050

REM Computed GOTO (old style)
: ON N9 GOTO 2000, , 1900, 2200, , , 2500  : REM Empty = fall through to STOP
: STOP
```

### Prefix Increment in Expressions

```kcml
: pages(++pages) = check_screen   : REM Increment pages, then use as index
: function(++fncs) = 14           : REM Common pattern for building arrays
```

### IF with Inline THEN (no ENDIF)

```kcml
: IF ki_status == 0 AND pf_scrname$ <> " " THEN DO
:   pages(++pages) = check_screen
: END DO
```

### Calling Convention

Subroutines called with tick-apostrophe prefix, args in parentheses:

```kcml
: GOSUB 'MESS_BOX("Returning to menu", 0)
: GOSUB 'READ_STOCK(PF_P1$, FALSE)
: GOSUB '120(Q6$)               : REM Line number subroutine (older style)
: CALL R7_DATE2J today$ TO today : REM CALL for external library functions
```

### Ternary in String Building

```kcml
: Q6$ = "Problem " & (SP_CREAT == 1 ? "writing" : "rewriting") & " selling price record."
```

### PACK / UNPACK — Binary Numeric Storage

Stores numbers as packed binary within a string buffer (used for database records):

```kcml
: PACK(######) STR(record$, offset, length) FROM numeric_value
: UNPACK(######) STR(record$, offset, length) TO numeric_value
: HEXUNPACK STR(A$, 2, 2) TO STR(A8$, 2)
```

Format strings: `#` = digit position, `-` = sign, `.` = decimal point.

### FLD() — Structured Field Access

Access named fields within a string buffer using dot notation inside `FLD()`:

```kcml
: IF FLD(pf_scrfld$(i).Type$) == "N" THEN ...
: FLD(pf_scrfld$(i).Row) == row
: FLD(STR(BS_LOG$, BS_K1(10) + (n*8), 8).GB_PACK_NUM) = value
```

### Error Handling with LOAD

When loading a dynamic program name, catch load failures:

```kcml
: LOAD N$ 1000
: ERROR GOTO 1200       : REM If load fails, go to 1200
```

### Standard Exit Pattern

Every program ends the same way:

```kcml
01900 REM End of program
    : GOSUB 'CLOSE_<module>()       : REM Close any open files
    : GOSUB 'MESS_BOX("Returning to menu", 0)
    : LOAD "PF/START" 1000          : REM Return to main menu
```

### Global Partition Access (ERP Pattern)

All database I/O and common UI routines live in the global partition. Programs call them as if they were local:

```kcml
REM Any GOSUB not found locally is searched in the global
: GOSUB 'KI_READ(GB_H(51), part_key$, 1, SYM(pf_rec$))
: IF KI_STATUS == 1 THEN ...   : REM KI_STATUS is a global variable
: GOSUB 'MESS_BOX("Not found", 0)
: GOSUB 'SELSCREEN()
```

`GB_H(n)` is an array in the global holding file handles indexed by file number constants.
`SYM(var)` passes a pointer to a record buffer — avoids copying large strings.

### Field Variables for Record Access

Never use raw `STR()` offsets for record fields in ERP code. Use field variables:

```kcml
REM Bad — fragile, unreadable
: part_no$ = STR(pf_rec$, 1, 16)

REM Good — readable, layout-independent
: part_no$ = FLD(pf_rec$.PF_PART_NO$)
: FLD(pf_rec$.PF_QTY) -= qty_sold
```

Record layouts are defined with `DEFRECORD` in libraries, creating a `_RecordName` size constant:

```kcml
DEFRECORD StockRecord
  FLD PF_PART_NO$16
  FLD PF_QTY = "######"
END RECORD
DIM pf_rec$_StockRecord    : REM Exactly the right size
```

### SYM() — Pass Large Variables by Reference

Pass record buffers into global subroutines using symbol pointers, not copies:

```kcml
: GOSUB 'KI_WRITE(GB_H(234), SYM(pf_rec$))    : REM Pass pointer, not value
: GOSUB 'PACK_OE_SP()                           : REM Uses SYM internally
```

### REPEAT...UNTIL Loop

A useful alternative to WHILE when at least one iteration is needed:

```kcml
: REPEAT
:   GOSUB 'KI_READ_NEXT(GB_H(51), 1, SYM(tmp_rec$))
:   IF KI_STATUS == 0 THEN GOSUB 'PROCESS_RECORD()
: UNTIL KI_STATUS <> 0
```

### Constants with _ Prefix

Constants use underscore prefix and are set at DIM time, never changed:

```kcml
DIM _MAX_RETRIES = 3
DIM _BUFSIZE = 8 * 1024
DIM buffer$(_BUFSIZE)     : REM Can use constant in DIM
```

### Multilingual Strings

For multi-country ERP, strings can have language variants:

```kcml
: msg$ = <<"Stock not found", "Artikel nicht gefunden", "Article introuvable">>
: PRINT msg$    : REM Shows string for language set in STR($OPTIONS,20,1)
```

### Q8 Key Code Navigation (Universal Form Pattern)

After every `GOSUB 'KEYSTR()` or `GOSUB 'KEYNUM()` call:
- `Q8 = 0` = Enter (proceed)
- `Q8 = 126` = Back tab (previous field)
- `Q8 = 127` = Escape (abort)
- `Q8 = 1..n` = Function key Fn (when ALLOWFNS=TRUE)

Standard navigation line immediately after every field input:
```kcml
: GOSUB 'KEYSTR(var$, row, col, maxlen)
: ON Q8-125 GOTO previous_field, abort_exit   : REM 126=back, 127=escape
: REM Q8=0 (Enter) falls through to normal processing
```

### Validate Single-Character Inputs

Canonical pattern for any constrained Y/N or type-code field:
```kcml
: GOSUB 'KEYSTR(answer$, 16, 21, 1)
: ON Q8-125 GOTO prev_field, abort
: GOSUB 'LOWTOUP(SYM(Q6$))               : REM Uppercase in place
: IF POS("YN" = Q6$) == 0 THEN DO        : REM Not in valid set
:   PRINT HEX(07);                        : REM Bell
:   GOTO retry_label
: END DO
```

### Handle Locked Records (KI_STATUS == 12)

```kcml
: GOSUB 'READ_RW_DD(key$, TRUE)
: IF KI_STATUS == 12 THEN DO
:   CONVERT KI_LOCKBY TO Q7$, (###)
:   Q6$ = "Record being edited by partition " & Q7$ & " - Retry?"
:   GOSUB 'MESSBOX_RETURN(Q6$, 0)
:   GOTO retry_label
: END DO
```

### Handle Full File on Write

```kcml
: GOSUB 'WRITE_RECORD(new_record)
: IF KI_STATUS == 5 OR KI_STATUS == 6 THEN DO
:   Q6$ = "File " & (KI_STATUS == 5 ? "Index" : "Data") & " area full"
:   GOSUB 'MESS_BOX(Q6$, 1)
:   GOSUB 'KEY_RETURN()
:   WINDOW CLOSE #0
: END DO
: ELSE IF KI_STATUS <> 0 THEN DO
:   GOSUB 'KI_FATAL_ERROR("Unexpected write error")
: END DO
```

### SELECT CASE (Preferred Over Cascaded IF)

```kcml
SELECT CASE TRUE
  CASE ki_status == 0
    : GOSUB 'DISPLAY_RECORD()
  CASE ki_status == 1
    : PRINT "Record not found"
  CASE ki_status == 12
    : PRINT "Record locked"
  CASE ELSE
    : GOSUB 'KI_FATAL_ERROR("Unexpected status")
END SELECT
```

## Source Documentation

Full KCML documentation is in the `kcmlrefman/` folder:

- **IntroLangBasics.md** - Variables, arrays, constants
- **IntroLangFeatures.md** - Advanced features
- **FOR.md**, **WHILE.md**, **DO.md** - Loop constructs
- **IFENDIF.md**, **SELECT_CASE.md** - Conditionals
- **PRINT.md**, **PRINTUSING.md** - Output formatting
- **DIM.md**, **COM.md** - Variable declarations
- **CONVERT_DATE.md** - Date conversion functions
- **Tutorial*.md** - Step-by-step tutorials
