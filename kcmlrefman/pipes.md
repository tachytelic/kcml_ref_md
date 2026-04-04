Working with pipes as devices

A powerful use of [\$DEVICE]($DEVICE.htm) is to connect a KCML device address with a pipeline of Unix processes which can either supply characters to the device or take characters written to a device:

\$DEVICE /290="\|lp"

will send any output directed to the /290 device address, to the Unix spooler program lp. The spooler program runs in parallel with the KCML process. KCML knows that a device is an output pipe when the string on the right hand side starts with the pipe symbol '\|' or '^'.

Pipes can also be used for input e.g.

\$DEVICE /290="someprog\|"

which will run the program *sumprog* and make its output available to be read from device /290.

When using a pipe to output to a spooler it is necessary to explicitly close the device with a [\$REWIND]($REWIND.htm) or [\$CLOSE]($CLOSE.htm) (if the device was previously [\$OPEN]($OPEN.htm)ed) before the printer daemon can spool the file to the printer, for example:

\$DEVICE /290="\|lp"\
\$OPEN /290\
SELECT PRINT /290\
REM Print Report\
...\
SELECT PRINT /005\
\$CLOSE /290

Alternatively \$DEVICE /290 could be used to close the device permanantly by removing the device from the DET.

See also [SELECT](SELECT.htm) to see how the INPUT, PRINT, LIST streams ca be connected to pipes without the need for a \$DEVICE.
