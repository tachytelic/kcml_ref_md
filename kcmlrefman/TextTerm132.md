132 Column support

The Kclient and Kerridge Windows DW terminal emulator are the only terminals that can correctly support 132 mode while running KCML. Modern DEC and Wyse terminals have this capability though it is incompatible with soft font boxes. To enable this mode byte 17 of [\$OPTIONS]($OPTIONS.htm#BYTE17) must be set to HEX(01). The screen width is then set to 132 columns with [SELECT PRINT](SELECT_PRINT.htm) /005(132), [SELECT LIST](SELECT_LIST.htm) /005(132) or [SELECT CO](SELECT_CO.htm) /005(132) , followed by a HEX(03) to clear the screen. Byte 8 of [\$MACHINE]($MACHINE.htm#BYTE8) gives the current screen width as a binary byte and is set to 132 after a width change if KCML thinks that it was able to switch the width because a *Col132* sequence is defined in the *TERMINFO* description file. To restore an 80 column screen set the screen width to 80 with SELECT PRINT and clear the screen again. Byte 8 of [\$MACHINE]($MACHINE.htm#BYTE8) will then be reset to 80.

The KCML *TERMINFO/src* file has had this feature added to the Kclient, kcml, wdw, DW, magna, vt100, vt220, wy60, wy160 and wy99 terminal descriptions.

The size of the screen table is increased from 6kb to 10kb on terminals that support this capability.
