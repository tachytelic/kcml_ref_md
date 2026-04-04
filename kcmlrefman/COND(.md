COND(

------------------------------------------------------------------------

General Form:\
\
     COND(cond1 \[operator cond2\] ... )\
\
     Where:\
     <img src="bitmaps/cond.gif" data-align="BOTTOM" data-border="0" alt="cond.gif" />\
     <img src="bitmaps/cond1.gif" data-align="BOTTOM" data-border="0" alt="cond1.gif" />\
\

------------------------------------------------------------------------

The COND( function converts a condition into a Boolean expression with zero considered to be [FALSE](FALSE.htm) and non-zero considered to be [TRUE](TRUE.htm). The condition may contain a mixture of both alpha and numeric conditions separated by logical operators.

The COND( function compliments the [BOOL(](BOOL(.htm) function which converts a numeric expression to a Boolean expression, for example:

age = 20\
height = 6.6\
sex\$ = "M"\
result = COND(age\<25 AND sex\$=="M")\
IF (BOOL(result) AND height\>6)\
     type\$="TALL MALE"\
END IF

would set the variable type\$ to "TALL MALE".

The COND( function is valid wherever a numeric expression is valid.

Syntax examples:

testing = COND(abc\<10 OR tmp\$=STR(a\$,,2))\
tmp = COND(NOT a\<=10 AND tmp\$=z\$ OR B=6)

See also:

[BOOL(](BOOL(.htm)

 
