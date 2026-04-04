KCML Operators

Introduction

As well as the normal operators found in most high level languages, **KCML** also allows many shorthand operators and ternary operators, most of which will be familiar to C programmers. Using these operators not only improves program readability but can also improve performance.

Shorthand operators

The following operators are all available to the **KCML** programmer:

|     |
|-----|
| +=  |
| -=  |
| \*= |
| /=  |
| ++  |
| --  |

All of these operators may be used anywhere that a numeric expression is valid. The first four require that a variable precedes the operator, and any numeric expression must follow the operator. Once the operation is performed the result is stored into the preceding variable, for example:

apple=5 apple\*=5+1 PRINT apple

would return 30. The last two lines could be combined to first perform the operation, assigning the result to the variable *apple,* then display the result, for example:

apple=5 PRINT apple\*=5+1

would perform the same function as the first example.

The ++ operator increments the value of the numeric variable by one and the -- operator decrements the value of the numeric variable by one. The ++ and -- operators may by used as a prefix or a post fix. When used as a prefix the variable concerned is incremented or decremented before it is used, and when used as a post fix it is incremented or decremented after it is used. For example:

pear = apple ++ orange = lemon --

would be the same as

pear = apple apple = apple + 1 orange = lemon lemon = lemon -1

and

pear = ++apple orange = --lemon

would be the same as

apple = apple +1 pear = apple lemon = lemon -1 orange = lemon

Shorthand operators can be used with numeric variables almost anywhere, e.g.

REPEAT PRINT count UNTIL count ++ == 10

would count from 0 to 10.

All of the above operators can also be used with field variables although using post fix and prefix operators with numeric fields should be avoided as it will have an effect on performance as the field will need to be unpacked, changed and repacked.

Ternary operators

Another useful form of operator familiar to C programmers is the ternary operator. Ternary operators allow [IF](IFTHEN.htm) ... THEN ... [ELSE](ELSE.htm) conditions to be used anywhere that a string or numeric expression is legal, for example:

IF (abc \< def) THEN result=1000 ELSE result=2000

could be re-written as

result = ( abc \< def ? 100 : 200 ) \* 10

which would set the variable *result* to 1000 if *abc* was less than the variable *def*, and

IF (total \< 0) THEN disp\$ = HEX(0E) ELSE disp\$=HEX(0F) PRINT "Total =";disp\$; total

could be re-written as

PRINT "Total =";(total\<0?HEX(0E):HEX(0F));total

which would PRINT the value returned by the variable *total* in bold text if it is less than zero. The HEX(0E) is used to change the following output to bold, HEX(0F) restores the to the default of no bold, no reverse video etc. in this case it does nothing.

Parentheses are used to surround the whole operation, the question mark signifies the end of the condition and the start of the return values. The value before the colon (:) is returned if the condition is true and the value after the colon is returned if the condition is false. The condition can be an alpha or numeric condition.

Ternary operators can be used anywhere that a numeric expression is valid and several ternary operators may be embedded within each other, for example:

ab = ((t1=(s\<\>t ? jkl : 100)?ps:200)\<\>xr ? TRUE : FALSE)
