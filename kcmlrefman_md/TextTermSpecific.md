# Specific Terminals Supported

> Overview of terminals with TERMINFO entries in the default KCML TERMINFO/src file.

## Terminals included in the default KCML TERMINFO

| KTERM value | Terminal |
|-------------|----------|
| `Kclient` | KClient (Windows, reference implementation) |
| `wdw` / `wkcml` | Kerridge Windows DW emulator |
| `ansi` | ANSI console (SCO UNIX) |
| `vt100` | DEC VT100 |
| `vt220` / `vt320` / `vt420` | DEC VT220 and compatible |
| `vt220box` / `vt320box` / `vt420box` | VT220 with soft font box graphics |
| `wang` / `w2236` | Wang 2x36 series |
| `magna` | Magna Falcon |
| `spx701` | Spectrix SPX701 |
| `wy30` / `wy50` | Wyse 30/50 |
| `wy60` / `wy99` / `wy120` / `wy160` / `wy325` | Wyse 60 and compatible |
| `wynnnbox` | Wyse 60/etc. with soft font box graphics |
| `hp` / `hpterm` | HP 700/9x |
| `ibm3151` | IBM 3151 (RS/6000 console) |
| `ACS` | ACS terminal |

Set the `KTERM` environment variable to the appropriate value before starting KCML.

## See Also

- `TextTermIntro` — terminal overview
- `TextTermCaps` — capability matrix
