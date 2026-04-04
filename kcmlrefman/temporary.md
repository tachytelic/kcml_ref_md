Working with KCML temporary files

KCML temporary files and tables are intended as a convenient way to ensure that these files and tables are removed when a program has finished with them, even if the program terminates abnormally. On Unix platforms this is achieved by unlinking the files from the filesystem after they have been opened. This means that although they exist and use disk space (as seen by **df**) they do not appear in the filesystem's directories (as seen by **ls**). On windows this is achieved using a special flag that indicates the files should be removed when they are closed, so unlike Unix they do appear in the filesystem's folders.

Temporary files are identified as having filenames starting with three hashes (###). Within KISAM they are identified as tables with names starting with three hashes (###).

Temporary files can be created with [OPEN#](OPENhash.htm). They will be removed by [CLOSE#](CLOSEhash.htm).

KISAM files can be created and opened with [KI_CREATE](mk:@MSITStore:kdb.chm::/tmp/KI_CREATE.htm). They can also be opened with [KI_OPEN](mk:@MSITStore:kdb.chm::/tmp/KI_OPEN.htm). They are removed by [KI_CLOSE](mk:@MSITStore:kdb.chm::/tmp/KI_CLOSE.htm).

Temporary tables can be created with [CREATE TABLE](mk:@MSITStore:kdb.chm::/CREATE_TABLE.htm), and manipulated with [CREATE TABLE](mk:@MSITStore:kdb.chm::/CREATE_TABLE.htm), [CREATE INDEX](mk:@MSITStore:kdb.chm::/CREATE_INDEX.htm), [INSERT](mk:@MSITStore:kdb.chm::/INSERT.htm), [DELETE](mk:@MSITStore:kdb.chm::/DELETE.htm), [SELECT](mk:@MSITStore:kdb.chm::/SELECT.htm) etc. They can then be opened with [KI_OPEN](mk:@MSITStore:kdb.chm::/tmp/KI_OPEN.htm) and removed with [KI_CLOSE](mk:@MSITStore:kdb.chm::/tmp/KI_CLOSE.htm).

Tables created with [CREATE TABLE](mk:@MSITStore:kdb.chm::/CREATE_TABLE.htm) are removed as soon as they are opened with [KI_OPEN](mk:@MSITStore:kdb.chm::/tmp/KI_OPEN.htm). The handle they are opened on can be used to add rows to the table. It may not appear possible to subsequently issue a [CREATE INDEX](mk:@MSITStore:kdb.chm::/CREATE_INDEX.htm) or [INSERT](mk:@MSITStore:kdb.chm::/INSERT.htm), [DELETE](mk:@MSITStore:kdb.chm::/DELETE.htm), [SELECT](mk:@MSITStore:kdb.chm::/SELECT.htm) etc as the table has already been removed. However, so long as a handle is still open on the table these commands are still possible. The table can be identified either as the "**\###....**" name it was created with or, more efficiently as "**\#n**" where **n** is the handle that the table is open on.

Tables created with [CREATE TABLE](mk:@MSITStore:kdb.chm::/CREATE_TABLE.htm) within a temporary [TABLESPACE](mk:@MSITStore:kdb.chm::/CREATE_TABLESPACE.htm) have the leading three hashes (###) added automatically.

Examples

OPEN \#stream,"###tempfile","W","0666" ... CLOSE \#stream sql\$ = "CREATE TABLE ""###temp"" (PARTNUM INTEGER(4) DEFAULT 900, PID VARCHAR(8), SNAME VARCHAR(20) OCCURS 2 DEFAULT 'Nicklaus', bavg NUMERIC(7,2) OCCURS 5 DEFAULT 15.75) TYPE 7, RECLEN 200" CALL KI_PREPARE ki_handle,sql\$ TO ki_status CALL KI_EXECUTE ki_handle TO ki_status CALL KI_CLOSE ki_handle TO ki_status REM Put an index on the working table sql\$ = "CREATE UNIQUE INDEX ""###temp_A1"" ON ""###temp"" (PID)" CALL KI_PREPARE ki_handle,sql\$ TO ki_status CALL KI_EXECUTE ki_handle TO ki_status CALL KI_CLOSE ki_handle TO ki_status CALL KI_OPEN ki_handle,"###temp","W" TO ki_status ... CALL KI_CLOSE ki_handle

See also:

[OPEN#](OPENhash.htm), [CLOSE#](CLOSEhash.htm), [READ#](READhash.htm), [WRITE#](WRITEhash.htm), [\$OPTIONS#]($OPTIONShash.htm) [CREATE TABLE](mk:@MSITStore:kdb.chm::/CREATE_TABLE.htm) [CREATE TABLESPACE](mk:@MSITStore:kdb.chm::/CREATE_TABLESPACE.htm) [KI_CREATE](mk:@MSITStore:kdb.chm::/tmp/KI_CREATE.htm) [KI_OPEN](mk:@MSITStore:kdb.chm::/tmp/KI_OPEN.htm) [KI_CLOSE](mk:@MSITStore:kdb.chm::/tmp/KI_CLOSE.htm)
