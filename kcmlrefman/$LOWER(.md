\$LOWER(

------------------------------------------------------------------------

General Form:\
\
1.     alpha_receiver = \$LOWER(alpha_expression)\
\
2.     alpha_receiver = \$LOWER()\
\
3.     \$LOWER() = alpha_expr\
\
\

------------------------------------------------------------------------

This statement is used in the first form to translate all characters in the specified alpha expression into their lowercase equivalents. The newly translated characters are then stored in the alpha receiver.

The translation is performed using a built in translation table and the table in use is determined by the value of byte 50 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE50)

|         |                         |
|---------|-------------------------|
| HEX(00) | US ASCII 7 bit codepage |
| HEX(01) | ISO Latin-1 codepage    |
| HEX(02) | User defined codepage   |

The Latin-1 codepage can be used to translate the case of most western European characters, for example:

STR(\$OPTIONS RUN,50,1)=HEX(01)\
Result\$ = \$LOWER("ABÄ")

would set Result\$ to "abä".

The second form of the statement can be used to extract the translate table currently in effect.

To use a different locale, say the Latin-2 codepage used in Eastern Europe, then the third form of the statement can be used to set a new user defined translate table which must be 256 bytes long. Though the table can be set using this form of the function at any time, to activate this table byte 50 of \$OPTIONS RUN should be set to hex(02).

STR(\$OPTIONS RUN,50,1)=HEX(02)\
\$LOWER() = latin2\$

Compatibility

This function was introduced with KCML 5.0. The user defined tables and the \$LOWER() functions were added for KCML 5.03

See also:

[\$UPPER]($UPPER(.htm)
