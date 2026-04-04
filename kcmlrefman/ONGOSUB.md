ON ... GOSUB/GOTO

------------------------------------------------------------------------

General Form:\
\
<img src="bitmaps/ongosub.gif" data-align="BOTTOM" data-border="0" alt="ongosub.gif" />\
\
Where:\
\
     label           = a defined subroutine name, or a program line number\
\

------------------------------------------------------------------------

The ON GOSUB/GOTO statement is used to conditionally branch to one of several possible line numbers or routines. Transfer is made to the Nth line number or subroutine label in the list of numbers and labels if the integer value of the expression is N.

For example if the variable count is set to 5 then the following statement would branch to line 9000:

00010 ON count GOTO 100,200,400,900,9000,9900

If the value of the expression is less than 1 or greater than the number of specified line-numbers or labels, or the value of the expression points to a null line-number, no branch is taken. Null line numbers are indicated by consecutive commas in the list of line-numbers and labels. If no branch is made then the [ELSE](ELSE.htm) clause, if specified, is executed, otherwise the next statement in the program is executed.

The branch value can also be specified with an alpha variable or string function. When an alpha variable or string function is used with the ON ... GOSUB/GOTO statement, the binary value of the first byte in the alpha variable or function is used as the branch variable.

For example, if the variable test\$ was set to HEX(02FFFFFF) then the following statement would branch to the defined subroutine 'open_record:

ON test\$ GOSUB 'close_record, 'open_record

Syntax examples:

ON var1 GOTO 1000, 2000, 3000, 4000,\
ON test GOSUB 90,30,,'temp,'open,,9000\
ON FLD(tmpfile\$.branch\$) GOSUB 40,60,,90

 
