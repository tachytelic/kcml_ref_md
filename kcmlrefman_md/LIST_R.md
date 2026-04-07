# LIST R

> Lists DEFRECORD record definitions and their fields.

## Syntax

```
LIST [title] R [record_name | field_name]
```

## Description

Without arguments: lists all records with their names and total sizes.

With a record name or field name (with leading `.`): shows the full field layout for that record.

```
: LIST R
pstat_record 48
TestRec      409

: LIST R TestRec
TestRec      409
 a                 (1, "SY8")
 b$24              (9, "CHAR(24)")
 c$<<9>>10         (33, "CHAR(10)")
 d(2)              (123,"UINT(3)")
```

The field display shows: `field_name (start_byte, "type_spec")`.

The program must be **resolved** before `LIST R` will work.

## Notes

- Specifying a field name (e.g. `LIST R .b$`) shows the record that defines that field — useful for tracking down which record owns a field.

## See Also

- `DEFRECORD` — define a record structure
- `FLD` — field within a DEFRECORD
- `FLD(` — access a field in a variable
