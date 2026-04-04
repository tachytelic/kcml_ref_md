ACS sequences

These are extensions to the original 2x36DW terminal and are accepted by the client while executing in [KCML mode](TextSeqDW.htm). They all start with HEX(02 00 *XX YY*), where *XX* *YY* are the following codes:

| Code | Description                |
|------|----------------------------|
| 000E | Status line on             |
| 000F | Status line off            |
| 010E | *Clicker on*               |
| 010F | *Clicker off*              |
| 020E | *Screen save on (20 min)*  |
| 020F | *Screen save off*          |
| 030E | Block cursor               |
| 030F | Underline cursor           |
| 040E | *Swap f/g & b/g Colors*    |
| 040F | *Restore f/g & b/g Colors* |
| 050E | Line 25 on                 |
| 050F | Line 25 off                |
| 060E | Restore screen from buffer |
| 060F | Save screen to buffer      |
| 080E | Screen dump                |
| 090E | Erase to end of line       |
| 090F | Erase to end of screen     |
| 0A0E | Load user line             |
| 0A0F | Load user line             |
| 0B0E | Load status line           |
| 0B0F | Load status line           |
| 0C0E | Load cursor position       |
| 0C0F | Read cursor position       |
| 0D0E | *Load time*                |
| 0D0F | *Read time*                |

Sequences in *italics* are accepted, but have no effect in this version.
