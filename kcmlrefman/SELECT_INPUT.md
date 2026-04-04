SELECT INPUT

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/selectinput.gif" data-align="BOTTOM" data-border="0" alt="selectinput.gif" />\
\
2.      alpha_receiver = SELECT INPUT\
\

------------------------------------------------------------------------

The INPUT select parameter is used to specify the device address to be used to enter data to the [KEYIN](KEYIN.htm), [LINPUT](LINPUT.htm), [LINPUT LINE](LINPUT_LINE.htm), and [LINPUT LIST](LINPUT_LIST.htm) statements.

The INPUT select parameter can receive input from any device that has previously been [\$DEVICEd]($DEVICE.htm) or input can be directed from Unix/DOS file by specifying the file name as a literal string.

SELECT INPUT can also be used as a function to return the current filename or device name currently assigned.

Syntax examples:

SELECT INPUT /001\
SELECT INPUT \<address\$(value)\>\
SELECT INPUT "/user1/input_file", LIST /204\
test\$ = SELECT INPUT

See also:

[ON ... SELECT](ONSELECT.htm)
