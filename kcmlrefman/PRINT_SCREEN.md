PRINT SCREEN

------------------------------------------------------------------------

General Form:\
\
     PRINT SCREEN alpha_variable \[,AT(row,column)\] \[, BOX(depth, width)\]\
\
Where:\
\
     row, column, height, width      = numeric expressions\
\

------------------------------------------------------------------------

The PRINT SCREEN statement is used to print the specified screen portion from the alpha variable. The information in the alpha variable is assumed to be in the format used by the [INPUT SCREEN](INPUT_SCREEN.htm) statement. This statement is only relevant when developing text based applications.

The information is printed row by row starting at the specified co-ordinates for the specified depth and width. The requested area of the screen is first cleared using the current video attribute and the information then displayed according to the video parameters stored in the header information fields contained the alpha variable (see [INPUT SCREEN](INPUT_SCREEN.htm)). The AT and BOX values stored in the alpha variable will also be used unless explicitly specified in AT or BOX clauses. A P34 error will result if AT or BOX values exceed the screen size.

The PRINT SCREEN statement will only display complete sections; if the alpha variable is not large enough to contain all sections, missing sections will then be defaulted. For example if the attributes section is not present, the normal video mode is then used and if the character section is not present, all spaces are assumed. If there are less than 80 bytes then nothing happens. Note that by using BOX values that do not match the saved values recorded by [INPUT SCREEN](INPUT_SCREEN.htm) unpredictable results may be expected. For this reason you should not use the BOX clause in all but the most sophisticated applications.

Example:

DIM screen\$152\
PRINT HEX(03);BOX(5,5)\
REPEAT\
     PRINT " Test"\
UNTIL count++ ==4\
INPUT SCREEN screen\$,AT(0,0),BOX(5,5)\
PRINT SCREEN screen\$,AT(10,37)

In the above example, a box containing the word test written 5 times is drawn in the top left hand corner of the screen, it is then copied and redrawn in the middle of the screen.

Syntax examples:

PRINT SCREEN screen1\$\
PRINT SCREEN wind\$(2),AT(10,column)\
PRINT SCREEN STR(an\$,,224),AT(2,2), BOX(12,12)

See also:

[INPUT SCREEN](INPUT_SCREEN.htm), [WINDOW](WINDOW.htm)

 
