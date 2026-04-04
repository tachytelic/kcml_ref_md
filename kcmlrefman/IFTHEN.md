IF ... THEN

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/if.gif" data-align="BOTTOM" data-border="0" alt="IF general form" />\
Where:\
     <img src="bitmaps/if1.gif" data-align="BOTTOM" data-border="0" alt="if1.gif" />\
     <img src="bitmaps/if2.gif" data-align="BOTTOM" data-border="0" alt="if2.gif" />\
     statement      =      any simple KCML statement except DATA or image (%).\
\

------------------------------------------------------------------------

The IF ... THEN statement is used to execute the specified statement or [DO group](DO.htm) if the overall result of all conditions is true.

Note that the statement following THEN must be either a DO group or a simple statement and should not be a complex multiline statement like IF ... THEN DO, IF ... ENDIF, WHILE ... WEND, REPEAT ... UNTIL or FOR ... NEXT. If you use a complex statement then the body of the statement will always be executed even if the condition is false as KCML will just skip to the next colon or end of line. Use the structured IF ... ENDIF for these situations.

This statement is available for compatibility reasons with other languages. The structured [IF ... END IF](IFENDIF.htm) statement is generally recommended instead of the IF ... THEN statement.
