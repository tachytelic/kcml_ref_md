\$IF ON/OFF

------------------------------------------------------------------------

General Form:\
     <img src="bitmaps/ifond.gif" data-align="BOTTOM" data-border="0" alt="ifond.gif" />\
\

------------------------------------------------------------------------

The \$IF ON/OFF statement is used to determine whether the current status of a device is ready or busy.

A device is only considered to be ready if it exists in the device equivalence table, i.e. has been [\$DEVICEd]($DEVICE.htm). An exception to this rule is the device /001 for the keyboard, which exists in the device table but is considered to be ready only if a terminal is attached and a character has been buffered in the keyboard. Similarly the device /005 for the screen is ready only if the terminal is attached.

If \$IF ON is used then the command will branch to the specified line number if the device is ready. The branch occurs in \$IF OFF statements if the device is not ready.

Syntax examples:

\$IF ON \#112, 12102\
\$IF ON \<address\$\>, 2002\
\$IF OFF /015, 908: ERROR GOTO 9000

 
