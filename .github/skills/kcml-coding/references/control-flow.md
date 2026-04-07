# KCML Control Flow

## Statement Separator

KCML uses `:` (colon) to separate statements. For script execution with `kcml -p`:

```kcml
REM Single line style
DIM x : x = 1 : PRINT x : $END

REM Continuation style (each line starts with :)
DIM x
: x = 1
: PRINT x
: $END
```

## IF-THEN-ELSE (Single Line)

```kcml
IF condition THEN statement ELSE statement
```

```kcml
DIM x
: x = 10
: IF x > 5 THEN PRINT "Big" ELSE PRINT "Small"
: $END
```

```kcml
DIM qty
: qty = 0
: IF qty == 0 THEN PRINT "Out of stock" ELSE PRINT "In stock: "; qty
: $END
```
<!-- UNTESTED -->

```kcml
DIM code$1
: code$ = "Y"
: IF code$ == "Y" THEN PRINT "Yes" ELSE IF code$ == "N" THEN PRINT "No" ELSE PRINT "Unknown"
: $END
```
<!-- UNTESTED -->

## IF-ENDIF (Multi-line Block)

```kcml
DIM x
: x = 10
: IF x > 5 THEN
:    PRINT "x is greater than 5"
:    PRINT "Processing large value"
: ELSE
:    PRINT "x is 5 or less"
: ENDIF
: $END
```

```kcml
DIM balance
: balance = -50
: IF balance < 0 THEN
:    PRINT "Overdrawn"
:    PRINT "Amount: "; balance
: ELSE IF balance == 0 THEN
:    PRINT "Zero balance"
: ELSE
:    PRINT "In credit: "; balance
: ENDIF
: $END
```
<!-- UNTESTED -->

```kcml
DIM flag
: flag = 1
: IF flag THEN
:    PRINT "Flag is set"
: ENDIF
: $END
```
<!-- UNTESTED -->

## FOR Loop

```kcml
FOR variable = start TO end [STEP increment]
   statements
NEXT variable
```

```kcml
DIM i
: FOR i = 1 TO 5
:    PRINT "Count: "; i
: NEXT i
: $END
```

With STEP:
```kcml
DIM i
: FOR i = 10 TO 1 STEP -2
:    PRINT i
: NEXT i
: $END
```
Output: 10, 8, 6, 4, 2

```kcml
DIM i, total
: total = 0
: FOR i = 1 TO 100
:    total += i
: NEXT i
: PRINT total              : REM 5050
: $END
```
<!-- UNTESTED -->

```kcml
DIM i
: FOR i = 0 TO 15 STEP 5
:    PRINT i
: NEXT i
: REM Output: 0  5  10  15
: $END
```
<!-- UNTESTED -->

## WHILE Loop

```kcml
WHILE condition
   statements
WEND
```

```kcml
DIM x
: x = 1
: WHILE x <= 5
:    PRINT x
:    x = x + 1
: WEND
: $END
```

```kcml
DIM n, sum
: n = 1 : sum = 0
: WHILE n <= 10
:    sum += n
:    n++
: WEND
: PRINT sum                : REM 55
: $END
```
<!-- UNTESTED -->

```kcml
DIM attempts
: attempts = 0
: WHILE attempts < 3
:    PRINT "Attempt: "; attempts + 1
:    attempts++
: WEND
: $END
```
<!-- UNTESTED -->

## DO-LOOP (REPEAT-UNTIL)

```kcml
DO
   statements
LOOP UNTIL condition

REM Or with WHILE
DO
   statements
LOOP WHILE condition
```

```kcml
DIM x
: x = 1
: DO
:    PRINT x
:    x = x + 1
: LOOP UNTIL x > 5
: $END
```

```kcml
DIM total, n
: total = 0 : n = 0
: DO
:    n++
:    total += n
: LOOP WHILE total < 20
: PRINT "Stopped at n="; n; " total="; total
: $END
```
<!-- UNTESTED -->

## REPEAT-UNTIL

```kcml
DIM x
: x = 1
: REPEAT
:    PRINT x
:    x = x + 1
: UNTIL x > 5
: $END
```

```kcml
DIM i
: i = 10
: REPEAT
:    PRINT i
:    i -= 3
: UNTIL i <= 0
: REM Output: 10  7  4  1
: $END
```
<!-- UNTESTED -->

## SELECT CASE

```kcml
SELECT CASE expression
   CASE value1
      statements
   CASE value2, value3
      statements
   CASE ELSE
      statements
END SELECT
```

```kcml
DIM day
: day = 3
: SELECT CASE day
:    CASE 1
:       PRINT "Monday"
:    CASE 2
:       PRINT "Tuesday"
:    CASE 3
:       PRINT "Wednesday"
:    CASE 4, 5
:       PRINT "Thu or Fri"
:    CASE ELSE
:       PRINT "Weekend"
: END SELECT
: $END
```

```kcml
DIM status$1
: status$ = "A"
: SELECT CASE status$
:    CASE "A"
:       PRINT "Active"
:    CASE "S"
:       PRINT "Suspended"
:    CASE "D"
:       PRINT "Deleted"
:    CASE ELSE
:       PRINT "Unknown status: "; status$
: END SELECT
: $END
```
<!-- UNTESTED -->

```kcml
DIM score
: score = 75
: SELECT CASE score
:    CASE 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100
:       PRINT "Distinction"
:    CASE 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,\
:         80, 81, 82, 83, 84, 85, 86, 87, 88, 89
:       PRINT "Pass"
:    CASE ELSE
:       PRINT "Fail"
: END SELECT
: $END
```
<!-- UNTESTED -->

## BREAK and CONTINUE

Exit or skip iterations in loops:

```kcml
DIM i
: FOR i = 1 TO 10
:    IF i = 3 THEN CONTINUE    : REM Skip 3
:    IF i = 7 THEN BREAK       : REM Exit at 7
:    PRINT i
: NEXT i
: $END
```
Output: 1, 2, 4, 5, 6

```kcml
DIM i, first_neg
: DIM arr(6)
: arr(1) = 5 : arr(2) = 3 : arr(3) = -1 : arr(4) = 8 : arr(5) = 2 : arr(6) = -4
: FOR i = 1 TO 6
:    IF arr(i) < 0 THEN first_neg = arr(i) : BREAK
: NEXT i
: PRINT first_neg          : REM -1
: $END
```
<!-- UNTESTED -->

```kcml
DIM i, evens$60
: FOR i = 1 TO 10
:    IF MOD(i, 2) <> 0 THEN CONTINUE   : REM skip odd numbers
:    DIM num_s$4
:    CONVERT i TO num_s$,(##)
:    evens$ = evens$ & LTRIM(num_s$) & " "
: NEXT i
: PRINT evens$             : REM "2 4 6 8 10 "
: $END
```
<!-- UNTESTED -->

Works with `FOR...NEXT`, `WHILE...WEND`, and `REPEAT...UNTIL`. 

**Constraint:** BREAK must physically appear inside the loop body — it cannot be inside a subroutine called from within the loop. The BREAK/loop pairing is checked at compile time.

## GOSUB / RETURN

Call subroutines by line number:

```kcml
10 GOSUB 100
20 PRINT "Back from subroutine"
30 $END
100 REM Subroutine
110 PRINT "In subroutine"
120 RETURN
```

## Named Subroutines

```kcml
DIM result
: GOSUB 'Calculate(5, 3)
: PRINT "Result: "; result
: $END
: DEFSUB 'Calculate(a, b)
:    result = a + b
: RETURN
```

## ON-GOTO / ON-GOSUB

Branch based on numeric value:

```kcml
DIM choice
: choice = 2
: ON choice GOTO 100, 200, 300
: PRINT "Invalid choice"
: $END
100 PRINT "Option 1" : $END
200 PRINT "Option 2" : $END
300 PRINT "Option 3" : $END
```

```kcml
REM ON-GOSUB dispatches to a subroutine by index
DIM op
: op = 2
: ON op GOSUB 'AddRec, 'EditRec, 'DeleteRec
: $END
: DEFSUB 'AddRec()    : PRINT "Add"    : RETURN
: DEFSUB 'EditRec()   : PRINT "Edit"   : RETURN
: DEFSUB 'DeleteRec() : PRINT "Delete" : RETURN
```
<!-- UNTESTED -->

```kcml
REM Q8-125 trick: map key codes 126,127 to 1,2 for ON-GOTO
DIM Q8
: Q8 = 126                 : REM simulate back-tab key
: ON Q8-125 GOTO 300, 400  : REM Q8=126 -> 1 -> 300; Q8=127 -> 2 -> 400
: PRINT "Enter key (Q8=0 falls through)"
: $END
300 PRINT "Back-tab pressed" : $END
400 PRINT "Escape pressed"   : $END
```
<!-- UNTESTED -->
