# REMOVE DIR

> Removes a directory and all its contents recursively.

## Syntax

```
REMOVE DIR directoryname$
REMOVE DIR "literal_path"
```

## Description

Deletes the specified directory and **all files and subdirectories** within it. Equivalent to `rm -rf` on Unix.

Operates relative to the **current working directory**, not the `SELECT DISK` directory.

## Examples

```kcml
REMOVE DIR "/tmp/WorkDir"
REMOVE DIR Directory$
```

## Notes

- **Destructive** — removes all nested content without confirmation. Use with care.
- Raises an error if the directory does not exist or cannot be removed (e.g. permissions).
- To remove a single file, use `REMOVE`.

## See Also

- `REMOVE` — delete a single file
- `MOVE` — rename / move a directory
- `COPY` — copy files
