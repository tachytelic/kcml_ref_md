Using \$DECLARE to access client filesystems

Here is a sample program which which will read a file back from the client. To execute this sample program in KCML, simply click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard, switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program.


    REM Example showing using $DECLARE to read a clie\
    nt file back to the server.
    REM for more information about the WIN32 API for \
    file access see
    REM msdn.microsoft.com/library/psdk/winbase/file\
    sio_7wmd.htm

    DIM buffer$1024, file$256
    DIM handle, bytesread, bufsize
    bufsize = LEN(STR(buffer$))
    file$ = "/tmp/a.txt"
    handle = 'CreateFile(file$, _GENERIC_READ, _FILE\
    _SHARE_READ, 0, _OPEN_EXISTING, 0, 0)
    IF (handle == -1)
    'error("open")
    ELSE
    WHILE 'ReadFile(handle, STR(buffer$), bufsize, B\
    YREF bytesread, 0) AND bytesread > 0 DO
    REM write it somewhere...
    WEND
    'CloseHandle(handle)
    END IF
    END


    DEFSUB 'error(msg$)
    PRINT "Error on ";msg$
    PRINT "Last NT error code",'GetLastError()
    END SUB

    DIM _GENERIC_READ=0x80000000, _GENERIC_WRITE=0x4\
    0000000
    DIM _FILE_SHARE_READ=0x01, _FILE_SHARE_WRITE=0x0\
    2
    DIM _CREATE_NEW=1, _ALWAYS_CREATE=2, _OPEN_EXIST\
    ING=3, _OPEN_ALWAYS=4, _TRUNCATE_EXISTING=5
    $DECLARE 'CreateFile(STR(),INT(),INT(),STR(),INT\
    (),INT(),INT()) TO INT(-)
    $DECLARE 'CloseHandle(INT())
    $DECLARE 'ReadFile(INT(),RETURN DIM(),INT(),RETU\
    RN INT(),STR())
    $DECLARE 'WriteFile(INT(),DIM(),INT(),RETURN INT\
    (),STR())
    $DECLARE 'GetLastError()
