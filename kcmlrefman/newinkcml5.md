What's new in KCML 5?

------------------------------------------------------------------------

<span id="Client_Server_Operation" client_server_operation=""></span>Client Server Operation

KCML5 running on NT or Windows 95 now operates in the same way as under Unix with the **KCML** execute engine separate from the presentation engine. Presentation is done with a new **KClient** client program which attaches over a TCP/IP socket to the KCML process. The client and server can both be on the same machine or they can be on separate machines. **KClient** is a simplified version of the WDW product used with KCML 4, the main difference being that KClient supports a text and forms engine, TCP/IP transport and client side [\$DECLARE]($DECLARE.htm). It does not have any support for serial connections (other than RAS or PPP).

When the server is running on NT a new KCML Service Manager program is installed to manage the KCML connection service. This program which has a forms front end, listens out for incoming TCP/IP connections from **KClient** tasks on this machine or elsewhere on the network and starts up **KCML** sessions to handle them. It also has responsibility for starting ODBC server sessions and can be used to start global library partitions automatically when the server boots.

Under Windows 95 the client can start the server automatically without the requirement for a listening process.

<span id="GUI_Forms" gui_forms=""></span>GUI Forms

<span id="What_are_forms_" what_are_forms_=""></span>What are forms?

Forms are a new graphical front end presentation method for KCML when using the Windows 32 bit client KClient. They contain a number of controls such as buttons, list boxes, grids and edit boxes. Generic OCX controls which are available from various third parties are also supported

<span id="Objects" objects=""></span>Objects

Forms are implemented as objects using a DEFFORM statement in which is encapsulated all the detail of how the form is to be displayed. The detail is normally hidden by the editor but the form object can be edited using a graphical editor called KFORM32 by just right clicking the DEFFORM in the code form within the normal program editor.

Objects are named with a dot notation e.g. SalesForm.AccountCode.text\$ might refer to the text\$ property of the AccountCode edit box control on the SalesForm form. Forms and their controls can have properties that can be inspected or set such as the text\$ property which contains the text input by the user into the edit box.

<span id="Events" events=""></span>Events

Held within the object, but visible to the programmer, are all the event handlers for the various events that the form might generate, such as the clicking of a button or the entry of text into a field. Other events are automatically generated without user action, such as the enter() event which is presumed to occur after the form has been created but before it is displayed. Each event has a built in handler with a default action so that clicking an OK button will dismiss the form, but programmers can intercept the event and process it in their own DEFEVENT handler. These event handlers act like DEFSUB subroutines but start with the DEFEVENT keyword and terminate on a END EVENT keyword. Normally exiting an event handler at the END EVENT will still cause the default action to take place but explicitly executing RETURN FALSE in an event handler will bypass the default. This would be useful in a handler for OK events which validated the entry and stopped the form being closed by returning FALSE if a field was in error.

The code for event handlers can be hidden or collapsed to reveal clearly the range of events supported by the object.

<span id="Object_browser" object_browser=""></span>Object browser

The KCML editor has an Object Browser which allows the programmer to see all the forms objects in the program together with their properties, methods and events. It can be used to add code to a program in that it will write the DEFFORM for a new form and add stub event handlers. Use F1 or the Context Help button to get help on control properties and methods.

The browser can be invoked from within the editor with CTRL-F.

<span id="Database" database=""></span>Database

KISAM has been enhanced to support type 6 files which allow considerably larger file sizes up from 16 million records on type 5 to 4 billion records in type 6. The number of key paths supported in type 6 has been raised from 9 to 18 and the number of segments per key is now 8, up from 4 on type 5.

All the standard ISAM access methods are available on both native KISAM files and also optionally on alternative SQL databases such as Oracle. The KISAM database will map ISAM operations such as READ, READ_NEXT, DELETE etc. into SQL and issue that against the SQL database. This support is available only on selected platforms through a dynamically linked library (kioracle.so in Unix and kioracle.dll in NT). In the initial beta program only Oracle 7.3 on Unixware 2 and NT will be supported. This support may be extended to other databases and other platforms.

To connect to databases other than KISAM a new KI_ALLOC_CONNECT call must be used to allocate a connection number. KISAM databases are assumed to be connected already on connection 1. The connection number is used when allocating the handle as handles must now be allocated and freed explicitly with KI_ALLOC_HANDLE and KI_FREE_HANDLE.

KI_OPEN now requires an absolute or relative file name and no longer uses the stream table. The stream parameter has been dropped and a connection number from KI_CONNECT is used in its place. For compatibility a connection number of 1 is pre-allocated as a connection to the built in KISAM database

KI_CREATE also requires a proper file name and the stream parameter is dropped. A new dictionary file name parameter has been added in its place but this is not currently used. The array describing the keys now has 33 bytes per element to provide for the extra key segments supported. The extra return value to get the number of sectors has been dropped.

LIST DT now shows current KISAM connections and handles as well as streams.

KI_LOCK_OWNER is now tracks locks by handle and so needs a handle parameter and can return a status code.

Because KISAM type 6 files allow more records the size of the data pointer returned by READ, WRITE etc has to be at least 4 bytes long to hold the bigger row identifier. If supporting an SQL database it may have to be much larger (16 bytes for Oracle 7.3 for instance). To be compatible KISAM will check the size of the variable passed in the CALL. If 3 bytes long then it will return the least significant 3 bytes of the record number in the buffer. If more than 3 bytes long then it will return 4 bytes leaving the rest of the buffer set to ALL(00). To be compatible with existing code you should be sure to dimension the ki_ptr\$ used in the KISAM stubs to be three bytes long until such time as you verify that your applications can handle a four byte value.

A new KISAM stub library KISAMLIB.src, also known as GB/libKI, is available on the ftp://ftp.kerridge.com FTP server for the beta program. This implements the changes to 'ki_open(), 'ki_create() and ki_lock_owner and it defines ki_ptr\$ as 3 bytes.

To handle the extra key information KISAM data dictionary records now permit \$KEY values of \$KEYA to \$KEYI for the extra nine keys and the occurs for the key segments is now 008 rather than 004.

<span id="Mixed_case_symbols" mixed_case_symbols=""></span>Mixed case symbols

KCML can now preserve the case of symbols if byte 40 of [\$OPTIONS LIST]($OPTIONS_LIST.htm#BYTE40) had bit HEX(01) set. The default is to have this byte set to HEX(00) and symbols will always be LISTed in lower case. When this bit is set KCML continues to ignore case when distinguishing symbols so that *MixedCase\$* is considered to be the same as *mixedcase\$*, but it will remember and recreate using either the form used in the first reference or the form used in an explicit [DIM](DIM.htm), [COM](COM.htm), [DEFSUB](DEFFNquote.htm) etc. KCML versions since version 4.0.16 have been able to LOAD programs saved with mixed case symbols. If you need to develop on KCML5 to run on earlier KCML versions then either don't turn this feature on or set the COMPAT40 environment variable.

<span id="Structured_IF" structured_if=""></span>Structured IF

It also supports a new [IF ELSE ENDIF](IFENDIF.htm) grammar for indented IF statements. This is distinguished from the older form by the lack of a THEN e.g.

IF (a == b)\
'DoThis()\
ELSE\
'DoThat()\
ENDIF

The parentheses are optional but KCML will always recreate using them. The ENDIF is required and KCML will automatically indent. Complex cascaded IFs are possible using ELSE IF.

<span id="PRINTUSING_TO" printusing_to=""></span>PRINTUSING TO

[PRINTUSING TO](PRINTUSING_TO.htm) and PRINT TO have new functionality controlled by byte 47 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE47).

|  |  |
|----|----|
| HEX(01) | The count in the first two bytes of the string is not required. The formatted output will start at bytes 1. No HEX(0D) will be appended and the receiver string will be blank filled. |
| HEX(02) | Tab characters (that is HEX(09)) will be inserted at each of the first blank character separating formats in the image. Surplus leading and trailing blank spaces will be removed. |

The tab inserting mode is intended to simplify the generation of suitable strings for use in list boxes and grids. Use the tabstop\$ property of the listbox to specify where the columns should appear. When multicolumn listboxes are populated this way the more natural proportionally spaced default font can be used without spoiling column alignment.

See also the [\$FMT(]($FMTfn.htm) string function.

<span id="Date_and_Time_functions" date_and_time_functions=""></span>Date and Time functions

[CONVERT DATE](CONVERT_DATE.htm) can be used to convert between ISO dates in CCYY-MM-DD format and Julian dates. Julian dates are day numbers counted from a standard date in 4716BCE. Julian dates are used by KISAM database DATE datatypes which stores the number as a 3 bytes integer ("B3" format). They are very similar to the date type used in Microsoft applications such as VB, Excel and Access. To convert a Microsoft date to a Julian date just add 2415019. The ISO date format of "CCYY-MM-DD" is the same as the format used in the KISAM ODBC driver. The full CCYY year must be used and it is not permitted to abbreviate to just the YY part. For example

CONVERT DATE "1997-02-11" TO j\
CONVERT DATE vbdate+2415019 TO vbdate\$

To access dates stored as 4 byte hexpacked CCYYMMDD format a new [\$PACK]($PACK.htm) format of HEX(FD04) can be used to convert to and from Julian format. This is available in [FLD(](FLD(.htm) functions as "MD4" e.g. DIM .invdate=(10,"MD4"). Three byte YYMMDD packed dates can be converted using a width of 3. When converting to a Julian date byte 48 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE48) is observed to determine the century (see below).

A new numeric date function [\#DATE](_DATE.htm) returns today's date as a Julian date.

A new time function [\#TIME](_TIME.htm) returns the time in seconds since midnight local time (note that [\$TIME]($TIME.htm) returns the time as seconds since midnight GMT 1970-01-01 on systems that support time zones).

The existing R7_DATE2J user function which can convert dates in DD/MM/YY format to Julian dates is still available but new applications can use [CONVERT DATE](CONVERT_DATE.htm). To ease the transition to the new century this function will check the integer value of [\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 48 and if the YY value in the date is less than the value of this byte the century will be assumed to be 2000, otherwise it will be taken to be 1900. This byte is defaulted to HEX(20) corresponding to 1932. If you wanted to make the cut-off year 1910 for a birthday prompt say then execute

STR(\$OPTIONS RUN,48,1)=BIN(10)

<span id="_CRC__function" _crc__function=""></span>\$CRC( function

Cyclic Redundancy Check (or CRC) functions are widely used for packet checksums in communications. KCML now has a [\$CRC(]($CRC(.htm) function to calculate a 32 bit CRC for a string. The grammar is

*strrcvr* = \$CRC(*strexpr1* \[,*strexpr2*\])

This function can only be used on the right hand side of a LET in this way and cannot be combined with other string operators such as &, AND, OR etc. Each byte of *strexpr1* is examined in turn and combined into a running CRC value which will then be copied into the *strrcvr* on the left hand side of the LET. This receiver must be at least 4 bytes long. Note that all the bytes of *strexpr1*, including trailing blanks, are incorporated into the CRC. The start value is taken from the optional *strexpr2* string which must be at least 4 byte long. If not present then the conventional value of HEX(FFFFFFFF) will be used.

<span id="_FMT__function" _fmt__function=""></span>\$FMT( function

The [\$FMT(]($FMTfn.htm)format\$, arg1 \[,arg2\] ...) function encapsulates some of the functions of [PRINTUSING TO](PRINTUSING_TO.htm) in a simple string function. Because a static buffer is used to generate the value of the function, it can only be used once per statement otherwise the second use will overwrite the first. E.g.

Edit1.text\$ = \$FMT("-###.##", value)

<span id="_LTRIM__function" _ltrim__function=""></span><span id="LTRIM__function" ltrim__function=""></span>LTRIM( function

The function [LTRIM(](LTRIMfn.htm)*str\$* \[,char\$\]) can be used to trim off leading blanks from the left hand side of the string *str\$*. The optional *char\$* can specify an alternative character to trim.

<span id="RTRIM__function" rtrim__function=""></span>RTRIM( function

The function [RTRIM(](RTRIM(.htm)*str\$* \[,char\$\]) can be used to trim off trailing blanks from the right of the string str\$. The optional char\$ can specify an alternative character to trim.

<span id="Internationalisation_issues" internationalisation_issues=""></span>Internationalisation issues

This version of KCML assumes the use of the ISO Latin 1 character set as the default character set. The so called alternate character set is still available for characters \>= HEX(90) on platforms that support it (it is supported by KClient).

The functions [\$UPPER(]($UPPER(.htm) and [\$LOWER(]($LOWER(.htm) can be used to change the case of all the characters in a string using a built in translation table corresponding to that ISO Latin 1 character set. Thus a\$= \$LOWER("ABÄ") will set a\$ to contain "abä".

Strings are always compared for equality by comparing each byte considering it to be an unsigned integer. However it is also possible to compare two strings for equality using a specific locale collating sequence using the [\$STRCOLL(]($STRCOLL(.htm)str1, str2) function. Which will return -1 if str1 is less than str2, +1 if greater or zero if they are equal. KCML contains a built-in collating sequence for ISO Latin 1 which will work for most Western European languages.

[FSORT](FSORT_BU.htm) and [SORT](SORT.htm) have been enhanced to support sorting using a collating sequence. Each element of the sort key is specified with a 4 byte segment descriptor. In the fourth byte of the descriptor bits can be set to modify the sort.

|         |                        |
|---------|------------------------|
| **Bit** | **Purpose**            |
| HEX(01) | Reserved               |
| HEX(02) | Reserved               |
| HEX(04) | Use collating sequence |

Other collating sequences for sorting are available by setting byte 50 of \$OPTIONS RUN to a non zero value.

A new type of field has been defined for a string field which is repeated for each language.

.langtext\$=(start, len, count)

Each element must have the same size, len, and up to 15 are supported (i.e. count \<= 15). When referenced KCML will check the current language defined in \$OPTIONS RUN byte 20 and use that as an index into the list. The \$PACK specifier Anxx (where n is the count and xx is the element length) can also be used to pack and unpack the appropriate string from a list depending on the current language.

<span id="Source_code_control" source_code_control=""></span>Source code control

KCML5 has specific support for the RCS and CVS source control systems which can be used to track changes in KCML programs. This requires programs to be kept in their ascii form using bytes 40 and 46 in \$OPTIONS RUN. Also byte 40 of \$OPTIONS LIST should be zero to force a consistent lower case for all symbols.

The \$Id: newinkcml5.htm,v 1.3 2000/02/16 12:24:15 pjc Exp \$ statement allows the embedding of an RCS \$Id stamp in a program. This could not be enclosed in a REM because of the colon nor in an image because only one image is permitted per line. The statement ends witha matching \$ sign. If the following is added to the program DISP.src

1000 \$Id: newinkcml5.htm,v 1.3 2000/02/16 12:24:15 pjc Exp \$

when booked out of the source control system RCS will expand this to

1000 \$Id: newinkcml5.htm,v 1.3 2000/02/16 12:24:15 pjc Exp \$

The chevrons generated by a CVS merge that failed are parsed by KCML allowing the program to be loaded and edited in the editor. Such a program cannot be executed as an error will be raised during resolve time. The F7 key in the editor can be used to find and mark the sections of the program that need inspection. KCML will now load ascii text even if it has unresolved merge conflicts. The editor can now search for such conflicts using F7. CTRL-W will switch between the start, middle and end of the conflict and SHIFT CTRL-W will select the conflicting area in which the cursor is found. CTRL-Q will strip selected merge text within the CVS markers.

<span id="New_file_maintenance_statements" new_file_maintenance_statements=""></span>New file maintenance statements

COPY and MOVE have been enhanced to support native files. The former will make a copy of a file under a new name whilst the latter will rename it. If the target file already exists then it will be overwritten silently. MOVE will copy and then delete the original if the files are on different filesystems. For example:

COPY "fred.exe" TO "/tmp/fred.exe"\
MOVE "C:\TEST\Long file name.exe" TO "G:\TEST\shortnm.exe"

These statements work with respect to the current working directory, not the directory specified by any SELECT DISK.

<span id="Removing_files" removing_files=""></span>Removing files

A new REMOVE statement can be used to delete native files. It works with respect to the current working directory and does not use the stream table or the value of SELECT DISK.

REMOVE "/tmp/file"\
REMOVE "tempfile009"\
REMOVE file\$

<span id="Creating_and_removing_directories" creating_and_removing_directories=""></span>Creating and removing directories

Directories are supported with new CREATE DIR and REMOVE DIR statements e.g.

CREATE DIR "/tmp/spoolarea"\
REMOVE DIR "/tmp/workfiles"

When a directory is removed with REMOVE DIR all the files and subdirectories it contains are also removed. These statements work with respect to the current working directory, not the directory specified by any SELECT DISK.

<span id="_COMPILE_changes" _compile_changes=""></span>\$COMPILE changes

Programs rather than directories can now be compiled with \$COMPILE e.g.

\$COMPILE "/tmp/work" TO "SL/DISP"

Filenames are relative to the current working directory.

<span id="Loading_ASCII_programs" loading_ascii_programs=""></span>Loading ASCII programs

A new \$OPTIONS RUN byte 46 controls the load order of programs with respect to a default extension. If you consider LOAD "file", then depending on the value of this byte it behaves as follows:

0 load "file" (this is the default)\
1 try "file.src" then "file"\
2 try "file" then "file.src"\
3 load "file.src"\
4 load with compile

This can be useful if you wish to keep all programs in ascii source format during development with a .src extension and only compile with \$COMPILE when for the released version. Ascii source can be searched with grep tools and is easier to source control. The use of an extension such as .src allows particular programs to be associated with KCML source programs.

If byte 46 is set to HEX(04) then KCML will prefer to load a compiled program with the specified name if one exists. However if a file with a .src extension exists in the directory with a later time stamp then a quick \$COMPILE is done on it and the resulting compiled program is loaded. This will make a later load a lot faster while preserving the advantages of having ascii source. This mechanism also works on compound loads.

<span id="Editor_changes" editor_changes=""></span>Editor changes

check box must be on. A literal string found this way can be converted to a single language chevron string with F12. A single language chevron string found this way can be converted into a multi-language chevron string with CTRL-L which will create a new entry for the current language as set in \$OPTIONS RUN byte 20. This must be greater than HEX(01) for this feature to be enabled.

Object definitions such as DEFFORM or DEFOBJ can be located using CTRL-E and SHIFT-CTRL-E to get the next and previous respectively.

<span id="LINPUT___changes" linput___changes=""></span>LINPUT + changes

LINPUT+ can now terminate single line input on PAGE-UP or PAGE-DOWN if control byte 30 is set to HEX(01).

<span id="TCP_IP_support" tcp_ip_support=""></span>TCP/IP support

The OPEN# statement now supports opening TCP/IP sockets allowing a KCML program to act as either a client or a server on a TCP/IP network.

To act as a client a program can issue an open statement such as

OPEN \#1,"alpha.bigco.com :10000", "@"\
OPEN \#stream,"10.1.1.2:rexec","@"

The " @" sign in the mode argument specifies that a socket is to be opened. The socket to use is specified in the filename argument with a colon separating the IP address from the port number. Port numbers may be supplied either as numbers or as known service names e.g. telnet or smtp. The server address may be either a numeric IP address in dot notation or a host name if there is a DNS or hosts file available to resolve this name. The OPEN will attempt to connect to that port and if there is no server available to accept the connection it will fail with a D82 error. However if a server does connect then the OPEN will succeed and the stream number may be used in subsequent \$IF \#, READ# and WRITE# statements to exchange data with the server. To close the connection use CLOSE \#.

To act as a server a KCML program also issues a OPEN \# statement but this time it does not have to specify the host address as this is fixed to be the address of the machine on which the program is executing. E.g.

OPEN \# ConnectStream, " :8123", "@"

This OPEN# will return immediately but the network layer will be primed to receive connections. You can check for a connection by using a \$IF \# e.g.

a=\$IF \# ConnectStream,timeout

The \$IF \# will return 1 in this example whenever a client connects and zero if the timeout expires. The stream in this form of the statement is reserved for connecting only and once a connection arrives the server program must then issue another OPEN to get the socket to use for sending messages. To get a working socket from a connection pass the initial stream as the filename in a further OPEN# thus

OPEN \# MsgStream,"#ConnectStream", "@"

And then use \#MsgStream in \$IF \#, READ#, WRITE \# and CLOSE \#. The connection stream should only be used in \$IF \# and CLOSE \#. Acting as a server requires more careful programming if a service has to be provided for more than one client at a time. The message streams should be allocated from a pool array and a \$IF \# used to test for messages that need to be processed. A READ# will block if no data is available so use \$IF \# first to see if there is any data available. The work done for each message should be completed as quickly as possible in order to provide a timely response for other clients.

<span id="Shared_Libraries" shared_libraries=""></span>Shared Libraries

KCML has a number of C external routines built in and referenced via the CALL verb. This list can be extended dynamically by loading your own shared libraries specified with the -x flag on the KCML command line. More than one library may be loaded. Shared libraries are supported on versions of Unix based on Unix 5.4 (e.g. Unixware 2, DG-UX, Digital Unix, ICL Unix), HP-UX 10.20 and NT. It is not supported on AIX or SCO.

<span id="_DECLARE_changes" _declare_changes=""></span>\$DECLARE changes

On NT servers a program can force a \$DECLARE function to execute on the server rather than the client by either prefixing the module name with an asterisk e.g.

\$DECLARE ‘SQLAllocEnv(RETURN INT())="\*ODBS32.SQLAllocEnv"

or by setting the HEX(80) bit in byte 35 of \$OPTIONS RUN for the duration of the call. The former method defines the function as always executing on the server whereas the latter method allows a dual mode function that can execute on either the server or the client. This second method may be more flexible but it requires explicit programming to ensure that the bit is set appropriately for each call. It is also necessary to preserve the other bits is byte 35 when the HEX(80) bit is toggled.

To support functions that are passed pointers to integers, such as the ‘SQLAllocEnv() example above, KCML5 allows the use of RETURN INT() and TO RETURN INT(). When calling the function this parameter must be passed as a SYM() e.g.

rc=‘SQLAllocEnv(SYM(hEnv))

This avoids the necessity to pass a 4 byte structure and \$UNPACK it.

<span id="_MACHINE_changes" _machine_changes=""></span>\$MACHINE changes

 

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-valign="TOP" width="76"><p><strong>Byte</strong></p></td>
<td data-valign="TOP" width="751"><p><strong>Purpose</strong></p></td>
</tr>
<tr>
<td data-valign="TOP" width="76"><p>2</p></td>
<td data-valign="TOP" width="751"><p>New client capabilities<br />
HEX(20) Client uses 8 bit character set<br />
HEX(40) Client supports forms</p></td>
</tr>
<tr>
<td data-valign="TOP" width="76"><p>25</p></td>
<td data-valign="TOP" width="751"><p>Most significant byte of user count</p></td>
</tr>
<tr>
<td data-valign="TOP" width="76"><p>26</p></td>
<td data-valign="TOP" width="751"><p>Least significant byte of user count</p></td>
</tr>
<tr>
<td data-valign="TOP" width="76"><p>27</p></td>
<td data-valign="TOP" width="751"><p>Most significant byte of maximum users allowed</p></td>
</tr>
<tr>
<td data-valign="TOP" width="76"><p>28</p></td>
<td data-valign="TOP" width="752"><p>Least significant byte of maximum users</p></td>
</tr>
</tbody>
</table>

<span id="_OPTIONS_RUN_changes" _options_run_changes=""></span>\$OPTIONS RUN changes

 

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-valign="TOP" width="95"><p><strong>Byte</strong></p></td>
<td data-valign="TOP" width="543"><p><strong>Purpose</strong></p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>35</p></td>
<td data-valign="TOP" width="543"><p>New $DECLARE option<br />
HEX(80) execute on server not client</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>40</p></td>
<td data-valign="TOP" width="543"><p>New <a href="$COMPILE.htm">$COMPILE</a> options<br />
HEX(40) use <a href="RESAVE.htm">RESAVE</a> rather than <a href="SAVE.htm">SAVE</a><br />
HEX(80) no .src extension when saving compiled</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>42</p></td>
<td data-valign="TOP" width="543"><p>Size in MB of the memory buffer used by <a href="FSORT_BU.htm">FSORT</a> and KI_REBUILD. Defaults to 8 on Unix and 4 on NT</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>43</p></td>
<td data-valign="TOP" width="543"><p>Reserved</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>44</p></td>
<td data-valign="TOP" width="543"><p>Maximum number of lines used to <a href="LIST_DIM.htm">LIST DIM</a> a variable in <a href="PANIC.htm">PANIC</a> listing</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>45</p></td>
<td data-valign="TOP" width="543"><p><a href="SELECT_@PART.htm">SELECT @PART</a> " " options<br />
HEX(00) keep global mapped<br />
HEX(01) detach shared memory</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>46</p></td>
<td data-valign="TOP" width="543"><p>Options for <a href="LOAD.htm">LOAD</a>ing programs<br />
HEX(00) try "file"<br />
HEX(01) try "file.src" then "file"<br />
HEX(02) try "file" then "file.src"<br />
HEX(03) try "file.src" only<br />
HEX(04) always load compiled "file" but save both "file" and "file.src". If "file.src" is newer than "file" then compile before loading.</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>47</p></td>
<td data-valign="TOP" width="543"><p><a href="PRINTUSING.htm">PRINTUSING</a> options<br />
HEX(01) no count in first 2 bytes of buffer<br />
HEX(02) put a TAB character between columns</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>48</p></td>
<td data-valign="TOP" width="543"><p>Start of current century. Defaults to 32 so years 0 to 31 will be assumed to be 2000 to 2031. Year 32 will be considered as 1932.</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>49</p></td>
<td data-valign="TOP" width="543"><p>Global fields<br />
HEX(00) ignore (this is the default)<br />
HEX(01) if not in local symbol table then lookup in global<br />
HEX(03) save global value in local symbol table</p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>50</p></td>
<td data-valign="TOP" width="543"><p>Language table for <a href="$LOWER(.htm">$UPPER</a>/<a href="$LOWER(.htm">$LOWER</a>/<a href="$STRCOLL(.htm">$STRCOL</a></p></td>
</tr>
</tbody>
</table>

<span id="_OPTIONS_LIST_changes" _options_list_changes=""></span>\$OPTIONS LIST changes

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-valign="TOP" width="95"><p><strong>Byte</strong></p></td>
<td data-valign="TOP" width="543"><p><strong>Purpose</strong></p></td>
</tr>
<tr>
<td data-valign="TOP" width="95"><p>40</p></td>
<td data-valign="TOP" width="543"><p>How variables names are presented<br />
HEX(00) preserve case from DIM<br />
HEX(01) force lowercase (the default)</p></td>
</tr>
</tbody>
</table>
