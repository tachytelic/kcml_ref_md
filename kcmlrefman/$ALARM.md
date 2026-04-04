\$ALARM

------------------------------------------------------------------------

General Form:

<div class="indent">

\$ALARM numeric_expression

</div>

------------------------------------------------------------------------

The \$ALARM statement is used to set an alarm timer running which will expire after the number of seconds specified by the numeric expression unless cancelled by another \$ALARM 0. When the alarm goes off, provided the program is blocked waiting for an external event, it interrupts the blocked instruction which fails with an I92 error. This error can be trapped for a specific statement with an [ERROR](ERROR.htm) clause or for the whole program with a [SELECT ON ALARM](SELECT_ON_ALARM.htm) statement. This function provides a simple method of interrupting a blocked I/O statement.


    REPEAT
        $ALARM 60
        KEYIN key_input$
        ERROR DO
            PRINT AT(23,0,);TIME;
            CONTINUE
        END DO
        $ALARM 0
    UNTIL key_input$ ="Q"

In the above example the time is printed on line 23 every minute until a key is pressed. This is a much more efficient construction than a simple looping [KEYIN](KEYIN.htm). Note that this example is only really relevant to text based applications. Forms applications should use the Idle() event to achieve the same result.

Syntax examples:

\$ALARM 60\*10\
\$ALARM sometime

Compatibility notes:

This statement has no effect on Windows versions of KCML prior to KCML 6.0.

See also:

[SELECT ON ALARM](SELECT_ON_ALARM.htm)
