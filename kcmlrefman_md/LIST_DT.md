# LIST DT

> Displays the device table (DT), device equivalence table (DET), XML handles, and file descriptor table.

## Syntax

```
LIST [title] DT
```

## Description

`LIST DT` shows five sections:

1. **Device table**: stream numbers with full filename, fd number, start/end sector, current file pointer. Files locked by the current process show `W`; files locked by other partitions show the partition number.

2. **Database connections**: current database connection and handle information.

3. **Device equivalence table (DET)**: maps device addresses to native filenames. Lists current `SELECT`ed devices for CI, INPUT, CO, PRINT, LIST, and TRACE.

4. **XML handles** (if any): XML handle numbers, open/parse state, filename or buffer prefix, and current element info.

5. **Handle table**: file descriptors used by KCML.

### Interpreting fd values

| fd value | Meaning |
|----------|---------|
| Negative | File/device not open (or closed) |
| Positive | File is open |
| `9999` | Temporarily closed due to OS limit on open files; auto-reopened when needed |

Native OS files have start sector = 0.

When displayed on screen, press RETURN to page through sections.

## See Also

- `SELECT INPUT` / `SELECT LIST` / `SELECT CO` — select devices
- `OPEN#` — open streams
- `LIST` — overview of LIST commands
