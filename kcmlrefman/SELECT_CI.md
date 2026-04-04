SELECT CI

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/selectci.gif" data-align="BOTTOM" data-border="0" alt="selectci.gif" />\
\
     2.      alpha_receiver = SELECT CI\
\

------------------------------------------------------------------------

The CI select parameter is used to set the Console Input device address used for immediate mode commands and program editing. The characters entered into the Console Input device are automatically echoed onto the Console Output Device. Console input can be directed in from another device that has previously been [\$DEVICEd]($DEVICE.htm) or input can be entered from a Unix/DOS file by specifying the file name as a literal string. When all the commands have been read from the file /001 is automatically reselected.

SELECT CI can also be used as a function returning the current filename or device name currently assigned.

Syntax examples:

SELECT CI /001\
SELECT CI "inputfile"\
SELECT CO /005, CI /001, LIST /204\
array\$(1) = SELECT CI

See also:

[ON ... SELECT](ONSELECT.htm), [SELECT CO](SELECT_CO.htm)
