DAC <span style="font-size: 16pt ; ">operator</span>

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = ... DAC alpha_operand ...\
\

------------------------------------------------------------------------

The DAC (decimal add with carry) alpha operator performs decimal addition on a pair of decimal values. The decimal value of the operand is added to the decimal value of the receiver variable, the sum is then assigned to the receiver variable. DAC is valid only in the alpha expression portion of an alphanumeric assignment statement.

Addition is performed on each individual byte of the alpha operand to each corresponding byte of the receiving alpha variable, working from right to left starting with the rightmost byte of both the receiver variable and the operand. DAC treats each byte of the alpha operand and receiver variable as an individual value, with automatic carry propagation between characters. DAC operates on the entire contents of the receiver variable or alpha operand including any trailing spaces.

The DAC operator assumes that both operands are true unsigned BCD (Binary Coded decimal) numbers. Any characters other than 0 through to 9 are invalid, and will produce undefined results.

Syntax examples:

bytes\$ = old\$ DAC new\$\
bytes\$ = old\$ DAC HEX(0099)

See also:

[DSC](DSC.htm), [PACK](PACK.htm), [UNPACK](UNPACK.htm), [ADD\[C\]](ADD.htm)

 
