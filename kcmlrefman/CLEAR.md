CLEAR

------------------------------------------------------------------------

General Form:\
     <img src="bitmaps/clear.gif" data-align="BOTTOM" data-border="0" alt="clear.gif" />\
Where:\
\
     start_line, end_line      = valid line numbers within the rang 0 to 32000\
\

------------------------------------------------------------------------

The CLEAR command is used to clear all program text and variables from memory. If no other parameters are specified then clear will also perform the following operations:

- All program text and variables are cleared from memory.
- All currently open devices are closed.
- All entries in the device table are cleared and set to the default values.
- Any [TRACE](TRACE.htm) and [TRAP](TRAP.htm) modes are turned off.
- Any pending [\$ALARMs]($ALARM.htm) are cleared.
- Any currently selected global partitions are deselected.
- The default trigonometric mode reverts back to [RADIANS](SELECT_DRG.htm).
- The [\$PROG]($PROG.htm) variable and the circular buffer of the last programs loaded is cleared.
- The screen is cleared, screen attributes are set back to normal, and the normal character set is selected. The copyright message followed by the KCML release number are displayed at the top of the screen.

Adding the V parameter to the CLEAR command instructs CLEAR to remove all variables from memory. CLEAR V has no effect on the program currently in memory, or on the device table.

Adding the N parameter to CLEAR will only remove non-common variables from memory. The values of common variables will be left unchanged. CLEAR N has no effect on the program currently in memory, or on the device table.

Adding the P parameter to CLEAR, removes program text from memory without altering any variables currently held in memory, also CLEAR P will not alter the device table. CLEAR P has several forms, for example:

|                |                                                         |
|----------------|---------------------------------------------------------|
| CLEAR P        | Remove the whole program from memory.                   |
| CLEAR P 1020   | Remove all lines after and including line 1020.         |
| CLEAR P ,9000  | Remove all lines before and including line 9000.        |
| CLEAR P 20,900 | Remove lines 20 inclusive up to and including line 900. |

 

 
