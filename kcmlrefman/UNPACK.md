UNPACK

------------------------------------------------------------------------

General Form:\
\
     UNPACK (image) alpha_variable TO numeric_variable\
\
Where:\
<img src="bitmaps/unpack.gif" data-align="BOTTOM" data-border="0" alt="unpack.gif" />\
\

------------------------------------------------------------------------

The UNPACK statement is used to unpack a list of numeric values from an alphanumeric variable, previously packed with the [PACK](PACK.htm) statement. The values are unpacked starting at the beginning of the alpha variable or array. Values are unpacked and converted to internal format and stored in the specified numeric variables. The format of the packed data is specified by the image (refer to the [PACK](PACK.htm) statement for information on the image specifications). The same image must be used to unpack the data as was used to pack the data. The data is sequentially unpacked and the values assigned to the receiving numeric variables.

Syntax examples:

UNPACK(###.###) file\$ TO total\
UNPACK(+###.##) FLD(record\$.type\$) TO type\
UNPACK(form\$) file\$ TO price()

See also:

[PACK](PACK.htm)

 
