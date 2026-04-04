BOOL operator

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = ... BOOL h operand ...\
\
Where:\
\
     h      = hex digit 0-9 or A-F\

------------------------------------------------------------------------

The BOOL logical operator performs a specified operation on the value of the receiver variable. The operation to be performed is specified by adding a hexadecimal digit after the BOOL statement. This digit must be surrounded by spaces. BOOL can only be used in the alpha expression portion of an alpha assignment statement. The values of both the operand and the receiver variable are operated on, and the result is then stored in the receiver variable. Multiple receiver variables are not allowed.

The BOOL operation is performed on a byte-by-byte basis moving from left to right, starting with the leftmost byte in each field.

If the defined length of the operand is shorter than the length of the receiver variable, then the remaining bytes are left unchanged. If the defined length of the operand is longer than the receiver, then the operation will terminate when the last byte in the receiver variable is operated on. The entire contents of both the receiver variable and the operand, including trailing spaces will be operated on.

The hex digit following the BOOL statement defines the logical operation to be performed. For example, BOOL 1 would specify that a \`not-or' operation is to be performed. Note that several BOOL operations are also available as separate operators, for example BOOL 8 is equivalent to [AND](AND.htm), BOOL E is equivalent to [OR](OR.htm), etc. See the table below for the 16 possible logical functions.

**BOOL Logical Functions**

| Hex Digit | Binary Representation | Logical Function                |
|-----------|-----------------------|---------------------------------|
| 0         | 0000                  | null                            |
| 1         | 0001                  | not OR                          |
| 2         | 0010                  | operand does not imply receiver |
| 3         | 0011                  | complement of receiver          |
| 4         | 0100                  | receiver does not imply operand |
| 5         | 0101                  | complement of operand           |
| 6         | 0110                  | exclusive [OR](XOR.htm)         |
| 7         | 0111                  | not AND                         |
| 8         | 1000                  | [AND](AND.htm)                  |
| 9         | 1001                  | equivalence                     |
| A         | 1010                  | receiver = operand              |
| B         | 1011                  | receiver implies operand        |
| C         | 1100                  | operand = receiver              |
| D         | 1101                  | operand implies receiver        |
| E         | 1110                  | [OR](OR.htm)                    |
| F         | 1111                  | identity                        |

Syntax examples:

test\$ = BOOL A HEX(7F)\
test1\$ = test21\$ BOOL 7 HEX(FF)\
now\$ = then\$ BOOL 6 ALL(HEX(4F))\
STR(was\$,4,2) = BOOL E HEX(2F)
