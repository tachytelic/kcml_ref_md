IF ... END IF

------------------------------------------------------------------------

General Form:\
\
<img src="bitmaps/ifendif.gif" data-align="BOTTOM" data-border="0" alt="ifendif.gif" />\
     ...\
     \[ELSE\]\
     ...\
     END IF\
    \
Where:\
     <img src="bitmaps/ifendif1.gif" data-align="BOTTOM" data-border="0" alt="ifendif1.gif" />\
     <img src="bitmaps/ifendif2.gif" data-align="BOTTOM" data-border="0" alt="ifendif2.gif" />\
\

------------------------------------------------------------------------

The IF ... END IF statement is used to execute the statements surrounded by the IF and END IF pair if the overall result of all conditions is true. Each IF statement must have a corresponding END IF statement otherwise a run time error will result. There is no limit to the number of statements that can appear between the IF ... END IF pair.

Each pair of operands within the condition should be of the same type (alpha, numeric or field). When evaluating numeric expressions each side of the condition is calculated before the evaluation takes place. The following is a list of valid numeric conditions:

|  |  |
|----|----|
| IF (x) | True if the value of x is anything other than zero. |
| IF (x==y) | True if the value of x equals the value of y. |
| IF (x\<y) | True if the value of x is less than the value of y. |
| IF (x\>y) | True if the value of x is greater than the value of y. |
| IF (x\<=y) | True if the value of x is less than or equal to the value of y. |
| IF (x\>=y) | True if the value of x is greater than or equal to the value of y. |
| IF (x\<\>y) | True if the value of x is not equal to the value of y. Note that \`!=' can be entered instead of \`\<\>' although KCML will always recreate the former as the latter. |

Statements can also contain any number of parentheses to allow conditions to be grouped before they are operated on:

IF ((x==1 AND y==1) OR (a==1 AND b==1))\
...\
END IF

True if the values of x and y are both equal to 1 or the values of a and b are equal to one, e.g. x=1, y=1, a=2, b=3, or x=1, y=2, a=1, b=1.

The evaluation of alphanumeric values is performed on a byte by byte basis working from left to right. The comparison of any two characters is based upon their binary values. For example, the binary value of \`A' is HEX(41), and the binary value of \`B' is HEX(42), therefore the condition "B" \> "A" will be true. The comparison continues until unequal characters are found (if any). The first pair of unequal characters determines the relationship between the values. If alphanumeric values of differing lengths are compared, then the shorter value will be padded out with trailing spaces before the comparison takes place. Alpha expressions can be compared in the same way as with numeric expressions.

Both alpha and numeric field variables can be tested with IF, although only the \`==' or \`\<\>' may be used, e.g.

IF (.field1== .field2 or .name\$\<\>.re\$)\
...\
END IF

Logical operators

Multiple conditions may be separated with the logical operators [AND](AND.htm), [OR](OR.htm) and [XOR](XOR.htm). The conditions are processed from left to right.

If the [AND](AND.htm) operator separates two conditions, the result of both conditions must be true before the overall result can be true. If the first condition is false then the second condition will not be evaluated. E.g.

IF (old\$==new\$ AND was==1)\
...\
END IF

If [OR](OR.htm) separates two conditions, the result of either one condition or both conditions must be true before the overall result can be true. If the first condition is true then the second condition will not be evaluated. E.g.

IF (old\$==new\$ OR was==1)\
...\
END IF

If [XOR](XOR.htm) separates two conditions, the result of exactly one condition must be true before the overall condition is true. Both conditions are evaluated in all cases. E.g.

IF (old\$==new\$ XOR was==1)\
...\
END IF

The END condition

The END keyword may be used in place of any condition within an IF statement. END is used to test whether the end-of-file marker was reached by the previous [READ \#](READhash.htm) statement. The result is true if the end-of-file marker was reached. E.g.

IF (END)

Preceeding END with NOT means that the test will be true if the previous [READ \#](READhash.htm) statement has not reached the end-of-file marker.

IF (NOT END)

The ELSE clause

The ELSE clause can be used within the IF ... END IF pair. The ELSE forces the statements between the ELSE clause and the corresponding END IF to be executed if result of the preceding IF condition is false. If the preceding IF condition is true then the statement in the ELSE clause will be ignored. Complex cascaded IF's are possible using ELSE IF.
