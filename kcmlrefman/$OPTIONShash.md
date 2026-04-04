\$OPTIONS \#

------------------------------------------------------------------------

<div class="Generalform">

General Form:

1.  \$OPTIONS \#numexpr = alpha_expression
2.  alpha_receiver = \$OPTIONS \# numexpr

Where:

> alpha_receiver = a minimum of 64 characters

</div>

------------------------------------------------------------------------

\$OPTIONS \# is used to set the port options for streams. These options are set using bits. The meanings of the bits are shown in the table below.

| Byte | Bit | Meaning |
|----|----|----|
| 1 | HEX(01) | All writes will append automatically to the end of the file if this bit is set. |
|  | HEX(02) | All writes are synchronous and do not use the buffer cache if this bit is set. Supported on Unix only. |
|  | HEX(04) | Reads and writes will not block if there are no characters available on a socket, telecommunications device or a pipe if this bit is set. KCML will return zero as the byte count. |
| 2 | HEX(01) | Enable or disable line orientated read mode. If set [READ \#](READhash.htm) will then only read up to the character specified by byte 5. Setting this bit enables this mode and will automatically allocate a buffer. |
|  | HEX(02) | Instructs [READ \#](READhash.htm) to ignore the character stored in byte 6. |
|  | HEX(04) | Instructs [READ \#](READhash.htm) to truncate the rest of the line if the receiver variable is not large enough to hold the current line. |
| 3 | HEX(01) | Maintained by KCML. If set then a buffer has been allocated. |
|  | HEX(02) | Maintained by KCML. If set then the ignore (see byte 6) character has been detected. |
|  | HEX(04) | Maintained by KCML. If set then the termination character (see byte 5) has been detected. |
|  | HEX(08) | Maintained by KCML. If set then truncation as specified by the HEX(04) bit of byte 2 has taken place. |
| 4 |   | Reserved. |
| 5 |   | Termination character, defaults to HEX(0A). Only relevant if byte two is not HEX(00). |
| 6 |   | Specifies the ignore character, defaults to HEX(0D). This character is used by [READ \#](READhash.htm) if the HEX(02) bit is set in byte 2. |

It is important that \$OPTIONS \# is modified directly as the number of bytes in \$OPTIONS \#n may be increased in a future version. The bits may be set as follows:

STR(\$OPTIONS \#3, 1, 1) = OR HEX(02)

which would turn on synchronous I/O and

STR(\$OPTIONS \#3, 1, 1) = AND HEX(FD)

which would turn it off. Note that synchronous IO is slower than buffered IO.

It is important that \$OPTIONS \# is modified directly in this way as the number of bytes in \$OPTIONS \# may be increased in a future version.

Note:

Unexpected results from [SEEK \#](SEEKhash.htm) can occur when the stream being used is opened in (t)ext mode on NT (See [OPEN \#](OPENhash.htm)) or in line oriented mode and/or an ignore character has been set on NT or Unix. This is due to [READ \#](READhash.htm) and [WRITE \#](WRITEhash.htm) returning only the number of bytes transfered to their buffers and not including termination or ignore characters, typically 0x0A and 0x0D. Example code for reading a text file on Unix or NT with HEX(0A) or HEX(0D0A) line termination, in line oriented mode follows.


    DIM buffer$1024, test$1
    DIM stream, lastOffset, currentOffset, bytesCopied
    REM open the file in read binary mode
    stream = 99
    OPEN #stream,"./textFile","rb"
    REM set line oriented mode and ignore character
    STR($OPTIONS #stream,2,1) = OR HEX(03)
    REM STR($OPTIONS #stream, 5, 1) defaults to HEX(0A)
    REM STR($OPTIONS #stream, 6, 1) defaults to HEX(0D)
    lastOffset = 0
    currentOffset = 0
    WHILE TRUE DO
        bytesCopied = READ #stream, buffer$
        IF (END)
            REM end of file
            BREAK
        END IF
        IF (bytesCopied >= LEN(STR(buffer$)))
            REM really long line
            STOP "Oops, buffer too small"
        END IF
        currentOffset += bytesCopied
        test$ = STR($OPTIONS #stream, 3, 1) AND HEX(02)
        IF test$==HEX(02)
            REM termination character detected, HEX(0A)
            currentOffset++ 
        END IF
        test$ = STR($OPTIONS #stream, 3, 1) AND HEX(04)
        IF (test$==HEX(04))
            REM ignore character detected, HEX(0D)
            currentOffset++ 
        END IF
        REM do something with the line and offset
        IF (bytesCopied==0)
            PRINT $PRINTF("offset %d, blank line\n", lastOffset)
        ELSE
            PRINT $PRINTF("offset %d, line ""%s""\n", lastOffset, STR(buffer$, 1, bytesCopied))
        END IF
        lastOffset = currentOffset
    WEND

\$OPTIONS# as a record

KCML defines a [KCML_OPTIONS_LIST](tmp/kintfld.htm#KCML_OPTIONS_HASH) built in [DEFRECORD](DEFRECORD.htm) that can be used to access the fields in \$OPTIONS# e.g.


    FLD($OPTIONS#stream.OPTIONS_HASH_EndOfLine$) = HEX(0A)

See Also:

[READ \#](READhash.htm), [OPEN \#](OPENhash.htm), [Internal structures](tmp/kintfld.htm)
