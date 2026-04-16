# inv_to_json.src

Extracts a sales invoice from the KISAM Sales Ledger and Order Entry databases
and emits a JSON object to stdout.

## Usage

```bash
/usr/local/bin/kcml -x /usr/lib/kcml/uf_json.so -p inv_to_json.src <sop_dir> <accounts_dir> <invoice_number>
```

| Argument | Example | Description |
|----------|---------|-------------|
| `sop_dir` | `/user1/kopen/sop` | Directory containing the OE database files |
| `accounts_dir` | `/user1/kopen/accounts` | Directory containing the SL database files |
| `invoice_number` | `153132` | Numeric invoice number from SPOOLMAST description |

## Data sources

Five database files are read across two directories. The program executes in
five sequential phases.

### Phase 1 — SALINV01 (scan, accounts_dir)

Scanned in full from the beginning. The record whose `Invoice Number` equals
the target is located. This gives the customer code, invoice date, and totals.

| Field | Offset | Len | Type | Used for |
|-------|-------:|----:|------|----------|
| Transaction Type | 20 | 1 | C | `transactionType` (`I` = invoice) |
| Invoice Date | 22 | 4 | D | `invoiceDate` |
| Invoice Number | 72 | 4 | I | Filter — must equal target |
| Customer Code | 62 | 6 | C | Key for SALLED01 lookup and `accNum` |
| Reference | 76 | 14 | C | `reference` (typically the order number) |
| Invoice Value (Base) | 90 | 8 | I dec=6 | `invoiceValue` (£, 2 dp) |
| VAT Value (Base) | 106 | 8 | I dec=6 | `vatValue` (£, 2 dp) |
| Narrative | 236 | 30 | C | `narrative` |

### Phase 2 — OEPIK01 (scan, sop_dir)

Scanned in full. Records where `Invoice No == target` are collected as invoice
lines (up to 50). The `Order Number` from the first matching record is used
for the OEHDR01 and OEENT01 lookups.

| Field | Offset | Len | Type | Used for |
|-------|-------:|----:|------|----------|
| Order Number | 18 | 10 | C | Key for OEHDR01 and OEENT01 |
| Part number | 62 | 15 | C | Line item part number |
| Invoice No | 102 | 4 | I | Filter — must equal target invoice number |
| Qty Picked | 126 | 8 | I dec=6 | Invoiced quantity |

### Phase 3 — OEHDR01 (direct key lookup, sop_dir)

Positioned with `KI_START` on the order number from Phase 2 (key field is
Order Number at offset 18). One record read.

| Field | Offset | Len | Type | Used for |
|-------|-------:|----:|------|----------|
| Customer Reference | 58 | 24 | C | `cusRef` |
| Order Date | 82 | 4 | D | `orderDate` |
| Delivery A/c Name | 114 | 30 | C | Delivery address line 1 |
| Delivery Address 1–4 | 144–234 | 30 | C | Delivery address lines |
| Invoice A/c Name | 264 | 30 | C | Invoice address line 1 |
| Invoice Address 1–4 | 294–384 | 30 | C | Invoice address lines |
| Payment Terms | 414 | 20 | C | `paymentTerms` |
| Additional Text 1–4 | 435–525 | 30 | C | `orderText` array |
| Sales Rep | 557 | 4 | C | `salesRep` |
| Delivery Method | 561 | 24 | C | `deliveryMethod` |
| VAT Number | 1066 | 20 | C | `vatNumber` |
| Delivery Postcode | 1112 | 8 | C | Delivery address postcode |
| Invoice Postcode | 1120 | 8 | C | Invoice address postcode |

### Phase 4 — SALLED01 (direct key lookup, accounts_dir)

Positioned with `KI_START` on the customer code from Phase 1 (key field is
Customer Code at offset 18). One record read to get the customer name.

| Field | Offset | Len | Type | Used for |
|-------|-------:|----:|------|----------|
| Customer Name | 33 | 30 | C | `customerName` |

### Phase 5 — OEENT01 (scan, sop_dir)

Scanned in full. Records where `Order Number (off=378)` matches the order
from Phase 2 are collected (up to 100 entries). Matched against Phase 2 lines
by part number to add descriptions, unit price, UOM, and VAT code.

| Field | Offset | Len | Type | Used for |
|-------|-------:|----:|------|----------|
| Part number | 19 | 15 | C | Join key to OEPIK01 lines |
| Description 1 | 91 | 30 | C | `description` |
| Description 2 | 121 | 30 | C | `lineFreeText` |
| Unit of Measure | 151 | 6 | C | `uom` |
| VAT Code | 167 | 1 | C | `vatCode` |
| Selling Price | 202 | 8 | I dec=6 | `unitPrice` (6 dp) |
| Order Number | 378 | 10 | C | Filter — must equal order number |

## JSON output

```json
{
  "docType": "Invoice",
  "brand": "AustenTapes",
  "docRef": "153132",
  "accNum": "CYP637",
  "cusRef": "JULIE WHIKE",
  "customerName": "CYPRIUM LIMITED,",
  "orderNumber": "133323",
  "invoiceDate": "10/04/2026",
  "orderDate": "10/04/2026",
  "invoiceValue": "598.20",
  "vatValue": "99.70",
  "transactionType": "I",
  "narrative": "JULIE WHIKE",
  "reference": "133323",
  "salesRep": "50",
  "deliveryMethod": "",
  "paymentTerms": "Monthly Account",
  "vatNumber": "",
  "orderText": [],
  "invoiceAddress": ["CYPRIUM LIMITED,", "UNIT 3, REDGRAVE BUS. CENTRE,", "..."],
  "deliveryAddress": ["CYPRIUM LIMITED,", "UNIT 3, REDGRAVE BUS. CENTRE,", "..."],
  "docLines": [
    {
      "partno": "856110033",
      "description": "PU PROTECTION TAPE - 8561",
      "uom": "ROLL",
      "vatCode": "S",
      "unitPrice": "498.500000",
      "qty": "1",
      "lineFreeText": "100MM X 33M (4\" X 36yds)"
    }
  ]
}
```

## Notes

- `invoiceValue` and `vatValue` are the base-currency (GBP) totals from the
  Sales Ledger transaction record, formatted to 2 decimal places.
- `unitPrice` is the selling price per unit from the Order Entry line,
  formatted to 6 decimal places to preserve pricing precision.
- Quantities are output as integers via `INT()`.
- Invoice lines are sourced from OEPIK01 (the picking records that were
  dispatched against this invoice), not from OEENT01 directly. OEENT01 is
  used only to enrich those lines with description, price, and UOM.
- If no OEPIK01 records are found for the invoice number the program exits
  with `{"error": "No picking lines found in OEPIK01 for this invoice"}`.
  This would occur for non-stock or manually-raised invoices.
- The `narrative` field on SALINV01 often holds the customer contact name
  rather than a description.
