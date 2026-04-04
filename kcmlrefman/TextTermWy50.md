Wyse 30/50

KTERM=wy30 or KTERM=wy50

This is a common cheap terminal with some significant drawbacks. As attributes occupy space on the screen KCML uses the terminals write protect mode for all attributes. The default write protect modes for all attributes should be set in the terminals set-up menu, setting the WPRT options to dim, no underline and reverse are the recommended settings. The standard *TERMINFO* assumes that you are using the 16 function key keyboard though all Wyse terminals are also available with VT220 and PC/AT keyboards. If you have one of these other keyboards then you may need to edit the *TERMINFO/src* file to re-map the keys you need onto the keys you have. The keyboard sends the same key for backspace and left arrow so it is not possible for KCML to distinguish these keys, both are interpreted as backspace. There is no support for box graphics or for alternative fonts (characters 0x80 to 0xFF) though some line graphic characters may be found between 0x10 and 0x1F. This terminal does support local printing.

A box table is defined by *TERMINFO* but is disabled by default. To use this table, set byte 1 of [\$BOXTABLE]($BOXTABLE.htm) to HEX(01), e.g:

STR(\$BOXTABLE,,1)=HEX(01)
