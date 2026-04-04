TAN(

------------------------------------------------------------------------

General Form:\
\
     TAN(numeric_expression)\
\

------------------------------------------------------------------------

The TAN( function calculates the tangent of a numeric expression. TAN( is valid wherever a numeric function is legal.

The calculation is performed in radians, unless previously instructed with one of the following [SELECT](SELECT_DRG.htm) statements:

SELECT D\
SELECT G\
SELECT R

to SELECT the mode for trigonometric calculations to degrees, gradians or radians respectively.

Syntax examples:

Test = TAN(.723)\
Value = 17+TAN(ABS(temp))

See also:

[ARCTAN(](ARCTAN(.htm), [SELECT D/R/G](SELECT_DRG.htm)

 
