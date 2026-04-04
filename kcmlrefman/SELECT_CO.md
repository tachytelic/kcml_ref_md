SELECT CO

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/selectco.gif" data-align="BOTTOM" data-border="0" alt="selectco.gif" />\
\
               2.      alpha_receiver = SELECT CO \[WIDTH\]\
\

------------------------------------------------------------------------

The CO select parameter is used to set the Console Output device address. Characters entered from the Console Input device in immediate mode or in program editing are displayed on the Console Output device. All responses to [LINPUT](LINPUT.htm), [LINPUT LINE](LINPUT_LINE.htm), [LINPUT LIST](LINPUT_LIST.htm), [KEYIN](KEYIN.htm), [TRACE](TRACE.htm), etc are all echoed to the CO device.

Console Output can be directed to another device that has previously been [\$DEVICEd]($DEVICE.htm) or output can be directed to a Unix/DOS file by specifying the file name as a literal string.

The CO select parameter can also be used as a function returning the currently assigned file or device name. If the reserved word WIDTH is added then the currently selected width is returned after the device address, in parentheses. WIDTH is only returned for devices that appear in the device table, e.g.

PRINT SELECT CO\
PRINT SELECT CO WIDTH\
 \
005\
005(80)

Syntax examples:

SELECT CO /005\
SELECT CO "outputfile"\
SELECT CO /005, CI /001, LIST /204\
array\$(2) = SELECT CO\
width\$ = SELECT CO WIDTH

See also:

[ON ... SELECT](ONSELECT.htm), [SELECT CI](SELECT_CI.htm)
