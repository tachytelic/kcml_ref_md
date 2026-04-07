# Terminal Capabilities Matrix

> Summary of feature support across KCML text terminals.

## Description

The following capabilities vary by terminal:

| Feature | Description |
|---------|-------------|
| **Attributes** | Bold, blink, reverse, underline support |
| **Local printing** | Print directly to a local printer attached to the terminal |
| **Boxes** | Native box-drawing graphics |
| **132 columns** | Wide-screen (132-column) mode |
| **Block graphics** | Full block/semi-block character graphics |
| **Function keys** | Number of hardware function keys |
| **Flow control** | Hardware or software flow control |
| **Editor support** | KCML 4 editor key support |

### Well-supported terminals

| Terminal | Attributes | Boxes | 132-col | Notes |
|----------|-----------|-------|---------|-------|
| KClient | Yes | Yes | Yes | Reference implementation |
| WDW/WKCML | Yes | Yes | Yes | Windows DW emulator |
| VT100/VT220 | Yes | No native | Yes | Use `$BOXTABLE` |
| Wyse 60/99/160 | Yes | Yes | Yes | |
| ANSI (SCO) | Yes | Yes | No | Color support |

## See Also

- `TextTermIntro` — terminal overview
- `TextTerm132` — 132-column mode
- `TextTermBox` — box graphics
- `TextTermKclient` — KClient details
