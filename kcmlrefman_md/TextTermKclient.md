# KClient Terminal

> KClient is the native KCML terminal for client-server mode on Windows.

## Description

`KTERM=Kclient`

KClient is the reference KCML terminal. It runs on Windows 9x, NT, CE, and later. In addition to text-mode emulation, it supports GUI forms (DEFFORM).

### Capabilities

- Full text-mode emulation (VT220 and native KCML mode)
- Full keyboard and screen support
- 132-column support
- GUI forms
- Local printing
- Internationalisation (uses native Windows code page)

### Limitation

No underline-by-ORing-with-HEX(80) — uses native Windows code page instead.

## See Also

- `TextTermIntro` — terminal overview
- `TextTerm132` — 132-column mode
- `DEFFORM` — GUI forms
