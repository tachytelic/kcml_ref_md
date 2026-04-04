LINPUT LINE

------------------------------------------------------------------------

General Form:\
\
     LINPUT LINE alpha_expression, num_receiver \[ ,alpha_receiver\]\
\

------------------------------------------------------------------------

The LINPUT LINE statement provides a ring menu feature similar to the menus used in many modern PC products. The alpha expression should be a string with one or more words separated by spaces.

This statement is only relevant when developing text based applications.

When executed KCML will print the string on the [CO](SELECT_CO.htm) device at the current cursor position and will reverse video the first word. The cursor is not explicitly turned off. The space-bar or right arrow keys will advance the reverse video marker to the next word, wrapping back to the start if the end has been reached. The backspace or left arrow keys move the marker backwards. Pressing a key corresponding to the first letter of any word will select the next instance of such a word. If the optional alpha receiver is specified then the value of the function key used to terminate the statement is returned in the alpha receiver. If no alpha receiver is specified then only RETURN or EXECUTE will terminate. In both cases the receiver variable is set to the index of the word currently marked. If CANCEL or SHIFT TAB is pressed then the statement terminates with zero as the index in the receiver.

By setting the receiver variable to a non-zero value the statement will start with the marker at the corresponding word. Words with embedded underscore characters have them displayed as spaces.

If running under Microsoft Windows, either using KClient or Windows DW, the mouse can be used to perform the tasks detailed below:

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| **Left Click** | **Left Double Click** | **Left Drag** | **Right Click** | **Right Double Click** | **Right Drag** |
| Positions cursor and makes selection | Positions cursor and makes selection. If cursor is off selection then action carriage return. | Positions cursor and makes selection | Abort | Abort | Positions cursor and then aborts |

 

Syntax examples:

LINPUT LINE "Exit Next Prev Select",index\
LINPUT LINE menu\$, position, fnkey\$\
LINPUT LINE FLD(men\$.master\$), position, key1\$

 
