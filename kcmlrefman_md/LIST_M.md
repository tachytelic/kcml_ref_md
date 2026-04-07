# LIST M

> Lists all loaded libraries and selected globals, showing their names and memory-mapped files.

## Syntax

```
LIST [title] M
```

## Description

Shows each loaded library and global partition with:
- Name
- Memory-mapped file it was loaded from
- For process globals: the partition number of the owning partition

Listed in load order (earliest first).

## See Also

- `LIBRARY ADD` — load a library
- `SELECT @PART` — select a global partition
- `LIST` — overview of LIST commands
