# Scripting in KCML

> How to use KCML in non-interactive shell scripts, batch files, and CGI scripts.

## Description

KCML can be used inside Unix shell scripts, Windows NT batch files, or CGI scripts. In script mode, it does not invoke the client for user interaction — it reads from standard input and writes to standard output. Runtime errors terminate KCML with a panic dump.

Use either:
- Redirect standard input: `kcml < myscript.src`
- The `-p` switch: `kcml -p someprog`

The `-p` switch is the preferred form when the script itself needs to read standard input (e.g. CGI scripts).

Standard input is available on device `/001`; standard output on `/005`. Scripts can use `INPUT`, `KEYIN`, or `READ #` for input and `PRINT` for output.

## Unix scripts

A KCML program can be run as a Unix script using the `#!` shebang:

```sh
#!/usr/lib/kcml/kcml -p
DIM ser$20
ser$ = $SER
PRINT ser$
$END
```

Make it executable with `chmod +x test.ks`.

**Linux note:** Linux does not pass the full `kcml` filename to the interpreter, so it cannot find its directory. Workaround: ensure the KCML directory is on `PATH`, or set the `KCMLPATH` environment variable.

## Windows NT batch scripts

NT batch files support stdin/stdout redirection:

```batch
kcml < myprog.asc
```

The `.ks` extension is registered with the shell, so `.ks` files can be run directly.

## Key rules for script mode (-p)

- Statements separated by `:`, continuation lines start with `: `
- **No blank lines** — a blank line silently terminates execution. Use `: REM` for spacing.
- A bare `REM` (without `: ` prefix) also terminates the script.
- Do not use `INPUT` or `KEYIN` for interactive input — the script is non-interactive.
- Every script must end with `$END`.
- **Never put `:` in a REM comment** — KCML treats it as a statement separator.

## Examples

```kcml
: DIM x
: x = 42
: PRINT x
: $END
```

## See Also

- `kcml` — interpreter command-line flags
- `cgi` — CGI scripts in KCML
- `$END` — terminate execution
