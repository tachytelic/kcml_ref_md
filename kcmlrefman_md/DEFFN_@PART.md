# DEFFN @PART

> Publishes the current global partition's variables and subroutines under a shared name so other partitions can access them.

## Syntax

```
DEFFN @PART "name"
```

Where `name` is either:
- A simple name of up to 8 characters (published to the `$PSTAT` table)
- A name/path string longer than 8 characters (copies shared memory to a file on `$BREAK!`)

## Description

`DEFFN @PART` makes the global variables and quoted subroutines of the current partition publicly accessible under the specified name. Only partitions running with the `-g` KCML switch (global partition mode) can execute this statement.

Other programs gain access to the published functions and `@` variables by executing `SELECT @PART "name"` with the same name.

### Simple name (≤8 characters)

The name is inserted into the `$PSTAT` shared memory table. An error occurs if the name is already taken by another global partition.

The global partition typically runs as a background daemon (started at boot), loops with `$BREAK!` to sleep, and uses `$ALERT` to wake when needed.

### File-based name (>8 characters, `name=filename` format)

If the name contains `=`, KCML parses it as `name=filename`. On `$BREAK!`, the shared memory is copied to `filename` and KCML terminates. Other processes can then access the functions via `SELECT @PART` without a permanently running daemon.

Note: Memory-mapped files are not interchangeable between different processor architectures.

If multiple `DEFFN @PART` statements appear at resolve time, only the first takes effect.

## Example

```kcml
DEFFN @PART "MYSERVICE"
$BREAK!
```

Other programs access it with:
```kcml
SELECT @PART "MYSERVICE"
```

## See Also

- `SELECT @PART` — select a named global partition
- `@LOCK`, `@UNLOCK` — advisory locking for global variables
- `$BREAK!` — sleep until signalled
- `$ALERT` — signal a sleeping process
- `$PSTAT` — partition status table
