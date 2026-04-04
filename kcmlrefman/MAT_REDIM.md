MAT REDIM

------------------------------------------------------------------------

General Form:\
\

MAT REDIM array_name(diml\[, dim2\])\[length\] \[, ...\]

Where:

|  |  |
|----|----|
| array_name | = an alpha or numeric array variable |
| dim1, dim2 | = positive integer expressions specifying new dimensions. |
| length | = positive integer expression specifying maximum length of each alpha array element. Defaults to 16. |

------------------------------------------------------------------------

The MAT REDIM statement is used to change the size of an array or number of arrays. The new sizes may be greater or smaller than the original size. If the new size is greater than the current allocation a new region of memory is allocated, the original contents copied into it and the original allocation is freed. This can be a relatively expensive operation in terms of CPU time. When the new dimensions are smaller than the original only the dimensions are changed, the surplus space is not freed and the contents of the array outside the new dimensions remain unchanged. To free space from such an array its size should first be set to the special value of zero, which tells KCML to release all the space, then it can then be redimensioned to the new size.

A good strategy for handling large temporary buffers held in COMmon is to [COM](COM.htm) their size to zero so KCML will not allocate any space for them then REDIM to the required size as you need the buffer, remembering to free the space again by REDIMing back to zero size. A more structured approach would be to change the program to call a subroutine to perform the function and to [LOCAL DIM](LOCAL_DIM.htm) the buffer.

Array dimensions can also be changed explicitly during execution of the following statements by specifying the new dimensions, enclosed in parentheses following the array name:

|                          |
|--------------------------|
| [MAT CON](MAT_CON.htm)   |
| [MAT IDN](MAT_IDN.htm)   |
| [MAT READ](MAT_READ.htm) |
| [MAT ZER](MAT_ZER.htm)   |

A one-dimensional array can be converted to a two dimensional array using REDIM. It is also possible to change the shape of an array from a two-dimensional array to a one-dimensional array by zeroing the unwanted dimension. For example:


    DIM a(5,5)
    MAT REDIM a(5)
    PRINT a(1)
    MAT REDIM a(10,10)
    PRINT a(1,1)

It is only possible to redimension shared data arrays to a larger size in the partition that originally dimensioned them.

Compatibility:

Prior to KCML 6.10 array dimensions and string element lengths were each limited to 65535. Now they are limited only by available memory.

Prior to KCML 6.10 if a one dimensional numeric was REDIMed to two dimensions but the second dimension was 1 then it was left as a one dimensional array. This caused problems with the following code


    DIM a(10,10)
    MAT REDIM a(0,0)
    MAT REDIM a(5,1)
    PRINT a(1,1)

which errored on the PRINT because the array was consider as if it had been REDIM a(5) and thus forcing the programmer to insert an extra REDIM to establish the shape e.g.


    DIM a(10,10)
    MAT REDIM a(0,0)
    MAT REDIM a(2,2)
    MAT REDIM a(5,1)
    PRINT a(1,1)

The keyword MAT is optional but it will always be recreated except for the special NPL case of redimensioning scalar strings when byte 2 of [\$OPTIONS LIST]($OPTIONS_LIST.htm#BYTE2) is set to HEX(01).

Syntax examples:

MAT REDIM temp(one,two), variable\$(20)length\
MAT REDIM xray(90)\
MAT REDIM shape(100,0)\
REDIM s\$500

See also:

[DIM](DIM.htm), [COM](COM.htm), [LIST DIM](LIST_DIM.htm), [LOCAL DIM](LOCAL_DIM.htm)
