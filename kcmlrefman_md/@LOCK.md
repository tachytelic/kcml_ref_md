# @LOCK

> Advisory-locks the currently SELECTed global partition so that other partitions block if they also try to `@LOCK` the same global.

## Syntax

```
@LOCK
```

## Description

`@LOCK` implements advisory locking on the currently selected global partition (selected with `SELECT @PART`). After a `@LOCK`, other partitions can still read or write global variables freely, but if another partition issues its own `@LOCK` on the same global, it will sleep until the lock is released with `@UNLOCK`.

If no global partition has been selected, `@LOCK` has no effect.

Only implemented for **process globals** — not for memory-mapped globals.

Advisory locking is cooperative: it relies on all code paths using `@LOCK`/`@UNLOCK` consistently. Code that doesn't call `@LOCK` can still access the global without restriction.

## Notes

- Must be paired with `@UNLOCK` to release the lock.
- Failing to `@UNLOCK` will cause other partitions to hang indefinitely.
- Use this to protect read-modify-write sequences on global variables.

## Example

```kcml
@LOCK
IF @lock_flag = 0 THEN @lock_flag = #PART
@UNLOCK
```

Atomically sets a global flag to the current partition number if it is unset.

## See Also

- `@UNLOCK` — release the advisory lock
- `SELECT @PART` — select the global partition to operate on
