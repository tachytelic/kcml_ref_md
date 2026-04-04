'KCMLFnKeyTitle(key, text\$, orig_text\$)

Kclient can display programmable function key buttons at the bottom of a text mode window using this function. Each button has a text string associated with it which can be redefined using this call. The previous text for the button is returned in the third argument and can be used to restore the original text.

It is first necessary to tell the client how many rows of buttons and how many buttons per row will be required by programming a special button zero. The default text for button zero is "0,0" which hides the buttons. To display two rows of eight buttons you would program button zero with "8,2". These buttons will then be displayed with their default text "F1", "F2" etc. corresponding to functions keys '1, '2 and so on.

In fact the buttons can be programmed with general text and can send arbitrary strings or function keys. KClient scans the string looking for a \< and uses the text before the \< as the button title text. Use an & prefix for any accelerator key. It then scans looking for a closing \> and the text between these characters is the text sent to the server when the button is clicked. Text after the closing \> is ignored. If the string inside the \< \> pair starts with a ' character and is numeric then it will be assumed to be a function key. Function keys in the range 0 to 255 are allowed. E.g. "GL\<'124 \>" could be used to program a Glossary key.

Up to 32 buttons can be displayed across up to 4 rows.

Syntax

\$DECLARE 'KCMLFNkeyTitle(INT(), STR(), RETURN STR())

Returns

The function has no return value.

Notes

If a particular program redefines the buttons it is good practice to reset them back to the defaults for the next application which may expect to find them that way. It is not necessary to restore buttons individually to their original texts as you can reset back to the defaults for all buttons with ['KCMLFNkeyDefault()](KCMLFNkeyDefault.htm).

It is vital that the *orig_text\$* variable is big enough to hold the original text. A minimum of 32 characters is recommended. If you don't need to know the original value use 0 instead.

Example

PRINT HEX(03);"FN key buttons demo" \$DECLARE 'KCMLFNkeyTitle(INT(),STR(),RETURN STR()) DIM orig_title\$(21)32 REM display 20 buttons with default titles 'KCMLFNkeyTitle(0, "10,2", orig_title\$(21)) INPUT a\$ REM change titles programmatically FOR i = 1 TO 20 'KCMLFNkeyTitle(i, \$FMT("SF'##", i), orig_title\$(i)) NEXT i INPUT a\$ REM hide buttons 'KCMLFNkeyTitle(0, "0,0", 0) INPUT a\$
