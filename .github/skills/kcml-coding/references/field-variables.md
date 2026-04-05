# KCML Field Variables and DEFRECORD

Field variables are named offsets into string buffers — the primary mechanism for accessing structured record data in KCML. They replace raw `STR(record$, offset, length)` calls with readable named access.

## The Problem They Solve

Without field variables:
```kcml
REM Hard to read, fragile if record layout changes
: part_no$ = STR(pf_rec$, 1, 16)
: description$ = STR(pf_rec$, 17, 40)
: unit_price = UNPACK("-########.##") STR(pf_rec$, 57, 10)
```

With field variables:
```kcml
: part_no$ = FLD(pf_rec$.part_no$)
: description$ = FLD(pf_rec$.description$)
: unit_price = FLD(pf_rec$.unit_price)
```

---

## Defining Field Variables

### Method 1: DEFRECORD (Recommended)

`DEFRECORD` defines a named record structure. KCML automatically calculates offsets:

```kcml
DEFRECORD StockRecord
  FLD part_no$16
  FLD description$40
  FLD unit_price = "-########.##"   : REM Packed numeric — image defines size
  FLD qty_in_stock = "######"        : REM 6-digit packed integer
  FLD location$4
END RECORD
```

This creates a constant `_StockRecord` equal to the total byte size of the record. Use it to dimension record buffers:

```kcml
DIM pf_rec$_StockRecord    : REM Exactly the right size
```

### Method 2: Explicit DIM with Offset/Length

Field variables start with a period (`.`) and store `(start, length)` pairs:

```kcml
DIM .part_no$ = (1, 16)
DIM .description$ = (17, 40)
DIM .unit_price = (57, "-########.##")   : REM Numeric — length from image
DIM .location$ = (67, 4)
```

Or use `DATA` to avoid manual offset calculation:

```kcml
READ .part_no$, .description$, .unit_price, .location$
DATA (1,16), (,40), (,"-########.##"), (,4)   : REM Omit start = auto-calculate
```

### Method 3: Global/Library Fields

If a field is not found in the executing program, KCML searches loaded libraries and then selected global partitions. This allows record layouts to be defined once in a library and used everywhere.

---

## Using Field Variables

### Reading a Field (Alpha)

```kcml
: part_no$ = FLD(pf_rec$.part_no$)
: PRINT FLD(pf_rec$.description$)
```

### Writing a Field (Alpha)

```kcml
: FLD(pf_rec$.part_no$) = "WIDGET-001"
: FLD(pf_rec$.location$) = "A12B"
```

### Numeric Fields — PACK/UNPACK Automatically

Numeric field variables automatically pack/unpack when read or written:

```kcml
REM Read (auto-unpacks)
: price = FLD(pf_rec$.unit_price)
: qty = FLD(pf_rec$.qty_in_stock)

REM Write (auto-packs)
: FLD(pf_rec$.unit_price) = 99.95
: FLD(pf_rec$.qty_in_stock) = 150
```

### Shorthand Operators Work

```kcml
: FLD(pf_rec$.qty_in_stock) += 10       : REM Increment
: FLD(pf_rec$.unit_price) *= discount    : REM Multiply in place
```

Avoid `++`/`--` with numeric fields — it works but is slower (unpack, change, repack).

---

## The FLD() Function — Access Any String

`FLD(string$.fieldname)` applies the field definition to any string variable:

```kcml
REM Same field definition, different record buffers
: part_a$ = FLD(record1$.part_no$)
: part_b$ = FLD(record2$.part_no$)

REM Works with array elements
: FLD(records$(i).description$) = new_desc$
```

---

## Array Field Access

Pack/unpack whole arrays with a single field operation:

```kcml
DIM prices(5)
.price_field = (1, "-####.##")    : REM 8 bytes per element

REM Unpack 5 consecutive prices from record
: prices() = FLD(price_record$.price_field)

REM Pack 5 prices back into record
: FLD(price_record$.price_field) = prices()

REM Access individual element by index
: second_price = FLD(price_record$.price_field<2>)
```

---

## Condition Testing

Field variables can be tested in IF statements:

```kcml
IF (.part_no$ == .search_key$)   : REM Compare two field specifications
IF (FLD(rec$.status$) == "A") THEN ...
IF (.legs$ <> (5, 9)) THEN ...   : REM Compare field spec against literal spec
```

---

## POS() and LEN() with Fields

```kcml
DIM .color$ = (6, 5)
: PRINT POS(.color$)    : REM 6  (start position)
: PRINT LEN(.color$)    : REM 5  (field length)
```

---

## Passing Fields to Subroutines

Field variables can be passed into `GOSUB '` calls:

```kcml
: GOSUB 'qsort(.name$, (2,"#.#"), (9,9), .ab())
```

The DEFSUB receives them as field parameters:

```kcml
DEFSUB 'qsort(.nm$, .num, .type$, .totals())
:   REM .nm$, .num, .type$ are local field variables
: END SUB
```

---

## Real-World Pattern: Record Layout from Library

In real ERP code, record layouts are defined in libraries or globals, then used identically across all programs:

```kcml
REM In library (StockRecord defined once)
DEFRECORD StockRecord
  FLD PF_PART_NO$16
  FLD PF_DESC$40
  FLD PF_COST = "-########.##"
  FLD PF_PRICE = "-########.##"
  FLD PF_QTY = "######"
  FLD PF_LOCN$4
END RECORD

REM In every program that uses stock records
DIM pf_rec$_StockRecord

REM Usage — readable, layout-independent
: PRINT FLD(pf_rec$.PF_PART_NO$)
: FLD(pf_rec$.PF_QTY) -= qty_sold
```

---

## DEFRECORD Constants

`DEFRECORD` automatically creates a constant named `_RecordName`:

```kcml
DEFRECORD Fred
  FLD a
  FLD b
END RECORD

DIM FredRec$_Fred    : REM _Fred = total byte size of record
```

---

## Inline Field Definitions (Without DEFRECORD)

Field variables can be defined inline without a name, useful for one-off access:

```kcml
REM Access bytes 5-9 of any string inline
: value$ = FLD(record$.(5, 5))

REM Unpack a number from a specific position
: amount = FLD(record$.(10, "-#####.##"))
```

---

## FLD() vs STR() Performance

`FLD()` is measurably faster than `STR()` for repeated sub-string access because:
- The offset/length is resolved at compile time (for named fields)
- No runtime offset calculation needed for each access

In tight loops processing many records, prefer `FLD()` over `STR()`.

---

## LIST DIM with Fields

`LIST DIM` shows field variables with type `D` (vs `C` for COM, `L` for local):

```
LIST DIM
D .name$         (1, 30)
D .balance       (31, "-#######.##")
D .status$       (41, 1)
```

---

## See Also

- [arrays-variables.md](arrays-variables.md) — DIM, COM, PACK/UNPACK
- [global-partitions.md](global-partitions.md) — Field definitions in globals/libraries
- [subroutines.md](subroutines.md) — Passing fields into DEFSUB
- [string-functions.md](string-functions.md) — STR(), LEN(), POS()
