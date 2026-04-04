WRITE LOG

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

WRITE LOG \[level,\] message

</div>

Where:\
\

<div class="indent">

|  |  |  |
|----|----|----|
| level | = | An integer ranging from 0 to 2 |
| message | = | An alpha expression containing the information to be written to the log |

</div>

</div>

------------------------------------------------------------------------

This statement is used to write messages into the system log (syslog) file if operating under UNIX or the application event log if operating under NT.

Messages are written into the log using three different levels. These are:

| KCML constant     | Level | Purpose             | Unix level code |
|-------------------|-------|---------------------|-----------------|
| \_LOG_INFORMATION | 0x00  | Information message | LOG_INFO        |
| \_LOG_WARNING     | 0x01  | Warning message     | LOG_WARNING     |
| \_LOG_ERROR       | 0x02  | Error message       | LOG_ERR         |

If no warning level is specified then a level of 0 (Information) is assumed.

Byte 52 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE52) sets a threshold that can be used to filter out specific warning levels, for example setting this byte to HEX(02) would mean that only WRITE LOG statements that specify a level of 2 will be executed. Setting it to HEX(FF) will disable logging. The default is HEX(00) to allow all WRITE LOG events.

On Unix systems it may be necessary to [configure the syslog daemon](syslog.htm) to accept messages. For KCML 6+ WRITE LOG uses the facility code LOG_LOCAL1 while KCML 5.02 uses the LOG_USER facility code.

On Windows 95 and Windows 98, where there is no operating system log, these log messages can be written to a nominated text file by setting a registry entry using **kservadm**. There are two values under the following key

HKEY_LOCAL_MACHINE\Software\Kerridge\EventLogging

The STRING value **LogFile** defines the filename and the DWORD value **Enabled** is a boolean flag turning logging on (0x01) or off (0x00). This key is ignored on NT.

Syntax examples:

WRITE LOG \_LOG_WARNING, Message\$\
WRITE LOG Information\$

See also:

[CLOSE](CLOSEhash.htm), [SEEK](SEEKhash.htm), [READ](READhash.htm), [OPEN](OPENhash.htm), [\$OPTIONS \#]($OPTIONShash.htm)
