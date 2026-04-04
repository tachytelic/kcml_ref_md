## Autocompletion

Auto-completion is available for

|                             |
|-----------------------------|
| IF:END IF                   |
| WHILE:WEND                  |
| SELECT CASE:CASE:END SELECT |
| ERROR DO:END DO             |
| FOR x:NEXT x                |

For instance pressing RETURN after [IF](mk:@MSITStore:kcmlrefman.chm::/IFTHEN.htm), provided it is the only thing on the line, will cause the editor to add :ENDIF automatically and position the cursor after the IF to allow you to enter the conditional expression. Similarly to get completion of [WHILE](mk:@MSITStore:kcmlrefman.chm::/WHILE.htm):WEND just type W and RETURN. [SELECT CASE](mk:@MSITStore:kcmlrefman.chm::/SELECT_CASE.htm) and [ERROR DO](mk:@MSITStore:kcmlrefman.chm::/ERROR.htm) require at least one letter from each keyword e.g. S C or E D. In a more complicated case pressing RETURN after [FOR](mk:@MSITStore:kcmlrefman.chm::/FOR.htm) followed by a variable as the only thing on a line will add a :NEXT followed by the variable and reposition back to allow you to enter the condition.
