LINPUT +

------------------------------------------------------------------------

General Form:

LINPUT+ alpha_receiver\$, proplist\$

------------------------------------------------------------------------

This statement is an enhanced version of the [LINPUT](LINPUT.htm) statement providing multiline entry, horizontal and vertical scrolling, word wrapping, and remote execution under Windows. The exact behaviour of the edit control is governed by a structure passed in the variable proplist\$. This should be 64 bytes in length and initialised to HEX(00) and the appropriate entries filled in before the statement is executed. The first three fields do not have to be defined as they are set and returned by LINPUT+ to indicate how the LINPUT+ was terminated and how many characters were in the string retrieved from the edit control. Refer to the table below for a details of this structure.

When executed KCML will display the text using the specified attribute in the editable area defined by the width and depth properties. If the select on entry property is set on then all the text will be reversed to indicate selection. If the display only property is set on then it will return immediately leaving the text on the screen.

Editing follows Common User Access (CUA) rules popularised by all true Windows applications, not the rules used in [console mode](mk:@MSITStore:workbench.chm::/LineEditor.htm) or original LINPUT statement. Note however that there is no overwrite mode.

If running under Microsoft Windows, either using KClient or the Windows DW terminal emulator, the mouse can be used to perform the tasks detailed below:

| Left Click | Left Double Click | Left Drag | Right Click | Right Double Click | Right Drag |
|----|----|----|----|----|----|
| Positions cursor | Positions cursor and selects text. If cursor is off selection then action carriage return. | Select text | If cursor is off selection then abort | If cursor is off selection then abort | If cursor is off selection then abort |

When editing is terminated by a function key (or HEX(0D) in the case of single line LINPUT+) then the first three fields are updated. Function keys '00 to '31, GL, Shift GL, TAB, SHIFT TAB are not used in editing and will terminate the LINPUT+. If a mouse is available, any attempt to click outside the editable area will also terminate the statement. The current text is redrawn in the original attribute if the attribute property is set to other than HEX(00).

In single line edit controls, depth zero or 1, then auto-horizontal scrolling is supported if the width field is less than the size of the alpha-receiver. If the width is zero then the size of the control will be set to the size of the alpha-receiver. If the width exceeds the size of the receiver then a X70 error occurs. RETURN or any non-editing function key will terminate the edit.

In multiline edit controls the text is formatted differently if the optional word wrap property is enabled. Without word wrap each line in the text, marked by a delimiter character which is specified in the delimiter property but which is normally HEX(0D), is put in a separate line of the control. With wrap the text is formatted to word wrap according to the control width with automatic vertical scrolling enabled if not all the text will fit in the depth available.

If the RemoteExec property is set while executing in Windows KCML or if using the WDW terminal emulator (version 3.00 or greater) then the editing will be delegated to Windows.

Horizontal and vertical scroll bars are optional for multiline controls and appear outside the defined area of the control. These can only be added if remotely executing under Windows.

When RETURN is pressed in a multiline control a delimiter character is embedded into the text at that point. When word wrap is enabled the control may break the text at the end of each row to fit the width but no record of this is embedded in the text. However it is possible to ask the control to mark the line ends when copying the text back to the alpha-receiver by setting the markrows property. Rows delimited this way can be separated into rows of an array variable for easy manipulation with [\$UNPACK]($UNPACK.htm) e.g.

LOCAL DIM text\$640, lines\$(8)80\
FLD(prop\$.ed_delimiter)=HEX(0D)\
FLD(prop\$.ed_markrows)=1\
LINPUT+text\$,prop\$\
\$UNPACK(D=HEX(010D))text\$ to lines\$()

The cursor state and the current attribute are preserved across a LINPUT+. If the interrupt key (Ctrl+BREAK) is pressed during a LINPUT+, there is no immediate effect until the LINPUT+ is terminated.

LINPUT + control bytes

Field Name

Used

Format

Description

.ed_resultlen

OUT

(1,"B4")

Size of returned string.

.ed_returnkey\$

OUT

(5,1)

Terminating key value e.g. HEX(0D) for return, HEX(7E) for TAB.

.ed_returnpf

OUT

(6,"B1")

Type of terminating key.\
1 for PF key or 0 for HEX(0D).

.ed_width

IN

(7,"B1")

Size of editable area. If zero then the full size of the alpha variable is assumed.

.ed_depth

IN

(8,"B1")

Depth of the edit control.\
0 or 1 for single line entry.

.ed_attribute\$

IN

(9,1)

Attribute to be used. Attributes are restored on exit. HEX(08) underline, HEX(20) bright, HEX(40) reverse video.

.ed_color\$

IN

(10,1)

Reserved.

.ed_wordwrap

IN

(11,"B1")

Wordwrap.\
0 for no wrap, 1 for word wrap. Only meaningful for multiline edit controls.

.ed_vscrollbar

IN

(12,"B1")

Vertical scrollbar.\
0 for no vertical scrollbar, 1 for add vertical scrollbar. Only meaningful for multiline edit controls done in Windows.

.ed_hscrollbar

IN

(13,"B1")

Horizontal scrollbar\
0 for none, =1 for add horizontal scrollbar. Only meaningful for multiline edit controls done in Windows.

.ed_delimiter

IN

(14,1)

Character that ends paragraphs. Uses HEX(0D) by default. Multiline edit controls only.

.ed_markrows

IN

(15,"B1")

End of line delimiter\
0 for none, 1 for delimiter characters to be added to the end of each row in a multiline edit control.

.ed_displayonly

IN

(16,"B1")

Display only\
0 for normal, 1 for display text in control and return immediately, 2 for display text but allow no modifications.

.ed_selectonentry

IN

(17,"B1")

Select text on entry\
0 to select all text initially, 1 for none.

.ed_remoteexec

IN

(18,"B1")

Remote execution\
0 for local execution, 1 for use Windows control. Only available in Windows KCML or with the KClient program

.ed_paragraph

IN

(19,1)

Paragraph symbol to use, HEX(00) for none. The suggested character is ¶ i.e. HEX(B6) in the 8 bit ISO-8/ANSI character set used with KCML5 or HEX(8F) in the 7 bit US KCML character set used with KCML4.

.ed_passwd

IN

(20,1)

Password character. If HEX(00) then display characters as entered. Otherwise display all characters as the specified value as they are entered.

.ed_startpos

IN\
OUT

(21,"B4")

4 byte integer maintained by LINPUT + containing the index of the top left hand corner character visible in a scrollable multiline input area, indexed from 0. (See below.) These bytes do not have any effect if remote execution is enabled. They will be zero if no scrolling has taken place.

.ed_cursorpos

IN\
OUT

(25,"B4")

4 byte integer maintained by LINPUT + containing the index of the current cursor character indexed from 0. (See below.) These bytes do not have any effect if remote execution is enabled.

.ed_arabic

IN

(29,"B1")

If in remote execution mode under Windows then this byte can be set to allow Arabic/Hebrew right to left style (R-to-L) input. A value of 0 instructs the control to assume standard English (L-to-R) input. A value of 1 instructs the control to start up in L-to-R mode but the mode can be changed to R-to-L if required using the Windows input method editor hot key. A value of 2 instructs the control to start accepting R-to-L input immediately.

.ed_pg_term

IN

(30,"B1")

If set to 1 then PgUp and PgDown will terminate a LINPUT+

Properties marked IN should be set before the LINPUT+ and properties marked OUT are set by the LINPUT+ and can be inspected after it has terminated.

Bytes 21 and 25 store the index of the first visible character and the index of the current cursor character. This is information is useful if, for example, you need to trap a function key, insert some text at the current cursor position and re-enter the LINPUT + with the text scrolled to the same place. Generally they should be set to zero before the initial LINPUT+ and left unaltered if it is reexecuted.

Sample record:

Click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy a [DEFRECORD](DEFRECORD.htm) defining the LINPUT+ structure into the clipboard. Then switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program.

DEFRECORD ed_linput FLD ed_resultlen = "UINT(4)" : REM Size of returned string. FLD ed_returnkey\$1 : REM Terminating key value e.g. HEX(0D) for return, HEX(7E) for TAB. FLD ed_returnpf = "UINT(1)" : REM Type of terminating key. FLD ed_width = "UINT(1)" : REM Size of editable area. FLD ed_depth = "UINT(1)" : REM Depth of the edit control. FLD ed_attribute\$1 : REM Attribute to be used. FLD ed_color\$1 : REM Reserved. FLD ed_wordwrap = "UINT(1)" : REM Wordwrap. FLD ed_vscrollbar = "UINT(1)" : REM Vertical scrollbar. FLD ed_hscrollbar = "UINT(1)" : REM Horizontal scrollbar FLD ed_delimiter\$1 : REM Character that ends paragraphs. FLD ed_markrows = "UINT(1)" : REM End of line delimiter FLD ed_displayonly = "UINT(1)" : REM Display only FLD ed_selectonentry = "UINT(1)" : REM Select text on entry FLD ed_remoteexec = "UINT(1)" : REM Remote execution FLD ed_paragraph\$1 : REM Paragraph symbol to use, HEX(00) for none. FLD ed_passwd\$1 : REM Password character. If HEX(00) then display characters as entered. FLD ed_startpos = "UINT(4)" FLD ed_cursorpos = "UINT(4)" FLD ed_arabic = "UINT(1)" : REM set to allow Arabic/Hebrew right to left style (R-to-L) input. FLD ed_pg_term="UINT(1)" : REM set to 1 if PgUp and PgDown to terminate LINPUT + END RECORD

Example:

The following example uses the above record and draws a 10x10 word wrapped edit box with a vertical scroll bar. In this example, the edit box is drawn by Windows therefore you must be using a Windows client. It uses the [\$UNPACK]($UNPACK.htm) delimiter mode to break out the lines from the buffer into an array.

DIM text\$640,line\$(8)80,prop\$\_ed_linput\
prop\$ = ALL(HEX(00))\
FLD(prop\$.ed_delimiter\$) = HEX(0D)\
FLD(prop\$.ed_markrows) = 1\
FLD(prop\$.ed_wordwrap) = 1\
FLD(prop\$.ed_width) = 10\
FLD(prop\$.ed_depth) = 10\
FLD(prop\$.ed_remoteexec) = 1\
FLD(prop\$.ed_vscrollbar) = 1\
PRINT AT(10,10);\
LINPUT+text\$,prop\$\
\$UNPACK(D=HEX(010D)) text\$ TO line\$()

See also:

[INPUT](INPUT.htm),\
[LINPUT](LINPUT.htm)
