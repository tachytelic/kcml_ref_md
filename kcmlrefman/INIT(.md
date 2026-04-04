INIT(

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/init.gif" data-align="BOTTOM" data-border="0" alt="INIT()" />\
Where:\

hh = two hexadecimal digits (0-9, A-F)

------------------------------------------------------------------------

The INIT statement defines a string of characters of unlimited length in much the same way as with the [ALL(](ALL(.htm) function, except that in this case INIT cannot be included on the right hand side of an alpha assignment statement. All characters in the receiver variables will be made equal to the character specified in the statement. If an alpha variable, literal or string function is used then only the first character is used by the INIT statement to initialize the alpha variable list. ALL() has largely made this usage redundant and ALL() is the preferred method of initializing a string.

Syntax examples:

INIT(HEX(FF)) place\$(), record\$\
INIT(STR(as\$,1,1)) fred\$, area\$()\

See also:

[ALL()](ALL(.htm)
