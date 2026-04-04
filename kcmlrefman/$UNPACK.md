\$UNPACK

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/unpackd.gif" data-align="BOTTOM" data-border="0" alt="$UNPACK" />\
\

------------------------------------------------------------------------

The \$UNPACK statement is used to unpack data from a buffer variable in a specified format. Values are sequentially read from the buffer, unformatted, and are then stored into the variables specified after the TO keyword. The unpacking terminates when the buffer is empty or the entire variable list is satisfied.

There are four forms of the \$UNPACK statement, these are:

- Delimiter form (specified by the D parameter)
- Field Form (specified by the F parameter)
- Extended Form (specified by the E parameter)
- Internal form (assumed if neither the D,F or E parameters are specified)

Delimiter Form(D=)

The delimiter form of \$UNPACK unpacks data values with a specified delimiter character in the buffer variable.

The first byte of the alpha variable or literal string following the D parameter is used by \$UNPACK as a control byte which should be within the range HEX(00) to HEX(03). The second byte specifies the delimiter character. The delimiter form of \$UNPACK accepts both alpha and numeric values. Trailing spaces are considered as part of an alpha value.

*Valid \$UNPACK Delimiter Specifications*

| Specification | Description |
|----|----|
| 00xx | Error if insufficient data for the variables in the variable list. Skip variables if successive delimiters occur in the buffer variable. |
| 01xx | Ignore remaining variables if insufficient data. Skip variables if successive delimiters occur in the buffer variable. |
| 02xx | Error if insufficient data for the variables in the variable list. Ignore successive delimiter. |
| 03xx | Ignore remaining variables if insufficient data. Ignore successive delimiter. |

By adding the HEX(04) bit to the rule byte, the rules will be changed to follow the normal practice for CSV format, or comma separated values, though the delimited does not have to be a comma. If a field contains either a delimiter character or the quoting character, currently fixed as " or HEX(22), then the field will be quoted using the quote character. If a quote character occurs inside the quoted field it will be doubled up to escape itself.

Internal Form

The internal form of [\$UNPACK]($UNPACK.htm) uses the same format as the old DATA SAVE DC statement.

Field Form (F=)

The field form of \$UNPACK unpacks data from the buffer in specified fields. Each field specification contains two bytes, the first specifies the field type, the second specifies the field width. See [Pack Field Specifiers](tmp/xp.htm#field) for a table containing the valid field specifications together with the [\$FORMAT]($FORMAT.htm) mnemonics.

Extended Form (E=)

The extended form of \$UNPACK is used only for the unpacking of strings according to just one format. The packing specification is in the mnemonic format and hex codes are not used. Only one output variable is allowed. These format mnemonics cannot be used in fields. See [Pack Field Specifiers](tmp/xp.htm#extended) for a table containing the valid packing specifications.

Syntax examples:

\$UNPACK source\$ TO temp\
\$UNPACK FLD(test\$.data\$) TO point\$, file\$\
\$UNPACK (F=format\$) array\$() TO cat()\
\$UNPACK (E="B6.2") buf1\$ to number\
\$UNPACK (E="BASE64") buf2\$ TO buf1\$\
\$UNPACK (D=del\$) xray\$() TO count, test()

See also:

[\$FORMAT]($FORMAT.htm), [\$PACK]($PACK.htm), [FLD(](FLD(.htm), [Field specifiers](tmp/xp.htm)
