PRINT BOX(

------------------------------------------------------------------------

General Form:\
\
     BOX(height, width \[,fill\] )\
\
Where:\
\
     height, width, fill           = numeric_expressions\
\

------------------------------------------------------------------------

The BOX( function is used to draw or erase boxes or lines on the screen. The BOX( function can only be used in conjunction with the [PRINT](PRINT.htm) statement. This statement is only relevant when developing text based applications. Multiple [PRINT](PRINT.htm) functions ( [AT(](PRINT_AT(.htm), BOX(, [HEXOF(](PRINT_HEXOF(.htm), [TAB(](PRINT_TAB(.htm) ) can be incorporated any where in the [PRINT](PRINT.htm) statement, separated with semi-colons or commas.

The BOX( function uses the current cursor position as the top left hand corner of the box. The height expression specifies the number of lines in the box, and the width expression specifies the number of character positions in the box. If both expressions are negative then the box, if it exists, will be erased.

If both numbers are positive and are both greater than 0, the BOX( function draws a box of the specified dimensions, for example:

PRINT AT(10,10); BOX(5,5)

will print a box 5 characters deep and five characters wide, with the top left hand corner at row 10, column 10.

To remove the same box you would enter:

PRINT AT(10,10); BOX(-5, -5)

By specifying row or column of 0, the BOX( function can be used to draw vertical or horizontal lines on the screen. To print a horizontal line across the screen, starting at row 5, column 5, you would enter:

PRINT AT(5,5); BOX(0, 74)

To remove the same line you would enter:

PRINT AT(5,5); BOX(0, -74)

The optional third parameter specifies the fill pattern for boxes drawn on page printers. This is implemented if the GpdHorizBox and GpdVertBox capabilities are defined within the printers GPDINFO definition. The fill pattern is defined as a percentage scale with 0 defined as no fill and 100 defined as a solid fill. This form of PRINT BOX( does not actually outline the box shape but instead it fills the region that the box bounds so that PRINT BOX(d,w,0) does not have any effect on the page. While this specification allows for a continuous range of fill patterns, in practice there will only be a discrete number of patterns that can be rendered and the printer will usually take the nearest one. A HP LaserJet II for instance can only render 6 distinct patterns. For more information refer to the General Printer Driver Database chapter in Volume 3.

Boxes can be simulated on some terminals that do not implement them natively. This is done in conjunction with the [\$BOXTABLE]($BOXTABLE.htm) function.

Syntax examples:

PRINT AT(10,10);BOX(10,10); box_title\$\
PRINT BOX(0,9); AT(4,4); name\$\
PRINT AT(4,10);BOX(-5,-10); AT(4,7); BOX(0,20)

See also:

[\$BOXTABLE]($BOXTABLE.htm), [PRINT](PRINT.htm), [PRINT AT(](PRINT_AT(.htm), [PRINT HEXOF(](PRINT_HEXOF(.htm), [PRINT TAB(](PRINT_TAB(.htm)
