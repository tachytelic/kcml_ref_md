Soft font boxes

Some terminals, especially modern Wyse and DEC terminals, support downloadable soft fonts which allow the characters displayed on the screen to be loaded from a file before KCML is started. Fonts for modern Wyse and DEC terminals to allow box graphics are supplied with all UNIX versions of KCML. Two fonts called *wyfont1* and *wyfont2* are supplied for Wyse 60/99/120/160 and 325 terminals, the font *vt220font* is supplied for DEC VT220 and VT320 terminals and the font *vt420font* is supplied for DEC VT420 and VT510 terminals. The fonts are loaded by sending the files to the terminal with the UNIX *cat* command, for example:

cat \$KCMLADDR/wyfont\[12\]

would be used to send the fonts to a Wyse terminal, while

cat \$KCMLADDR/vt220font

would be used to send the fonts to a DEC VT220 or VT320 terminal. While the font is being sent to the terminal the screen is cleared until the font has been downloaded.

Once loaded with an extra font in which the standard characters are overscored then KCML will simulate regular boxes if byte 1 of [\$BOXTABLE]($BOXTABLE.htm) is set to HEX(02). The *TERMINFO* capabilities *BoxStart* and *BoxEnd* tell KCML how to switch fonts. While horizontal box segments can be reproduced with the extra font, vertical box segments have to be drawn as characters. Again they will not be drawn in a non-blank cell. Bytes 2 to 9 of [\$BOXTABLE]($BOXTABLE.htm) tell KCML which characters in the new font to use for vertical box characters. The characters must be in the soft font and be constructed from left overscores, right overscores and a vertical segment through the centre of the cell.

| Byte | L   | R   | V   |
|------|-----|-----|-----|
| 2    |     |     |     |
| 3    |     |     | \*  |
| 4    |     | \*  |     |
| 5    |     | \*  | \*  |
| 6    | \*  |     |     |
| 7    | \*  |     | \*  |
| 8    | \*  | \*  |     |
| 9    | \*  | \*  | \*  |

[\$BOXTABLE]($BOXTABLE.htm) byte settings for soft font boxes

The standard *TERMINFO/src* that is shipped with KCML has entries for Wyse and DEC terminals that support soft fonts. To use these entries you must append the word *box* to the terminal name specified with the *KTERM* environment variable. The simplest way of doing this is to use the KCML *selfidselfid* utility which is used to determine the exact type of terminal being used. If the terminal supports downloadable fonts then [selfid](selfid.htm) returns the terminal name with the *box* extension added. For example if a DEC VT420 terminal was being used then *selfidselfid* would return *vt420box*, but if a DEC VT100 terminal was being used then *selfidselfid* would return *vt100* as VT100 terminals do not support soft fonts. The default *.profile* that is created by the *kcmladmin* installation program uses [selfid](selfid.htm) to set the *KTERM* environment variable which is used by KCML to determine which terminal description file should be loaded. Refer to [selfid](selfid.htm) in the utilities chapter for more information.

The standard font files that are shipped with KCML can be modified with the FONTEDIT.EXE program which is a utility supplied with DOS versions of KCML4 only, refer to the DOS KCML installation guide for more information.
