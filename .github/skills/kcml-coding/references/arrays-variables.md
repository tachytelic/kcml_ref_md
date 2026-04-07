# KCML Arrays and Variables

## Variable Types

| Type | Suffix | Example | Auto-init |
|------|--------|---------|-----------|
| Numeric | (none) | `count`, `total` | 0 |
| String | `$` | `name$`, `buffer$` | spaces |
| Array | `()` | `items(10)`, `grid(5,5)` | 0 or spaces |
| Field | `.` prefix | `.name$`, `.salary` | n/a |
| Global | `@` prefix | `@counter`, `@shared$` | 0 or spaces |
| Constant | `_` prefix | `_MAXSIZE` | set once |

## Declaring Variables

### DIM Statement

```kcml
DIM count                 : REM Numeric scalar
DIM name$50               : REM String of 50 chars
DIM items(100)            : REM 1D numeric array
DIM grid(10, 20)          : REM 2D numeric array
DIM names$(50, 30)        : REM Array of 50 strings, 30 chars each
```

### COM Statement (Persistent)

Variables survive LOAD:

```kcml
COM persistent_counter
COM saved_name$100
```

### LOCAL DIM (Subroutine Scope)

```kcml
DEFSUB 'MyRoutine()
   LOCAL DIM temp$100, i
   : REM temp$ and i only exist in this subroutine
RETURN
```

## Array Operations

### Initialize to Zero/One

```kcml
DIM nums(10)
: nums() = ZER            : REM All zeros
: nums() = CON            : REM All ones
: $END
```

```kcml
DIM scores(5)
: scores() = ZER
: scores(3) = 99
: PRINT scores(1)         : REM 0
: PRINT scores(3)         : REM 99
: $END
```
<!-- UNTESTED -->

### Initialize Strings

```kcml
DIM names$(5, 20)
: names$() = ALL("*")     : REM Fill with asterisks
: names$() = " "          : REM Fill with spaces
: $END
```

```kcml
DIM tags$(3, 4)
: tags$() = ALL("-")
: tags$(2) = "LIVE"
: PRINT tags$(1)           : REM "----"
: PRINT tags$(2)           : REM "LIVE"
: $END
```
<!-- UNTESTED -->

### Array Bounds

Arrays are 1-based. Valid indices: 1 to declared size.

```kcml
DIM arr(10)
: arr(1) = 100            : REM First element
: arr(10) = 999           : REM Last element
: $END
```

```kcml
DIM vals(3)
: vals(1) = 10 : vals(2) = 20 : vals(3) = 30
: DIM i, total
: FOR i = 1 TO 3
:    total += vals(i)
: NEXT i
: PRINT total              : REM 60
: $END
```
<!-- UNTESTED -->

### Dynamic Resizing: MAT REDIM

```kcml
DIM data(0)               : REM Start with size 0
: MAT REDIM data(100)     : REM Grow to 100
: data(50) = 123
: MAT REDIM data(200)     : REM Grow to 200 (preserves data)
: MAT REDIM data(0)       : REM Free memory
: $END
```

```kcml
DIM lines$(0, 80)
: DIM n
: n = 0
: MAT REDIM lines$(++n, 80) : lines$(n) = "First"
: MAT REDIM lines$(++n, 80) : lines$(n) = "Second"
: PRINT lines$(1)          : REM "First"
: PRINT lines$(2)          : REM "Second"
: $END
```
<!-- UNTESTED -->

```kcml
DIM buf(0)
: MAT REDIM buf(5)
: buf() = CON
: PRINT buf(3)             : REM 1  (CON fills with ones)
: MAT REDIM buf(0)         : REM free
: $END
```
<!-- UNTESTED -->

## Matrix Operations

### MAT READ

Read DATA into array:

```kcml
DIM nums(5)
: MAT READ nums()
: DATA 10, 20, 30, 40, 50
: FOR i = 1 TO 5
:    PRINT nums(i)
: NEXT i
: $END
```

### MAT PRINT

Print entire array:

```kcml
DIM nums(3)
: nums(1) = 10 : nums(2) = 20 : nums(3) = 30
: MAT PRINT nums()
: $END
```

### MAT COPY

```kcml
DIM source(5), dest(5)
: source(1) = 1 : source(2) = 2 : source(3) = 3
: MAT COPY source() TO dest()
: $END
```

### MAT SEARCH

Find value in array:

```kcml
DIM arr(10), pos
: MAT READ arr()
: DATA 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
: MAT SEARCH arr() FOR 25 GIVING pos
: PRINT "Found at position: "; pos    : REM 5
: $END
```

```kcml
DIM codes$(5, 4), idx
: codes$(1) = "AABB" : codes$(2) = "CCDD" : codes$(3) = "EEFF"
: codes$(4) = "GGHH" : codes$(5) = "IIJJ"
: MAT SEARCH codes$() FOR "EEFF" GIVING idx
: PRINT idx                           : REM 3
: $END
```
<!-- UNTESTED -->

## Constants

Variables starting with `_` are constants - set once, cannot change:

```kcml
DIM _MAX_ITEMS = 100
DIM _PI = 3.14159
: REM _MAX_ITEMS = 200   : This would cause an error
: PRINT _MAX_ITEMS
: $END
```

Built-in constant: `#PI` = 3.14159265359

```kcml
DIM _VATRATE = 20
DIM price, vat
: price = 100
: vat = price * _VATRATE / 100
: PRINT vat                          : REM 20
: $END
```
<!-- UNTESTED -->

```kcml
DIM _STATUS_LIVE$4 = "LIVE"
DIM _STATUS_ARCH$4 = "ARCH"
DIM rec_status$4
: rec_status$ = _STATUS_LIVE$
: IF rec_status$ == _STATUS_LIVE$ THEN PRINT "Active record"
: $END
```
<!-- UNTESTED -->

## Global Variables

Variables starting with `@` are shared across partitions:

```kcml
DIM @shared_counter
: @shared_counter = @shared_counter + 1
: PRINT "Counter: "; @shared_counter
: $END
```

```kcml
REM Reading a global string declared in the global partition
: PRINT "Company: "; @company_name$
: PRINT "Site:    "; @site_code$
: $END
```
<!-- UNTESTED -->

## Field Variables

Fields define sub-records within strings (like struct members):

```kcml
DIM record$100
DIM .name$30, .age, .salary

: REM Define field positions
: .name$ = 1              : REM Starts at byte 1
: .age = 31               : REM Starts at byte 31
: .salary = 35            : REM Starts at byte 35

: REM Use fields
: STR(record$, .name$, 30) = "John Smith"
: $END
```

## Pointers with SYM()

Reference variables by symbol index:

```kcml
DIM myvar$20, ptr
: myvar$ = "Hello"
: ptr = SYM(myvar$)              : REM Get symbol index
: SYM(*ptr)$ = "World"           : REM Modify via pointer
: PRINT myvar$                   : REM "World"
: $END
```

```kcml
REM SYM() is most commonly used to pass a variable by reference to a library sub
DIM name$30
: name$ = "hello world"
: GOSUB 'LOWTOUP(SYM(name$))     : REM Uppercase in place
: PRINT name$                    : REM "HELLO WORLD"
: $END
```
<!-- UNTESTED -->

```kcml
REM Negative SYM index distinguishes global from local variables
DIM local_var$10, gbl_ptr
: local_var$ = "test"
: PRINT (SYM(local_var$) > 0 ? "local" : "global")   : REM "local"
: $END
```
<!-- UNTESTED -->
