# PANIC

> Forces a KCML panic dump — records program state to an XML file for debugging.

## Syntax

```
PANIC
PANIC CONTINUE
PANIC "message"
PANIC CONTINUE "message"
```

## Description

`PANIC` immediately halts execution and writes a diagnostic dump of the current program state (call stack, variable values, program name, line number) to an XML file. In KCML 6+ the dump file is XML format.

`PANIC CONTINUE` writes the dump but allows execution to continue after the panic — useful for non-fatal diagnostics.

An optional string message is included in the dump to provide context.

The dump file is written to the current working directory (or the configured panic directory) as `panic<pid>.xml`.

## Examples

```kcml
REM Force a panic for debugging
DIM x
x = 42
PANIC "Reached debug checkpoint"
$END
```

```kcml
REM Non-fatal panic — log state and continue
DIM status
status = check_status()
IF status <> 0 THEN DO
  PANIC CONTINUE "Unexpected status: " & STR(status)
END DO
REM execution continues here after PANIC CONTINUE
```

```kcml
REM Panic inside error handler
ON ERROR errcode, errmsg$ GOTO 9000
REM ... program code ...
$END

9000 PANIC "Unhandled error " & STR(errcode) & ": " & TRIM(errmsg$)
```

## Panic dump format (KCML 6+)

```xml
<?xml version="1.0"?>
<panic>
  <program>MYPROG</program>
  <line>150</line>
  <message>Reached debug checkpoint</message>
  <variables>
    <var name="x" value="42"/>
  </variables>
</panic>
```

## Notes

- Dump files accumulate — clean them up periodically (`rm panic*.xml`).
- `PANIC` (without CONTINUE) terminates the program after writing the dump.
- `PANIC CONTINUE` is available in KCML 6.x; earlier versions may not support it.
- In a production system, unexpected panics usually indicate a programming error — monitor for panic files.

## See Also

- `ON ERROR` — legacy error capture
- `TRY / CATCH` — structured exception handling
- `$ERR` — current error code
