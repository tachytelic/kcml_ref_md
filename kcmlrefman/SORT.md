SORT

------------------------------------------------------------------------

General Forms:

1.  SORT \[-\] numeric_array
2.  SORT alpha-array
3.  SORT alpha-array \< start, length \>
4.  SORT alpha-array \< field-variable \>
5.  SORT alpha-array KEY key-expr

------------------------------------------------------------------------

The SORT statement is used to sort arrays of alpha or numeric data.

Numeric arrays are sorted by default in ascending order though the order may be reversed by specifying a minus sign before the array name.

Alphanumeric arrays are normally sorted on the whole of each array element but by specifying the start and length of a sub-field within each element the sort can be restricted to that sub-field. Field variables may also be used to specify a subfield, refer to [Field Variables](TutorialFields.htm) for more information. By default alphanumeric arrays are sorted in ascending order, but by specifying a negative start position the array can be sorted into descending order.

Collating sequences:

Starting with KCML 6.0 SORT been enhanced to support sorting strings using multiple segments and optionally using a [collating sequence](collate.htm). This sort mode uses the optional keyword of KEY followed by a string expression defining the segments as 4 byte [segment descriptors](sortdesc.htm).

For example to make a case insensitive sort of the 8 bytes starting at byte 2 you would code something like

DIM segs\$(1)4\
segs\$(1)=HEX(0800 02C0)\
SORT a\$() KEY segs\$()

In this example the array is sorted descending using the first 10 bytes of the element as a key

DIM names\$(4)\
MAT READ name\$()\
DATA "John","Steve","Alan","Paul"\
SORT name\$()\
SORT name\$()\<-1,10\>

Syntax examples:

SORT array1()\
SORT -array1()\
SORT test\$()\
SORT fred\$()\<21,5\>\
SORT records\$()\<.name\$\>\
SORT test\$() KEY segs\$()

See also:

[FSORT](FSORT_BU.htm)
