# KCML Exit Codes

> Codes returned by the KCML process on termination. Application programs should restrict their own return values to the range **1–100** to avoid clashing with KCML system codes.

| Code | Meaning |
|------|---------|
| 0 | Normal successful termination |
| 101 | Error during initialisation |
| 102 | KCML licence expired |
| 103 | Client disconnected |
| 106 | Memory error — cannot panic |
| 107 | Licensing problem |
| 108 | CORBA initialisation error |
| 109 | Internal error |
| 110 | Assertion failed |
| 111 | Internal error |
| 112 | KTERM terminal not found in terminal database |
| 113 | PANIC due to runtime error |
| 114 | Program error or forced panic |
| 115 | PANIC statement executed |
| 116 | Internal error |
| 117–125 | Internal error |
| 126 | Unable to open TERMFILE |
| 128 | KCML checksum failed |
| 129 | Screen saver terminated |
| 130 | Terminated on SIGTERM signal |
| 131 | Runtime-only system |
| 132 | Wrong grace password |
| 133 | Recursive PANIC |
| 134 | Unable to find error file (`berror.d`) |
| 135 | Unable to find terminal file |
| 136 | Error in shared memory or semaphore |
| 137–140 | Connection / I/O failures |
| 141 | Internal error during startup |
| 142 | Unable to load CORBA shared library |
| 143–145 | Memory allocation failures |
| 144 | Memory allocation failure (licence-related context) |
| 146 | Unable to determine ttyname |
| 147 | Memory error creating `$PSTAT` |
| 148 | Invalid KCML command line |
| 150–174 | Various errors (registry, sessions, signals, configuration, language, HTTP, SSO, etc.) |

## Common Codes on Linux

| Code | Likely cause | Fix |
|------|-------------|-----|
| 107 | Licence problem — often a background process exhausting the single-user licence | Always run KCML in the foreground; kill any leaked background instances |
| 126 | `TERMFILE` environment variable not set, or path does not exist / is not writable | Set `TERMFILE=/usr/local/kcml/TERMFILE` in `/etc/profile.d/kcml.sh`; ensure the directory exists and is writable |
| 144 | Memory allocation failure, also seen with licence exhaustion from leaked processes | As for 107 |
| 134 | `KCMLPATH` not set or `berror.d` missing from that directory | Set `KCMLPATH` to the directory containing `berror.d` |
| 148 | Bad command-line arguments to `kcml` | Check flags passed to the interpreter |

## Notes

- Exit codes 107 and 144 are commonly caused by **leaked background KCML processes** consuming the single-user licence. Always run KCML scripts in the foreground.
- Exit code 126 on a fresh install almost always means `TERMFILE` is not set. Add it to `/etc/profile.d/kcml.sh` alongside the `PATH` entry.
- Codes above 100 are reserved for KCML system use. Application code using `$END value` should keep values in the range 1–100.

## See Also

- `EnvVars.md` — `TERMFILE`, `KCMLPATH`, `PANICDIR`, `SYSTEMID`
- `PANIC.md` — runtime panic behaviour
- `IntroExec.md` — program execution and termination
