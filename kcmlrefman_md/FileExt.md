# KCML File Extensions

> Reference for the special file extensions recognised by the KCML runtime and tools.

## Extensions

| Extension | Meaning |
|-----------|---------|
| `.asc` | ASCII program source (KCML 2 legacy). Recognised by the `compile` utility as input. Obsolete — use `.src` instead. |
| `.kapp` | KCML application. Usually a compiled program. On Windows, clicking it in Explorer opens a client window and runs it locally. |
| `.kcml` | Compiled KCML program (KCML 6.0+). Shown in the Workbench File Browser. On Windows, automatically registered in the registry and IIS ScriptMap for CGI scripting. |
| `.ks` | KCML script file. Reads from standard input, writes to standard output. May be ASCII source or compiled. On Windows, registered in IIS ScriptMap for CGI scripting. |
| `.src` | ASCII program source. Recognised by `LOAD` when `$OPTIONS RUN` byte 40 is set (load/save ASCII and compiled programs together). Shown in the Workbench File Browser and saveable with this extension. |

## Notes

- `.asc` is obsolete. Use `.src` for ASCII KCML source files.
- `.kcml` and `.ks` are the two extensions used for CGI-style scripting on Windows IIS.
- Extensionless files and `.Bre` files are also valid KCML source (see `$SPECIAL` environment variable for the `.Bre` per-customer override mechanism).

## See Also

- `LOAD` — load a program
- `$SPECIAL` — per-customer program override mechanism
- `$OPTIONS RUN` — runtime option flags
