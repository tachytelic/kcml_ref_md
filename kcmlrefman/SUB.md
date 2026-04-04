SUB\[C\] <span style="font-size: 16pt ; ">operator</span>

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = ... SUB\[C\] alpha_operand ...\
\

------------------------------------------------------------------------

The SUB operator performs binary subtraction on a pair of binary values. The binary value of the operand is subtracted from the binary value of the receiver variable, the difference is then assigned to the receiver variable. SUB is valid only in the alpha expression portion of an alphanumeric assignment statement.

Subtraction is performed on each individual character of the alpha operand to each corresponding character of the receiving alpha variable, working from right to left starting with the rightmost byte of each character. SUB treats each byte of the alpha operand and receiver variable as an individual value, with no carry propagation between characters. SUB operates on the entire contents of the receiver variable or alpha operand including any trailing spaces.

Example:

DIM record\$2\
record\$ = HEX(0410)\
record\$ = SUB HEX(00F9)

If the \`C' parameter immediately follows SUB, then the value of the alpha operand is treated as a single binary number, it will then be subtracted from the binary value of the receiver variable with automatic carry propagation between characters.

Example:

DIM record\$2\
record\$ = HEX(0410)\
record\$ = SUBC HEX(00F9)

If the alpha operand and the receiver variable are of differing sizes, then the shorter value will be implicitly extended with leading zeros, before the addition takes place. If the result of the subtraction is longer than the receiver variable, then the left most bytes that cannot be stored in the receiver variable, and are truncated.

Syntax examples:

Variable\$ = SUB HEX(FFFC)\
New\$ = SUBC ALL(segment\$)\
FLD(Record\$.type\$) = flag\$ SUB other\$\
Sector\$ = SUBC type\$ SUBC record\$ SUB flag\$
