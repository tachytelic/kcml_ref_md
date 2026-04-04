MAT COPY

------------------------------------------------------------------------

General Form:

MAT COPY \[-\] alpha_variable1 \[\<start,count\>\] TO alpha_variable2 \[\<start,count\>\]

Where:

start, count = a numeric expression

------------------------------------------------------------------------

The MAT COPY statement is used to copy the contents of the source alpha variable or array into another alpha variable or array.

The copy is performed on a byte-by-byte basis, until the receiver variable is filled. If the receiver variable is larger than the source variable, MAT COPY will fill the remaining bytes with spaces.

Portions of data can be copied to or from the variables or arrays using either the [FLD(](FLD(.htm) or [STR(](STR(.htm) functions. An obsolete and deprecated syntax using \<\> also allows the start and count parameters used by the [STR(](STR(.htm) function to be specified separately. For example the following two statements both perform the same task:

MAT COPY STR(temp\$(),5,5) TO STR(file\$(),7,5)\
MAT COPY temp\$() \<5,5\> TO file\$() \<7,5\>

By default MAT COPY copies the data in the order specified by the source variable and left justifies the data in the output variable. A minus sign can precede either the source variable or the receiving variable or both.

- If a minus sign precedes the source alpha variable then MAT COPY copies the data from the source in reverse order, starting with the last byte of the source variable and ending with the first. This is copied to the destination and placed from left to right and blank filled on the right. This has the effect of reversing the order of the string.
- If a minus sign precedes the receiver variable then MAT COPY reverses the order in which each byte is received by the receiver variable. The first byte received is copied into the last position of the receiver variable. This reverses the original string but right justifies it.
- If both source and destination are prefixed with a minus sign then the effect is to right justify the string in the destination without changing the order of the bytes.

The following example shows the various versions of the MAT COPY statement with the contents of the receiver variable when given the two lines of code shown below.

DIM abc\$(4)2, xyz\$(5)2\
abc\$() = "A B C D "

|                               |                        |
|-------------------------------|------------------------|
| MAT COPY abc\$() TO xyz\$()   | xyz\$() = "A B C D   " |
| MAT COPY -abc\$() TO xyz\$()  | xyz\$() = " D C B A  " |
| MAT COPY abc\$() TO -xyz\$()  | xyz\$() = "   D C B A" |
| MAT COPY -abc\$() TO -xyz\$() | xyz\$() = "  A B C D " |
