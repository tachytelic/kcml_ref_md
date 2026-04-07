# selfid (Unix)

> Identify the terminal type and set `KTERM` automatically.

## Syntax

```
selfid [-abcCdfsvwWx] [-t ms] [-k kcmladdress]
```

## Description

`selfid` determines the exact terminal type by sending identification sequences to the terminal. It eliminates the need to maintain a terminal type database for `KTERM`, since it negotiates the type directly.

On success, it echoes the terminal type to stdout. For example, on a generic Wyse 60: `wy60box` (supports soft fonts) or `wy60` (no soft fonts).

### Terminals detected

KClient, WDW, DW, Wyse 60/99/120/160/325, DEC VT100/220/320/420/510, Wang, ACS, Magna. ANSI and SCO ANSI cannot be auto-detected as they have no terminal identification capability.

### Wyse terminal detection

VT100 sequences can hang Wyse terminals. `selfid` checks for Wyse first, but only if `$TERM` starts with `wy`. Use:
- `-w` to skip Wyse detection entirely (if no Wyse terminals on the system)
- `-W` to force Wyse detection regardless of `$TERM`

### KClient auto-identification

KCML 5.03+ KClient negotiates the terminal type and answerback directly over telnet (or via special login environment variables `_KTERM` and `_ANSWERBACK`). `selfid` from KCML 5.03+ checks for these variables first and replies immediately without querying the terminal.

If `_KTERM` and `_ANSWERBACK` are set, login scripts can check them directly instead of running `selfid`.

## Typical `.profile` usage

```sh
KTERM=`selfid`
export KTERM
case $KTERM in
  wy60box)
    REM download softfont here
    ;;
esac
```

## See Also

- `tik` — TERMINFO compiler
- `TextTermIntro` — text terminal overview
- `TextTermKclient` — KClient terminal details
