# pik_to_json.src

Extracts a picking note from the KISAM Order Entry database and emits a JSON
object to stdout.

## Usage

```bash
/usr/local/bin/kcml -x /usr/lib/kcml/uf_json.so -p pik_to_json.src <sop_dir> <picking_note_number>
```

| Argument | Example | Description |
|----------|---------|-------------|
| `sop_dir` | `/user1/kopen/sop` | Directory containing the OE database files |
| `picking_note_number` | `114315` | Numeric picking note number |

## Data sources

The program reads three database files, all in `sop_dir`:

### Phase 1 — OEPIK01 (scan)

Scanned in full from the beginning (`KI_START_BEG`). Records matching
`Picking Note No == target` are collected into line buffers (up to 50 lines).

| Field | Offset | Len | Type | Used for |
|-------|-------:|----:|------|----------|
| Order Number | 18 | 10 | C | Key for OEHDR01 lookup |
| Part number | 62 | 15 | C | Line item part number |
| Picking Note No | 110 | 4 | I | Filter — must equal target |
| Qty to Pick | 118 | 8 | I dec=6 | Invoice quantity |
| Advice Note Date | 154 | 4 | D | Document date |

### Phase 2 — OEHDR01 (direct key lookup)

Positioned with `KI_START` on the order number from Phase 1 (key field is
Order Number at offset 18). One record read.

| Field | Offset | Len | Type | Used for |
|-------|-------:|----:|------|----------|
| SA Account | 48 | 6 | C | `accNum` |
| Customer Reference | 58 | 24 | C | `cusRef` |
| Order Date | 82 | 4 | D | `orderDate` |
| Delivery A/c Name | 114 | 30 | C | Delivery address line 1 |
| Delivery Address 1–4 | 144–234 | 30 | C | Delivery address lines |
| Invoice A/c Name | 264 | 30 | C | Invoice address line 1 |
| Invoice Address 1–4 | 294–384 | 30 | C | Invoice address lines |
| Sales Rep | 557 | 4 | C | `RepCode` |
| Delivery Method | 561 | 24 | C | `DeliveryMethod` |
| Delivery Postcode | 1112 | 8 | C | Delivery address postcode |
| Invoice Postcode | 1120 | 8 | C | Invoice address postcode |

### Phase 3 — OEENT01 (scan)

Scanned in full. Records where `Order Number (off=378)` matches the order
number from Phase 1 are collected into match buffers (up to 100 entries).
Matched against Phase 1 lines by part number to enrich the output.

| Field | Offset | Len | Type | Used for |
|-------|-------:|----:|------|----------|
| Part number | 19 | 15 | C | Join key to OEPIK01 lines |
| Description 1 | 91 | 30 | C | `description` |
| Description 2 | 121 | 30 | C | `lineFreeText` |
| Qty to follow | 186 | 8 | I dec=6 | `toFollow` |
| Order Number | 378 | 10 | C | Filter — must equal order number |

## JSON output

```json
{
  "docType": "PickingNote",
  "brand": "AustenTapes",
  "docRef": "114315",
  "accNum": "CYP637",
  "cusRef": "JULIE WHIKE",
  "orderNumber": "133201",
  "DeliveryMethod": "",
  "RepCode": "50",
  "orderDate": "10/04/2026",
  "documentDate": "10/04/2026",
  "invoiceAddress": ["CYPRIUM LIMITED,", "UNIT 3, REDGRAVE BUS. CENTRE,", "..."],
  "deliveryAddress": ["CYPRIUM LIMITED,", "UNIT 3, REDGRAVE BUS. CENTRE,", "..."],
  "docLines": [
    {
      "partno": "856110033",
      "description": "PU PROTECTION TAPE - 8561",
      "qty": "1",
      "toFollow": "0 TO FOLLOW",
      "lineFreeText": "100MM X 33M (4\" X 36yds)"
    }
  ]
}
```

## Notes

- Quantities are output as integers via `INT()` — fractional quantities are
  not currently supported.
- The document date (`documentDate`) comes from the `Advice Note Date` field
  on OEPIK01, not from OEHDR01.
- The `toFollow` value is taken from OEENT01 `Qty to follow`; by the time an
  invoice is raised this will typically be 0.
- Line items are ordered by their position in the OEPIK01 scan, which reflects
  the B-tree key order (Order Number + sequence within order).
