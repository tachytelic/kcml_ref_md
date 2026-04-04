AND <span style="font-size: 16pt ; ">operator</span>

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = .... AND alpha_operand ....\
\
Where:\

<img src="bitmaps/and.gif" data-align="BOTTOM" data-border="0" alt="and.gif" />\
\

------------------------------------------------------------------------

The AND logical operator performs a logical AND operation on the alpha operand and the contents of the alpha receiver variable, the result is then assigned to the alpha receiver. The AND operator is valid only in the alpha expression portion of an alphanumeric assignment statement.

The AND operation is performed on a character-by-character basis moving from left to right, starting with the leftmost character in each field. If the defined length of the operand is shorter than the length of the receiver, then the remaining characters are left unchanged. If the defined length of the operand is longer than the receiver, the operation will terminate when the last character in the receiver is operated on.

The entire contents of the receiver variable, including trailing spaces will be operated on. Likewise, the entire contents of the operand, including trailing spaces will be used.

Syntax examples:

include\$ = AND HEX(4F)\
the\$ = AND byte\$\
was\$ = temporary\$ AND HEX(9F)

See also:

[OR](OR.htm), [XOR](XOR.htm)

<span style="font-family: Courier,monospace; "> </span> 
