# ERR$(

> Returns the descriptive error message text for a given KCML error code.

## Syntax

```
ERR$( error_code )
```

| Parameter | Description |
|-----------|-------------|
| `error_code` | An integer expression from 0 to 99 |

Returns an alpha string. Valid wherever a string expression is legal. **Use only once per statement** — using it more than once in the same statement gives unexpected results.

## Description

`ERR$(` looks up the text description for a KCML error code number. The messages are stored in the text file `berror.d` in the KCML directory (and can be customised according to instructions at the start of that file).

KCML often has multiple messages for a given error code (to be more specific about the nature of the problem). `ERR$(` always returns the **first** entry in the file for the given code.

From KCML 6.0+, `$ERR` is equivalent to `ERR$(ERR)` and returns the most recent error message (possibly more specific than `ERR$(`).

## Examples

### Look up error codes

```kcml
: PRINT ERR$(73)
: PRINT ERR$(82)
: PRINT ERR$(83)
: $END
```

Output:
```
Illegal input data
File not found
File already catalogued
```

### Use with ERR after an error

```kcml
errcode = ERR
PRINT ERR$(errcode)
```

### Common pattern in TRY/CATCH

```kcml
TRY
    OPEN #1, filename$, INPUT
CATCH
    errcode = ERR
    errmsg$ = ERR$(errcode)
    PRINT "Error "; errcode; ": "; errmsg$
END TRY
```

## Notes

- Call `ERR$(` only once per statement. Multiple calls in the same statement give unexpected results.
- `ERR$(ERR)` is the canonical way to get the last error message; `$ERR` is a shorthand.
- `ERR` is reset to 0 after being read; always copy it before calling `ERR$()`.

## See Also

- `ERR` — numeric error code of the last error
- `$ERR` — last error message text (KCML 6.0+)
- `$OSERR` — last OS-level error string
- `TRY` / `CATCH` — structured error handling
- `ERROR` — old-style per-statement error trap
