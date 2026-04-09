# $LIC(

> Reads a value from the KCML licence file.

## Syntax

```
alpha_receiver = $LIC(section$, key$)
```

## Description

`$LIC(` retrieves a key value from a named section of the KCML licence file. Both `section$` and `key$` are case-insensitive. Returns a blank string if the section or key is not found.

`$LIC(` is only valid on the right-hand side of a `LET`/assignment statement.

> The `[General]` section of the licence file cannot be inspected with `$LIC(`.

### Common sections and keys

| Section | Key | Purpose |
|---------|-----|---------|
| `KCML` | `Users` | Maximum concurrent KCML users |
| `Kclient` | `Users` | Maximum concurrent Kclient connections |
| `ODBC` | `Users` | Maximum concurrent ODBC users |
| `Kprint` | `Users` | Number of supported printers |

## Examples

### Example 1 — Read the KCML user licence count
```kcml
01000 REM Read KCML licence user limit
: DIM lic$20
: lic$ = $LIC("KCML","Users")
: PRINT "KCML licence Users: " ; RTRIM(lic$)
: $END
```
**Output** (result depends on installed licence):
```
KCML licence Users: 
```
> A blank result means either the section/key doesn't exist or the `[General]` section was queried.

### Example 2 — Check licence before starting a service
```kcml
01000 REM Check Kclient licence before starting
: DIM users$10
: users$ = $LIC("Kclient","Users")
: IF RTRIM(users$) == "" THEN PRINT "No Kclient licence found"
: IF RTRIM(users$) <> "" THEN PRINT "Kclient licenced for " ; RTRIM(users$) ; " users"
: $END
```

### Example 3 — Read print licence
```kcml
01000 REM Check Kprint licence
: DIM printers$10
: printers$ = $LIC("Kprint","Users")
: PRINT "Kprint licence: " ; RTRIM(printers$)
: $END
```

## Notes

- Returns a blank string for unknown sections/keys — does not error.
- Section and key names are case-insensitive.
- The `[General]` section is protected and always returns blank.
- Only valid on the right-hand side of assignment.
