## Collapse mode

Collapse mode provides a simplified display of the program currently being viewed. Collapse mode works in both edit and debug modes however, any attempt to execute or modify the current program will cause KCML to revert back to normal mode.

When the Collapse Mode key (CTRL-I) is pressed the contents of any

[DO ... ENDDO](mk:@MSITStore:kcmlrefman.chm::/DO.htm),\
[SELECT CASE](mk:@MSITStore:kcmlrefman.chm::/SELECT_CASE.htm),\
[FOR ... NEXT](mk:@MSITStore:kcmlrefman.chm::/FOR.htm),\
[WHILE ... WEND](mk:@MSITStore:kcmlrefman.chm::/WHILE.htm),\
[REPEAT ... UNTIL](mk:@MSITStore:kcmlrefman.chm::/REPEAT.htm)\

constructs are collapsed down to three periods. Pressing the toggle again restores the original text. The collapse level depends on where the cursor was when the Collapse Mode key was pressed. For example:

<span style="color: Blue;">WHILE count\<10 DO <span style="color: Red;">PRINT count IF count=5 THEN DO</span> <span style="color: Blue;">GOSUB'test1() CONTINUE</span> <span style="color: Red;">END DO GOSUB'test2()</span> WEND</span>

Pressing the Collapse Mode key with the cursor on any of the second level statements (shown above in red) would result in the following:

WHILE count\<10 DO PRINT count IF count=5 THEN DO ... ENDDO GOSUB'test2() WEND

Pressing the Collapse Mode key a second time restores the program back to it's original form. If the Collapse key was pressed on any of the first level statements (shown in blue in the first example) would result in the following:

WHILE count\<10 DO ... WEND

When displaying collapsed text the title of the editor window is changed to Editor:COLLAPSE
