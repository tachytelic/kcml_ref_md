SELECT LIST

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/selectlist.gif" data-align="BOTTOM" data-border="0" alt="selectlist.gif" />\
\
2.      alpha_receiver = SELECT LIST \[WIDTH\]\
\
Where:\
\
     width           = a numeric expression in the range 0-255.\
\

------------------------------------------------------------------------

The LIST select parameter is used to define the output device on which all output from the LIST command is to be displayed.

The LIST select parameter can be selected to another device that has previously been [\$DEVICEd]($DEVICE.htm) or output can be directed to a Unix/DOS file by specifying the file name as a literal string.

The optional width parameter may be used to restrict the listing to the specified line width.

SELECT LIST can also be used as a function to return the current filename or device name currently assigned. If the reserved word WIDTH is added then the currently selected width is returned after the device address, in parentheses. WIDTH is only returned for files that appear in the device table. e.g.

PRINT SELECT LIST\
PRINT SELECT LIST WIDTH\
RUN\
215\
215(132)

Syntax examples:

SELECT LIST /215\
SELECT LIST /204(80)\
SELECT LIST "/tmp/report1"\
SELECT LIST \<address\$(2)\>, PRINT \<address\$(2)\>\
listfile\$ = SELECT LIST\
width\$ = STR(SELECT LIST WIDTH, 5,3)

See also:

[LIST](LIST.htm), [ON ... SELECT](ONSELECT.htm)

 
