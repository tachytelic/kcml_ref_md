ADD\[C\] <span style="font-size: 16pt ; ">operator</span>

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = ... ADD\[C\] alpha_operand ...\
\

------------------------------------------------------------------------

The ADD operator performs binary addition on a pair of binary values. The binary value of the operand is added to the binary value of the receiver variable, the sum is then assigned to the receiver variable. ADD is valid only in the alpha expression portion of an alphanumeric assignment statement.

Addition is performed on each individual character of the alpha operand to each corresponding character of the receiving alpha variable, working from right to left starting with the rightmost byte of each character. ADD treats each byte of the alpha operand and receiver variable as an individual value, with no carry propagation between characters. ADD operates on the entire contents of the receiver variable or alpha operand including any trailing spaces.

If the \`C' parameter immediately follows ADD, then the value of the alpha operand is treated as a single binary number, it will then be added to the binary value of the receiver variable with automatic carry propagation between characters.

If the alpha operand and the receiver variable are of differing sizes, the shorter value will be implicitly extended with leading zeros, before the addition takes place. If the result of the addition is longer than the receiver variable, the left most bytes that cannot be stored in the receiver variable are truncated.

Syntax examples:

variable\$ = ADD HEX(FFFC)\
variable\$ = ADDC ALL(section\$)\
FLD(record1\$.type\$) = flag1\$ ADDC other\$\
see\$ = ADDC saw\$ ADDC record\$ ADDC record\$

See also:

[DAC](DAC.htm)

<span style="font-family: Courier,monospace; "> </span> 
