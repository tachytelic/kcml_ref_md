LINPUT

------------------------------------------------------------------------

General Form:

LINPUT \[literal_string\[,\]\] \[?\] \[-\] alpha_variable \[,\[mask\] \[,cursor_pos\]\]

Where:

mask = reserved\<\
cursor_pos = a numeric expression

------------------------------------------------------------------------

The LINPUT statement allows alphanumeric text to be entered from the keyboard directly into an alpha variable. The text to be entered can contain leading spaces, quotes and commas. The maximum number of bytes that can be received into the alpha variable is 1900.

This statement is only relevant when programming text based applications. New programs should probably use the more functional [LINPUT+](LINPUTplus.htm) statement in preference.

When the LINPUT statement is executed, the optional literal string is displayed on the CO device, followed by a space and the entire contents of the specified alpha variable are recalled and displayed at the current cursor position. The cursor is repositioned to the first character of the recalled input string.

If a minus sign '-' is included immediately before the alpha variable, each character of the variable is underlined, even if the alpha variable is blank.

If a question mark '?' is included before the alpha variable, entry will then start in Text Entry mode as opposed to Edit mode. In Edit mode the function keys are used for cursor positioning or editing. In Text Entry mode the function keys are used to execute a DEFFN' function. The EDIT key toggles between these modes. If the terminal hardware allows, the cursor will blink when in edit mode.

If the optional cursor position is specified, the cursor will initially be positioned at the specified character within the input text. The position is counted from 1 corresponding to the start of the field. Positions outside the limits of the field are ignored and the default value of 1 is assumed.

Example:

temp\$ = "ABCDEFGHIJKLMNOP"\
LINPUT "Enter Text : "-temp\$,,5

If the above example was executed the prompt followed by the contents of temp\$ would be displayed with the cursor located at position 5 (under the letter E).

While entering data at a LINPUT prompt, cursor movement is limited to the area of the screen occupied by the receiving alpha variable. Any attempt to move the cursor or enter text beyond the limits of this area will cause an alarm to bleep every time a key is pressed. The original contents of the alpha variable can be restored if RETURN has not been pressed by pressing the line ERASE key followed by RECALL, in edit mode and ERASE and EDIT RECALL if in text entry mode.

When in text entry mode, any function key may be pressed in response to a LINPUT prompt. If the function key has been defined for text entry with the DEFFN' function, pressing the key at a LINPUT prompt will display the text and insert it into the alpha variable. If the function key has been defined as a subroutine, pressing the key will initiate the subroutine. When a [RETURN](RETURN.htm) statement is executed within the subroutine, program control is returned to the statement immediately after the LINPUT statement.

If running under Microsoft Windows, either using Windows KCML or the KClient program, the mouse can be used to perform the tasks detailed below:

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| **Left Click** | **Left** **Double Click** | **Left** **Drag** | **Right Click** | **Right** **Double Click** | **Right** **Drag** |
| Position cursor | Carriage return | Positions cursor | Abort then execute ‘127 subroutine | Abort then execute ‘127 subroutine | Positions cursor and then aborts and executes ‘127 subroutine |

Input is taken from the INPUT device which can be redirected with the [SELECT INPUT](SELECT_INPUT.htm) statement to allow input from a Unix/DOS file or pipe. An X70 error occurs if LINPUT reads beyond the end of the file. In the example below the [INPUT](SELECT_INPUT.htm) device is selected to read from the Unix date command. The output from the date command is then read into the variable act\$ on line 30:

Example:

DIM act\$64\
SELECT INPUT "date ^"\
LINPUT act\$\
SELECT INPUT /001

Syntax examples:

LINPUT ?-string\$(count)\
LINPUT "Enter field =",FLD(temp\$.name\$),,12

See also:

[INPUT](INPUT.htm),\
[LINPUT+](LINPUTplus.htm)
