LET

------------------------------------------------------------------------

<div class="Generalform">

General Forms:\

<div class="indent">

|                                           |     |                     |
|-------------------------------------------|-----|---------------------|
| string-variable \[, string-variable\] ... |     | = string-expression |
| REDIM string-variable                     |     | = string-expression |
| num-variable \[, num-variable\] ...       |     | = num-expression    |
| field-variable \[, field-variable\] ...   |     | = field-expression  |

</div>

\
Where:\

<div class="indent">

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="clear">
<td>string-expression</td>
<td>=</td>
<td>string-operand [string operator string-operand]<br />
string-operand [ &amp; string-operand]</td>
</tr>
<tr class="clear">
<td>field-expression</td>
<td>=</td>
<td>(start , field-spec)</td>
</tr>
<tr class="clear">
<td>field-spec</td>
<td>=</td>
<td>length (string fields)<br />
pack image (numeric fields)<br />
$FORMAT field spec (numeric fields)</td>
</tr>
</tbody>
</table>

</div>

</div>

------------------------------------------------------------------------

The LET statement evaluates the expression on the right hand side of the equals sign and assigns the result to the variable(s) on the left hand side of the equals sign. If more than one variable is used on the left hand side of the equals sign, each variable should be separated with a comma. All variables on the left hand side should all be of the same type (string or numeric), otherwise an error will result.

Note that the LET keyword, allowed in some dialects of BASIC, is not permitted in KCML.

String assignment

The string expression on the right hand side of an string assignment statement can contain any number of string operands and operators. The order in which these are evaluated is from left to right. For example:

Variable1\$ = Var2\$ & Var3\$ & Var4\$

will first concatenate var3\$ to var2\$ and will finally concatenate var4\$ to the end of the previous result. The final string will then be assigned to var1\$.

If the receiving variable(s) are shorter in length than the total length of the result of the string expression, then only the characters up to and including the length of the receiver will be assigned to the receiver. If the receiving variable(s) are longer in length than the total length of the result of the string expression, then the remainder will be padded with trailing spaces.

String assignment with REDIM

This is like the string assignment except that

- Only one variable may appear on the left of the = operator
- The REDIM modifier is used before the variable on the left hand side
- The defined length of the variable will be set to the length of the right hand size clipping any trailing blanks

It is especially useful with [LOCAL DIM](LOCAL_DIM.htm) variables in subroutines as you do not have to oversize them in order to handle incoming string arguments of unknown size. However there is a significant penalty incurred in the resizing process so fixed size strings of up to 200 bytes are probably going to be faster than using a REDIM string.

Numeric assignment

The numeric expression on the right hand side of an numeric assignment statement can contain any number of numeric scalar variables, arrays, constants, functions and expressions, all separated by arithmetic operators. The order in which these are evaluated is from left to right, except when affected by operator priorities. For example:

Variable1 = Var2 + Var3 + Var4

will first add the content of var3 to var2, the total will then be added to var4. The final result will then be assigned to var1.

Each arithmetic operator is given a priority, these are as follows:

1.  ^ exponentation (highest)
2.  \- negation
3.  \*,/ multiplication, division
4.  +,- addition, subtraction (lowest)

Therefore:

v1 = v2 + v3 / v4

will first divide v3 by v4, and add v2 to the result. Parentheses can be used to change the priority, for example to make the above line add v2 to v3 and then divide the result by v4 you would enter:

v1 = (v2 + v3) / v4

Initializing Field variables

The LET statement can also be used to assign values to field variables. Field variables must always start with a full stop. The right hand side of the field assignment should contain two numeric parameters enclosed in parentheses. For example:

.Description\$ = (2,5)\
.Department\$ = (7,14 + Length)\
.Value = (Start, "-#.##)

Syntax examples:

One = 123 \* 45\
Two\$, Reply\$ = First\$ & Second\$ & STR(Third\$,1,2)\
Result\$ = Text\$ AND ALL(HEX(FF))\
One, Two, Three = SIN(Abc) + cir \* \#PI\
.Name\$ = (154, EndRecord)
