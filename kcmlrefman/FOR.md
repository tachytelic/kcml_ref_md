FOR ... TO ... NEXT

------------------------------------------------------------------------

General Form:\
\
     FOR index_variable = expression_1 TO expression_2 \[STEP expression_3\]\
     ...\
     NEXT index_variable\
\

------------------------------------------------------------------------

The FOR ... TO statement is used in conjunction with the NEXT statement to form repetitive loops. Each FOR ... TO statement must be paired with a NEXT statement. Both statements must use the same reference variable.

When the FOR ... TO statement is first executed the reference variable is set to the value of the first expression. Program execution then continues until the corresponding NEXT statement is executed. If no STEP parameter is added then the reference variable is incremented by one and is tested against the second expression, if its value is less than or equal to the second expression, the loop will then restart with the new value. The reference variable will continue to be incremented until it is greater than the expression, then program execution continues with the statement following the NEXT statement. The statements contained in the loop will always be executed at least once even if the value of the reference variable exceeds the second expression.

The optional STEP parameter can be incorporated to change the step with which the reference variable is incremented. If a negative step is used then the reference variable will be decremented by the given step each time the loop is re-executed.

Example:

FOR Count1 = 10 TO 1 STEP -1\
     FOR Count2 = 1 to 100\
          CONVERT INT(RND(1)\*1000) TO Abc\$,(####)\
          .KCMLGrid1.MoveCell(Count2, Count1)\
          .KCMLGrid1.Cell.Text\$ = Abc\$\
     NEXT Count2, Count1

Jumping into a FOR ... TO loop will cause an error at the corresponding NEXT statement if the loop has not already been executed at least once.

Jumping out of a FOR ... TO loop is allowed but should be avoided as it is bad programming practice. Terminating loops incorrectly can cause stack overflow errors. If a program has to jump out of a loop then a [BREAK](BREAK.htm) statement should be used to abandon the loop entirely or the [CONTINUE](CONTINUE.htm) statement may be used skip the remaining body of the loop. E.g.

FOR Count = pos1 TO pos2\
     CONVERT Count to Text\$,(####)\
     .static1.Text\$ = Text\$\
     IF count\>50 AND count\<80 THEN CONTINUE\
     IF count\>100 THEN BREAK\
     'Update_Record()\
NEXT Count

In the above example the subroutine 'update_record would only be executed if the variable count is less than 50 or greater than 80, if the variable count is greater than 100 then the loop is abandoned, leaving the variable count unchanged.

FOR loops are automatically indented by the KCML editor provided that when the program is resolved each FOR ... TO statement has a corresponding NEXT

Syntax examples:

FOR Loop = 1 TO last_record\
FOR Count = last TO first STEP -5\
FOR Loop2 = first_5 TO last_5 STEP 0.5

See also:

[BREAK](BREAK.htm), [CONTINUE](CONTINUE.htm), [RETURN CLEAR](RETURN_CLEAR.htm)

 
