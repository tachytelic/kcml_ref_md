Collating sequences

When sorting strings KCML needs rules, called collating sequences, to determine how characters are to be compared. The default case of US ASCII is easy as the position in the code page determines how it should sort - the letter A has an ASCII value of 65 and Z of 90. However in the Latin1 code page where Ä has a value of 196 the relationship between code page value and sorting position has been lost and Ä would sort after Z and not between A and B.

To allow for this KCML has support for two built in collating sequences and there is also a mechanism to allow any arbitrary collating sequence to be added using a shared library. By setting byte 50 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE50) the current table can be specified:

HEX(00)

Default US ASCII

HEX(01)

Latin1

HEX(02)

User defined

This byte also controls how [\$UPPER]($UPPER(.htm) and [\$LOWER]($LOWER(.htm) determine case and how [\$STRCOLL]($STRCOLL(.htm) compares characters. [SORT](SORT.htm) can use collating sequences if the key segments are described using the option KEY clause.
