# KCML Screen I/O Reference

Screen and terminal I/O in KCML — cursor positioning, input, menus, boxes, and control codes.

---

## DEFFORM / DEFEVENT — GUI Forms

### CRITICAL: DEFEVENTs must be INSIDE the DEFFORM block

Every `DEFEVENT` for a form **must be a continuation line inside that form's `DEFFORM...FORM END` block**. If a DEFEVENT is placed outside (e.g. as a separate numbered line), KCML does not associate it with the form. The form opens, has no event handlers, does nothing, and immediately closes — silently, with no error.

This is especially critical for `Enter()` — it is the only place to load data and set control properties before the form is sent to the client. A form with no Enter() handler has no data and closes instantly.

**WRONG — events as separate numbered lines (form will close immediately):**

```kcml
01011 + DEFFORM MyForm()={...}
    : FORM END MyForm
01012 + DEFEVENT MyForm.Enter()   : REM WRONG - outside the DEFFORM block
    :   .lblTitle.Text$ = "Hello"
    : END EVENT
01013 result = MyForm.Open()      : REM form opens, does nothing, closes
```

**CORRECT — events as continuation lines inside the DEFFORM block:**

```kcml
01011 + DEFFORM MyForm()={...}
    : + DEFEVENT MyForm.Enter()   : REM correct - inside, note the + prefix
    :   .lblTitle.Text$ = "Hello"
    : END EVENT
    : FORM END MyForm
01012 result = MyForm.Open()      : REM form opens, Enter() fires, form stays open
```

Note the `+ DEFEVENT` prefix (with `+`) — required when inside a DEFFORM block.

### All DEFFORM blocks must appear before any .Open() call

All `DEFFORM` blocks (with their events and `FORM END`) must appear **before** the first `.Open()` call in physical execution order. When one form opens another, both must be fully defined before either is opened:

```kcml
01010 + DEFFORM MainForm()={...}
    : + DEFEVENT MainForm.btnDetail.Click()
    :   result = DetailForm.Open()
    : END EVENT
    : FORM END MainForm
01011 + DEFFORM DetailForm()={...}
    : + DEFEVENT DetailForm.Enter()
    :   REM populate detail
    : END EVENT
    : FORM END DetailForm
01012 result = MainForm.Open()
    : GOTO 9000
```

**`FORM END` is required syntax** — it closes the DEFFORM block. It does NOT open the form.

### .Open() must assign a result variable

Always assign the return value: `result = MyForm.Open()`. Calling `MyForm.Open()` as a bare statement (no assignment) causes a runtime error.

### Diagnosing a form that closes immediately

1. Check that all DEFEVENTs are continuation lines **inside** the DEFFORM block
2. Use `TRAP` then step through — if execution skips from inside the DEFFORM directly to the exit, the events are outside the block
3. Wrap file opens inside Enter() with `ERROR DO / sv_ok = 0 / END DO` and guard the read loop with `IF sv_ok == 1 THEN DO` — an unhandled file error inside Enter() also closes the form silently

---

## PRINT AT — Cursor Positioning

`PRINT AT(row, col)` positions the cursor before printing:

```kcml
PRINT AT(row, col);
PRINT AT(row, col, width);   : REM width clears/pads the field
```

- `row` is 0-based (0 = top line, 23 = bottom line on a 24-line terminal)
- `col` is 0-based (0 = leftmost column)
- `width` fills the field with spaces before printing (useful for clearing)

### Examples

```kcml
REM Print at row 5, column 10
: PRINT AT(5,10); "Hello"

REM Clear a 20-char field then print
: PRINT AT(10,0,20); name$

REM Status line at bottom of screen
: PRINT AT(23,0,79); HEX(0E); "*** PRESS ANY KEY ***"; HEX(0F);
```

## TAB — Column Positioning

`TAB(n)` moves to absolute column n within the current line:

```kcml
PRINT "Name:"; TAB(20); name$
PRINT HEX(0C); company$; TAB(99); time$; "  "; date$   : REM 99 = far right
```

## Control Codes (HEX values)

KCML uses embedded hex codes for terminal control:

| Code | Effect |
|------|--------|
| `HEX(03)` | Clear screen |
| `HEX(06)` | Home cursor (top-left) |
| `HEX(0306)` | Clear screen and home cursor |
| `HEX(0C)` | Form feed / new page (on printer) |
| `HEX(0D)` | Carriage return |
| `HEX(0E)` | Highlight / reverse video ON |
| `HEX(0F)` | Highlight / reverse video OFF |
| `HEX(01)` | Cursor control prefix |
| `HEX(07)` | Bell / beep |
| `HEX(1B)` | Escape |

### Common Patterns

```kcml
REM Clear screen and home cursor
: PRINT HEX(0306);

REM Highlighted status message
: PRINT AT(23,0,79); HEX(0E); "Message here"; HEX(010F);

REM Bell on error
: PRINT HEX(07);
```

## KEYIN — Single Key Input

`KEYIN` reads a single keypress without requiring Enter:

```kcml
KEYIN var$
```

```kcml
DIM key$1
: PRINT AT(23,0); "Press any key to continue..."
: KEYIN key$
: IF key$ == GB_ABORT$ THEN GOTO exit_label
```

`GB_ABORT$` is typically the Escape key — a standard library constant for "user pressed escape/cancel".

### Waiting for specific keys

```kcml
DIM a9$1
: PRINT AT(23,20); HEX(0E); "*** PRESS ANY KEY FOR OPTIONS ***"; HEX(010F);
: KEYIN a9$
: IF a9$ == GB_ABORT$ THEN 1900
```

## LINPUT — Line Input with Prompt

`LINPUT` reads a full line of input:

```kcml
LINPUT "Enter name: "; name$
LINPUT LINE prompt$, option   : REM Menu-style: returns index of selected word
```

The `LINE` form is used for menus — it displays `prompt$` and returns the index (1-based) of the word the user selected or typed.

### Menu Pattern (from real source)

```kcml
DIM prompt$80, option, bxsz, bxpos
: prompt$ = "Find Next Prev Add Edit Delete Exit"
: bxsz = LEN(prompt$) + 1
: bxpos = 40 - INT(bxsz / 2)
: PRINT AT(22, bxpos); BOX(1, bxsz);
: PRINT AT(22, bxpos+1);
: LINPUT LINE prompt$, option
: PRINT AT(22, bxpos, LEN(prompt$)+1); BOX(-1, -bxsz)
```

## BOX — Draw/Remove Screen Boxes

`BOX(depth, width)` draws or removes a highlighted box at the current cursor position:

```kcml
PRINT AT(row, col); BOX(depth, width);    : REM Draw box
PRINT AT(row, col); BOX(-depth, -width);  : REM Remove box
PRINT AT(row, col); BOX(depth, 0);        : REM Box separator (vertical divider)
```

- Positive values draw the box
- Negative values remove/restore the box
- `depth` = number of rows
- `width` = number of columns

### Example: Highlight a menu option

```kcml
: PRINT AT(22, 5); BOX(1, 20);      : REM Draw box around menu
: PRINT AT(22, 5); "  Select item  ";
: REM ... user selects ...
: PRINT AT(22, 5, 20); BOX(-1, -20) : REM Remove box
```

## $PSTAT — Program Status Bar

`$PSTAT` sets the program identifier shown in the status bar:

```kcml
$PSTAT = "PROGNAME" & U7$
```

`U7$` is a COM variable (2 chars) typically holding the terminal/session ID suffix. This is a common pattern in all programs:

```kcml
: $PSTAT = "S/MANG" & U7$     : REM "S/MANG01" etc.
```

## WINDOW — Window Management

KCML supports overlapping windows on terminals:

```kcml
WINDOW OPEN #n AT row, col SIZE rows, cols   : REM Open a window
WINDOW CLOSE #n                               : REM Close and restore background
WINDOW CLOSE #0                              : REM Close all windows
```

### Window Example

```kcml
DIM msg$60
: msg$ = "File not found"
: WINDOW OPEN #1 AT 10, 20 SIZE 3, 40
: PRINT AT(11, 22); HEX(0E); msg$; HEX(0F);
: KEYIN key$
: WINDOW CLOSE #1
```

## Screen Attributes and Highlighting

Programs use attribute codes for coloured/styled display:

```kcml
REM Attribute codes sent via HEX sequences
: PRINT HEX(0204); scattr$(attrno+1); HEX(0E);
```

In real programs, `scattr$()` is an array of 2-byte attribute codes loaded from screen definitions.

## $SCREEN — Screen Control Statement

`$SCREEN` provides screen-level operations:

```kcml
$SCREEN CLEAR               : REM Clear screen
$SCREEN SAVE                : REM Save current screen image
$SCREEN RESTORE             : REM Restore saved screen
```

## SELSCREEN — Select Screen (Library Function)

`GOSUB 'SELSCREEN()` is a standard library call that selects/activates the current terminal window. Commonly called at program start and after returning from sub-programs:

```kcml
: GOSUB 'SELSCREEN()
```

## Multi-Assignment to Clear Variables

A common KCML idiom is assigning multiple variables at once:

```kcml
REM Set multiple vars to same value
: a$, b$, c$ = " "       : REM Clear three strings
: x, y, z = 0            : REM Zero three numerics
: nextok, prevok = TRUE   : REM Set two flags
```

## COM CLEAR — Clear a COM Variable

To reset a COM string variable to spaces:

```kcml
COM CLEAR varname$
```

Used when returning from a sub-program and cleaning up shared state.

## Common Screen Patterns from Real Code

### Status message at bottom of screen
```kcml
: PRINT AT(23,0,79); HEX(070E 06); message$; HEX(010F);
```
(`HEX(070E 06)` = bell + highlight + some attribute)

### Clear a line
```kcml
: PRINT AT(row, 0, 79);
```

### Print page header (for reports)
```kcml
: PRINT HEX(0C); company_name$; TAB(99); time$; "  "; date$; "  Page"; page_num
: PRINT HEX(0E); TAB(27 - LEN(title$)/2); "****  "; title$; "  ****"
: PRINT
```

### Computed GOSUB (function dispatch)
```kcml
REM Call one of several functions based on option number
: ON option GOSUB 'FIND, 'NEXT, 'PREV, 'DISPLAY_RECORD, 'ADD, 'CHANGE, 'DELETE
```

### Computed GOTO
```kcml
: ON n GOTO 2000, 1900, 2200, 2500
: STOP   : REM Safety stop if n is out of range
```

## Q8 — Key Code Conventions

After any `GOSUB 'KEYSTR()` or `GOSUB 'KEYNUM()` call, `Q8` holds the key that ended input:

| Q8 value | Key | Meaning |
|----------|-----|---------|
| `0` | Enter/Return | Accept input, proceed to next field |
| `1` | F1 | Function key 1 |
| `2` | F2 | Function key 2 |
| `n` | Fn | Function key n |
| `126` | Back tab / left arrow | Go to previous field |
| `127` | Escape | Abort / cancel |

### Standard Navigation Pattern

Almost every input field uses this idiom immediately after the KEYSTR/KEYNUM call:

```kcml
: GOSUB 'KEYSTR(field$, row, col, maxlen)
: ON Q8-125 GOTO previous_field, escape_exit
: REM Q8=0 (Enter) falls through here — normal processing
```

- `Q8-125 = 1` (Q8=126) → back tab → go to `previous_field`
- `Q8-125 = 2` (Q8=127) → escape → go to `escape_exit`
- `Q8=0` (Enter) → neither matches → falls through to normal processing

### Field Navigation in a Form

Real forms chain fields together with explicit back-navigation:

```kcml
01060 GOSUB 'KEYSTR(field_type$, 8, 21, 1)
    : ON Q8-125 GOTO 1050, 1050        : REM Back or escape = go to field above
    : REM ... validate field_type$ ...

01070 GOSUB 'KEYNUM(start_pos, 10, 21, "####")
    : ON Q8-125 GOTO 1060, 1050        : REM Back = previous field; escape = top
    : REM ... process start_pos ...

01080 GOSUB 'KEYNUM(field_len, 12, 21, "####")
    : ON Q8-125 GOTO 1070, 1050        : REM Back = previous field
```

Each field's `ON Q8-125 GOTO` points to the previous field's line number (back tab) and the top of the form (escape).

## KEYSTR — String Input at Screen Position

Global subroutine for accepting keyboard input at a specific screen location:

```kcml
GOSUB 'KEYSTR(variable$, row, col, maxlen)
```

- Displays current value of `variable$` at position, allows editing
- On completion: `Q6$` = entered value, `Q8` = terminating key
- Supports ? prefix for help lookup

```kcml
: GOSUB 'KEYSTR(DD_NAME$, 3, 21, 35)
: ON Q8-125 GOTO 1020, 1900    : REM Back=retry; Escape=exit program
: IF Q6$ == " " THEN 1020      : REM Empty input — try again
: DD_NAME$ = Q6$
```

### ? for Help Lookup

Programs conventionally test for `?` as the first character to trigger a help/browse screen:

```kcml
: GOSUB 'KEYSTR(DD_NAME$, 3, 21, 35)
: ON Q8-125 GOTO 1020, 1900
: IF STR(Q6$,, 1) == "?" THEN DO
:   GOSUB 'HELP_RW_CAT(1, 5, 10)     : REM Browse/search popup
:   IF Q6$ == " " THEN 1020
:   PRINT AT(3, 21, 35); Q6$;
: END DO
: DD_NAME$ = Q6$
```

## KEYNUM — Numeric Input at Screen Position

Global subroutine for accepting a numeric value at a specific screen location:

```kcml
GOSUB 'KEYNUM(current_value, row, col, image$)
```

- Displays `current_value` formatted with `image$`, allows editing
- On completion: `Q9` = entered numeric value, `Q8` = terminating key

```kcml
: GOSUB 'KEYNUM(RWD_NUM(1), 10, 21, "####")
: ON Q8-125 GOTO 1060, 1050    : REM Back=previous field; Escape=top
: RWD_NUM(1) = Q9
```

## LINPUT_LINE — Prompted Choice Input

Global subroutine for presenting a question with a set of word options:

```kcml
GOSUB 'LINPUT_LINE(question$, options$, default, row, col, maxopt, confirm, sep$)
```

- `question$` — the prompt text
- `options$` — space-separated list of choices ("Yes No", "Add Edit Delete")
- `default` — index of default option (1-based)
- `row`, `col` — screen position
- `maxopt` — maximum number of options
- `confirm` — TRUE to require confirmation
- `sep$` — separator character (usually `" "`)

Returns `LINPUT_OPTION` = 1-based index of the selected option.

```kcml
: GOSUB 'LINPUT_LINE("Delete Field?", "Yes No", 1, 7, 20, 2, TRUE, " ")
: IF LINPUT_OPTION <> 1 THEN 1060    : REM Not "Yes" — go back
: GOSUB 'KI_DELETE(GB_H(221), RWD_DATAPTR$)

: GOSUB 'LINPUT_LINE("Data Dictionary not found - Create?", "Yes No", 1, 8, 5, 1, FALSE, " ")
: IF LINPUT_OPTION == 1 THEN DO
:   REM Create the file
: END DO
```

## ALLOWFNS — Enable Function Key Handling

`ALLOWFNS` is a flag that controls whether function key presses are intercepted:

```kcml
: ALLOWFNS = TRUE             : REM Enable F-key handling
: GOSUB 'KEYSTR(RWD_KEY$, 6, 21, 20)
: ALLOWFNS = FALSE            : REM Disable after input
: IF Q8 == 1 THEN ...        : REM F1 was pressed
: IF Q8 == 2 THEN ...        : REM F2 was pressed
```

When `ALLOWFNS = TRUE` and a function key is pressed during KEYSTR/KEYNUM, `Q8` is set to the function key number (1, 2, etc.) and input returns normally.

### Function Key Handlers (DEFFN '1, DEFFN '2)

Programs define function key behaviour with numbered DEFFN routines. The number corresponds to the F-key:

```kcml
03000 DEFFN '1
    : REM F1 handler — Print report
    : IF BOOL(DD_PRINT) THEN DO
    :   REM ... perform the print ...
    : END DO

---

## Grid Control (KCMLgrid$) — Verified Patterns and Pitfalls

### CursorRow updates correctly for both left-click and right-click

`CursorRow` is updated by both left and right mouse clicks. It can be read safely inside both `grid.LeftClick()` and `grid.RightClick()` event handlers:

```kcml
+ DEFEVENT MyForm.grid.RightClick()
    LOCAL DIM sv_row
    sv_row = ..CursorRow    : REM correctly reflects the right-clicked row
    IF sv_row > 1 THEN DO
        REM ... process sv_row ...
    END DO
END EVENT
```

### CRITICAL: Do NOT store per-row data in grid cell Text$ using a loop variable

Assigning a LOCAL string variable to `Cell(row,col).Text$` inside a loop does **not** copy the value — the grid stores a reference to the variable. After the loop ends, all cells point to the same variable, which holds its last assigned value. Every row will read back identical data.

**WRONG — all rows end up with the same index (last value of sv_i_s$):**

```kcml
FOR sv_i = 1 TO sv_sp_next-1
    ...
    CONVERT sv_i TO sv_i_s$,(######)
    .grid.Cell(sv_row,8).Text$ = LTRIM(sv_i_s$)    : REM all rows get last sv_i value
NEXT sv_i
```

**WRONG — numeric assigned to Text$ converts to boolean (non-zero = "1"):**

```kcml
.grid.Cell(sv_row,8).Text$ = sv_i    : REM always stores "1" for any sv_i > 0
```

### CORRECT: Use a form-level array to map grid rows to record indices

The reliable way to associate each grid row with a backing record index is a form-level numeric array:

```kcml
REM At program level:
DIM grid_idx(500)

REM During grid population:
FOR sv_i = 1 TO sv_sp_next-1
    DATA LOAD BU T#gb_h(213),(sv_i*128)sp_rec$
    IF STR(sp_rec$,57,1)<>"6" THEN DO
        sv_row++
        .grid.Cell(sv_row,2).Text$ = RTRIM(STR(sp_rec$,17,30))
        grid_idx(sv_row) = sv_i    : REM numeric assignment to array — always correct
        REM ... other cell assignments ...
    END DO
NEXT sv_i

REM In click/right-click handlers:
sv_spool_idx = grid_idx(..CursorRow)
DATA LOAD BU T#gb_h(213),(sv_spool_idx*128)sp_rec$
```

### Right-click context menus — capture row in RightClick, use it in Select()

The `CursorRow` value at the time a context menu item's `Select()` event fires may differ from when `RightClick()` fired (focus changes can move the cursor). Store the row and derived data in form-level variables during `RightClick()`:

```kcml
REM Form-level:
DIM sel_spool_idx, sel_rclick_row

+ DEFEVENT MyForm.grid.RightClick()
    LOCAL DIM sv_row
    sv_row = ..CursorRow
    IF sv_row > 1 THEN DO
        sel_rclick_row = sv_row
        sel_spool_idx = grid_idx(sv_row)
        .ctxMenu.TrackPopup(..MouseX+..Left,..MouseY+..Top)
    END DO
END EVENT

+ DEFEVENT MyForm.ctxMenu.mnuDoSomething.Select()
    REM Use sel_rclick_row and sel_spool_idx — do NOT re-read CursorRow here
    GOSUB 'do_something(sel_spool_idx)
    .grid.Cell(sel_rclick_row,4).Text$ = "UPDATED"
END EVENT
```

### DATA SAVE BU — updating both the DC buffer and disk

`DATA LOAD DC OPEN` loads a file into an in-memory DC buffer. Subsequent `DATA LOAD BU` reads from that buffer. `DATA SAVE BU` behaviour depends on context:

- **Without `$OPEN`**: writes to the DC buffer only. The in-process refresh (`DATA LOAD BU`) sees the new value. Other programs that do a fresh `DATA LOAD DC OPEN` will re-read from disk and see the old value.
- **With `$OPEN` active**: writes to disk. The DC buffer is NOT updated. In-process `DATA LOAD BU` still sees the old (buffered) value.

To update **both** the DC buffer (so your own refresh works) and disk (so other programs see it), do two saves:

```kcml
DATA LOAD BU T#gb_h(213),(idx*128)sp_rec$
STR(sp_rec$,57,1) = new_stat$
DATA SAVE BU T#gb_h(213),(idx*128)sp_rec$    : REM updates DC buffer
$OPEN #gb_h(213)
DATA SAVE BU T#gb_h(213),(idx*128)sp_rec$    : REM commits to disk
$CLOSE #gb_h(213)
```
    : Q8 = 1    : REM Restore Q8 so caller knows F1 was pressed
    : RETURN

04000 DEFFN '2
    : REM F2 handler — Edit catalogue
    : IF BOOL(DD_PRINT) AND U6$(1) == "9" THEN Q8 = 2
    : RETURN
```

The pattern is to use a secondary flag (e.g., `DD_PRINT`) to distinguish context — the DEFFN '1 handler may be called from several places but should only act in certain contexts.

## LOWTOUP — In-Place Uppercase Conversion

Standard global subroutine to convert a string variable to uppercase in place, using a SYM pointer:

```kcml
: GOSUB 'LOWTOUP(SYM(Q6$))    : REM Uppercase Q6$ in place
: GOSUB 'LOWTOUP(SYM(input$)) : REM Any string variable
```

Used universally after KEYSTR for single-character validation inputs where only uppercase is valid:

```kcml
: GOSUB 'KEYSTR(answer$, 16, 21, 1)
: ON Q8-125 GOTO 1100, 1050
: GOSUB 'LOWTOUP(SYM(Q6$))
: IF POS("YN" = Q6$) == 0 THEN DO    : REM Not Y or N
:   PRINT HEX(07);                    : REM Bell
:   GOTO 1100
: END DO
```

## POS() — Set Membership Test

`POS(set$ = char$)` checks whether `char$` appears anywhere in `set$`. Returns 0 if not found, position if found. Commonly used to validate single-character inputs against a list of valid values:

```kcml
: IF POS("CDBI" = Q6$) == 0 THEN DO  : REM Q6$ is not C, D, B, or I
:   PRINT HEX(07);                    : REM Bell — invalid input
:   GOTO 1060
: END DO

: IF POS("YN" = Q6$) == 0 THEN ...   : REM Must be Y or N
: ON POS("CDB" = field_type$) GOTO 1110, 1110, 1100  : REM Dispatch on type
```

### POS() with Negation — Reverse Search

`POS(-str$ = substr$)` finds the **last** occurrence of `substr$` in `str$`:

```kcml
: Q9 = POS(-DATADICT$ = "/")         : REM Find last "/" in path
: dir$ = STR(DATADICT$,, Q9-1)       : REM Directory part
: file$ = STR(DATADICT$, Q9+1)       : REM Filename part
```

## LIMITS — Check File Existence

`LIMITS T filename$, a, b, c, type` checks properties of a KDB file. The last parameter (`type`) returns 2 if the file exists and is a valid KDB file:

```kcml
: LIMITS T Q6$, Q8, Q8, Q8, Q9
: IF Q9 <> 2 THEN DO
:   PRINT HEX(07);          : REM Bell — file doesn't exist
:   GOTO 2520               : REM Re-prompt
: END DO
```

## HEXOF, HEXUNPACK, HEXPACK — Hex Conversion

Convert between binary bytes and their hex string representation:

```kcml
REM Binary → hex string for display
: PRINT HEXOF(STR(record$, offset, length))   : REM Shows "1A2B3C..."

: HEXUNPACK binary_str$ TO hex_display$       : REM Same conversion to variable

REM Hex string → binary (user-entered hex back to bytes)
: HEXPACK binary_result$ FROM hex_input$      : REM "1A2B" → binary bytes
: ERROR DO                                     : REM HEXPACK errors on invalid hex
:   PRINT HEX(07);
:   GOTO retry_label
: END DO
```

## BIN() — Create Binary Byte(s)

`BIN(n)` creates a 1-byte binary string with value n. `BIN(n, m)` packs n into m bytes:

```kcml
: STR(record$, offset, 1) = BIN(CODE_BIT)    : REM Store single byte value
: header$ = "N" & BIN(2, 2) & BIN(20) & ALL(HEX(00))  : REM Build binary header
```

Useful for constructing binary file headers and control bytes.

## LINPUT — Raw Input Modes

The `KEYSTR` and `KEYNUM` global routines internally use `LINPUT` with special modifiers:

```kcml
LINPUT -STR(var$,, maxlen)     : REM Input restricted to maxlen chars, no F-key capture
LINPUT ?-STR(var$,, maxlen)    : REM Same but ? prefix enables F-key capture
```

The `-` prefix limits input length to the string's allocated size. The `?` prefix enables function key interception — without it, pressing F1-F31 is ignored.

This is why `ALLOWFNS = TRUE` must be set before KEYSTR/KEYNUM for function keys to work — it controls whether `LINPUT ?-` or `LINPUT -` is used internally.

## $TRAN — String Translation

`$TRAN` translates characters in a string using a mapping table:

```kcml
$TRAN(str$, "AaBbCcDd...")R   : REM R = in-place; pairs = from→to
```

The string after `$TRAN` contains pairs: odd characters are replaced by the following even character. The `R` suffix means replace in-place (without R, returns a new string).

Used in `LOWTOUP` to convert lowercase to uppercase:
```kcml
: $TRAN(SYM(*sym)$, "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")R
```
The string `"AaBb..."` means: replace 'a'→'A', 'b'→'B', etc. (reversed pairs because the mapping goes from→to left-to-right in the pair).

Also used to strip control codes from display strings:
```kcml
: $TRAN(prompt$, HEX(0E3C 0F3E))R   : REM Replace HEX(0E)→'<', HEX(0F)→'>'
```

## VER() — Verify String Pattern

`VER(str$, pattern$)` verifies a string matches a pattern and returns the number of matching characters (0 if no match):

```kcml
REM Pattern characters:
REM  # = any digit (0-9)
REM  - = any non-space character
REM  any other char = literal match

IF VER(date$, "##/##/####") == 10 THEN ...  : REM Valid 10-char date
IF VER(code$, "##/##/##") == 8 THEN ...     : REM Valid 8-char date
IF VER(str$, "--/--/##--") == 10 THEN ...   : REM Two non-space, slash, two non-space, two digits, two non-space
```

## $IF — Poll Stream for Input

`$IF #stream, timeout` checks whether input is available on a stream:

```kcml
: SELECT #gb_h(255) /001           : REM Point stream to keyboard
: result = $IF #gb_h(255), 100     : REM Poll, timeout = 100 (tenths of second?)
: SELECT #gb_h(255) <u$(3)>        : REM Restore stream to terminal
: IF result == 0 THEN ...          : REM 0 = timed out, no input
```

Used in `libWI` to implement timeout behaviour in selection windows. The terminal device is in `u$(3)` (a COM variable holding the current terminal device address).

## NUM() — Count Numeric Characters

`NUM(str$)` returns the count of digit characters in a string:

```kcml
: IF NUM(input$) <> LEN(STR(input$)) THEN ...  : REM Not all digits
: IF NUM(gb_q7$) <> LEN(STR(gb_q7$)) THEN 116  : REM Reject non-numeric input
```

Used in KEYNUM validation: if the number of digit characters doesn't equal the length of the trimmed string, the input isn't a valid number.

## SELECT #stream \<directory\> — Select Stream to Directory

```kcml
SELECT #GB_H(221) <STR(DATADICT$,, Q9-1)>   : REM Select stream to directory path
```

The angle brackets denote directory selection (as opposed to a device address). After this, KI_OPEN on that stream looks for files relative to the selected directory.

## See Also

- [print-input.md](print-input.md) — PRINT, PRINT USING, formatted output
- [control-flow.md](control-flow.md) — IF/ELSE, loops
- [subroutines.md](subroutines.md) — DEFFN, DEFSUB, GOSUB
- [com-chaining.md](com-chaining.md) — COM variables, LOAD, shared state
