SELECT ON ALARM GOSUB

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/selectonalarm.gif" data-align="BOTTOM" data-border="0" alt="selectonalarm.gif" />\
Where:\
\
     label           = integer or a symbolic name\
\

------------------------------------------------------------------------

The SELECT ON ALARM GOSUB statement is used to trap any timeout errors given by the [\$ALARM]($ALARM.htm) statement. When a timeout error (I92) is detected, the subroutine specified after the [GOSUB](GOSUB.htm) statement is executed. Upon return execution continues with the statement following the previously timed out statement.

Syntax examples:

SELECT ON ALARM GOSUB 9010\
SELECT ON ALARM GOSUB 'alarm_trap\
SELECT ON ALARM GOSUB 'test, LIST "/tmp/fred"

See also:

[\$ALARM]($ALARM.htm), [ON ... SELECT](ONSELECT.htm)

 
