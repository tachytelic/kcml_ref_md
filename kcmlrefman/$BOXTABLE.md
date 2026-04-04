\$BOXTABLE

General Forms:\
\
1.      \$BOXTABLE = alpha_expression\
\
2.      alpha_variable = \$BOXTABLE\
\

------------------------------------------------------------------------

The \$BOXTABLE function is used to set a table used on text mode terminal to simulate the [PRINT BOX()](PRINT_BOX(.htm) KCML box graphic segments using characters. Terminals such as Kclient and WDW can draw boxes as overscores without any special help. The size of the string and the actual characters used will be specific to the terminal and for more details you should refer to the section about [character boxes](TextTermCharBox.htm) and [soft font boxes](TextTermSoftFont.htm) in the Text Terminal chapter.

Generally the TERMINFO database will predefine the string for you but ofter it will leave the first byte as HEX(00). This disables the use of \$BOXTABLE. Other possible values are

| Byte 1 | Purpose |
|----|----|
| HEX(00) | Assume terminal can do true KCML boxes and issue native sequences. |
| HEX(01) | [Characters boxes](TextTermCharBox.htm). This implements boxes with special line drawing characters. Boxes drawn this way are bigger than regular KCML boxes as a row of characters above the box is used. Character boxes will only be used if the cell would otherwise be blank. In this mode the \$BOXTABLE string is 17 bytes long. Typically used with [VT100](TextTermVT100.htm) and [ANSI](TextTermAnsi.htm) terminals but also available for legacy applications with WKCML, [WDW](TextTermWDW.htm) and [Kclient](TextTermKclient.htm). |
| HEX(02) | [Soft font boxes](TextTermSoftFont.htm). This implements boxes as overscored characters in a special downloaded soft font. These are similar to KCML boxes though the box segments will take on the attributes of the characters beneath them. Typically used with [VT220](TextTermVT220box.htm) and [Wyse60](TextTermWy60box.htm) terminals. In this mode the string is 9 bytes long. |
| HEX(7F) | Do not issue any sequences to the terminal for boxes. |

Syntax examples:

STR(\$BOXTABLE,1,1) = HEX(00)
