# NT Core Files

> Reference for generating and using core dump files on Windows KCML (NT) for debugging.

## Description

Core dump files are memory snapshots created when KCML or the application crashes. Similar to KCML Panic files, they help diagnose problems that are otherwise impossible to reproduce.

**Note:** Core dumps are only supported on Windows NT — not Unix or Windows 95/98.

## Enabling core files

By default, core files are never created. Enable via registry settings (use the provided KCML program to set them — see the KCML manual for the registry program).

Core files are named with date/time: `core1999-11-12_172311`.

### Network core files

Set the `KCML_CORE_FTP` environment variable (in the Connection Manager) to send cores to a central FTP repository:

```
KCML_CORE_FTP="directory,server,userid,password"
```

Example:
```
KCML_CORE_FTP="/cores,callisto,pjc,secret"
```

Network cores take precedence over local core file settings.

## Using core files

Must use **exactly the same KCML version** as the one that generated the core.

### Recover program source

```sh
kcml -corelist core1999-11-12_172311 > myprog.src
```

### Open in Workbench (read-only debugging)

```sh
kcml -coreeditor core1999-11-12_172311
```

Shows the state at crash time. Variables, code, and debug options are available. Code cannot be executed.

## Notes

- Core dump support is experimental.
- KCML Panic files are the more common crash artifact — see PANICDIR environment variable.

## See Also

- `EnvVars` — PANICDIR, DUMPCORE, KCML_CORE_FTP
- `PANIC` — force a KCML panic/crash dump
