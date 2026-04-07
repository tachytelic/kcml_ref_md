# COPY

> Copies a file from one path to another.

## Syntax

```
COPY source TO destination
```

| Parameter | Description |
|-----------|-------------|
| `source` | String expression — the path of the file to copy |
| `destination` | String expression — the destination path or directory |

## Description

`COPY` copies a native OS file. Use `COPY` instead of shelling out to the OS `cp` command.

`COPY` operates relative to the current working directory (not a `SELECT DISK` directory). Errors (file not found, invalid path) are recoverable and can be trapped with `ERROR DO ... END DO`.

## Examples

### Copy a file

```kcml
: COPY "/tmp/myfile.txt" TO "/tmp/myfile_backup.txt"
: PRINT "copy ok"
: $END
```

### Using a variable

```kcml
COPY FileName$ TO "PROGS"
COPY "/tmp/PROG1" TO "/user1/backup"
```

### With error handling

```kcml
ERROR DO
    COPY source$ TO dest$
END DO
IF (ERR)
    PRINT "Copy failed: "; ERR$
END IF
```

## Notes

- `COPY` works with the current working directory — it is not affected by `SELECT DISK`.
- An error occurs if the destination already exists (as a directory) or if the path is invalid.
- To rename or move a file, use `MOVE`.
- To delete a file, use `REMOVE`.

## See Also

- `MOVE` — move or rename a file or directory
- `REMOVE` — delete a file
- `CREATE DIR` — create a directory
- `REMOVE DIR` — delete a directory
