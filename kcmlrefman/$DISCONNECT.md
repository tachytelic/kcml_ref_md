\$DISCONNECT

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/disconnectd.gif" data-align="BOTTOM" data-border="0" alt="disconnectd.gif" />\
\

------------------------------------------------------------------------

The \$DISCONNECT statement is used to define special handling for the HANGUP signal that is sent to a KCML process when its controlling terminal is disconnected. This may be due to the line dropping on a modem connection, the terminal being turned off or a network link being broken. Previous versions of KCML ignored this signal and waited for the connection to be restored as this was the behaviour of a BASIC-2 terminal. It was possible however, by setting the environment variable HANGUP, to make KCML terminate tidily when it next read from the keyboard. As network connections would never be restored when broken this was the recommended procedure for connections through telnet over TCP/IP.

The HANGUP environment variable still functions as before but now, if KCML executed \$DISCONNECT ON, then it will receive a [\$ALERT]($ALERT.htm) signal instead of the hangup if disconnected. This can be fielded with a [SELECT ON ALERT GOSUB](SELECT_ON_ALERT.htm) statement which can call a subroutine to tidy up and [\$END]($END.htm). If there is no [SELECT ON ALERT GOSUB](SELECT_ON_ALERT.htm) in the program then the hangup will be effectively ignored. \$DISCONNECT OFF will restore the original hangup behaviour.

The optional timeout clause is currently ignored.

 
