# @UNLOCK

> Releases the advisory lock on the currently SELECTed global partition that was acquired with `@LOCK`.

## Syntax

```
@UNLOCK
```

## Description

`@UNLOCK` releases a lock previously acquired with `@LOCK` in the current partition. Any other partitions that are sleeping waiting for `@LOCK` on the same global will then be allowed to proceed.

If no global has been selected, or if no `@LOCK` is currently outstanding, `@UNLOCK` has no effect.

## Notes

- Must be called after every `@LOCK` — failing to unlock causes other partitions to hang indefinitely.
- Only applies to process globals, not memory-mapped globals.

## Example

```kcml
@LOCK
IF @lock_flag = 0 THEN @lock_flag = #PART
@UNLOCK
```

## See Also

- `@LOCK` — acquire the advisory lock
- `SELECT @PART` — select the global partition to operate on
