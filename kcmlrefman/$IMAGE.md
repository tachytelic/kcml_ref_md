\$IMAGE image specifier

------------------------------------------------------------------------

General Form:\
\
     \$IMAGE \<\< literal_string \[ \[, literal_string\] ...\] \>\>\
\

------------------------------------------------------------------------

Normally the optional line number specified by the [PRINTUSING](PRINTUSING.htm) statement points to a line containing % (Image) statement followed by the format information. If the software is to be distributed in several different countries then the \$IMAGE statement can be used to specify multiple images, one for each language. Byte 20 of the [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20) system variable or the KLANG environment variable is used to select the image. E.g.

STR(\$OPTIONS RUN,20,1)=BIN(1)\
PRINTUSING 9000, 1234.12\
\$IMAGE\<\<"£####.##","####.##BF","####.##FF"\>\>\
RUN\
£1234.12

If byte 20 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20) is set to [BIN(3)](BIN(.htm) then the third image would be used, for example:

STR(\$OPTIONS,20,1)=BIN(3)\
PRINTUSING 9000, 1234.12\
\$IMAGE\<\<"£####.##","####.##BF","####.##FF"\>\>\
RUN\
1234.12FF

For details of the format specification allowed within the literal strings see the [% (Image)](image.htm) statement.

See also:

[PRINTUSING](PRINTUSING.htm), [\$OPTIONS RUN]($OPTIONS_RUN.htm), [% (Image)](image.htm)
