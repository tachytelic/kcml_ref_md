ARCCOS(

------------------------------------------------------------------------

General Form:\
\
     ARCCOS(numeric_expression)\
\

------------------------------------------------------------------------

The ARCCOS( function calculates the arc cosine of a numeric expression. ARCCOS( is valid wherever a numeric function is legal.

The calculation is performed in radians, unless previously instructed with one of the following [SELECT](SELECT.htm) statements:

SELECT DEGREES\
SELECT GRADIANS\
SELECT RADIANS

to SELECT the mode for trigonometric calculations to degrees, gradians or radians respectively.

Syntax examples:

temp = ARCCOS(.723)\
numeric = 17+ARCCOS(ABS(value))

See also:

[COS(](COS(.htm), [SIN(](SIN(.htm), [ARCSIN(](ARCSIN(.htm), [SELECT D/R/G](SELECT_DRG.htm)

<span style="font-family: Courier,monospace; "> </span> 
