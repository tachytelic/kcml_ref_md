READ \#

------------------------------------------------------------------------

General Form:\
\
     numeric_receiver = READ \#stream, alpha_variable\
\

------------------------------------------------------------------------

This READ# statement is used to read data from the file currently open on the specified stream. The number of bytes copied to the buffer are returned in the numeric receiver. After the read the current file pointer is advanced by the number of bytes read. If there are not enough bytes to fill the alpha variable then the numeric receiver will be less than the size of the buffer variable and the end of file flag will be set. This can be tested with the [END](IFTHEN.htm) condition in an [IF](IFENDIF.htm), [WHILE](WHILE.htm) or [UNTIL](REPEAT.htm) statement.

The [SEEK \#](SEEKhash.htm) statement can be used to change the position of the file pointer prior to a read.

READ# will return -1 to the numeric receiver if an error occurs. The reason for the error can be found using the [ERR](ERR.htm) function. Possible errors are:

D80      file not open\
I92      Timeout error\
I96      file has read access only

Example:

DIM buffer\$128\
OPEN \#1, "file1", "r+"\
WHILE TRUE DO\
     posn = READ \#1, buffer\$\
     IF (END)\
          BREAK\
     END IF\
     'Processinfo()\
WEND

Syntax examples:

pointer = READ \#1,buffer\$\
WHILE READ \#1,buffer\$ == LEN(buffer\$)) DO

See also:

[CLOSE#](CLOSEhash.htm), [SEEK#](SEEKhash.htm), [WRITE#](WRITEhash.htm), [OPEN#](OPENhash.htm), [\$OPTIONS \#]($OPTIONShash.htm)
