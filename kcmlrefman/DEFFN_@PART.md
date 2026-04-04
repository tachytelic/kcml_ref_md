DEFFN @PART

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
<img src="bitmaps/deffnpart.gif" data-align="BOTTOM" data-border="0" alt="deffnpart.gif" />\
\

</div>

------------------------------------------------------------------------

The DEFFN @PART statement makes the global variables and quoted subroutines of the current partition public or "global" under the name supplied. Only partitions which have been declared global by running KCML with the -g switch can execute this statement. A calling program selects the global partition and gains access to the functions and @ variables by executing a [SELECT @PART](SELECT_@PART.htm) statement containing the same partition name.

The string value is interpreted either as a simple name of up to 8 characters or, if more than 8 characters, KCML will attempt to parse it as the name of a file.

If a simple name then it is inserted into the [\$PSTAT]($PSTAT.htm) table (at bytes 17-24) to publish its availability to other partitions. An error will occur if the specified partition name is a simple name already being used by another global partition. The shared memory containing the global program will exist only while this KCML is executing and when it terminates the global subroutines will no longer be available to other partitions. Generally such global partitions are run in the background as Unix or NT daemons and are often launched by the operating system when the server is rebooted. The daemon will initialize itself and the go to sleep using a [\$BREAK!]($BREAK.htm) so that it runs all the time. A [\$ALERT]($ALERT.htm) can be used to interrupt this sleep and allow the process to reload.

However if the name is longer than 8 characters, and can be parsed as a name of up to 8 characters followed by a '=' sign followed by a filename, then KCML will copy the shared memory to this file and terminate when it sees a [\$BREAK!]($BREAK.htm). It is not necessary to have a permanently running process to own the global code and other processes can get access to the functions by using the same name string in a [SELECT @PART](SELECT_@PART.htm). However memory mapped files are not interchangeable between different processor architectures.

If more than one DEFFN @PART statement is found in the global partition at resolve time, then the name of the most recently executed DEFFN @PART statement will be used. Wherever the statement occurs in the program, all the quoted subroutines and @ variables will be public.

Compatibility

Shared memory in memory mapped files is available with KCML 5.03 and later and is supported on both Unix and NT.

Syntax examples:

DEFFN @PART "LIBRARY"\
DEFFN @PART global_name\$\
DEFFN @PART STR(globals\$,16,8)\
DEFFN @PART "LIBRARY=/user1/home/rev8/globallib"

See also:

[SELECT @PART](SELECT_@PART.htm),\
[\$BREAK]($BREAK.htm),\
[\$PSTAT]($PSTAT.htm),\
[LIBRARY](MODULE.htm)
