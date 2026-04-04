SEEK \#

------------------------------------------------------------------------

General Forms:\
\
     <img src="bitmaps/seekhash.gif" data-align="BOTTOM" data-border="0" alt="seekhash.gif" />\

------------------------------------------------------------------------

The SEEK \# function repositions the current file pointer for file open on the specified stream relative to the BEGinning, the END, or FOR an increment from the current position. Specifying just an offset is shorthand for BEG. The new offset is returned as the value. By not specifying any offset the current position in the file may be determined.

An error will cause SEEK \# to return -1.

A negative seek expression is valid with FOR and END, otherwise it will give a recoverable P34 error.

The following program shows the result of several SEEK \# functions assuming that the functions were executed in the order of appearance. The return values are shown on the right hand side.

DIM file\$1000\
OPEN \#1, "./file1", "w+"\
ret = WRITE \#1, file\$\
offset = SEEK \#1, BEG                0\
offset = SEEK \#1, BEG, 100           100\
offset = SEEK \#1, END, -100           900\
offset = SEEK \#1, 500                500\
offset = SEEK \#1, FOR, 100           600\
offset = SEEK \#1                     600\
CLOSE \#1

Note:

Unexpected results from SEEK \# can occur when the stream being used is opened in (t)ext mode on NT (See [OPEN \#](OPENhash.htm)) or in line oriented mode and/or an ignore character has been set (See [\$OPTIONS \#]($OPTIONShash.htm)) on NT or Unix. This is due to [READ \#](READhash.htm) and [WRITE \#](WRITEhash.htm) returning only the number of bytes transfered to their buffers and not including termination or ignore characters, typically 0x0A and 0x0D.

See also:

[CLOSE \#](CLOSEhash.htm), [READ \#](READhash.htm), [WRITE \#](WRITEhash.htm), [OPEN \#](OPENhash.htm), [\$OPTIONS \#]($OPTIONShash.htm)
