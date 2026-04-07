# MOVE

> Renames a file or directory. Preferred over shelling out to OS commands.

## Syntax

```
MOVE file_or_dir1 TO file_or_dir2
```

## Description

Renames files or directories. If source and destination are on different filesystems, KCML copies the file then deletes the original.

Note: not all operating systems support renaming directories across filesystems.

Operates relative to the **current working directory**, not the `SELECT DISK` directory.

## Examples

```kcml
MOVE file1 TO file2$
MOVE "WorkDir" TO "OldWorkDir"
```

## See Also

- `COPY` — copy a file without removing the source
- `REMOVE` — delete a file
- `$COMPILE` — compiler (sometimes cited alongside MOVE)
