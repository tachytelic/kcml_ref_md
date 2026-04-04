SELECT CASE

------------------------------------------------------------------------

General Form:\
\
     SELECT CASE expr\
     CASE expr1\[\[,expr1a\], ...\]\
          statements ...\
     CASE expr2\[\[,expr2a\], ...\]\
          statements ...\
     <img src="bitmaps/selectcase.gif" data-align="BOTTOM" data-border="0" alt="selectcase.gif" />\
     END SELECT\
\

------------------------------------------------------------------------

The SELECT CASE statement specifies an expression which is then subsequently compared against a series of sub-expressions specified by CASE clauses until a match occurs. When a match occurs the statements following the CASE clause are executed until the next CASE or CASE ELSE clause is reached, then execution is transfered to the statement after the END SELECT. The optional CASE ELSE clause always matches and therefore should be the last CASE clause before the END SELECT. There is no limit to the number of statements in each case and they may extend accross multiple lines. Directly executing a CASE or CASE ELSE transfers control to the statement after the END SELECT.

The SELECT CASE expression and the CASE expressions can be numeric or string expressions but they must agree in type, i.e. if the SELECT CASE expression is a numeric then all the CASE expressions must be numeric. Type checking is done at execution time. Boolean expressions are treated as numeric expressions with [TRUE](TRUE.htm) having a value of 1 and [FALSE](FALSE.htm) having a value of zero.

A CASE statement may have more than one expression separated by commas. Each will be checked against the SELECT CASE expression in turn until a match occurs, e.g.

SELECT CASE test\
CASE 1\
     'OK()\
CASE 2,3\
     'NotOK()\
END SELECT

The CASE ELSE clause is optional but if present will terminate the statement so any following CASE clauses will be ignored at execution time.
