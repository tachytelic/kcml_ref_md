SELECT DISK/stream

------------------------------------------------------------------------

General Forms:\
\
<img src="bitmaps/selectdisk.gif" data-align="BOTTOM" data-border="0" alt="selectdisk.gif" />\
\
<img src="bitmaps/selectdisk1.gif" data-align="BOTTOM" data-border="0" alt="selectdisk1.gif" />\
\

------------------------------------------------------------------------

The DISK/stream select parameter is used to set or change a stream entry in the device table. SELECT DISK can only change the value of \#stream 0, which is used as the default [LIST DC](LIST_DC.htm), [LOAD](LOAD.htm), [SAVE](SAVE.htm) etc. device.

Specifying a \#stream allocates the specified device to the specified \#stream. Using a \#stream of zero is the same as using the DISK parameter.

A native filesystem directory may be selected by specifying a literal string in place of the device address. Device addresses or directory names can be assigned to alpha variables, but must be surrounded by angle brackets \`\<\>'. For example:

SELECT \#22 \<data_directory\$\>

The SELECT DISK/stream statement can also be used as a function to return the current filename or device name currently assigned, for example:

device_entry\$(1) = SELECT \#1

would place the 3 hex digit device address currently selected to stream \`#1' into the variable device_entry\$(1). If the stream had previously been selected to a directory, the directory name would then be placed into device_entry\$(1).

Syntax examples:

SELECT DISK /D10\
SELECT \#1 "D:\KCC", \#2 /D99\
address\$ = SELECT \#27

See also:

[ON ... SELECT](ONSELECT.htm)
