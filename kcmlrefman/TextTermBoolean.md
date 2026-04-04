TERMINFO Booleans

There are a number of boolean flags that can be set to TRUE or FALSE (1 or 0). If you don't explicitly set the flag it is presumed to be FALSE.

|  |  |
|----|----|
| ACSfix | A workaround for problem with attributes on [ACS terminals](TextTermACS.htm). Only set for these terminals. |
| AutoWrap | Set to TRUE if the terminal with automatically issue a linefeed when sent a carriage return. |
| CS8bits | Enables 8 bit character set support. This is turned on automatically for Kclient and WDW using information from their terminal identification reply. |
| CuaMode | If TRUE the terminal will remap Esc, TAB and SHIFT TAB to send '7F,'7B and '7E. |
| DefaultScreen | If set to TRUE it indicates that the screen understands native KCML sequences e.g. [WDW](TextTermWDW.htm) or [KClient](TextTermKClient.htm). |
| Editor | Set to TRUE to enable support for the KCML4 editor. |
| FastClear | If set then KCML will use clear to end of line and clear to end of screen sequences, if available, to clear text using the third parameter to PRINT AT(). This is much faster then blanking with space characters. If the terminal supports box graphics these will be cleared which is not correct so you may want to set this only for applications that do not use these grpahics. |
| Ideographic | Only necessary on the Taiwanese version of the 2236. It supresses HEX(0202040F). |
| MultiScreen | Supresses screen switching in the editor. Do not use. |
| RobustFlow | If set then KCML will send FDF6 on CLEAR. Necessary only on the Redhaw version of the Wyse 50. |
| SpecTerm | Set only for [Spectrix terminals](TextTermSpx.htm). Works around flow control problem. |
