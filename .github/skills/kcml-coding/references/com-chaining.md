# KCML COM Variables and Program Chaining

How KCML programs share data and chain together using COM variables, LOAD, and CHAIN.

## COM Variables — Persistent Shared Memory

`COM` declares variables that survive a `LOAD` or `CHAIN` operation. They are the primary mechanism for passing data between KCML programs.

```kcml
COM varname$size
COM varname
COM arrayname(dim1)
COM arrayname$size(dim1)
```

### COM in Practice

COM declarations always appear at the very start of a program (before any executable code), typically at line 0 or 1:

```kcml
00000 REM Stock control
    : COM U7$2, PF_COMP, A4$(5)5, N8, N9, USESORT, Q8$124, Q9$124, A9$1, E9$1
00001 COM OE_SP$256, OE_SP_KEY$30, OE_SPDATAPTR$3, OE_SP1(15), OE_SP2(15)
```

Each program in a suite declares the **same** COM variables in the **same order** — this is how they share the memory block. The order and sizes must match exactly across all programs.

### COM Variable Conventions

In real KCML business systems, COM variables follow naming conventions:

| Variable | Type | Purpose |
|----------|------|---------|
| `U7$` | String 2 | Terminal/session identifier suffix |
| `N8`, `N9` | Numeric | General-purpose working numbers |
| `Q8$`, `Q9$` | String 124 | General-purpose working strings |
| `A9$` | String 1 | Last key pressed / action flag |
| `E9$` | String 1 | Error flag |
| `U6$(n)` | String array | User access levels/permissions |

### COM Arrays

COM arrays are declared with the count first, then the size:

```kcml
COM A4$(5)5      : REM Array of 5 strings, each 5 chars
COM OE_SP1(15)   : REM Numeric array of 15 elements
```

## LOAD — Load and Run Another Program

`LOAD` replaces the current program with another. COM variables are preserved.

```kcml
LOAD "programname"              : REM Load and start at default entry
LOAD "programname" linenumber   : REM Load and start at specific line
LOAD "PF/START" 1000            : REM Common pattern: load with entry point
```

### LOAD with BEG (Begin at)

`BEG` specifies a line to branch to after the loaded program initialises:

```kcml
LOAD "PF/GOMEN" 9999 BEG 1200
```

This loads PF/GOMEN, enters at line 9999 (initialisation), and then jumps to line 1200 in the calling program context. The exact semantics depend on how the library program uses BEG.

### Returning to Menu

The standard way to exit a program and return to the menu:

```kcml
: GOSUB 'MESS_BOX("Returning to menu", 0)
: LOAD "PF/START" 1000
```

Or after cleanup:

```kcml
01900 REM End of program
    : GOSUB 'CLOSE_SALES_LEDGER()
    : GOSUB 'CLOSE_PURCHASE_LEDGER()
    : GOSUB 'MESS_BOX("Returning to menu", 0)
    : LOAD "PF/START" 1000
```

### LOAD with Variable

Programs can load dynamically based on a variable:

```kcml
: LOAD N$ 1000             : REM Load program named in N$
: ERROR GOTO 1200          : REM If load fails, goto 1200
```

## COM CLEAR — Reset a COM Variable

Clears a COM string to spaces without affecting other COM variables:

```kcml
COM CLEAR varname$
```

Used when a sub-program stores its return context in a COM variable and needs to clear it on exit:

```kcml
01100 REM Return point for external programs
    : COM CLEAR PF_RSYS$
    : CPAGE = -1
    : GOTO 1050
```

## Conditional Return (Multi-Program Navigation)

Programs often check a COM variable to decide where to return:

```kcml
01900 REM End of program
    : U6$(1) = SV_PRIORITY$
    : IF PF_RSYS$ <> " " THEN 1910
    : GOSUB 'MESS_BOX("Returning to menu", 0)
    : LOAD "PF/START" 1000
01910 REM Return to caller
    : Q6$ = PF_RSYS$ & "/MENU"
    : LOAD Q6$ 1000 BEG 2020
```

Here `PF_RSYS$` is set by whoever called this program to indicate where to return. If blank, go to main menu; if set, return to the calling module's menu.

## DATA Statements and DATA LOAD

`DATA` statements store literal values in the program that can be read at runtime:

```kcml
01800 DATA "PF/DISP  ", " ", " ", " ", " ", 00.00, "1", 01, "Display stock record"
01805 DATA "PF/DTRN2 ", " ", "X", " ", " ", 00.00, "1", 01, "Transaction log enquiry"
```

Reading DATA with DATA LOAD:

```kcml
DATA LOAD DC OPEN T#stream, filename$
```

`DATA LOAD` is used to open transient (T#) data files from DATA statements embedded in the program. This is an older KCML database access pattern.

## Program Structure Conventions

Real KCML programs follow a consistent line number layout:

| Line Range | Purpose |
|------------|---------|
| 0-99 | COM declarations, initialisation, GOSUB library opens |
| 1000 | Main entry point (standard convention) |
| 1200-1900 | Main program loop |
| 1900 | Exit/cleanup routine |
| 2000+ | DEFFN subroutines |
| 9997-9999 | RESAVE / compile metadata lines |

### Metadata Lines (End of File)

Real programs end with special DEFFN lines used by the development environment:

```kcml
09997 DEFFN '26"RESAVE";HEX(22);"PF/MENU.Bre";HEX(22);"1000"
09999 DEFFN '0"PRINT HEX(03):LISTSD1700,";HEX(0D)
```

These are editor macros — ignore them when reading source for logic.

## Passing Parameters via COM

Because LOAD destroys the call stack, programs pass parameters through COM variables:

```kcml
REM Caller sets COM vars before LOAD
: Q6$ = selected_part$
: N8 = selected_locn
: LOAD "PF/DISP" 1090    : REM Enter display at line 1090 (external entry)
```

The called program checks these at its external entry point:

```kcml
01090 REM Entry from elsewhere
    : PF_RSYS$ = Q8$        : REM Remember who called us
    : SV_AC_CODE$ = AC_CODE$
    : IF Q8$ == "OE/EHDR" THEN 1020
```

## CHAIN vs LOAD

`CHAIN` is similar to LOAD but typically used for chaining to a completely separate application rather than within the same program suite. In practice, real code almost always uses `LOAD`.

## $CLOSE — Close Current Program Resources

`$CLOSE` releases all open files and resources for the current program before loading another:

```kcml
: $CLOSE
: GOSUB 'CLOSE_PURCHASE_LEDGER()
: LOAD "PF/START"
```

## Typical Program Entry Points

Programs conventionally support multiple entry points:

| Entry | Description |
|-------|-------------|
| `1000` | Standard start (from menu) |
| `1090` | Entry from another program (external call) |
| `1100` | Return point after sub-program finishes |
| `1200` | Return from menu helper (BEG point) |

## See Also

- [arrays-variables.md](arrays-variables.md) — DIM, variable scope
- [error-handling.md](error-handling.md) — ERROR GOTO pattern
- [screen-io.md](screen-io.md) — Screen display in multi-program apps
- [subroutines.md](subroutines.md) — DEFFN, DEFSUB, GOSUB
