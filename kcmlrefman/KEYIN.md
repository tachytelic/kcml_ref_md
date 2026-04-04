KEYIN

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/keyin.gif" data-align="BOTTOM" data-border="0" alt="keyin.gif" />\
<img src="bitmaps/keyin1.gif" data-align="BOTTOM" data-border="0" alt="keyin1.gif" />\
<img src="bitmaps/keyin2.gif" data-align="BOTTOM" data-border="0" alt="keyin2.gif" />\
Where:\
\
     \#stream                = numeric_expression 0\< 255\
\

------------------------------------------------------------------------

The KEYIN statement is used to receive a single character from an input device, usually the keyboard. This statement is only relevant when programming text based applications.

The input device from which KEYIN receives data can be specified with a device address or stream number. If no explicit device specification is used then the input comes from the [INPUT](SELECT_INPUT.htm) device.

The first form of the KEYIN statement contains either no line numbers or a single line number preceded by two commas. This form of KEYIN waits until a character is received from the input device. When the character is received, execution then continues on the statement after the KEYIN statement. If the line number is specified, and the input device is the keyboard, then KEYIN checks to see if the input was a function key, if so program execution will continue at the specified line number.

In the second form of the KEYIN statement, sometimes referred to as a polling KEYIN, the input device is only checked once. If no character is ready to be input then KEYIN will continue with the next statement. If a character is received then KEYIN will jump to the appropriate line. The first line number specifies where to jump to if a standard character is received, the second specifies where to jump to if a [function key](keycodes.htm) in pressed. This form of KEYIN should only be used to clear the input buffer or for the occasional check to see if a break key has been pressed.

When the interrupt key is pressed (Ctrl+BREAK) and input is from the keyboard device then KEYIN will wait for a character before acting on the interrupt but if the input is from any other device then it will interrupt immediately and the contents of the receiver byte will not be predictable.

If running under Microsoft Windows, either using Windows KCML or the KClient program, the mouse can be used to perform the tasks detailed below:

| Left Click | Left Double Click | Left Drag | Right Click | Right Double Click | Right Drag |
|----|----|----|----|----|----|
| 0xF1 at DOWN event. 0xF2 at UP event. | 0xF1 at DOWN event. 0xF2 at UP event. Followed by 0xF3. | 0xF1 at DOWN event. 0xF7 while dragging. 0xF2 at UP event. | 0xF4 at DOWN event. 0xF5 at UP event. | 0xF4 at DOWN event. 0xF5 at UP event. Followed by 0xF6. | 0xF4 at DOWN event. 0xF7 while dragging. 0xF5 at UP event. |

Syntax examples:

KEYIN key_9\$\
KEYIN \#27, test\$,, 420\
KEYIN /01C, temp\$, 5000, 17000\
KEYIN \<address\$\>, temp\$\
KEYIN next_point\$,400,400\
KEYIN PAUSE ON /001\
KEYIN PAUSE OFF /001

See also:

[SELECT INPUT](SELECT_INPUT.htm), [\$BREAK]($BREAK.htm), [KCML key codes](keycodes.htm)
