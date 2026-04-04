\$STRCOLL(

------------------------------------------------------------------------

General Form:\
\
     numeric_receiver = \$STRCOLL(alpha_expression1, alpha_expression2)\
\

------------------------------------------------------------------------

This function is used to compare two strings for equality using a specific [collating sequence](collate.htm).

Normally strings are always compared for equality by comparing each byte considering it to be an unsigned integer. However, it is also possible to compare two strings for equality using a specific locale collating sequence using the \$STRCOLL( function. \$STRCOLL( returns -1 the first string is less than the second string,+1 if the first string is greater that the second or zero if both strings are equal.

KCML contains a built-in collating sequence for US ASCII and for ISO Latin 1 which will work for most Western European languages. By default KCML uses US ASCII, however this can be changed by setting byte 50 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE50) appropriately.
