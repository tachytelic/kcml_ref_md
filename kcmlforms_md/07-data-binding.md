# KCML Forms — Data Binding

## Overview

KCML forms offer several approaches to connecting controls to data:

1. **Manual** — set `Text$` in event handlers using `STR()`, KISAM reads, SQL fetches (most common in practice)
2. **Bespoke data awareness** — bind controls to a named variable / field via `DataSource` and `DataField`
3. **DataBind control** — modern binding via `DataBind$` control type with `SetDataField()` / `GetDataField()`
4. **Native KDB data-aware** — automatic binding to KDB table columns (type 7 tables only)

For most real-world work with type 6 KISAM files, **manual** is the right choice. Data binding is most useful with type 7 KDB tables that have an embedded schema.

---

## Manual Binding (Recommended for KISAM)

Read the record, extract fields with `STR()` or `UNPACK`, assign to control `Text$` properties:

```kcml
+ DEFEVENT MyForm.Enter()
    LOCAL DIM rec$1024, part$15, desc$30, qty
    REM ... open and read from KISAM ...
    part$ = STR(rec$, 20, 15)
    desc$ = STR(rec$, 36, 30)
    UNPACK (#########.######) STR(rec$, 513, 8) TO qty
    .txtPart.Text$ = RTRIM(part$)
    .txtDesc.Text$ = RTRIM(desc$)
    .txtQty.Text$ = qty
END EVENT
```

To write back (on OK):

```kcml
+ DEFEVENT MyForm.btnSave.Click()
    LOCAL DIM part$15, desc$30
    part$ = .txtPart.Text$
    desc$ = .txtDesc.Text$
    STR(rec$, 20, 15) = part$
    STR(rec$, 36, 30) = desc$
    CALL KI_REWRITE handle TO ki_status
    .form.Terminate(1)
END EVENT
```

---

## Bespoke Data Awareness

Bind controls to named field variables defined with `DIM`. The control automatically reads/writes the variable when the buffer changes or when the form commits.

### Step 1 — Define field variables

```kcml
: DIM .partno$=(1, 15), .desc$=(16, 30), .qty=(46, "B4")
```

The `(offset, length)` or `(offset, "typespec")` syntax defines a field at a byte position within a buffer.

### Step 2 — Bind controls in DEFFORM

```kcml
{.txtPart,.KCMLedit$,...,.DataSource=row$,.DataField=.partno$}
{.txtDesc,.KCMLedit$,...,.DataSource=row$,.DataField=.desc$}
{.txtQty,.KCMLedit$,...,.DataSource=row$,.DataField=.qty}
```

- `DataSource` = the name of the string variable that holds the record buffer
- `DataField` = the field variable reference

### Step 3 — Load the buffer

When the buffer (`row$`) changes, assign it and call `Flush()` to push to the client:

```kcml
: row$ = rec$         : REM load buffer from KISAM record
: .form.Flush()       : REM update all bound controls from buffer
```

### Step 4 — Write back

When the user changes a bound control, the buffer is updated automatically at the next event boundary. Read it back:

```kcml
: rec$ = row$         : REM updated buffer back to record
```

---

## DataBind Control (KCML 6.x)

The `DataBind$` control type provides more flexible binding, particularly with `DEFRECORD`-defined structures.

### Properties

| Property | Description |
|----------|-------------|
| `Bind` | Variable to bind to |
| `Record` | DEFRECORD structure name |
| `DataField$` | Field name as a string |

### Methods

| Method | Description |
|--------|-------------|
| `SetDataField(field_name$)` | Bind to a named field in the record |
| `SetDataField(col_index, type$)` | Bind to a column by ordinal and type |
| `GetDataField()` | Retrieve current bound value |

### Example with DEFRECORD

```kcml
: DEFRECORD StockRec
:     FLD SR_PART$15
:     FLD SR_DESC$30
:     FLD SR_QTY = "########.##"
: END RECORD
: DIM stock_rec$_StockRec

+ DEFEVENT MyForm.Enter()
    .bindPart.SetDataField("SR_PART$")
    .bindDesc.SetDataField("SR_DESC$")
    .bindQty.SetDataField("SR_QTY")
END EVENT
```

---

## Native KDB Data Awareness (Type 7 Tables)

For type 7 KDB tables, controls can bind directly to table columns using the Object Browser. Drag a column onto the form; the KCML Forms Designer sets `DataSource` and `DataField` automatically.

**This only works with type 7 tables** (those created with `CREATE TABLE` and having an embedded schema). It does not work with type 6 KISAM files.

### KDB Grid Data Awareness

For a grid bound to a KDB query result:

```kcml
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: .grid.DataAwareRow(handle)    : REM populate one row from result set
```

The grid `RowRequest()` event can be used to call `DataAwareRow()` for deferred loading.

---

## Grid Data Loading Pattern (Manual, Most Common)

Even when not using formal data binding, a consistent pattern makes grid loading clean:

```kcml
01500 DEFFN 'LOAD_GRID()
    LOCAL DIM ki_status, ki_sym, ki_dataptr$6, ki_key$64
    LOCAL DIM rec$1024, row, part$15, desc$30, qty
    .grid.Rows = 1
    CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
    CALL KI_OPEN handle, "/data/S_STOK01", "R" TO ki_status
    IF ki_status <> 0 THEN RETURN
    CALL KI_START_BEG handle, 1 TO ki_status
    ki_sym = SYM(rec$)
    row = 1
    REPEAT
        CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
        IF ki_status == 0 THEN DO
            row++
            .grid.Rows = row
            part$ = STR(rec$, 20, 15)
            desc$ = STR(rec$, 36, 30)
            UNPACK (#########.######) STR(rec$, 513, 8) TO qty
            .grid.Cell(row, 1).Text$ = RTRIM(part$)
            .grid.Cell(row, 2).Text$ = RTRIM(desc$)
            .grid.Cell(row, 3).Text$ = qty
            .grid.Cell(row, 1).LeftAction = &.Click
            .grid.Cell(row, 2).LeftAction = &.Click
            .grid.Cell(row, 3).LeftAction = &.Click
            .grid.LeftSelect = &.Row
            IF MOD(row,2)==0 THEN .grid.Cell(row,0).BackColor = &.clrAlt
            IF MOD(row,2)<>0 THEN .grid.Cell(row,0).BackColor = &.Default
        END DO
    UNTIL ki_status <> 0
    CALL KI_CLOSE handle TO ki_status
    CALL KI_FREE_HANDLE handle TO ki_status
    .pane1.Text$ = (row-1) & " records"
    RETURN
```
