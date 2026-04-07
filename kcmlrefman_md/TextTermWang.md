# Wang 2x36 Series Terminals

> KCML terminal configuration for Wang 2x36 series terminals.

## Description

`KTERM=wang` or `KTERM=w2236`

The Wang 2536 supports optional XON/XOFF flow control and can connect to any Unix CPU. Earlier 2x36 terminals (2236, 2336) require the 2200 proprietary flow control protocol.

### Flow control

Wang-style flow control uses 4 reserved characters. It is supported on specific hardware:
- Altos 1000, CCI6/32, ICL DRS500
- 386/486 PCs with Chase Research or DigiBoard bus controllers
- Older Wang terminals: only via external protocol converters (Kerridge Z-net, Chase Research IOLAN)

### SF17/SF19 conflict

If the hardware does not support Wang flow control, SF17 and SF19 will not work (they send XON/XOFF characters).

### Capabilities

- Straightforward TERMINFO — responds directly to KCML sequences
- Local printing supported (but screen goes off-line if printer goes off-line)
- 7-bit proprietary character set (US, German, Swiss variants)

### Non-English locale

For KCML 5+ (Latin-1) with non-English Wang character sets, add character mapping entries to TERMINFO.

## See Also

- `TextTermIntro` — terminal overview
- `TextTermMagna` — Magna Falcon (Wang personality)
