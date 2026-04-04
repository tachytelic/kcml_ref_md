DIM(

------------------------------------------------------------------------

General Form:\

1.  DIM(array-name, dimension)\
    \
2.  DIM(field)

Where:

array-name = numeric array name, alpha array name or field array name.\
\
dimension = 1 or 2\
\
field = numeric or string field

------------------------------------------------------------------------

The DIM( function returns the current size of the specified dimension of an array. A value of zero will be returned if the second dimension of a one-dimensional array is requested. The DIM( function is valid wherever a numeric expression is legal.

Starting with KCML6.10, the DIM() function may also be used with numeric or string values to determine the occurs value of the field. This will be one if no occurs is specified. For instance, if .a is (1, "DATE") and .b is (2, "DATE\*5"), then DIM(.a) will be 1 and DIM(.b) will be 5.

Syntax examples:

FOR loop = 1 TO DIM(record(),2)\
size = DIM(flow(),1) \* 2

See also:

[DIM](DIM.htm), [COM](COM.htm), [LIST DIM](LIST_DIM.htm), and the field operators [POS](POS(.htm), [LEN()](LEN(.htm) and [PACK()](PACKfn.htm).
