\$PACK

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/packd.gif" data-align="BOTTOM" data-border="0" alt="$PACK general form" />\
\

------------------------------------------------------------------------

The \$PACK statement is used to pack data into a buffer in a specified format. Variables specified after the FROM keyword are sequentially read, formatted and placed into the buffer variable which precedes the FROM keyword.

There are four forms of the \$PACK statement:

- Delimiter form (specified by the D parameter)
- Field Form (specified by the F parameter)
- Extended Form (specified by the E parameter)
- Internal form (assumed if neither the D, F or E parameters are specified)

Arrays in the source list are packed one element at a time using the common pack format for the array. For some packing formats this may not be desirable and for strings you should instead enclose a source string array in a [STR()](STR(.htm) operator to flatten it into a unstructured string e.g.


    $PACK(E="BASE64") buffer$() FROM STR(source$())

Delimiter Form(D=)

The delimiter form of \$PACK separates data values with a specified delimiter character in the buffer variable. See [table]($UNPACK.htm#delimiter) in \$UNPACK for details of valid delimiter specifications

The first byte of the alpha variable or literal string following the D parameter is used by [\$UNPACK]($UNPACK.htm). The second byte contains the character to be used as the delimiter. The delimiter form of \$PACK accepts both alpha and numeric values. Trailing spaces are considered as part of an alpha value. Array elements are stored in the buffer with the delimiter separating each element.

Field Form (F=)

The field form of \$PACK stores data in the buffer in specified fields. Each field specification contains two bytes, the first specifies the field type, the second specifies the field width. See [Pack Field Specifiers](tmp/xp.htm#field) for a table containing the valid field specifications together with the [\$FORMAT]($FORMAT.htm) mnemonics.

Extended Form (E=)

The extended form of \$PACK is used only for the packing of strings according to just one format. The packing specification is in the mnemonic format and hex codes are not used. Nor can these formats be used with fields. See [Pack Field Specifiers](tmp/xp.htm#extended) for a table containing the valid packing specifications. Unlike the other formats, the extended form of \$PACK will space fill the target buffer if the packed information is shorter.

Internal Form

The internal form of [\$UNPACK]($UNPACK.htm) uses the same format as the old DATA SAVE DC statement and must be considered obsolete.

Syntax examples:

\$PACK source\$ FROM temp\
\$PACK FLD(test\$.part1\$) FROM part1, file\$\
\$PACK (F=format\$) array\$() FROM cat()\
\$PACK (E="B6.2") buf1\$ FROM 34.6\$\
\$PACK (E="BASE64") buf1\$ FROM buf2\$\
\$PACK (D=act\$) sector\$() FROM count, test()

See also:

[\$FORMAT]($FORMAT.htm), [\$UNPACK]($UNPACK.htm) [Field specifiers](tmp/xp.htm)
