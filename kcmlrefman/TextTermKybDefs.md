TERMINFO Keyboard definitions

|  |  |
|----|----|
| AnsiKey | Special keyword for the SCO console driver where all escape sequences consist of 3 characters Esc \`\[ x'. This keyword should be set to \`\E\[' and the key will be returned as a complex key value x for each of the 64 possible x's from 0x40 to 0x7F. |
| AutoInsert | Defines the AUTOINSERT key. Once pressed all text after the current cursor position is highlighted, new text can then be inserted, pressing the same key again turns off auto insert mode. This key works in Immediate mode and within [LINPUT](LINPUT.htm) and INPUT statements. |
| Cancel | Used by the editor to change edit mode. Returns HEX(F0) to [KEYIN](KEYIN.htm). |
| Clear | When pressed in the editor the text "[CLEAR](CLEAR.htm) " appears. Returns HEX(81) to [KEYIN](KEYIN.htm). |
| Complex(n) | Returns the complex key n. May be re-mapped with second half of the [\$KEYBOARD]($KEYBOARD.htm) function. |
| Continue | When pressed in the editor the text "[CONTINUE](CONTINUE.htm) " appears. Returns HEX(84) to [KEYIN](KEYIN.htm). |
| DeadKey(n) | Defines a key sequence which [KEYIN](KEYIN.htm) will interpret as two characters, HEX(FF) followed by *n*. For instance the underline key on 2236 terminals would be described as DeadKey(0xA0) = \xFE\xA0. |
| Dectab | Not used in the editor. Returns function key HEX(5F) to [KEYIN](KEYIN.htm). Same as pf(0x5F). |
| Delete | Used by the editor to delete a single character at the cursor. Returns function key HEX(49) to [KEYIN](KEYIN.htm). Same as pf(0x49). |
| East | Right arrow cursor movement key. Moves right one character in the editor or within [LINPUT](LINPUT.htm) fields. When used at start of a blank line, or immediately after a line number has been entered, in the editor this key will recall the previous line or the line whose number is to the left. Returns function key HEX(4C) to [KEYIN](KEYIN.htm). Same as pf(0x4C). |
| Edit | Synonym for cancel. |
| Erase | Used by the editor to delete from the cursor to the end of the line. Returns HEX(E5) to [KEYIN](KEYIN.htm). |
| Execute | Returns ordinary key HEX(82) to [KEYIN](KEYIN.htm). Terminates [LINPUT](LINPUT.htm). |
| Fn | Synonym for tab. |
| FunctionKey | Special key word for Wang 2x36 type terminals. If set to \xFD it tells **KCML** that the character to follow should be considered a complex function key. |
| Gl | Glossary key. Returns function key HEX(7C) to [KEYIN](KEYIN.htm). Executes DEFFN'124 from editor or [LINPUT](LINPUT.htm) if not in edit mode and the program is resolved. Same as pf(0x7C). |
| Help | Invokes the help system. No key is passed to the application but it is equivalent to function key 'E1. |
| Ignore | The key sequence is read but ignored. |
| Insert | Used by the editor to insert a single character at the cursor. Returns function key HEX(4A) to [KEYIN](KEYIN.htm). Same as pf(0x4A). |
| Load | When pressed in the editor the text "LOADload " appears. Returns HEX(A1) to [KEYIN](KEYIN.htm). |
| Map(n) | Returns the simple key *n* to [KEYIN](KEYIN.htm). May be re-mapped with the first half of the [\$KEYBOARD]($KEYBOARD.htm) statement. |
| Next | Used by the editor to display the next stored command from the circular immediate mode command, program line or paste buffer. Ignored by [LINPUT](LINPUT.htm). Returns function key HEX(43) to [KEYIN](KEYIN.htm). Same as pf(0x43) |
| North | Up arrow cursor movement key. Moves up a line in the editor or [LINPUT](LINPUT.htm). Returns function key HEX(46) to [KEYIN](KEYIN.htm). Same as pf(0x46). |
| Paste | Defines the paste key. Pastes text from the cut and paste buffer. The text is entered into the buffer with the SelectMode key. This key works in Immediate mode and within [LINPUT](LINPUT.htm) and INPUT statements. |
| Pf(*n*) | Defines a function key. Returns value *n* as a function key. *n* can be any number but if *n* is between 32 and 63 it is considered to be the same as *n*-32. This is to cope with terminals which use the extended DW keyboard protocol. |
| Prev | Used by the editor to display the previous stored command from the circular command buffer. Ignored by [LINPUT](LINPUT.htm). Returns function key HEX(42) to KEYIN. Same as pf(0x42). |
| Recall | Recalls either last immediate mode line or the line whose number is to the left of the cursor. Returns function key HEX(4F) to [KEYIN](KEYIN.htm). Same as pf(0x4F). Has same effect as pressing right arrow at the end of a line. |
| Run | Synonym for execute. When pressed in the editor the text "[RUN](RUN.htm)" appears. |
| SelectMode | Defines the select mode key. Once pressed the arrow keys may be used to mark text, pressing the same key a second time turns off this mode and copies the marked text into the cut and paste buffer. The paste key may be used to paste the new text at the current cursor position. This key works in immediate mode and within [LINPUT](LINPUT.htm) and INPUT statements. |
| ShiftCancel | Not used in the editor. Returns function key HEX(50) to [KEYIN](KEYIN.htm). Same as pf(0x50). |
| ShiftDelete | Used by the editor to delete 5 characters at the cursor. Returns function key HEX(59) to [KEYIN](KEYIN.htm). Same as pf(0x59). |
| ShiftEast | Shifted right arrow cursor movement key. Moves right 5 characters in the editor or [LINPUT](LINPUT.htm). Returns function key HEX(5C) to [KEYIN](KEYIN.htm). Same as pf(0x5C). |
| ShiftErase | Used by the editor to delete the entire line. Returns function key HEX(E5) to [KEYIN](KEYIN.htm). Same as pf(0xE5). |
| ShiftFn | Synonym for ShiftTab. |
| ShiftGl | Shifted glossary key. Returns function key HEX(7D) to [KEYIN](KEYIN.htm). Executes DEFFN'125 from editor or [LINPUT](LINPUT.htm) if not in edit mode and the program is resolved. Same as pf(0x7D). |
| ShiftInsert | Used by the editor to insert 5 characters at the cursor. Returns function key HEX(5A) to [KEYIN](KEYIN.htm). Same as pf(0x5A). |
| ShiftNext | Not used by the editor or [LINPUT](LINPUT.htm). Returns function key HEX(53) to [KEYIN](KEYIN.htm). Same as pf(0x53). |
| ShiftNorth | Shifted up arrow cursor movement key. Move to start of line in the editor or [LINPUT](LINPUT.htm). Returns function key HEX(56) to [KEYIN](KEYIN.htm). Same as pf(0x56). |
| ShiftPrev | Not used by the editor or [LINPUT](LINPUT.htm). Returns function key HEX(52) to [KEYIN](KEYIN.htm). Same as pf(0x52). |
| ShiftSouth | Shifted down arrow cursor movement key. Move to end of line in the editor or [LINPUT](LINPUT.htm). Returns function key HEX(55) to [KEYIN](KEYIN.htm). Same as pf(0x55). |
| ShiftTab | Returns function key HEX(7F) to [KEYIN](KEYIN.htm). Executes DEFFN'127 from editor or [LINPUT](LINPUT.htm) if not in edit mode and the program is resolved. Same as pf(0x7F). |
| ShiftWest | Shifted left arrow cursor movement key. Moves left 5 characters in the editor or [LINPUT](LINPUT.htm). Returns function key HEX(5D) to [KEYIN](KEYIN.htm). Same as pf(0x5D). |
| Simple(n) | Returns the simple key n to [KEYIN](KEYIN.htm). May be re-mapped with the first half of the [\$KEYBOARD]($KEYBOARD.htm) function. |
| South | Down arrow cursor movement key. Moves down a line in the editor or [LINPUT](LINPUT.htm). Returns function key HEX(45) to [KEYIN](KEYIN.htm). Same as pf(0x45). |
| SwapMode | Special key used on the SCO/Interactive console to toggle the screen between text and graphics modes in order to use the MultiScreen feature. |
| Tab | Returns function key HEX(7E) to [KEYIN](KEYIN.htm). Executes DEFFN'126 from editor or [LINPUT](LINPUT.htm) if not in edit mode and the program is resolved. Same as pf(0x7E). |
| West | Left arrow cursor movement key. Moves left one character in the editor or [LINPUT](LINPUT.htm). Returns function key HEX(4D) to [KEYIN](KEYIN.htm). Same as pf(0x4D). |
| XparKey | Defines a character which is itself ignored but which indicates that the following character is not to be considered as complex. E.g. on a 2236 terminal you should define XparKey=\xFC. |
