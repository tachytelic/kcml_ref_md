# MAT COPY

> Copies the contents of an alpha variable or array to another, with optional byte-order reversal.

## Syntax

```
MAT COPY [-] source [<start,count>] TO [-] dest [<start,count>]
```

Prefer using `FLD(` or `STR(` for the range syntax:
```
MAT COPY STR(temp$(), 5, 5) TO STR(file$(), 7, 5)
```

The `<start,count>` chevron syntax is deprecated.

## Description

Copies on a byte-by-byte basis. If the receiver is larger than the source, remaining bytes are padded with spaces.

### Minus sign behaviour

| Sign position | Effect |
|--------------|--------|
| No minus | Left-to-right copy, left-justified in receiver |
| `-source` | Source read in reverse order (right-to-left); stored left-to-right in receiver (reverses string) |
| `-dest` | Source stored right-to-left in receiver (reverses placement; right-justified) |
| Both `-source` and `-dest` | Right-justified without reversing order |

### Summary table

Given `abc$() = "A B C D "`:

| Statement | Result in `xyz$()`|
|-----------|------------------|
| `MAT COPY abc$() TO xyz$()` | `A B C D   ` |
| `MAT COPY -abc$() TO xyz$()` | ` D C B A  ` |
| `MAT COPY abc$() TO -xyz$()` | `   D C B A` |
| `MAT COPY -abc$() TO -xyz$()` | `  A B C D ` |

## Examples

```kcml
MAT COPY STR(temp$(), 5, 5) TO STR(file$(), 7, 5)
MAT COPY -abc$() TO xyz$()    REM reverse the string
```

## See Also

- `MAT MOVE` — element-by-element array transfer (with optional locator)
- `MAT_assignment` — simple array copy
- `STR(` — substring
