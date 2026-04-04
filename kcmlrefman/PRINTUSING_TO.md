PRINTUSING TO

------------------------------------------------------------------------

General Form:\
\
<img src="bitmaps/printusingto.gif" data-align="BOTTOM" data-border="0" alt="printusingto.gif" />\
\
Where:\
<img src="bitmaps/printusingto1.gif" data-align="BOTTOM" data-border="0" alt="printusingto1.gif" />\
<img src="bitmaps/printusingto2.gif" data-align="BOTTOM" data-border="0" alt="printusingto2.gif" />\
\

------------------------------------------------------------------------

The PRINTUSING TO statement is used to store formatted print output in an alpha variable for later use. The statement works in exactly the same way as the [PRINTUSING](PRINTUSING.htm) statement except that the output is printed into an alpha variable instead of the currently selected [PRINT](SELECT_PRINT.htm) device.

The first two bytes of the variable are used to store a binary count of the number of characters stored in the alpha variable. Whenever the PRINTUSING TO statement is executed, the count is retrieved to determine the start position within the variable to begin storing a formatted print line. The first two bytes of the variable should be initialised to HEX(00) before the PRINTUSING TO statement is executed.

If the total number of characters to be stored in the alpha variable exceeds the length of the alpha variable, output is truncated, and the count is set to the length of the alpha variable.

The default action used by PRINTUSING TO can be modified by changing byte 47 of \$OPTIONS RUN as follows:

|  |  |
|----|----|
| HEX(01) | The count in the first two bytes of the string is not required. The formatted output will start at byte 1. No HEX(0d) will be appended and the receiver string will be blank filled. |
| HEX(02) | Tab characters (that is HEX(09)) will be inserted at each of the first blank character separating formats in the image. Surplus leading and trailing blank spaces will be removed. |

The tab insertion mode is intended to simplify the generation of suitable strings for use in list boxes and the KCML grid control. The TabStop\$ property of a listbox can be used to specify where columns should appear. When multicolumn listboxes are populated this way the more natural proportionally spaced default font can be used without spoinling column alignment.

Syntax examples:

PRINTUSING TO pop\$, "-\$###,###.###", array(1)\
PRINTUSING TO xray\$, 9000, temp\$, act(1)\*4\
PRINTUSING TO pqr\$, images\$, test(1)

See also:

[PRINTUSING](PRINTUSING.htm), [\$FMT(]($FMTfn.htm)

 
