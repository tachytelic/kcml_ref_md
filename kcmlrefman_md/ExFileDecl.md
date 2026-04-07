# Example: Accessing client filesystem via $DECLARE

> Shows how to use `$DECLARE` to call Win32 API functions and read a file from the client machine.

## Description

When KCML runs on a server with a Windows client (via DW terminal or kclient), `$DECLARE` can be used to call Win32 API functions directly on the client. This example reads a client-side file by declaring and calling `CreateFile`, `ReadFile`, and `CloseHandle`.

## Key Win32 constants

```kcml
DIM _GENERIC_READ    = 0x80000000
DIM _GENERIC_WRITE   = 0x40000000
DIM _FILE_SHARE_READ = 0x01
DIM _FILE_SHARE_WRITE= 0x02
DIM _CREATE_NEW      = 1
DIM _ALWAYS_CREATE   = 2
DIM _OPEN_EXISTING   = 3
DIM _OPEN_ALWAYS     = 4
DIM _TRUNCATE_EXISTING = 5
```

## $DECLARE statements

```kcml
$DECLARE 'CreateFile(STR(),INT(),INT(),STR(),INT(),INT(),INT()) TO INT(-)
$DECLARE 'CloseHandle(INT())
$DECLARE 'ReadFile(INT(),RETURN DIM(),INT(),RETURN INT(),STR())
$DECLARE 'WriteFile(INT(),DIM(),INT(),RETURN INT(),STR())
$DECLARE 'GetLastError()
```

## Example program

```kcml
DIM buffer$1024, file$256
DIM handle, bytesread, bufsize
bufsize = LEN(STR(buffer$))
file$ = "/tmp/a.txt"

handle = 'CreateFile(file$, _GENERIC_READ, _FILE_SHARE_READ, 0, _OPEN_EXISTING, 0, 0)
IF (handle == -1)
    'error("open")
ELSE
    WHILE 'ReadFile(handle, STR(buffer$), bufsize, BYREF bytesread, 0) AND bytesread > 0 DO
        REM process buffer$ here
    WEND
    'CloseHandle(handle)
END IF
END


DEFSUB 'error(msg$)
    PRINT "Error on "; msg$
    PRINT "Last NT error code: "; 'GetLastError()
END SUB
```

## Notes

- `$DECLARE` maps a KCML subroutine label to a native (Win32) function. This only works when KCML is connected to a Windows client.
- `CreateFile` returns `-1` (i.e. `INVALID_HANDLE_VALUE`) on failure.
- `ReadFile` fills `STR(buffer$)` in place and sets `bytesread` to the number of bytes actually read. The loop ends when `bytesread` reaches 0 (EOF).
- The `RETURN DIM()` in the `$DECLARE` for `ReadFile` means KCML passes a pointer to the DIM'd variable and the function writes into it.
- This pattern is Windows-specific. For server-side file I/O, use standard KCML `OPEN#` / `READ#` / `WRITE#` instead.

## See Also

- `$DECLARE` — declare an external function reference
- `BYREF` — pass by reference
- `OPEN#` — open a server-side file
- `COM` — client/server communication variables
