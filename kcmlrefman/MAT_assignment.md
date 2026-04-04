MAT assignment

------------------------------------------------------------------------

General Form:\

- \[MAT\] numeric_receiver_array = numeric_array2

------------------------------------------------------------------------

The MAT assignment assignment statement replaces each element of the receiver array with the contents of the array on the right hand side of the equals sign. The dimensions of a numeric receiver array are automatically adjusted to agree with the dimensions of the array on the right hand side.

The keyword MAT is not required and the KCML workbench will drop it automatically. This is to be consistent with the usage of the [LET](LET.htm) statement. Thus the old deprecated BASIC grammar of


    MAT A = B

will be automatically rewritten by KCML as


    A() = B()

Note that string arrays can also be copied with a similar grammar though this is just a special case of [LET](LET.htm) and there is no automatic resizing of the destination unless the REDIM keyword is used


    p$() = q$()

Syntax example:

first() = second()\
