# STOP PANIC

> Makes STOP statements behave like PANIC (dump and terminate).

## Syntax

```
STOP PANIC ON
STOP PANIC OFF
```

## Description

`STOP PANIC ON` — instructs KCML to treat all subsequent `STOP` statements as `PANIC` statements (write a diagnostic dump and terminate rather than entering the debugger).

`STOP PANIC OFF` — restores the original STOP behaviour (enter debugger).

Useful when deploying code that still has `STOP` statements as debugging stubs — with `STOP PANIC ON`, they produce diagnostic dumps in production rather than hanging in the debugger.

### NOPROG interaction

When the `NOPROG` environment variable is set and `STOP PANIC` is active, entering immediate mode also triggers a PANIC.

## Examples

```kcml
STOP PANIC ON
REM  All STOP statements from here on behave like PANIC
STOP         : REM  writes panic dump and terminates
```

```kcml
STOP PANIC OFF
STOP         : REM  enters debugger as normal
```

## See Also

- `STOP` — halt and enter debugger
- `PANIC` — force diagnostic dump and terminate
