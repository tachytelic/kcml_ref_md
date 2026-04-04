The SELECT CASE statement

Introduction

The [SELECT CASE](SELECT_CASE.htm) statement is an efficient and easy to read alternative to complex cascaded IF ... THEN ... [ELSE](ELSE.htm) statements. Conditional expressions specified by the SELECT CASE statement are evaluated and an attempt is made to match them against any number of conditions or expressions specified by CASE clauses. If a match is found then a series of statements can then be executed. If no match is found and the optional CASE ELSE statement exists then the statements following the CASE ELSE are executed otherwise normal program execution will resume after the END SELECT statement. SELECT CASE statements can span over any number of program lines. [LIST](LIST.htm) will automatically indent the body of the SELECT CASE statement.

It is recommended that conditions or expressions specified after the CASE clauses that are most likely to match the SELECT CASE condition or expression are placed at or near to the beginning of the statement, especially if the statement spans over many program lines.

Structure of the SELECT CASE statement

The statement is divided up as follows:

SELECT CASE expr or condition

The result of the expression or condition is tested for a match against all the expressions and conditions specified by the CASE clauses. The expression or condition can be alpha or numeric.

CASE expr or condition \[ ,expr or condition\] ...

Any number of CASE clauses can be specified after the SELECT CASE statement. Each CASE clause can have any number of tests each separated by commas. The type of expression or condition, either alpha or numeric, should match the type used by the expression or condition specified by the SELECT CASE statement otherwise an X74 error will result. If a match is found then statements following the CASE clause up to the next CASE clause, or the CASE ELSE statement, or the END SELECT statement are executed.

CASE ELSE

If no matches are found after testing the result against each CASE clause then the statements following the CASE ELSE up to the next CASE or END SELECT are executed. Any CASE clauses entered after the CASE ELSE will be ignored.

END SELECT

This statement signifies the end of the SELECT CASE statement.

Numeric SELECT CASE example

The following program example reads in a number from the [DATA](DATA.htm) statement on the last line and passes it into the SELECT CASE statement. The first two values read are 1 and 2 therefore the first two times that the SELECT CASE statement is executed the statements on in the first CASE clause are executed, the [CONTINUE](CONTINUE.htm) statement is used to jump to the end of the WHILE ... WEND loop and read in the next value. Each iteration of the WHILE ... WEND loop will read in a new value, the value is then tested against each expression in each CASE clause. The last value read in (99) does not match any of the values in the CASE clauses so the statements after the CASE ELSE will be executed. Note that in the example actual values have been specified after each CASE clause, numeric variables and expressions could also be used.

REM example of numeric CASE WHILE TRUE DO READ test_number SELECT CASE test_number CASE 1,2 REM this will catch 1 and 2 PRINT "test_number is either 1 or 2" CONTINUE CASE 3 REM this will catch 3 only PRINT "test_number is now 3" CONTINUE CASE 4,5,6,7,8,9,10 REM this will catch 4 - 10 PRINT "test_number is now either 4,5,6,7,8,9,10" CONTINUE CASE ELSE PRINT "Number out of range" BREAK REM Next case statement will never get executed CASE 98,97,96,95 REM Rubbish END SELECT REM we only execute this code if case does not match PRINT "test_number not found in CASE" WEND DATA 1,2,3,4,5,6,7,8,9,10,99 test_number is either 1 or 2 test_number is either 1 or 2 test_number is now 3 test_number is now either 4,5,6,7,8,9,10 test_number is now either 4,5,6,7,8,9,10 test_number is now either 4,5,6,7,8,9,10 test_number is now either 4,5,6,7,8,9,10 test_number is now either 4,5,6,7,8,9,10 test_number is now either 4,5,6,7,8,9,10 test_number is now either 4,5,6,7,8,9,10 Number out of range

Alpha SELECT CASE example

The following example is basically the same as the previous example, one item of data is read for each iteration of the WHILE ... WEND loop. Note that expressions or a mixture of expressions can be used as is the case with the third and fourth CASE clauses.

REM example of string CASE astring\$ = "XXXXSteveXXXX" WHILE TRUE DO READ test_string\$ PRINT """";test_string\$;"""", SELECT CASE test_string\$ CASE "END" BREAK CASE "Peter","Bill" REM this will catch Peter and Bill PRINT "test_string\$ is now either Peter or Bill" CONTINUE CASE STR(test_string\$,5,5) REM this will catch Steve PRINT "test_string\$ is now Steve" CONTINUE CASE "Alan","Graham","Dave","Fred",STR(astring\$,4,5) REM this will catch Alan, Fred and Dave PRINT "test_string\$ is now Alan, Fred or Dave" CONTINUE END SELECT REM we only execute this code if case does not match PRINT "test_string\$ not found in CASE" WEND DATA "Bill","Steve","Alan","Fred","Dave","Peter","Rob","END" "Bill" test_string\$ is now either Peter or Bill "Steve" test_string\$ is now to Steve "Alan" test_string\$ is now either Alan, Fred or Dave "Graham" test_string\$ is now either Alan, Fred or Dave "Dave" test_string\$ is now either Alan, Fred or Dave "Peter" test_string\$ is now either Peter or Bill "Rob" test_string\$ not found in CASE "END"

Conditional SELECT CASE example

In the following example each CASE clause is tested to see if the result of the condition is true, if it is then the statements following the CASE clause are executed. The [TRUE](TRUE.htm) keyword on the SELECT CASE statement could be replaced with any combination of expressions and conditions, similar to the expressions and conditions that can be specified in IF ... THEN, [WHILE](WHILE.htm), or UNTIL statements. If the result of the conditions is [TRUE](TRUE.htm) then only the statements after the first true CASE clause would be executed.

REM example of logical CASE value_one = 1 value_three = 3 FOR loop_value = -2 TO 2 PRINT "(";loop_value;")", SELECT CASE TRUE CASE loop_value\<0 REM this will catch \< 0 PRINT "loop_value is \< 0" CASE loop_value==0 REM this will catch = 0 PRINT "loop_value is = 0" CASE loop_value\>0 REM this will catch \> 0 PRINT "loop_value is \> 0" END SELECT NEXT loop_value (-2 ) loop_value is \< 0 (-1 ) loop_value is \< 0 ( 0 ) loop_value is = 0 ( 1 ) loop_value is \> 0 ( 2 ) loop_value is \> 0
