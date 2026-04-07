# Text Program Format (New ASCII Format)

> Reference for the new KCML 6.10+ source format that supports conditional loading, optional colons, and optional line numbers.

## Description

The new text format is enabled by setting `$OPTIONS RUN` byte 46 to `HEX(05)` or by setting the `OPTIONS_RUN_46` environment variable.

### Key differences from classic format

| Feature | Classic | New format |
|---------|---------|------------|
| Statement separator `:` | Required | Optional (one statement per line assumed) |
| Line numbers | Required | Optional (KCML auto-numbers) |
| Conditional loading | No | Yes |
| Extension | Any | `.src` (preferred) |

### Conditional loading

The new format supports conditional compilation/loading directives (similar to `#ifdef` in C). Useful for maintaining different code variants without separate files.

### Saving

`SAVE` and `SAVE ASCII` still generate colons and line numbers for backward compatibility. Files are always saved with the `.src` extension when using this mode. Use `$COMPILE` to produce binary versions for deployment.

### For development

Keep all programs in text/source format with `.src` extension during development. Use `kmake` / `$COMPILE` for deployment builds.

## Enabling

```sh
OPTIONS_RUN_46="05" ; export OPTIONS_RUN_46
```

Or in KCML:
```kcml
STR($OPTIONS RUN, 46, 1) = HEX(05)
```

## Notes

- `$COMPILE` accepts the new format for input but does not apply the `.src` extension convention (controlled by its own byte 40).
- Libraries compiled from source using this format work the same way as classic compiled libraries.

## See Also

- `$OPTIONS RUN` — byte 46 (source format control), byte 40 ($COMPILE options)
- `LOAD` — load a program (recognises `.src` extension when configured)
- `SAVE` — save in ASCII or compiled format
