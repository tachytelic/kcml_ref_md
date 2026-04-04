LIST DT

------------------------------------------------------------------------

<div class="Generalform">

General Form:

> LIST \[title\] DT

Where:

> title = alpha_variable or a literal string

</div>

------------------------------------------------------------------------

The LIST DT statement displays the current contents of the device table (DT) and device equivalence tables (DET).

The display is divided into five sections, the first lists the device table showing those stream numbers that have been allocated with the full file name, file descriptor (fd) number, start sector, end sector and current file pointer. Files locked by the executing process have a 'W' (for Write lock) in the last column, while files locked by other partitions have the partition number in the last column.

The second section shows information relating to current database connections and handles.

The third section displays the device equivalence table (DET), which maps device addresses to native filenames and types. The currently [SELECTed](SELECT.htm) devices for [CI](SELECT_CI.htm), [INPUT](SELECT_INPUT.htm), [CO](SELECT_CO.htm), [PRINT](SELECT_PRINT.htm), [LIST](SELECT_LIST.htm)and [TRACE](SELECT_TRACE.htm) follow.

The fourth section shows any XML handles currently in use. If no XML handles are currently in use then this section will not be displayed. The display shows the handle number. If the document has not yet been parsed the line includes wither the handle was created with [XML_OPEN](mk:@MSITStore:kdb.chm::/tmp/XML_OPEN.htm) **O** or [XML_PARSE_BUFFER](mk:@MSITStore:kdb.chm::/tmp/XML_PARSE_BUFFER.htm) **P**. For the former the filename is shown, for the latter the first few bytes of the given buffer. If the document is being processed with [XML_NEXT](mk:@MSITStore:kdb.chm::/tmp/XML_NEXT.htm) then the first, last and current element names are given, along with the depth of the current tag and its type. See [XML_NEXT](mk:@MSITStore:kdb.chm::/tmp/XML_NEXT.htm) for more information.

The last section shows the handle table. This lists the file descriptors used by KCML and the files they are associated with.

If LISTed to the screen, the screen will be cleared before the display, and on pressing RETURN, the subsequent pages of the device table followed by the device equivalence table and its subsequent pages.

Native files are distinguished by having a start sector of zero.

The file descriptor (fd) will be negative if the file or device has not been opened or has been closed and positive if it is open. It is set to 9999 if a device has been temporarily closed as a result of operating systems limits on the number of open files allowed. It will be automatically opened when next used.
