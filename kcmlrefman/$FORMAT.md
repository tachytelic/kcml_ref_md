\$FORMAT

------------------------------------------------------------------------

General Form:\
     <img src="bitmaps/formatd.gif" data-align="BOTTOM" data-border="0" alt="formatd.gif" />\
\
Where:\
\
     field_expression           = (start, field_spec)\
\
     field-spec           = length (string fields)\
                                 pack image (numeric fields)\
                                 \$FORMAT field spec (numeric fields)\
\

------------------------------------------------------------------------

The \$FORMAT statement is a form of assignment statement used to simplify the use of the field form of [\$PACK]($PACK.htm) and [\$UNPACK]($UNPACK.htm). The definition on the right hand side must be a true alpha expression, it is also case insensitive. Keywords supported with their [\$PACK]($PACK.htm) field specifiers are shown in the table below

The [\$PACK]($PACK.htm) field specification for field variables can be obtained by specifying either a field variable or a field expression, e.g.

\$FORMAT pck1\$=(2,3)\
\$FORMAT pck2\$=(10,"-####.##")\
.total=(4,"##.##"): \$FORMAT pck3\$=.total

The maximum field width for binary fields is 5. The field specifier of [HEX(8205)](HEX(.htm) is equivalent to the [PACK](PACK.htm) picture -#######.##.

See the table of [\$PACK field specifiers](tmp/xp.htm#field) for a list of the supported mnemonics.

Syntax examples:

\$FORMAT fmt\$ = A\$\
\$FORMAT fmt\$ = "Skip5, I5, D7.3"\
\$FORMAT alpha\$ = (12,43)\
\$FORMAT fmt\$ = "BASE64"\
\$FORMAT beta\$ = (10,"-######.###")

See also:

[\$PACK]($PACK.htm), [\$UNPACK]($UNPACK.htm)
