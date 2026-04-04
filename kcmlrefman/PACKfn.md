PACK(

------------------------------------------------------------------------

General Form:

PACK(field_variable)

------------------------------------------------------------------------

The PACK( string function, when applied to a [field](TutorialFields.htm), is used to determine the [packing format](tmp/xp.htm) used by the field. It can be used anywhere a string expression is allowed.

.f1\$ = (1,"CHAR(16)")\
pack\$=PACK(.f1\$)\
PRINT pack\$\
\
CHAR(16)

The [POS(](POS(.htm) function may be used to return the starting position of a field variable and the [LEN(](LEN(.htm) function can return the size in bytes occupied by the field.
