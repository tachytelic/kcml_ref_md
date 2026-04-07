# INPUT

> Reads one or more values from the keyboard (or redirected input device) into variables.

## Syntax

```
INPUT [literal_string[,]] receiver [, receiver ...]
```

Where `receiver` is a numeric or alpha variable.

## Description

`INPUT` prompts the user (optionally with a literal string followed by `?`) and reads values from the `INPUT` device into the specified variables. Leading spaces, quotes, and commas are accepted in the input text. Up to 1900 bytes can be read into an alpha variable.

The `INPUT` device defaults to the console (`/001`). It can be redirected with `SELECT INPUT` to read from a file or pipe.

**Note:** `INPUT` is considered obsolete. `LINPUT` and `LINPUT+` are the modern replacements and provide a superset of functionality.

**Do not use `INPUT` in scripts run with `kcml -p`** — it is non-interactive and will hang waiting for input that never arrives.

## Examples

### Basic keyboard prompt

```kcml
DIM temp$80
INPUT "Enter Text  : " temp$
```

Displays: `Enter Text  : ?` then waits for keyboard input.

### Redirected input from a Unix command

```kcml
DIM act$64
SELECT INPUT "date ^"
INPUT act$
SELECT INPUT /001
PRINT act$
```

This reads the output of the Unix `date` command into `act$`.

### Reading a number

```kcml
DIM amount
INPUT "Enter amount: ", amount
PRINT "You entered: "; amount
```

## Notes

- `INPUT` is for **text-mode/interactive** programs only. Do not use it in `-p` script mode (it will hang).
- The `?` prompt character is appended automatically after the optional literal string.
- The `INPUT` device can be redirected with `SELECT INPUT`.
- End-of-file on a redirected INPUT device causes an **X70** error.
- Prefer `LINPUT` or `LINPUT+` for new code — they support editing, prompts, validation, and more.

## See Also

- `LINPUT` — modern replacement for INPUT
- `LINPUT+` — extended interactive input
- `SELECT INPUT` — redirect the input device
- `KEYIN` — single character input (screen programs)
