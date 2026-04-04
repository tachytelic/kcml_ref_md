SELECT ON ALERT

------------------------------------------------------------------------

General Form:\
     <img src="bitmaps/selectonalert.gif" data-align="BOTTOM" data-border="0" alt="selectonalert.gif" /> \
\

------------------------------------------------------------------------

The ON/OFF ALERT select parameter may be used to enable or disable the current ALERT interrupt handler. If a [GOSUB](GOSUB.htm) statement is added after the ON ALERT parameter, the program will branch if an ALERT is received. Execution of the SELECT OFF ALERT statement disables the ALERT interrupt handler.

The SELECT ON ALERT statement is only processed at resolve time, therefore only the first SELECT ON ALERT statement is acted upon.

Syntax examples:

SELECT ON ALERT GOSUB 9000\
ON test SELECT OFF ALERT, SELECT PRINT /005

Compatibility notes:

To allow a process to receive an ALERT signal, the effective user id (UID) of both foreground and global processes must be the same. This may cause problems on versions of Unix that prevent users from having the same effective UID number, i.e. SCO Unix and Unix 5.4 machines such as the IBM RS6000 and the ICL DRS6000. This can be done by setting the SUID bit on the KCML file, usually /usr/lib/kcml/kcml. Refer to your Unix documentation for more information.

See also:

[\$ALERT]($ALERT.htm), [ON ... SELECT](ONSELECT.htm)

 
