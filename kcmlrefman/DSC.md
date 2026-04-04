DSC <span style="font-size: 16pt ; ">operator</span>

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = ... DSC alpha_operand ...\
\

------------------------------------------------------------------------

The DSC (decimal subtract with carry) alpha operator performs decimal subtraction on a pair of unsigned packed decimal values. The decimal value of the operand is subtracted from the decimal value of the receiver variable, the sum is then assigned to the receiver variable. DSC is valid only in the alpha expression portion of an alphanumeric assignment statement.

Subtraction is performed on each individual byte of the alpha operand to each corresponding byte of the receiving alpha variable, working from right to left starting with the rightmost byte of both the receiver variable and the operand. DSC treats each byte of the alpha operand and receiver variable as an individual value, with automatic carry propagation between characters. DSC operates on the entire contents of the receiver variable or alpha operand including any trailing spaces.

The DSC operator assumes that both operands are true unsigned BCD numbers. Any characters other than 0 through to 9 are invalid and will produce undefined results.

Syntax examples:

color\$ = count\$ DSC bytes\$\
paint\$ = field\$ DSC HEX(0099)

See also:

[DAC](DAC.htm), [PACK](PACK.htm), [UNPACK](UNPACK.htm)

 
