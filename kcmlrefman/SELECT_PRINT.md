SELECT PRINT

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/selectprint.gif" data-align="BOTTOM" data-border="0" alt="selectprint.gif" />\
\
2.       SELECT PRINT\
\
\
3.       alpha_receiver= SELECT PRINT \[WIDTH\]\
\
Where:\
\
     width           = a numeric expression in the range 0-255.\
\

------------------------------------------------------------------------

The PRINT select parameter is used to define the output device on which all output from PRINT and [PRINTUSING](PRINTUSING.htm) statements in programs is to be displayed.

The PRINT select parameter can be selected to another device that has previously been [\$DEVICEed]($DEVICE.htm) or output can be directed to a Unix/DOS file by specifying the file name as a literal string. If the SELECT PRINT statement is used on its own then the output device is reset to the default.

The optional width parameter may be used to restrict the output to the specified line width.

The PRINT select parameter can also be used as a function returning the file or device name currently assigned. If the reserved word WIDTH is added then the currently selected width is returned after the device address, in parentheses. WIDTH is only returned for files that appear in the device table, e.g.

PRINT SELECT PRINT\
PRINT SELECT PRINT WIDTH\
 \
215\
215(132)

Syntax examples:

SELECT PRINT /215\
SELECT PRINT /204(80)\
SELECT PRINT "/tmp/report1"\
SELECT LIST \<address\$(2)\>, PRINT \<address\$(2)\>\
printer\$ = SELECT PRINT\
width\$ = STR(SELECT PRINT WIDTH,5,3)

See also:

[ON ... SELECT](ONSELECT.htm)
