# CREATE DIR

> Creates a new directory in the native file system.

## Syntax

```
CREATE DIR dirname
```

| Parameter | Description |
|-----------|-------------|
| `dirname` | String expression — the path of the directory to create |

## Description

`CREATE DIR` creates a new OS directory. Use it instead of shelling out to the OS `mkdir` command.

Errors are recoverable (directory already exists, invalid path) and can be trapped with `ERROR DO ... END DO`.

## Examples

### Create a directory

```kcml
: CREATE DIR "/tmp/kcml_test_dir"
: PRINT "created ok"
: REMOVE DIR "/tmp/kcml_test_dir"
: PRINT "removed ok"
: $END
```

### Using a variable

```kcml
CREATE DIR Directory$
CREATE DIR "/tmp/NewDir"
```

### With error handling

```kcml
ERROR DO
    CREATE DIR newdir$
END DO
IF (ERR)
    PRINT "Failed to create dir: "; ERR$
END IF
```

## Notes

- Errors if the directory already exists or the path is invalid.
- Use `REMOVE DIR` to delete a directory and `MOVE` to rename one.
- Works with the current working directory (not affected by `SELECT DISK`).

## See Also

- `REMOVE DIR` — delete a directory
- `MOVE` — rename or move a file or directory
- `COPY` — copy a file
- `REMOVE` — delete a file
