SELECT PRECISION

------------------------------------------------------------------------

General Forms:\
\
1.      SELECT PRECISION numeric_expression\
\
2.      alpha_receiver = SELECT PRECISION\
\

------------------------------------------------------------------------

KCML represents numbers internally in a form of binary notation. This leads to fast arithmetic, but could lead to problems with comparison. For example \`1.23456' might be represented internally as \`1.2345999999999', therefore the statement \`1.23456 \* 100000 = 123456' could be false.

In order to overcome this problem, any two numbers that are \`sufficiently close' are considered to be equal. The PRECISION select parameter defines \`sufficiently close' to mean two numbers differing by less than the specified numeric expression. By default the precision is \`1E-10'.

The PRECISION select parameter can also be used as a function returning the current precision value.

Example:

SELECT PRECISION 1E-8\
IF 1 = 1 + 1E-9 THEN PRINT "True"\
 \
 True

Syntax examples:

SELECT PRECISION 1E-5\
SELECT PRECISION precision(value)\
SELECT LIST /005, PRECISION precision(value)\
prec\$ = SELECT PRECISION\
PRINT "Current precision is : "; SELECT PRECISION

See also:

[ON ... SELECT](ONSELECT.htm)

 
