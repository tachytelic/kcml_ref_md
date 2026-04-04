General TERMINFO definitions

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Above80</td>
<td>A parameterized string to print character '%p1' if that character is HEX(80) or greater. Many terminals (e.g. vt100) have a seven bit character set and will need to switch fonts to print such characters. The font should be returned to normal after printing the character. If not defined characters above HEX(80) are printed unaltered.</td>
</tr>
<tr>
<td>ACSFix</td>
<td>A Boolean parameter used to fix a bug in ACS terminals where the terminal would incorrectly change the font when attributes were changed.</td>
</tr>
<tr>
<td>AttribOff</td>
<td>Disables all attributes. No parameters required. On terminals without bold capability dim should be selected to allow normal to be used as the bright attribute.</td>
</tr>
<tr>
<td>AttribOn</td>
<td>A parameterized string to select a combination of attributes depending on the parameters supplied. If any of the parameters is non-zero then it should have the corresponding attribute enabled.<br />
&#10;<table>
<tbody>
<tr>
<td width="50">%p1</td>
<td>bold</td>
</tr>
<tr>
<td>%p2</td>
<td>blink</td>
</tr>
<tr>
<td>%p3</td>
<td>reverse</td>
</tr>
<tr>
<td>%p4</td>
<td>underline</td>
</tr>
<tr>
<td>%p5</td>
<td>always zero</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>Below20</td>
<td>A parameterized string to print character '%p1' if that character is less than HEX(20). Many terminals cannot directly print such characters and may require a font change to do so. The font should be returned to normal after printing the character. If not defined characters below HEX(20) are printed unaltered.</td>
</tr>
<tr>
<td>BoxEnd</td>
<td>Issued at the end of box drawing to restore the normal font.</td>
</tr>
<tr>
<td>BoxStart</td>
<td>A font selection sequence to be issued at the start of a box. This is used when the terminal needs a special font selected for character boxes (e.g. vt100).</td>
</tr>
<tr>
<td>Boxtable</td>
<td>Default value for the <a href="$BOXTABLE.htm">$BOXTABLE</a> table which specifies the method to be used for drawing boxes in the <a href="PRINT_BOX(.htm">BOX(</a> function.</td>
</tr>
<tr>
<td>CGAborder</td>
<td>A parameterized string with '%p1' the required border or overscan color for a CGA display (as above). The 0x08 bit can be set for bright.</td>
</tr>
<tr>
<td>CGAcolour</td>
<td>Synonym for CGAcolor.</td>
</tr>
<tr>
<td>CGAcolor</td>
<td>A parameterized string to print color if possible. '%p1' is the required background color and '%p2' is the foreground color using legal color numbers for the IBM CGA color display.
<table>
<tbody>
<tr>
<td width="50">0</td>
<td>black</td>
</tr>
<tr>
<td>1</td>
<td>blue</td>
</tr>
<tr>
<td>2</td>
<td>green</td>
</tr>
<tr>
<td>3</td>
<td>cyan</td>
</tr>
<tr>
<td>4</td>
<td>red</td>
</tr>
<tr>
<td>5</td>
<td>magenta</td>
</tr>
<tr>
<td>6</td>
<td>brown</td>
</tr>
<tr>
<td>7</td>
<td>white</td>
</tr>
</tbody>
</table>
So on the SCO UNIX console,
CGAcolor=\E[=%p1%dG\E[=%p2%dF
On screens which support the ANSI color sequences the %r command can be used to change these IBM codes into the corresponding ANSI codes for foreground colors. Adding decimal 10 to foreground colors gives the corresponding color code for the background. E.g.
CGAcolor=\E[%r%p2%d;%p1%{10}%+%dm</td>
</tr>
<tr>
<td>ClearEndLine</td>
<td>Specifies the sequence used to clear from the current cursor position to the end of the current line. This can be used to speed up PRINT AT(n, m, c) on DEC and Wyse terminals. This sequence is ignored and spaces are issued if there are any box attributes within the area to be cleared.</td>
</tr>
<tr>
<td>ClearRestOfScreen</td>
<td>Specifies the sequence used to clear from the current cursor position to the end of the screen. This can be used to speed up PRINT AT(n, m, ) on DEC and Wyse terminals. This sequence is ignored and spaces are issued if there are any box attributes within the area to be cleared.</td>
</tr>
<tr>
<td>ClearScreen</td>
<td>The sequence to clear the screen. It is assumed that this sequence homes the cursor. If this is not the case then the home sequence should be included.</td>
</tr>
<tr>
<td>Columns</td>
<td>A numeric parameter that specifies the number of columns on the screen. If not specified a default of 80 is assumed.</td>
</tr>
<tr>
<td>CUATab</td>
<td>Key that is to return '7B.</td>
</tr>
<tr>
<td>CUAMode</td>
<td>Turns on CUA mode by re-mapping Escape to return HEX(7F), Shift Tab to return HEX(7E), and Tab to return HEX(7B).</td>
</tr>
<tr>
<td>CurBlink</td>
<td>Turn on a blinking cursor. Issued in response to a HEX(0205 0F) sequence. If not supported by a terminal the same sequence as used for 'CurOn' should be given.</td>
</tr>
<tr>
<td>CurDown</td>
<td>Move the cursor down a line in the same column. The screen is assumed to scroll if issued in the last row.</td>
</tr>
<tr>
<td>CurHome</td>
<td>Position the cursor in the top left.</td>
</tr>
<tr>
<td>CurLeft</td>
<td>Move the cursor non-destructively one column to the left in the same row. The cursor is assumed to stay in the first column if issued in that column.</td>
</tr>
<tr>
<td>CurOff</td>
<td>Make cursor invisible.</td>
</tr>
<tr>
<td>CurOn</td>
<td>Turn on a steady cursor.</td>
</tr>
<tr>
<td>CurParmDown</td>
<td>Parameterized version of 'CurUp' to move up '%p1' lines in the same column.</td>
</tr>
<tr>
<td>CurParmLeft</td>
<td>Parameterized version of 'CurLeft' to move '%p1' columns to the left in the same row.</td>
</tr>
<tr>
<td>CurParmRight</td>
<td>Parameterized version of 'CurRight' to move '%p1' columns to the right in the same row.</td>
</tr>
<tr>
<td>CurParmUp</td>
<td>Parameterized version of 'CurUp' to move up '%p1' lines in the same column.</td>
</tr>
<tr>
<td>CurPos</td>
<td>Position the cursor to row '%p1' and column '%p2'. Both row and column positions are counted from (0,0) as the top left.</td>
</tr>
<tr>
<td>CurRight</td>
<td>Move the cursor non-destructively one column to the right in the same row. The cursor is assumed to stay in the last column if issued in that column. Hence any autowrap capability of the terminal must be disabled in the ‘Enter’ string.</td>
</tr>
<tr>
<td>CurUp</td>
<td>Move the cursor up a line in the same column. If already in row 0 this cursor need not move as KCML will position the cursor automatically to the last row in the same column.</td>
</tr>
<tr>
<td>DefaultColours</td>
<td>May be required by color terminals that need to support the editor but which have not capability to save and restore screens. It defines a sequence which causes the terminal to restore the colors saved by the terminals setup.</td>
</tr>
<tr>
<td>DefaultScreen</td>
<td>A Boolean parameter which indicates that a terminal can accept KCML screen commands directly. The default is false. If set then most parameters are ignored and need not be specified but 'Enter' and 'Exit' sequences are still issued allowing dual mode terminals to be switched into KCML mode by the 'Enter' sequence.</td>
</tr>
<tr>
<td>Editor</td>
<td>A Boolean parameter used to enable the full screen editor and debugger for this terminal. Note that the editor is only really supported by the Kclient and the Kerridge Windows DW terminal emulator. Enabling the editor on other terminals will work but only limited functionality is available. For best results the Multiscreen clause should also be enabled.</td>
</tr>
<tr>
<td>Enter</td>
<td>This sequence is sent when KCML starts and also on return from a <a href="SHELL.htm">SHELL</a> command. This should be used to disable any autowrap, to select application keyboard mode if necessary and to select suitable fonts.</td>
</tr>
<tr>
<td>Exit</td>
<td>This sequence is sent when KCML terminates and just before starting a <a href="SHELL.htm">SHELL</a> command. It can be used to re-enable autowrap if required.</td>
</tr>
<tr>
<td>FastClear</td>
<td>A Boolean used to increase the speed of the PRINT AT(x, y, z) statement used to blank portions of the screen on Wyse and DEC terminals. KCML keeps a copy of what is known to be on the screen an if this flag is set then it will only issue space characters to the screen if required. If not set then the required number of spaces is sent but see also <em>ClearEndLine</em> and <em>ClearRestOfScreen</em>.</td>
</tr>
<tr>
<td>FontBox</td>
<td>For type 2 boxes where STR($BOXTABLE,,1) == HEX(02)boxtabled, this parameterized string is used to draw an overscored character ‘%p1’. It can be used in combination with <em>BoxStart</em> and <em>BoxEnd</em>.</td>
</tr>
<tr>
<td>Ideographic</td>
<td>A Boolean parameter used to enable the use of ideographic characters.</td>
</tr>
<tr>
<td>Init</td>
<td>This sequence is sent when KCML starts up just before the Enter sequence is issued. It is not sent on return from a <a href="SHELL.htm">SHELL</a> statement. It can be requested by a programmer who issues a HEX(0203 0C0D 0F) terminal initialisation command. In this case the <em>Init</em> string will be followed by an 'Enter' string.</td>
</tr>
<tr>
<td>Lines</td>
<td>A numeric parameter that specifies the number of writable rows on the screen. If not specified a default of 24 is assumed.</td>
</tr>
<tr>
<td>Multiscreen</td>
<td>A Boolean parameter used to enable the multiscreen characteristics used by the full screen editor and debugger. This parameter should only be enabled if the Editor clause is enabled.</td>
</tr>
<tr>
<td>PrintOff</td>
<td>Ends local print mode and re-selects screen.</td>
</tr>
<tr>
<td>PrintOn</td>
<td>Selects local printer. Only supply this sequence if the terminal is capable of diverting output directly to the local printer without it appearing on the screen.</td>
</tr>
<tr>
<td>RobustFlow</td>
<td>A Boolean parameter used to enable the sending of the FBF6 sequence to instruct 2x36 terminals to start sending unsolicited XONs. This should be used when MICOM multiplexors are used with Chase Research IOLAN cards.</td>
</tr>
<tr>
<td>ScreenDump</td>
<td>Specifies the key that is to be mapped to force KCML to create a screen dump file. The screen is written to a file named scrnd<em>xxx</em> in the current directory where <em>xxx</em> is the partition. This file can then be loaded from disk by another user and displayed on their screen with the <a href="PRINT_SCREEN.htm">PRINT SCREEN</a> statement.</td>
</tr>
<tr>
<td>SpecTerm</td>
<td>A Boolean parameter which tells KCML that the terminal used the Spectrix bi-directional flow control and that certain screen sequences must be escaped. The default is false. It should only be set to true for SPX701 terminals.</td>
</tr>
<tr>
<td>Termcode</td>
<td>Copied into byte 9 of <a href="$MACHINE.htm#BYTE9">$MACHINE</a>. Each terminal within the source file has a <em>Termcode</em> allocated see the list of specific terminals supported later in this chapter.</td>
</tr>
<tr>
<td>Use</td>
<td>Instructs <em><a href="tik.htm">tik</a></em> to copy information from the specified terminal. This makes it easier to create terminal definitions for terminals that are very similar, for example the "sun" and the "sun-cmd" entries where only the <em>Enter</em> and <em>Exit</em> clauses are different.</td>
</tr>
<tr>
<td>WinBorder</td>
<td>Optional string used to override the default attributes and characters used for the border of a window drawn with the <a href="WINDOW.htm">WINDOW OPEN</a> statement. It is an 11 character string with the first 3 bytes specifying attributes to use and the remaining 8 bytes specifying characters to use. All 11 bytes must be specified.
<table>
<tbody>
<tr>
<td width="50">1</td>
<td>title attribute</td>
</tr>
<tr>
<td>2</td>
<td>border attribute</td>
</tr>
<tr>
<td>3</td>
<td>font flag (0x00 or 0x01)</td>
</tr>
<tr>
<td>4</td>
<td>left edge character</td>
</tr>
<tr>
<td>5</td>
<td>right edge character</td>
</tr>
<tr>
<td>6</td>
<td>bottom edge character</td>
</tr>
<tr>
<td>7</td>
<td>bottom left corner character</td>
</tr>
<tr>
<td>8</td>
<td>bottom right corner character</td>
</tr>
<tr>
<td>9</td>
<td>top left corner character</td>
</tr>
<tr>
<td>10</td>
<td>top right corner character</td>
</tr>
<tr>
<td>11</td>
<td>title fill character</td>
</tr>
</tbody>
</table>
Attributes are a binary OR of the attributes bits used in the INPUT SCREEN statement
<table>
<tbody>
<tr>
<td width="50">80</td>
<td>alternate char set</td>
</tr>
<tr>
<td>40</td>
<td>reverse video</td>
</tr>
<tr>
<td>20</td>
<td>blink</td>
</tr>
<tr>
<td>10</td>
<td>bright</td>
</tr>
</tbody>
</table>
The font flag should be set to 0x01 if the border characters require a change of font. The BoxStart sequence will then be issued at the start of drawing the border and the BoxEnd sequence at the end.</td>
</tr>
</tbody>
</table>
