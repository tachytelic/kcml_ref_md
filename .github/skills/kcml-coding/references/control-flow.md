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
