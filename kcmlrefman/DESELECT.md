DESELECT

------------------------------------------------------------------------

General Form:\
\
     DESELECT \#stream \[ , \#stream\] ...\
\

------------------------------------------------------------------------

KCML supports up to 256 stream numbers (0 to 255), but a certain amount of memory is required each time a new stream number is activated. When that stream number is no longer required the memory can be recovered with the DESELECT statement. Any file open on the stream number must first have been closed or a P48 error will occur.

Syntax examples:

DESELECT \#25, \#89, \#250\
DESELECT \#file1, \#27, \#present

See also:

[SELECT DISK/stream](SELECT_DISK.htm)

 
