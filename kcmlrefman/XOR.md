XOR <span style="font-size: 16pt ; ">operator</span>

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = .... XOR alpha_operand ....\
\
Where:\
<img src="bitmaps/xor.gif" data-align="BOTTOM" data-border="0" alt="xor.gif" />\
\

------------------------------------------------------------------------

The XOR logical operator performs a logical XOR (exclusive [OR](OR.htm)) operation on the alpha operand and the contents of the alpha receiver, the result is then assigned to the alpha receiver. The XOR operator is valid only in the alpha expression portion of an alphanumeric assignment statement. The forms

alpha\$ = alpha\$ XOR beta\$\
alpha\$ = XOR beta\$

are considered to be the same however in the second case it is not permitted to have multiple receivers on the left hand size of the \`='.

The [XOR](XOR.htm) operation is performed on a character-by-character basis moving from left to right, starting with the leftmost character in each field.

If the defined length of the operand is shorter than the length of the receiver, then the remaining characters are left unchanged. If the defined length of the operand is longer than the receiver, then the operation will terminate when the last character in the receiver is operated on.

The entire contents of the receiver variable, including trailing spaces will be operated on. Likewise, the entire contents of the operand, including trailing spaces will be used.

The XOR operator can also be used in [IF ... THEN](IFTHEN.htm) statements to separate multiple conditions.

DIM source\$10\
source\$ = ALL(HEX(0F)) XOR HEX(13)\
PRINT HEXOF(source\$)\
 \
 1C0F0F0F0F0F0F0F0F0F

See also:

[AND](AND.htm), [OR](OR.htm), [BOOL](BOOL.htm), [IF ... THEN](IFTHEN.htm)
