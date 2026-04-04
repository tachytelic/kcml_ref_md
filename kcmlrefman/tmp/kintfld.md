# Internally defined structures

#### DEFRECORD definitions

<div class="indent">

|  |  |
|----|----|
| [KCML_DEFRECORD_Entry](#KCML_DEFRECORD_Entry) | '\_Enum\_\* and '\_Find\_\* record |
| [KCML_PSTAT](#KCML_PSTAT) | KCML \$PSTAT structure |
| [KCML_MACHINE](#KCML_MACHINE) | KCML \$MACHINE structure |
| [KCML_OPTIONS](#KCML_OPTIONS) | KCML \$OPTIONS structure |
| [KCML_OPTIONS_HASH](#KCML_OPTIONS_HASH) | KCML \$OPTIONS \# structure |
| [KCML_OPTIONS_LIST](#KCML_OPTIONS_LIST) | KCML \$OPTIONS LIST structure |
| [KCML_OPTIONS_RUN](#KCML_OPTIONS_RUN) | KCML \$OPTIONS RUN structure |
| [KDB_CATALOG](#KDB_CATALOG) | Structure of the KDB system catalog |
| [KDB_INFO_CONN](#KDB_INFO_CONN) | KDB connection information |
| [KDB_INFO_COL](#KDB_INFO_COL) | KDB index column information |
| [KDB_INFO_IDX](#KDB_INFO_IDX) | KDB table index information |
| [KDB_INFO_WS_COL](#KDB_INFO_WS_COL) | KDB Word search index component column information |
| [KDB_INFO_WSX](#KDB_INFO_WSX) | KDB Word search index information |
| [KDB_INFO_HAND](#KDB_INFO_HAND) | KDB open table summary information (type 7 superset) |
| [KCML_SORTKEY](#KCML_SORTKEY) | SORT key descriptors |
| [KCML_COVERAGE_ENTRY](#KCML_COVERAGE_ENTRY) | Coverage information |
| [KCML_SESSION_SETTIMEOUT](#KCML_SESSION_SETTIMEOUT) | Record passed to KCML_Session_SetTimeout function |
| [KCML_SESSION_TIMEOUT](#KCML_SESSION_TIMEOUT) | Record passed to KCML_Session_Timeout callback function |
| [KCML_TERMINFO](#KCML_TERMINFO) | Structure return by 'KCML_Get_TermInfo |
| [KCML_BuildInfo](#KCML_BuildInfo) | Record returned by 'KCML_Build_GetInfo() containing build/version information |
| [KCML_FILE_STAT](#KCML_FILE_STAT) | For 'KCML_File_Stat and KI_STAT |
| [KCML_PerfMetricRec](#KCML_PerfMetricRec) | A record describing a performance metric |
| [KCML_PerfTimerRec](#KCML_PerfTimerRec) | A record to store the result of an execution timer. |

</div>

#### \$DECLARE definitions

<div class="indent">

|  |  |
|----|----|
| ['MessageBox()](#MessageBox) | Invoke a Windows message box dialog |
| ['KCMLCommandLine()](#KCMLCommandLine) | Returns -C command line bookmark passed to client |
| ['KCMLSetTitleTemplate()](#KCMLSetTitleTemplate) | Set a persistent title template |
| ['KCMLObjectExport()](#KCMLObjectExport) | Defines the interface for a COM or SOAP server |
| ['KCMLObjectGetUsername()](#KCMLObjectGetUsername) | Returns the user authorization details for a SOAP request |
| ['KCMLStringMD5()](#KCMLStringMD5) | Returns an MD5 hash for a buffer. |
| ['KCMLStartExecTimer()](#KCMLStartExecTimer) | Start an execution timer |
| ['KCMLStopExecTimer()](#KCMLStopExecTimer) | Returns the execution time. |
| ['KCML_Socket_SetSSL()](#KCML_Socket_SetSSL) | Turn TLS/SSL on socket on or off |
| ['KCML_PerfStats_Start()](#KCML_PerfStats_Start) | Start performance measuring |
| ['KCML_PerfStats_Comment()](#KCML_PerfStats_Comment) | Add comment to performance stats |
| ['KCML_PerfStats_IsRunning()](#KCML_PerfStats_IsRunning) | Is perfstats running? |
| ['KCML_PerfStats_End()](#KCML_PerfStats_End) | Stop performance measuring |
| ['KCML_Session_SetTimeout()](#KCML_Session_SetTimeout) | Sets a session timeout callback |
| ['KCML_Get_TermInfo()](#KCML_Get_TermInfo) | Return information about the connected terminal |
| ['KCML_Panic_Suppress()](#KCML_Panic_Suppress) | Hide return stack from PANIC |
| ['KCML_Lic_Acquire()](#KCML_Lic_Acquire) | Consume an application license and store it in \$PSTAT |
| ['KCML_Lic_Release()](#KCML_Lic_Release) | Release an application from \$PSTAT |
| ['KCML_Lic_Count()](#KCML_Lic_Count) | Counts the number of application licenses in use |
| ['KCML_Lic_GetApplications()](#KCML_Lic_GetApplications) | Enumerates what application licenses a partition has acquired. |
| ['KCML_Build_GetInfo()](#KCML_Build_GetInfo) | Returns build information about the KCML executable |
| ['KCML_File_Stat()](#KCML_File_Stat) | Returns information about the given file |
| ['KCML_Uuid_FromString()](#KCML_Uuid_FromString) | Converts a string to a UUID. |
| ['KCML_Uuid_ToString()](#KCML_Uuid_ToString) | Converts a UUID to a printable string. |
| ['KCML_Uuid_Create()](#KCML_Uuid_Create) | Creates a 16-byte UUID. |
| ['KCML_PerfMetric_Get()](#KCML_PerfMetric_Get) | Returns a list of performance metrics. |
| ['KCML_PerfMetric_Set()](#KCML_PerfMetric_Set) | Enable a performance metric. |
| ['KCML_PerfMetric_Clear()](#KCML_PerfMetric_Clear) | Stop a performance metric. |
| ['KCML_PerfMetric_Flush()](#KCML_PerfMetric_Flush) | Flush the current value of a performance metric. |
| ['KCML_PerfMetric_Send()](#KCML_PerfMetric_Send) | Send an application performance metric. |
| ['KCML_MessageQueue_IsEnabled()](#KCML_MessageQueue_IsEnabled) | Check if a message queue has been enabled. |
| ['KCML_PerfTimer_Start()](#KCML_PerfTimer_Start) | Start a performance timer. |
| ['KCML_PerfTimer_Poll()](#KCML_PerfTimer_Poll) | Poll a performance timer. |
| ['KCML_PerfTimer_Stop()](#KCML_PerfTimer_Stop) | Stop a performance timer. |

</div>

\

------------------------------------------------------------------------

<span id="KCML_DEFRECORD_Entry"></span>

### DEFRECORD KCML_DEFRECORD_Entry

**'\_Enum\_\* and '\_Find\_\* record**

| FLD name         | Pack format | Purpose                          |
|------------------|-------------|----------------------------------|
| DEFRECORD_Name\$ | CHAR(64)    | The name of the field            |
| DEFRECORD_Start  |             | The start byte counted from 1    |
| DEFRECORD_Pack\$ | CHAR(32)    | The packing format               |
| DEFRECORD_Rem\$  | CHAR(64)    | Any REM associated with this FLD |

\
[More info](../DEFRECORD.htm#enum)\

------------------------------------------------------------------------

<span id="KCML_PSTAT"></span>

### DEFRECORD KCML_PSTAT

**KCML \$PSTAT structure**

| FLD name | Pack format | Purpose |
|----|----|----|
| PSTAT_UserStatus\$ | CHAR | User settable status |
| PSTAT_KCMLRelease | UNUM | KCML release |
| PSTAT_Programmable\$ | CHAR | Set to "P" if programmable |
| PSTAT_TermStatus\$ | CHAR | Terminal status |
| PSTAT_GlobalName\$ | CHAR | Global partition name (all 0x00 if not a global) |
| PSTAT_ErrorMajor | UNUM | Major portion of last error code |
| PSTAT_DeviceStatus | UINT | Device status |
| PSTAT_ProcessId | UINT | Process ID |
| PSTAT_Terminal | UINT | \#TERM |
| PSTAT_Partition | UINT | \#PART |
| PSTAT_GlobalPartition | UINT | Global partition ID, or grouping ID |
| PSTAT_ErrorMinor | UINT | Minor portion of last error number |
| PSTAT_ClientIP\$ | CHAR | IP address of client |
| PSTAT_HeapSize | UINT | Dynamic heap size in KB |
| PSTAT_ClientCategory\$ | CHAR | Client category |
| PSTAT_ClientName\$ | CHAR | Name of client |
| PSTAT_LastAccessed | UINT | Timestamp of last keyboard access |
| PSTAT_UserId\$ | CHAR | User Id |
| PSTAT_MACaddress\$ | CHAR | MAC address of client |
| PSTAT_ConnectType | UINT | Connection Type |
| PSTAT_Uuid\$ | HEX | Universally Unique identifier. Will be only be set unless extended partitions have been configured. |

\
[More info](../$PSTAT.htm)\

------------------------------------------------------------------------

<span id="KCML_MACHINE"></span>

### DEFRECORD KCML_MACHINE

**KCML \$MACHINE structure**

| FLD name | Pack format | Purpose |
|----|----|----|
| MACHINE_OsType\$ | CHAR(1) | Operating system type |
| MACHINE_TermCaps | UINT(1) | Terminal capabilities (see also MACHINE_TermCaps2) |
| MACHINE_TermLanguage\$ | CHAR(1) | Terminal language as deduced by KClient from Windows |
| MACHINE_MaxTerm | UINT(2) | Maximum value of \#TERM |
| MACHINE_MaxPart | UINT(2) | Maximum value of \#PART |
| MACHINE_KClientUsers | UINT(2) | Number of KClient users at startup |
| MACHINE_MaxKClientUsers | UINT(2) | Maximum KClient users allowed by license |
| MACHINE_LicenseType | UINT(1) | Type of license |
| MACHINE_GMTOffset | INT(2) | Local timezone offset from GMT in minutes |
| MACHINE_ServerIP\$ | CHAR(4) | Server IP address (Zero if direct connect) |
| MACHINE_ClientIP\$ | CHAR(4) | Client IP address (Zero if direct connect) |
| MACHINE_TermCaps2 | UINT(1) | Terminal capabilities (see also MACHINE_TermCaps) |
| MACHINE_OptFeatures | UINT(1) | Optional features set during connection or compiled into KCML |
| MACHINE_KCMLUsers | UINT(2) | Number of distinct users logged on when KCML started |
| MACHINE_Compliance | UINT(1) | \$COMPLIANCE language support |
| MACHINE_ServerMode | UINT(1) | Server mode (0x01 SOAP server, 0x02 render forms as XML) |
| MACHINE_ServerEncoding | UINT(1) | Character encoding to use |
| MACHINE_PartitionSize | UINT | Size of a partition expressed as a power of 2 |

\
[More info](../$MACHINE.htm)\

------------------------------------------------------------------------

<span id="KCML_OPTIONS"></span>

### DEFRECORD KCML_OPTIONS

**KCML \$OPTIONS structure**

| FLD name | Pack format | Purpose |
|----|----|----|
| OPTIONS_DollarReplacement\$ | CHAR(1) | Replacement for '\$' in PRINTUSING |
| OPTIONS_CommaReplacement\$ | CHAR(1) | Replacement for ',' in PRINTUSING |
| OPTIONS_PeriodReplacement\$ | CHAR(1) | Replacement for decimal point in PRINTUSING |
| OPTIONS_DisableReset | UINT(1) | Disable Ctrl+Alt+BREAK |
| OPTIONS_DisableControlBreak | UINT(1) | Disable Ctrl+BREAK |
| OPTIONS_ForceDIMs | UINT(1) | Force all variables to be dimmed (see also \$COMPLIANCE) |

\
[More info](../$OPTIONS.htm)\

------------------------------------------------------------------------

<span id="KCML_OPTIONS_HASH"></span>

### DEFRECORD KCML_OPTIONS_HASH

**KCML \$OPTIONS \# structure**

| FLD name | Pack format | Purpose |
|----|----|----|
| OPTIONS_HASH_WriteMode | UINT(1) | Controls appending, synchronous writes, blocking |
| OPTIONS_HASH_ReadMode | UINT(1) | Controls line orientated read mode, truncation |
| OPTIONS_HASH_Status | UINT(1) | Status (controlled by KCML) |
| OPTIONS_HASH_EndOfLine\$ | CHAR(1) | End of line character (if OPTIONS_HASH_ReadMode 0x01 bit set) |
| OPTIONS_HASH_IgnoreChar\$ | CHAR(1) | Ignore character (if OPTIONS_HASH_ReadMode 0x02 bit set) |

\
[More info](../$OPTIONShash.htm)\

------------------------------------------------------------------------

<span id="KCML_OPTIONS_LIST"></span>

### DEFRECORD KCML_OPTIONS_LIST

**KCML \$OPTIONS LIST structure**

| FLD name | Pack format | Purpose |
|----|----|----|
| OPTIONS_LIST_BlankLines | UINT(1) | Blank lines in workbench |
| OPTIONS_LIST_MaxClipLength | UINT(1) | Maximum line length to copy to clipboard |
| OPTIONS_LIST_Continuation\$ | CHAR(1) | Continuation character when splitting statements |
| OPTIONS_LIST_IndentSpaces | UINT(1) | Number of spaces to indent code |
| OPTIONS_LIST_MixedCase | UINT(1) | Allow mixed case variables |

\
[More info](../$OPTIONS_LIST.htm)\

------------------------------------------------------------------------

<span id="KCML_OPTIONS_RUN"></span>

### DEFRECORD KCML_OPTIONS_RUN

**KCML \$OPTIONS RUN structure**

| FLD name | Pack format | Purpose |
|----|----|----|
| OPTIONS_RUN_NoEndDoError | UINT(1) | No END DO error flag |
| OPTIONS_RUN_PanicOnDump | UINT(1) | Create a PANIC file prior to a core dump |
| OPTIONS_RUN_KeepShared | UINT(1) | Keep shared libraries over LOADs flag |
| OPTIONS_RUN_Language | UINT(1) | Current language (multi-language systems) |
| OPTIONS_RUN_HelpStart\$ | CHAR(1) | Character used to start a \$HELP special sequence |
| OPTIONS_RUN_HelpStop\$ | CHAR(1) | Character used to end a \$HELP special sequence |
| OPTIONS_RUN_MaxPart | UINT(2) | Maximum value of \#PART |
| OPTIONS_RUN_EditorHistory | UINT(1) | Editor history lines |
| OPTIONS_RUN_Win32Mode | UINT(1) | \$DECLARE interface mode |
| OPTIONS_RUN_DisableProg | UINT(1) | Disable programming |
| OPTIONS_RUN_ShellMode | UINT(1) | SHELL mode bits |
| OPTIONS_RUN_SaveOptions | UINT(1) | Options for \$COMPILE and saving programs |
| OPTIONS_RUN_HelpOptions | UINT(1) | Options for \$HELP |
| OPTIONS_RUN_LoadOptions | UINT(1) | Options for loading programs |
| OPTIONS_RUN_PRINTUSINGMode | UINT(1) | PRINTUSING mode |
| OPTIONS_RUN_Century | UINT(1) | Start of current century |
| OPTIONS_RUN_GlobalFLDs | UINT(1) | Lookup FLDs in libraries if not defined in program |
| OPTIONS_RUN_LangTable | UINT(1) | Language table for \$UPPER/\$LOWER/\$STRCOLL |
| OPTIONS_RUN_LogThreshold | UINT(1) | Write log threshold |
| OPTIONS_RUN_PanicEndOptions | UINT(1) | Options for END and PANIC |
| OPTIONS_RUN_Constants | UINT(1) | Constants flag |
| OPTIONS_RUN_Locale | UINT(1) | Locale for UTF-8 conversion |
| OPTIONS_RUN_Compatibility | UINT(1) | Compatibility options |

\
[More info](../$OPTIONS_RUN.htm)\

------------------------------------------------------------------------

<span id="KDB_CATALOG"></span>

### DEFRECORD KDB_CATALOG

**Structure of the KDB system catalog**

| FLD name             | Pack format | Purpose            |
|----------------------|-------------|--------------------|
| CATALOG_Tablename\$  | CHAR(35)    | Tablename          |
| CATALOG_Tablespace\$ | CHAR(40)    | Tablespace         |
| CATALOG_Update\$     | CHAR(1)     | Update allowed Y/N |
| CATALOG_Module\$     | CHAR(2)     | Module             |
| CATALOG_Company\$    | CHAR(2)     | Company            |
| CATALOG_LongName\$   | CHAR(64)    | Long name          |
| CATALOG_ColMode\$    | CHAR(1)     | Column mode        |

\

------------------------------------------------------------------------

<span id="KDB_INFO_CONN"></span>

### DEFRECORD KDB_INFO_CONN

**KDB connection information**

| FLD name             | Pack format | Purpose                           |
|----------------------|-------------|-----------------------------------|
| INFO_CONN_Type\$     | CHAR(64)    | Database type                     |
| INFO_CONN_Name\$     | CHAR(64)    | Database name                     |
| INFO_CONN_MajorError | UINT(1)     | Last major error number           |
| INFO_CONN_MinorError | UINT(1)     | Last minor error number           |
| INFO_CONN_SysError   | UINT(1)     | Last operating system errno value |
| INFO_CONN_ConnStatus | UINT(1)     | Connection status                 |

\
[More info](../tmp/KI_INFO.htm#conn)\

------------------------------------------------------------------------

<span id="KDB_INFO_COL"></span>

### DEFRECORD KDB_INFO_COL

**KDB index column information**

| FLD name        | Pack format | Purpose            |
|-----------------|-------------|--------------------|
| INFO_COL_Start  | UINT(2)     | Key segment start  |
| INFO_COL_Length | UINT(1)     | Key segment length |

\
[More info](../tmp/KI_INFO.htm#col)\

------------------------------------------------------------------------

<span id="KDB_INFO_IDX"></span>

### DEFRECORD KDB_INFO_IDX

**KDB table index information**

| FLD name | Pack format | Purpose |
|----|----|----|
| INFO_IDX_KeyLen | UINT(1) | Key length |
| INFO_IDX_Dups\$ | CHAR(1) | Duplicates allowed (ASCII 'N') |
| INFO_IDX_kspec\$(\_KDB_MAX_KEY_COLS)\_KDB_INFO_COL |  | Key columns |

\
[More info](../tmp/KI_INFO.htm#idx)\

------------------------------------------------------------------------

<span id="KDB_INFO_WS_COL"></span>

### DEFRECORD KDB_INFO_WS_COL

**KDB Word search index component column information**

| FLD name           | Pack format | Purpose            |
|--------------------|-------------|--------------------|
| INFO_WS_COL_Start  | UINT(2)     | Key segment start  |
| INFO_WS_COL_Length | UINT(2)     | Key segment length |
| INFO_WS_COL_Type\$ | CHAR(1)     | Key segment type   |

\
[More info](../tmp/KI_INFO.htm#wscol)\

------------------------------------------------------------------------

<span id="KDB_INFO_WSX"></span>

### DEFRECORD KDB_INFO_WSX

**KDB Word search index information**

| FLD name | Pack format | Purpose |
|----|----|----|
| INFO_WSX_OrderBy | UINT(1) | Order by path number |
| INFO_WSX_MinWordLen | UINT(1) | Minimum word length |
| INFO_WSX_MaxWordLen | UINT(1) | Maximum word length |
| INFO_WSX_DBCSstart | UINT(1) | DBCS start code point |
| INFO_WSX_DBCSend | UINT(1) | DBCS end code point |
| INFO_WSX_kspec\$(\_KDB_MAX_WS_KEY_COLS)\_KDB_INFO_WS_COL |  | Key segments |
| INFO_WSX_NonAlphaChars\$ | CHAR(16) | Non-alpha characters allowed |

\
[More info](../tmp/KI_INFO.htm#wsx)\

------------------------------------------------------------------------

<span id="KDB_INFO_HAND"></span>

### DEFRECORD KDB_INFO_HAND

**KDB open table summary information (type 7 superset)**

| FLD name | Pack format | Purpose |
|----|----|----|
| INFO_HAND_Telltale\$ | CHAR(1) | 'K' for native KDB database table |
| INFO_HAND_Version\$ | CHAR(1) | Version number (ASCII '7') |
| INFO_HAND_MinorVersion\$ | CHAR(1) | Minor version number |
| INFO_HAND_PageSize | UINT(1) | Page size in Kb |
| INFO_HAND_RowLen | UINT(2) | Row length in Kb |
| INFO_HAND_IdxCount | UINT(1) | Number of indices |
| INFO_HAND_WsCount | UINT(1) | Number of word search indices |
| INFO_HAND_Serial | UINT(4) | Serial number |
| INFO_HAND_SerialOffset | UINT(2) | Serial number offset |
| INFO_HAND_ExclLockedBY | UINT(2) | Partition number of exclusive owner (in binary) |
| INFO_HAND_MajorError | UINT(1) | Last major error number |
| INFO_HAND_MinorError | UINT(1) | Last minor error number |
| INFO_HAND_SysError | UINT(1) | Last operating system errno value |
| INFO_HAND_HandleStatus | UINT(1) | Handle status |
| INFO_HAND_Handle | UINT(2) | Handle number as an integer |
| INFO_HAND_RowCount | UINT(4) | Count of rows in table |
| INFO_HAND_OpenMode\$ | CHAR(1) | Mode the table was opened with, eg 'R'ead or 'W'rite |
| INFO_HAND_PageCount | UINT(4) | Number of pages in use |
| INFO_HAND_PageTotal | UINT(4) | Number of pages in table |
| INFO_HAND_StampFlags | UINT(4) | Date, user and timestamp flags |
| INFO_HAND_DateOffset | UINT(2) | Offset to auto-datestamp |
| INFO_HAND_UserOffset | UINT(2) | Offset to auto-userstamp |
| INFO_HAND_UserLen | UINT(1) | Length of auto-userstamp |
| INFO_HAND_ExcludeColumnOffset | UINT(2) | Offset to exclude column |
| INFO_HAND_AutoTransact\$ | CHAR(1) | 'T' if this table starts Oracle transaction |
| INFO_HAND_TablePath\$ | CHAR(128) | File name of KDB file |
| INFO_HAND_TableName\$ | CHAR(128) | Table name |
| INFO_HAND_iprefix\$ | CHAR(20) | IPREFIX from CREATE TABLE statement for KI_FLD |
| INFO_HAND_TimeOffset | UINT(2) | Offset to auto-timestamp |

\
[More info](../tmp/KI_INFO.htm#hand7)\

------------------------------------------------------------------------

<span id="KCML_SORTKEY"></span>

### DEFRECORD KCML_SORTKEY

**SORT key descriptors**

| FLD name         | Pack format | Purpose                                       |
|------------------|-------------|-----------------------------------------------|
| SORTKEY_Length   | UINT(1)     | Length, zero marks end of descriptors         |
| SORTKEY_Position | UINT(2)     | Start of segment, counted from 1              |
| SORTKEY_Sequence | UINT(1)     | Bits defining how the segment is to be sorted |

\
[More info](../SORT.htm)\

------------------------------------------------------------------------

<span id="KCML_COVERAGE_ENTRY"></span>

### DEFRECORD KCML_COVERAGE_ENTRY

**Coverage information**

| FLD name                       | Pack format | Purpose                  |
|--------------------------------|-------------|--------------------------|
| KCML_COVERAGE_ENTRY_FileName\$ | CHAR        | Source file filename     |
| KCML_COVERAGE_ENTRY_LineNo     | UINT        | Line number              |
| KCML_COVERAGE_ENTRY_StatNo     | UINT        | Statement number         |
| KCML_COVERAGE_ENTRY_Count      | UINT        | Hit count                |
| KCML_COVERAGE_ENTRY_Reserved   | UINT        | Reserved for future use. |

\

------------------------------------------------------------------------

<span id="KCML_SESSION_SETTIMEOUT"></span>

### DEFRECORD KCML_SESSION_SETTIMEOUT

**Record passed to KCML_Session_SetTimeout function**

| FLD name | Pack format | Purpose |
|----|----|----|
| KCML_SESSION_SETTIMEOUT_Timeout |  | Time in seconds from last access before timeout is first called. |
| KCML_SESSION_SETTIMEOUT_KeepAlive |  | Time in seconds to wait for keepalive prompt from the client. |
| KCML_SESSION_SETTIMEOUT_Callback |  | SYM of function that is called when the timeout is reached |

\

------------------------------------------------------------------------

<span id="KCML_SESSION_TIMEOUT"></span>

### DEFRECORD KCML_SESSION_TIMEOUT

**Record passed to KCML_Session_Timeout callback function**

| FLD name | Pack format | Purpose |
|----|----|----|
| KCML_SESSION_TIMEOUT_Time |  | Total time of inactivity |
| KCML_SESSION_TIMEOUT_Count |  | Number of times callback has been called since last activity |
| KCML_SESSION_TIMEOUT_Broker | BOOL | TRUE if using the connection broker |
| KCML_SESSION_TIMEOUT_Connected | BOOL | A test ping of KClient returned successful |
| KCML_SESSION_TIMEOUT_Terminated | BOOL | TRUE if signalled to terminate |

\

------------------------------------------------------------------------

<span id="KCML_TERMINFO"></span>

### DEFRECORD KCML_TERMINFO

**Structure return by 'KCML_Get_TermInfo**

| FLD name | Pack format | Purpose |
|----|----|----|
| TERMINFO_WINDOWS | BOOL | Windows drawn with WINDOW OPEN are done by the terminal. |
| TERMINFO_SAVESCREEN | BOOL | Screen saving (HEX(0000)) is done locally |
| TERMINFO_NEWDECLARE | BOOL | Support \$DECLARE |
| TERMINFO_DECLARE_32BIT | BOOL | Support for 32 bit \$DECLARE |
| TERMINFO_EIGHT_BIT_CHARS | BOOL | Client uses an 8 bit character set |
| TERMINFO_FORMS | BOOL | Client supports KCML forms |
| TERMINFO_CE | BOOL | Client running on Windows CE |
| TERMINFO_NETIER | BOOL | Client is running on a Netier NT terminal |
| TERMINFO_WTS | BOOL | Client is running on a Citrix or WTS thin client |
| TERMINFO_WKCML | BOOL | Client is connected directly (i.e. client and server are running as one process and not in client server mode). This is the mode in which the WKCML product always runs |
| TERMINFO_UNICODE | BOOL | Client is a Unicode version |
| TERMINFO_WYSE_NT | BOOL | Client is running on a Wyse NT terminal |
| TERMINFO_KSTRESS | BOOL | For internal use only |
| TERMINFO_SUPPORT | BOOL | For internal use only |
| TERMINFO_CLIENTCOM | BOOL | General ClientCOM objects supported |
| TERMINFO_KCLIENT_CLIENTCOM | BOOL | Internal "KClient" ClientCOM object supported |
| TERMINFO_MESSAGEBOX | BOOL | 'MessageBox \$DECLARE is supported |
| TERMINFO_InternalDeclare | BOOL | Internal \$DECLARE client functions are supported (not all may be implelmented - some may error function not found) |
| TERMINFO_Role\$ | CHAR | The role, if set in a KClient lic.txt SUPPORT section |
| TERMINFO_DealerRole\$ | CHAR | The role, if set in a KClient lic.txt DEALER section |
| TERMINFO_Pilot | BOOL | Server lic.txt contains Pilot key |
| TERMINFO_ClientLic | BOOL | For internal use only |

\

------------------------------------------------------------------------

<span id="KCML_BuildInfo"></span>

### DEFRECORD KCML_BuildInfo

**Record returned by 'KCML_Build_GetInfo() containing build/version information**

| FLD name                       | Pack format | Purpose                      |
|--------------------------------|-------------|------------------------------|
| KCML_BuildInfo_Version\$       | CHAR        | KCML Version string          |
| KCML_BuildInfo_MajorVersion    |             | Major KCML version number    |
| KCML_BuildInfo_MinorVersion    |             | Minor KCML version number    |
| KCML_BuildInfo_Revision        |             | Revision number              |
| KCML_BuildInfo_Build           |             | Daily build number           |
| KCML_BuildInfo_Architecture\$  | CHAR        | Platform architecture        |
| KCML_BuildInfo_OSVersion       |             | Operating system version     |
| KCML_BuildInfo_OSName\$        | CHAR        | Name of the operating system |
| KCML_BuildInfo_SSLVersion\$    | CHAR        | OpenSSL version string       |
| KCML_BuildInfo_SSLMajorVersion |             | OpenSSL major version        |
| KCML_BuildInfo_SSLMinorVersion |             | OpenSSL minor version        |
| KCML_BuildInfo_SSLFixVersion   |             | OpenSSL patch fix version    |
| KCML_BuildInfo_Debug           | BOOL        | Debug build                  |

\

------------------------------------------------------------------------

<span id="KCML_FILE_STAT"></span>

### DEFRECORD KCML_FILE_STAT

**For 'KCML_File_Stat and KI_STAT**

| FLD name    | Pack format | Purpose                       |
|-------------|-------------|-------------------------------|
| KST_type    |             | file type. KCML_FILE_TYPE     |
| KST_dev     | UINT        | device                        |
| KST_ino     | UINT        | inode                         |
| KST_mode    | UINT        | protection                    |
| KST_nlink   | UINT        | number of hard links          |
| KST_uid     | UINT        | user ID of owner              |
| KST_gid     | UINT        | group ID of owner             |
| KST_rdev    | UINT        | device type (if inode device) |
| KST_size    | UINT        | total size (in bytes)         |
| KST_atime\$ | CHAR        | time of last access           |
| KST_mtime\$ | CHAR        | time of last modification     |
| KST_ctime\$ | CHAR        | time of last status change    |

\

------------------------------------------------------------------------

<span id="KCML_PerfMetricRec"></span>

### DEFRECORD KCML_PerfMetricRec

**A record describing a performance metric**

| FLD name | Pack format | Purpose |
|----|----|----|
| KCML_PerfMetric_Name\$ | CHAR | Performance metric name |
| KCML_PerfMetric_Desc\$ | CHAR | Description |
| KCML_PerfMetric_Flag |  | Flag value |
| KCML_PerfMetric_Enabled | BOOL | TRUE if statistics for this metric are being collected |

\

------------------------------------------------------------------------

<span id="KCML_PerfTimerRec"></span>

### DEFRECORD KCML_PerfTimerRec

**A record to store the result of an execution timer.**

| FLD name | Pack format | Purpose |
|----|----|----|
| KCML_PerfTimer_Elapsed |  | Number of microseconds since the timer was started |
| KCML_PerfTimer_Exec |  | Number of microseconds spent executing application code. |
| KCML_PerfTimer_User |  | Amount of processor user time, in microseconds, consumed since the timer was started. |
| KCML_PerfTimer_Kernel |  | Amount of processor kernel time, in microseconds, consumed since the timer was started. |

## \$DECLARE definitions

\

------------------------------------------------------------------------

<span id="MessageBox"></span>

### \$DECLARE 'MessageBox(hWnd, Msg\$, Title\$, nOpts)

#### Invoke a Windows message box dialog

| Argument | Format | Purpose                                |
|----------|--------|----------------------------------------|
| hWnd     | INT()  | Parent window (ignored, leave as zero) |
| Msg\$    | STR()  | The message text                       |
| Title\$  | STR()  | Titlebar text                          |
| nOpts    | INT()  | Options (see constants) e.g. MB_OK     |


    REM $DECLARE 'MessageBox(hWnd, Msg$, Title$, nOpts)
    REM Invoke a Windows message box dialog
    $DECLARE 'MessageBox(INT(), STR(), STR(), INT())

This executes on the **client**.

\

------------------------------------------------------------------------

<span id="KCMLCommandLine"></span>

### \$DECLARE 'KCMLCommandLine(cmdline\$)

#### Returns -C command line bookmark passed to client

| Argument  | Format       | Purpose                            |
|-----------|--------------|------------------------------------|
| cmdline\$ | RETURN STR() | Buffer to receive the command line |


    REM $DECLARE 'KCMLCommandLine(cmdline$)
    REM Returns -C command line bookmark passed to client
    $DECLARE 'KCMLCommandLine(RETURN STR())

This executes on the **client**.

[More info](implbmarks.htm)\

------------------------------------------------------------------------

<span id="KCMLSetTitleTemplate"></span>

### \$DECLARE 'KCMLSetTitleTemplate(TitleTemplate\$)

#### Set a persistent title template

| Argument        | Format | Purpose                  |
|-----------------|--------|--------------------------|
| TitleTemplate\$ | STR()  | Template for form titles |


    REM $DECLARE 'KCMLSetTitleTemplate(TitleTemplate$)
    REM Set a persistent title template
    $DECLARE 'KCMLSetTitleTemplate(STR())

This executes on the **client**.

[More info](KCMLSetTitleTemplate.htm)\

------------------------------------------------------------------------

<span id="KCMLObjectExport"></span>

### \$DECLARE 'KCMLObjectExport(ObjectType\$, interface\$, wsdl\$, endpoint\$)

#### Defines the interface for a COM or SOAP server

This defines the interface for a COM or SOAP server. For COM server calls the last two arguments should be zero or blank.

**Returns:** a boolean, TRUE for success, FALSE for bad arguments

| Argument | Format | Purpose |
|----|----|----|
| ObjectType\$ | STR() | Must be "SOAP or COM" |
| interface\$ | STR() | Interface prefix for DEFSUBs |
| wsdl\$ | STR() | (SOAP) if non-blank the WSDL will be written to this file |
| endpoint\$ | STR() | (SOAP) URL for the server |


    REM $DECLARE 'KCMLObjectExport(ObjectType$, interface$, wsdl$, endpoint$)
    REM Defines the interface for a COM or SOAP server
    $DECLARE 'KCMLObjectExport(STR(), STR(), STR(), STR()) = "*"

This executes on the **server**.

[More info](../soapserver.htm#security)\

------------------------------------------------------------------------

<span id="KCMLObjectGetUsername"></span>

### \$DECLARE 'KCMLObjectGetUsername(ObjectType\$, user\$, bCheckUser)

#### Returns the user authorization details for a SOAP request

| Argument     | Format       | Purpose                        |
|--------------|--------------|--------------------------------|
| ObjectType\$ | STR()        | Must be "SOAP"                 |
| user\$       | RETURN STR() | Returns userid                 |
| bCheckUser   | INT()        | If TRUE KCML will authenticate |


    REM $DECLARE 'KCMLObjectGetUsername(ObjectType$, user$, bCheckUser)
    REM Returns the user authorization details for a SOAP request
    $DECLARE 'KCMLObjectGetUsername(STR(), RETURN STR(), INT()) = "*"

This executes on the **server**.

[More info](../soapserver.htm#security)\

------------------------------------------------------------------------

<span id="KCMLStringMD5"></span>

### \$DECLARE 'KCMLStringMD5(buffer\$, hash\$)

#### Returns an MD5 hash for a buffer.

Uses Rivest's MD5 algorithm (see RFC1321) to generate a 128 bit hash of a document. It is mathematically very unlikely that two different strings will generate the same message digest. This is very much more secure than a traditional CRC checksum but computationally more expensive to derive.

**Returns:** a boolean, TRUE for success, FALSE for bad arguments

| Argument | Format | Purpose |
|----|----|----|
| buffer\$ | STR() | Buffer to be hashed. Trailing blanks clipped unless enclosed in STR() or FLD(). |
| hash\$ | RETURN DIM() | Returns the MD5 digest (must be 16 bytes or more) |


    REM $DECLARE 'KCMLStringMD5(buffer$, hash$)
    REM Returns an MD5 hash for a buffer.
    $DECLARE 'KCMLStringMD5(STR(), RETURN DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCMLStartExecTimer"></span>

### \$DECLARE 'KCMLStartExecTimer()

#### Start an execution timer

Starts a millisecond timer that counts the time spent executing code. The timer is suspended when waiting for mouse/keyboard input and when executing \$BREAK and \$IF statements.

**Returns:** Returns the ID of the new timer, zero for failure.


    REM $DECLARE 'KCMLStartExecTimer()
    REM Start an execution timer
    $DECLARE 'KCMLStartExecTimer() = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCMLStopExecTimer"></span>

### \$DECLARE 'KCMLStopExecTimer(timerId, pollTimer, tExec\$)

#### Returns the execution time.

Returns the number of milliseconds of execution time, in \$TIMESTAMP format, since the timer was started with 'KCMLStartExecTimer(). Time spent waiting on input is not counted. If pollTimer is FALSE the timer is stopped and the timer's ID is no longer valid.

**Returns:** a boolean, TRUE for success, FALSE for bad argumentents, or if the timer ID is not valid.

| Argument | Format | Purpose |
|----|----|----|
| timerId | INT() | The timer's identifier |
| pollTimer | INT() | If TRUE return the execution time but keep the timer running. |
| tExec\$ | RETURN DIM() | Execution time |


    REM $DECLARE 'KCMLStopExecTimer(timerId, pollTimer, tExec$)
    REM Returns the execution time.
    $DECLARE 'KCMLStopExecTimer(INT(), INT(), RETURN DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Socket_SetSSL"></span>

### \$DECLARE 'KCML_Socket_SetSSL(hSocket, bOpt)

#### Turn TLS/SSL on socket on or off

Turn TLS/SSL on existing socket on or off. Pass TRUE to switch on. Pass FALSE to switch off.

**Returns:** Returns zero for success or an error number on failure.

| Argument | Format | Purpose              |
|----------|--------|----------------------|
| hSocket  | INT()  | Socket handle        |
| bOpt     | INT()  | TRUE/FALSE On or Off |


    REM $DECLARE 'KCML_Socket_SetSSL(hSocket, bOpt)
    REM Turn TLS/SSL on socket on or off
    $DECLARE 'KCML_Socket_SetSSL(INT(), INT()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfStats_Start"></span>

### \$DECLARE 'KCML_PerfStats_Start(filename\$)

#### Start performance measuring

Start performance measuring. Measuring stops with a matching 'KCML_PerfStats_End. This function may only be called once within a session.

| Argument   | Format | Purpose                         |
|------------|--------|---------------------------------|
| filename\$ | STR()  | Name of HTML file to be created |


    REM $DECLARE 'KCML_PerfStats_Start(filename$)
    REM Start performance measuring
    $DECLARE 'KCML_PerfStats_Start(STR()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfStats_Comment"></span>

### \$DECLARE 'KCML_PerfStats_Comment(comment\$)

#### Add comment to performance stats

Comments are printed at the top of the performance stats report.

| Argument  | Format | Purpose         |
|-----------|--------|-----------------|
| comment\$ | STR()  | Text of comment |


    REM $DECLARE 'KCML_PerfStats_Comment(comment$)
    REM Add comment to performance stats
    $DECLARE 'KCML_PerfStats_Comment(STR()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfStats_IsRunning"></span>

### \$DECLARE 'KCML_PerfStats_IsRunning()

#### Is perfstats running?

Is perfstats running?

**Returns:** Returns TRUE if performance statistics are being gathered.


    REM $DECLARE 'KCML_PerfStats_IsRunning()
    REM Is perfstats running?
    $DECLARE 'KCML_PerfStats_IsRunning() = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfStats_End"></span>

### \$DECLARE 'KCML_PerfStats_End()

#### Stop performance measuring

Used to stop performance measuring started with 'KCML_PerfStats_Start.


    REM $DECLARE 'KCML_PerfStats_End()
    REM Stop performance measuring
    $DECLARE 'KCML_PerfStats_End() = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Session_SetTimeout"></span>

### \$DECLARE 'KCML_Session_SetTimeout(Set\$)

#### Sets a session timeout callback

Sets a session timout callback function to enable the application to react to inactive sessions or sessions where the client is no longer reachable.

| Argument | Format | Purpose                                            |
|----------|--------|----------------------------------------------------|
| Set\$    | DIM()  | String defined to record \_KCML_SESSION_SETTIMEOUT |


    REM $DECLARE 'KCML_Session_SetTimeout(Set$)
    REM Sets a session timeout callback
    $DECLARE 'KCML_Session_SetTimeout(DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Get_TermInfo"></span>

### \$DECLARE 'KCML_Get_TermInfo(sTermInfo\$)

#### Return information about the connected terminal

This function returns information about the capabilities of the connected terminal. See the help for \_KCML_TERMINFO for more information.

| Argument    | Format       | Purpose                                  |
|-------------|--------------|------------------------------------------|
| sTermInfo\$ | RETURN DIM() | String defined to record \_KCML_TERMINFO |


    REM $DECLARE 'KCML_Get_TermInfo(sTermInfo$)
    REM Return information about the connected terminal
    $DECLARE 'KCML_Get_TermInfo(RETURN DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Panic_Suppress"></span>

### \$DECLARE 'KCML_Panic_Suppress()

#### Hide return stack from PANIC

Code called after this routine is not recorded in PANIC files.


    REM $DECLARE 'KCML_Panic_Suppress()
    REM Hide return stack from PANIC
    $DECLARE 'KCML_Panic_Suppress() = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Lic_Acquire"></span>

### \$DECLARE 'KCML_Lic_Acquire(sLicSection\$, sLicKey\$, nLimit)

#### Consume an application license and store it in \$PSTAT

Counts the number of application licenses used in \$PSTAT and then verifies that against the maximum, nLimit. Application licences are counted in the same way as foreground KCML licences. If nLimit is zero, then the limit is taken from the license file. Upto eight different 4-byte keys can be stored in \$PSTAT. Requires an extended \$PSTAT to be configured.

| Argument | Format | Purpose |
|----|----|----|
| sLicSection\$ | STR() | License file section |
| sLicKey\$ | STR() | 4-byte license key name, must be unique |
| nLimit | INT() | Optional license limit, pass in zero to check against lic.txt |


    REM $DECLARE 'KCML_Lic_Acquire(sLicSection$, sLicKey$, nLimit)
    REM Consume an application license and store it in $PSTAT
    $DECLARE 'KCML_Lic_Acquire(STR(), STR(), INT()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Lic_Release"></span>

### \$DECLARE 'KCML_Lic_Release(sLicSection\$, sLicKey\$)

#### Release an application from \$PSTAT

Clears one of eight license keys in the shared memory for \$PSTAT

| Argument      | Format | Purpose                                 |
|---------------|--------|-----------------------------------------|
| sLicSection\$ | STR()  | License file section                    |
| sLicKey\$     | STR()  | 4-byte license key name, must be unique |


    REM $DECLARE 'KCML_Lic_Release(sLicSection$, sLicKey$)
    REM Release an application from $PSTAT
    $DECLARE 'KCML_Lic_Release(STR(), STR()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Lic_Count"></span>

### \$DECLARE 'KCML_Lic_Count(sLicSection\$, sLicKey\$)

#### Counts the number of application licenses in use

Counts the number of application licenses used in \$PSTAT. Application licences are counted in the same way as foreground KCML licences. Requires an extended \$PSTAT to be configured.

| Argument      | Format | Purpose                                 |
|---------------|--------|-----------------------------------------|
| sLicSection\$ | STR()  | License file section                    |
| sLicKey\$     | STR()  | 4-byte license key name, must be unique |


    REM $DECLARE 'KCML_Lic_Count(sLicSection$, sLicKey$)
    REM Counts the number of application licenses in use
    $DECLARE 'KCML_Lic_Count(STR(), STR()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Lic_GetApplications"></span>

### \$DECLARE 'KCML_Lic_GetApplications(nPartition, nSym)

#### Enumerates what application licenses a partition has acquired.

Returns a the number of application licences found and a string array of application license keys that have been acquired by the specified partition. Requires an extended \$PSTAT to be configured.

| Argument | Format | Purpose |
|----|----|----|
| nPartition | INT() | Partition number |
| nSym | INT() | SYM() of a string array which will be redimensioned to the number of application licenses found. |


    REM $DECLARE 'KCML_Lic_GetApplications(nPartition, nSym)
    REM Enumerates what application licenses a partition has acquired.
    $DECLARE 'KCML_Lic_GetApplications(INT(), INT()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Build_GetInfo"></span>

### \$DECLARE 'KCML_Build_GetInfo(sBuildInfo\$)

#### Returns build information about the KCML executable

This function returns build and version information about the KCML executable

| Argument     | Format       | Purpose                                   |
|--------------|--------------|-------------------------------------------|
| sBuildInfo\$ | RETURN DIM() | String defined to record \_KCML_BuildInfo |


    REM $DECLARE 'KCML_Build_GetInfo(sBuildInfo$)
    REM Returns build information about the KCML executable
    $DECLARE 'KCML_Build_GetInfo(RETURN DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_File_Stat"></span>

### \$DECLARE 'KCML_File_Stat(sFileName\$, pInfo\$)

#### Returns information about the given file

Fills the given structure with detailed information about the given file. Returns TRUE if successful or FALSE if it failed

| Argument    | Format       | Purpose                                          |
|-------------|--------------|--------------------------------------------------|
| sFileName\$ | STR()        | Name of the file                                 |
| pInfo\$     | RETURN DIM() | KCML_FILE_STAT record to receive the information |


    REM $DECLARE 'KCML_File_Stat(sFileName$, pInfo$)
    REM Returns information about the given file
    $DECLARE 'KCML_File_Stat(STR(), RETURN DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Uuid_FromString"></span>

### \$DECLARE 'KCML_Uuid_FromString(string\$, uuid\$)

#### Converts a string to a UUID.

Converts a string to a 16-byte hexadecimal UUID. String must be correctly formatted and can be optionally contained within { and }. Format of a UUID is XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX where X is any hexadecimal character.

**Returns:** a boolean, TRUE for success, FALSE for bad arguments

| Argument | Format       | Purpose                             |
|----------|--------------|-------------------------------------|
| string\$ | STR()        | UUID string in a printable format   |
| uuid\$   | RETURN DIM() | Returns the UUID (must be 16 bytes) |


    REM $DECLARE 'KCML_Uuid_FromString(string$, uuid$)
    REM Converts a string to a UUID.
    $DECLARE 'KCML_Uuid_FromString(STR(), RETURN DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Uuid_ToString"></span>

### \$DECLARE 'KCML_Uuid_ToString(uuid\$, string\$)

#### Converts a UUID to a printable string.

Converts a string to a 16-byte hexadecimal UUID. String must be correctly formatted and can be optionally contained within { and }. Format of a UUID is XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX where X is any hexadecimal character.

**Returns:** a boolean, TRUE for success, FALSE for bad arguments

| Argument | Format | Purpose |
|----|----|----|
| uuid\$ | STR() | 16-byte UUID |
| string\$ | RETURN DIM() | String representation of a UUID, must be at least 36 bytes |


    REM $DECLARE 'KCML_Uuid_ToString(uuid$, string$)
    REM Converts a UUID to a printable string.
    $DECLARE 'KCML_Uuid_ToString(STR(), RETURN DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_Uuid_Create"></span>

### \$DECLARE 'KCML_Uuid_Create(uuid\$)

#### Creates a 16-byte UUID.

Generates a new UUID

**Returns:** a boolean, TRUE for success, FALSE for bad arguments

| Argument | Format       | Purpose      |
|----------|--------------|--------------|
| uuid\$   | RETURN DIM() | 16 byte UUID |


    REM $DECLARE 'KCML_Uuid_Create(uuid$)
    REM Creates a 16-byte UUID.
    $DECLARE 'KCML_Uuid_Create(RETURN DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfMetric_Get"></span>

### \$DECLARE 'KCML_PerfMetric_Get(nSym, nPartition)

#### Returns a list of performance metrics.

Returns an array KCML_PerfMetricRec records that describe a performance metric. Requires an extended \$PSTAT to be configured.

**Returns:** Returns TRUE on success or FALSE if nPartition does not exist or \$PSTAT is not large enough.

| Argument | Format | Purpose |
|----|----|----|
| nSym | INT() | SYM() of a string array which will be redimensioned to the number of performance metrics. |
| nPartition | INT() | Partition number |


    REM $DECLARE 'KCML_PerfMetric_Get(nSym, nPartition)
    REM Returns a list of performance metrics.
    $DECLARE 'KCML_PerfMetric_Get(INT(), INT()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfMetric_Set"></span>

### \$DECLARE 'KCML_PerfMetric_Set(nMetric, nPartition)

#### Enable a performance metric.

Set the flag to enable the collection of the specified performance metric via kmsg.so. Requires an extended \$PSTAT to be configured.

**Returns:** Returns TRUE on success or FALSE if nMetric is not a valid KCML_PERFMETRICS value, nPart does not exist or \$PSTAT is not large enough.

| Argument   | Format | Purpose            |
|------------|--------|--------------------|
| nMetric    | INT()  | Performance metric |
| nPartition | INT()  | Partition number   |


    REM $DECLARE 'KCML_PerfMetric_Set(nMetric, nPartition)
    REM Enable a performance metric.
    $DECLARE 'KCML_PerfMetric_Set(INT(), INT()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfMetric_Clear"></span>

### \$DECLARE 'KCML_PerfMetric_Clear(nMetric, nPartition)

#### Stop a performance metric.

Clear the flag to stop the collection of the specified performance metric. Requires an extended \$PSTAT to be configured.

**Returns:** Returns TRUE on success or FALSE if nMetric is not a valid KCML_PERFMETRICS value, nPart does not exist or \$PSTAT is not large enough.

| Argument   | Format | Purpose            |
|------------|--------|--------------------|
| nMetric    | INT()  | Performance metric |
| nPartition | INT()  | Partition number   |


    REM $DECLARE 'KCML_PerfMetric_Clear(nMetric, nPartition)
    REM Stop a performance metric.
    $DECLARE 'KCML_PerfMetric_Clear(INT(), INT()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfMetric_Flush"></span>

### \$DECLARE 'KCML_PerfMetric_Flush(nMetric)

#### Flush the current value of a performance metric.

Reports the current value of this process's performance metric to the message queue. Only applicable to process-wide metrics such as \_KCML_PERFMETRIC_KCML_CPU_USAGE, \_KCML_PERFMETRIC_KCML_MEM_USED & \_KCML_PERFMETRIC_KCML_TOTAL_IO.

**Returns:** Returns TRUE if nMetric is one of the above and that metric was enabled.

| Argument | Format | Purpose            |
|----------|--------|--------------------|
| nMetric  | INT()  | Performance metric |


    REM $DECLARE 'KCML_PerfMetric_Flush(nMetric)
    REM Flush the current value of a performance metric.
    $DECLARE 'KCML_PerfMetric_Flush(INT()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfMetric_Send"></span>

### \$DECLARE 'KCML_PerfMetric_Send(Queue\$, Metric\$, StatList\$)

#### Send an application performance metric.

Send the list of performance metrics to a RabbitMQ server. If Queue\$ is blank, then the same queue as KCML's performance metrics is used. StatList\$ is a comma seperated list of key=value pairs.

**Returns:** Returns TRUE on success.

| Argument | Format | Purpose |
|----|----|----|
| Queue\$ | STR() | Queue name. |
| Metric\$ | STR() | Metric name. Names beginning with kcml are reserved for use by KCML. |
| StatList\$ | STR() | Comma separated list of key=value pairs. |


    REM $DECLARE 'KCML_PerfMetric_Send(Queue$, Metric$, StatList$)
    REM Send an application performance metric.
    $DECLARE 'KCML_PerfMetric_Send(STR(), STR(), STR()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_MessageQueue_IsEnabled"></span>

### \$DECLARE 'KCML_MessageQueue_IsEnabled(queue\$, error\$)

#### Check if a message queue has been enabled.

Returns TRUE if a message queue has been configured. If not FALSE is returned and an appropriate message is stored in error\$.

**Returns:** Returns TRUE on success.

| Argument | Format       | Purpose                              |
|----------|--------------|--------------------------------------|
| queue\$  | STR()        | Queue name.                          |
| error\$  | RETURN STR() | Buffer to receive any error message. |


    REM $DECLARE 'KCML_MessageQueue_IsEnabled(queue$, error$)
    REM Check if a message queue has been enabled.
    $DECLARE 'KCML_MessageQueue_IsEnabled(STR(), RETURN STR()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfTimer_Start"></span>

### \$DECLARE 'KCML_PerfTimer_Start()

#### Start a performance timer.

Start a performance timer and return its ID.

**Returns:** Returns the ID of the new timer, zero for failure.


    REM $DECLARE 'KCML_PerfTimer_Start()
    REM Start a performance timer.
    $DECLARE 'KCML_PerfTimer_Start() = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfTimer_Poll"></span>

### \$DECLARE 'KCML_PerfTimer_Poll(timerId, rTimes\$)

#### Poll a performance timer.

Returns duration of the timer the amount spent executing and the processor times in the rTimes\$ record.

**Returns:** Returns TRUE on success.

| Argument | Format       | Purpose                                        |
|----------|--------------|------------------------------------------------|
| timerId  | INT()        | Timer ID allocated by 'KCML_PerfTimer_Start(). |
| rTimes\$ | RETURN DIM() | Buffer to receive the result.                  |


    REM $DECLARE 'KCML_PerfTimer_Poll(timerId, rTimes$)
    REM Poll a performance timer.
    $DECLARE 'KCML_PerfTimer_Poll(INT(), RETURN DIM()) = "*"

This executes on the **server**.

\

------------------------------------------------------------------------

<span id="KCML_PerfTimer_Stop"></span>

### \$DECLARE 'KCML_PerfTimer_Stop(timerId, rTimes\$)

#### Stop a performance timer.

Returns duration of the timer the amount spent executing and the processor times in the rTimes\$ record. The timer is then destroyed.

**Returns:** Returns TRUE on success.

| Argument | Format       | Purpose                                        |
|----------|--------------|------------------------------------------------|
| timerId  | INT()        | Timer ID allocated by 'KCML_PerfTimer_Start(). |
| rTimes\$ | RETURN DIM() | Buffer to receive the result.                  |


    REM $DECLARE 'KCML_PerfTimer_Stop(timerId, rTimes$)
    REM Stop a performance timer.
    $DECLARE 'KCML_PerfTimer_Stop(INT(), RETURN DIM()) = "*"

This executes on the **server**.
