OR <span style="font-size: 16pt ; ">operator</span>

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = .... OR alpha_operand ....\
\
Where:\
<img src="bitmaps/or.gif" data-align="BOTTOM" data-border="0" alt="or.gif" />\
\

------------------------------------------------------------------------

The OR logical operator performs a logical OR operation on the alpha operand and the contents of the alpha receiver, the result is then assigned to the alpha receiver. The OR operator is valid only in the alpha expression portion of an alphanumeric assignment statement.

The OR operation is performed on a character-by-character basis moving from left to right, starting with the leftmost character in each field. If the defined length of the operand is shorter than the length of the receiver, then the remaining characters are left unchanged. If the defined length of the operand is longer than the receiver, then the operation will terminate when the last character in the receiver is operated on.

The entire contents of the receiver variable, including trailing spaces will be operated on. Likewise, the entire contents of the operand, including trailing spaces will be used.

The OR operator can also be used in the [IF ... END IF](IFENDIF.htm) statement to separate multiple conditions.

Example:

DIM source\$10\
source\$ = ALL(HEX(0F) OR HEX(13)

Syntax examples:

one\$ = OR HEX(4F)\
two\$ = OR three\$\
test\$ = OR STR(new\$,10,1)\
town\$ = first\$ OR second\$

See also:

[AND](AND.htm), [XOR](XOR.htm), [IF ... END IF](IFENDIF.htm)

 
