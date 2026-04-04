WRITE \#

------------------------------------------------------------------------

General Form:\
\
     numeric_receiver = WRITE \#stream, alpha_variable\
\

------------------------------------------------------------------------

This statement is used to write data to the file currently open on the specified stream. The number of bytes written to the file are returned in the numeric receiver. After the write the current file pointer is advanced by the number of bytes written. The entire contents of the buffer variable are written including any trailing blanks.

The [SEEK \#](SEEKhash.htm) statement can be used to change the position of the file pointer prior to a write. WRITE \# will automatically extend the file to the new position if the pointer is set to a position beyond the end.

WRITE \# will return -1 to the numeric receiver if an error occurs. The reason for the error can be found using the [ERR](ERR.htm) function. Possible errors are:

     D80      file not open\
     I96      file has read access only

Syntax examples:

pointer = WRITE \#1,buffer\$\
IF (WRITE \#1,buffer\$ \<\> -1) THEN DO

See also:

[CLOSE](CLOSEhash.htm), [SEEK](SEEKhash.htm), [READ](READhash.htm), [OPEN](OPENhash.htm), [\$OPTIONS \#]($OPTIONShash.htm)
