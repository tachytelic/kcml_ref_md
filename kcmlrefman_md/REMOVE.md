# REMOVE

> Deletes a file from the filesystem.

## Syntax

```
REMOVE filename$
REMOVE "literal_path"
```

## Description

Deletes the specified file. Operates relative to the **current working directory**, not the `SELECT DISK` directory.

Preferred over shelling out to OS commands (`rm`, `del`).

## Examples

```kcml
REMOVE "/tmp/WorkFile"
REMOVE FileName$
REMOVE "/tmp/test_" & id$ & ".tmp"
```

## Notes

- Raises an error if the file does not exist or cannot be deleted (e.g. permissions).
- To delete a directory (and all its contents), use `REMOVE DIR`.
- To rename/move a file, use `MOVE … TO`.
- To copy a file, use `COPY`.

## See Also

- `REMOVE DIR` — delete a directory tree
- `MOVE` — rename / move a file
- `COPY` — copy a file
