SELECT D/R/G

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/selectdgr.gif" data-align="BOTTOM" data-border="0" alt="selectdgr.gif" />\
\
Where:\
\
     D           = use degrees for trigonometric functions\
\
     G           = use gradians for trigonometric functions\
\
     R           = use radians for trigonometric functions\
\

------------------------------------------------------------------------

The {D,R,G} select parameter statement sets the mathematical mode for calculating trigonometric functions. By default all calculations are performed in radians. The system resets to the default of radians after a [CLEAR](CLEAR.htm) or a SELECT R.

Example:

SELECT RADIANS\
PRINT SIN(120)\
SELECT GRADIANS\
PRINT SIN(120)\
SELECT DEGREES\
PRINT SIN(120)\
 \
 0.5806111842123\
 0.9510565162952\
 0.8660254037844

See also:

[ON ... SELECT](ONSELECT.htm)
