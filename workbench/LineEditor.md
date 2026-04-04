Line Editing

For terminals that do not support the full screen editor and debugger a simple line editor is available. This is also available in the console window of the KCML Workbench.

Whenever KCML is at the immediate mode colon prompt in the console window it is ready to accept program lines and KCML commands. Program lines are entered by first typing in the required line number, ranging from 0 to 32000, followed by the statements required. If typing reaches the edge of the screen the cursor will wrap-around to the beginning of the next line. Each line can contain up to 1900 characters, although care should be taken when entering long lines as KCML may recreate some statements in a different form that may require more characters. Note that the full screen Workbench editor and debugger has no real limit to the number of characters that can appear on a line. Such very long lines cannot be modified by the line editor as only 1900 characters can appear on the screen at any one time.

Moving the cursor

The EAST and WEST arrow keys may be used to move left and right along the line, and the NORTH and SOUTH cursor keys may be used to move to the line above and below. If the NORTH or SOUTH key is pressed and there are no more lines above or below, then the cursor will jump to the beginning or the end of the line respectively.

Inserting and deleting text

The AUTOINSERT, INSERT and DELETE keys may be used to insert characters and delete characters. These keys may be SHIFT'ed to perform other functions, a full list of keys available during the line editing process is shown in the table. Blocks of text can be deleted by moving the cursor to the first character to be deleted and pressing the SELECT MODE key, next move the cursor to the end of the text and press the DELETE key.

Recalling lines

Lines may be re-edited by pressing the EAST arrow key immediately after the program line number has been typed at the immediate mode prompt. Alternatively the EDIT key followed by the RECALL key may be pressed immediately after the line number. Once the line has been recalled, the cursor is positioned at the end of the line.

The entire contents of a line may be appended to an existing line by typing the line number immediately after the colon separator, and by pressing the EAST arrow key, or the EDIT key followed by the RECALL key. The specified line is then appended to the current line, the specified line number after the colon separator being overwritten.

Cut and pasting text

Text can be copied into the CUT/PASTE buffer by first pressing the SELECT MODE key followed by the directional arrow keys which change the text to be copied into reverse video, once the text has been marked the SELECT MODE key is pressed again which copies the marked text into the paste buffer. To paste the text move the cursor to the correct position and press the PASTE key.

The recall buffer

Previously entered immediate mode commands, modified and deleted program lines and the contents of the CUT and PASTE buffers are all stored in three separate circular buffers. The PAGE-UP and PAGE-DOWN keys will move up and down through the immediate mode commands circular buffer.

Previously deleted or modified program lines can be recalled by first typing any number immediately followed by the PAGE-UP key, which will recall previously deleted and modified program lines. Subsequent depressions of the PAGE-UP and PAGE-DOWN keys will move up and down within the buffer. The line number entered before the initial PAGE-UP has no significance apart from instructing PAGE-UP to use the program line circular buffer.

Text previously placed into the CUT and PASTE buffers is also entered into a circular buffer. To recall text from the buffer the PASTE key should be pressed followed by the PAGE-UP key which will display the previous contents of the paste buffer, subsequent depressions of the PAGE-UP and PAGE-DOWN keys will move up and down through the CUT and PASTE circular buffer.

The maximum number of entries in each of the three circular buffers defaults to 16, this default can be changed with the [\$OPTIONS RUN](mk:@MSITStore:kcmlrefman.chm::/$OPTIONS_RUN.htm) system variable.

Replacing and deleting lines

To replace an existing line with a new line, enter the new line with a line number identical to that of the original line, followed by the new statements and press RETURN. The original line will then be overwritten.

To delete a program line, enter only the line number followed by RETURN. The word "Deleted" appears to confirm the deletion and the line is saved in the recall buffer.

Program lines may be renumbered with the [RENUMBER](mk:@MSITStore:kcmlrefman.chm::/RENUMBER.htm) command.

The keys described in the following table are mapped with the [KCML TERMINFO terminal database](mk:@MSITStore:kcmlrefman.chm::/TextTermGrammar.htm) on UNIX systems Not all keys will be available on all terminals, refer to the Terminal support chapter later in this volume for more information.

<table>
<caption>Keys available during immediate mode and line editing</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Key name<br />
</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr>
<td>AUTOINSERT</td>
<td>Selects AUTOINSERT mode. Once pressed all text after the current cursor position is highlighted, new text can then be inserted, pressing the same key again turns off auto insert mode. Usually CTRL-A</td>
</tr>
<tr>
<td>BACKSPACE</td>
<td>Replaces the character to the left of the cursor with a blank.</td>
</tr>
<tr>
<td>DELETE</td>
<td>Deletes the character at the current cursor position. All text to the right of the cursor moves one character to the left.</td>
</tr>
<tr>
<td>EAST</td>
<td>Moves cursor one character to the right. If pressed immediately after a line number, the line (if it exists) will be recalled.</td>
</tr>
<tr>
<td>EDIT</td>
<td>The EDIT key causes KCML to go into edit mode, deactivating the function keys and allowing them to be used to move the cursor. Pressing edit again takes KCML out of edit mode. As most terminals support cursor naviagation keys the mode is now obsolete.</td>
</tr>
<tr>
<td>ERASE</td>
<td>Deletes all text from the current cursor position to the end of the line. Usually CTRL-E</td>
</tr>
<tr>
<td>HELP</td>
<td>Displays the text mode help screen. Usually CTRL-L</td>
</tr>
<tr>
<td>INSERT</td>
<td>Inserts a blank character at the current cursor position, shifting all text after the cursor to the right by one space.</td>
</tr>
<tr>
<td>NEXT</td>
<td>In edit mode this key can be used to search through the paste circular buffer. In immediate mode the next command or modified program line from the immediate mode or program line circular buffer is recalled, program lines are only recalled if a number is typed before the key is pressed.</td>
</tr>
<tr>
<td>NORTH</td>
<td>Moves the cursor up one line if possible.</td>
</tr>
<tr>
<td>PASTE</td>
<td>Pastes text from the cut and paste buffer. Usuallu CTRL-V</td>
</tr>
<tr>
<td>PREV</td>
<td>In edit mode this key can be used to search through the paste circular buffer. In immediate mode the previous command or modified program line from the immediate mode or program line circular buffer is recalled, program lines are only recalled if a number is typed before the key is pressed.</td>
</tr>
<tr>
<td>RECALL</td>
<td>Recalls the specified program line, or the previous immediate mode command.</td>
</tr>
<tr>
<td>RETURN</td>
<td>Enters the line of text. If RETURN is pressed after an immediate mode command the command is executed.</td>
</tr>
<tr>
<td>SELECT MODE</td>
<td>Also called MARK key. Once pressed the arrow keys may be used to mark text, pressing the same key a second time turns off this mode and copies the marked text into the cut and paste buffer. Usually CTRL-K</td>
</tr>
<tr>
<td>SHIFTEAST</td>
<td>Moves the cursor five characters to the right.</td>
</tr>
<tr>
<td>SHIFTERASE</td>
<td>Deletes the entire line of text in which the cursor is positioned.</td>
</tr>
<tr>
<td>SHIFTNORTH</td>
<td>Moves the cursor to the start of the line.</td>
</tr>
<tr>
<td>SHIFTSOUTH</td>
<td>Moves the cursor to the beginning of the line.</td>
</tr>
<tr>
<td>SHIFTWEST</td>
<td>Moves the cursor five characters to the left.</td>
</tr>
</tbody>
</table>
