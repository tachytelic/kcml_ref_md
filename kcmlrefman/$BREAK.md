\$BREAK

------------------------------------------------------------------------

General Form:

<img src="bitmaps/breakd.gif" data-align="BOTTOM" data-border="0" alt="$BREAK" />

Where:

delay = numeric expression

------------------------------------------------------------------------

The \$BREAK statement is used to put the current partition to \`sleep' for a specified length of time. The length of time that \$BREAK will sleep for is specified by the integer portion of the expression. In the default case \$BREAK N will sleep for approximately 20N milliseconds, if no expression is specified then a default value of one is used. If zero or blank is specified then no break will occur.

KCML can also accumulate \$BREAK units until they reach a threshold before delaying. This threshold is specified as a non-zero binary digit in byte 36 of [\$OPTIONS]($OPTIONS.htm#BYTE36). If this byte is non-zero then the number of \$BREAK units requested is accumulated but no delay is taken unless the accumulated value from previous \$BREAKs exceeds the threshold when the delay will be the threshold value divided by 50, in seconds. If the threshold is non-zero but less than HEX(19) then \$BREAK will never delay. Delaying at the threshold is most useful with the implied \$BREAK 1 that is performed automatically by KCML in polling [KEYINs](KEYIN.htm) and [\$IF ON]($IF_ON.htm) statements. These statements can otherwise waste CPU time if included in tight loops. The drawback of this strategy is that the occasional long delays can give a jerky response.

If the delay time is negative then KCML will delay for that number of seconds. For example:

\$BREAK -5

will delay for 5 seconds.

After a \$BREAK OFF, all simple \$BREAKs are then ignored. This simulates a Wang 2200 with one user. \$BREAK ON restores the default. \$BREAK OFF can be used in an initial conversion from a 2200 to see if performance would be improved by re-coding \$BREAKs.

The \$BREAK ! form will give an infinite delay that can only be broken by interrupting the program with Ctrl+BREAK (if enabled) or by receiving a [\$ALERT]($ALERT.htm) or [\$ALARM]($ALARM.htm) signal. This is the preferred way of terminating execution in a shared text partition. KCML will set byte 29 of the [\$PSTAT]($PSTAT.htm) for a partition sleeping on a \$BREAK ! to HEX(FB).

Special cases

If executed in a shared text partition (using the -g switch to KCML) where the [DEFFN @PART](DEFFN_@PART.htm) specifies that a memory mapped file is to be used, then \$BREAK! will terminate the program writing the contents of the shared memory to the file.

If executed in a [COM server](comserver.htm) program, that is a program that was started via a COM object interface, then \$BREAK! will block permanently while COM waits for and processes method requests. When COM detects that the object is no longer needed the the \$BREAK! will be exited and the program will resume at the next statement so that tidy up code can be executed and a \$END performed.

If executed in a [CORBA server](corbaserver.htm) program, that is a program that has performed a 'KCMLOBJECTExport() [\$DECLARE]($DECLARE.htm) call, then \$BREAK! will block permanently while CORBA requests are processed. As CORBA servers do not terminate, the next statement will only be reached if there is a fatal error.

If executed in a [SOAP server](soapserver.htm) program, that is a program that has performed a 'KCMLOBJECTExport() [\$DECLARE]($DECLARE.htm) call, then \$BREAK! will block permanently while SOAP requests are processed. As SOAP servers do not terminate, the next statement will only be reached if there is a fatal error.

Syntax examples:

\$BREAK\
\$BREAK 250\
\$BREAK 25\*length\
\$BREAK -(60\*extra)\
\$BREAK !\
\$BREAK ON\
\$BREAK OFF

Compatibility notes:

Under Windows and many modern versions of Unix (e.g. IBM AIX, Unix 5.4, HP-UX, Solaris) short sleeps are possible subject to the granularity of the system clock which is often 50, 60 or 100Hz. For these implementations **KCML** will make an absolute delay of the number of 20 milliseconds units requested, rounded up to the next clock tick.

On older versions of Unix timing is done with a one second timer which expires every absolute second of real time. This means that if **KCML** asks for a one second sleep it will get on average a half second delay depending on when in the cycle it started. On these implementations **KCML** will delay for the requested number of units, divided by 50, as seconds. \$BREAK will not delay if the requested number of units is less than 25.

With all Unix implementations delays can also be longer than requested if the machine is heavily loaded and there are still other higher priority processes in the run queue when the sleep expires.

See also:

[\$OPTIONS]($OPTIONS.htm),\
[DEFFN @PART](DEFFN_@PART.htm),\
[\$ALERT]($ALERT.htm),\
[\$ALARM]($ALARM.htm)\
