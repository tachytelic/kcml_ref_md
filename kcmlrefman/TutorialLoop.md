Loop constructs

Introduction

There are three different loop constructs available to the **KCML** programmer. As well as the simple [FOR ... NEXT](FOR.htm) loop construct found in most BASIC style languages, **KCML** also has [REPEAT ... UNTIL](REPEAT.htm) and [WHILE ... WEND](WHILE.htm) loop constructs. Also the [BREAK](BREAK.htm) and [CONTINUE](CONTINUE.htm) statements can be used to exit a loop prematurely and skip the remaining body respectively.

FOR ... NEXT loops

The [FOR](FOR.htm) statement is used in conjunction with the NEXT statement to form iterated loops. FOR ... NEXT loops can be used to count in ascending or descending order, also the rate that the count increases or decreases may be changed. Each [FOR](FOR.htm) statement must have a corresponding NEXT statement, both specifying the same index variable. If no STEP clause is specified then the index variable is incremented by one and is tested against the expression following the TO clause, if the index variable is less than or equal to the expression following the TO clause, the loop will then restart with the new value. For example:

FOR count=1 TO 10 PRINT count; NEXT count

would display the numbers 1 - 10. By specifying a STEP of 2 then only the odd numbers 1 - 9 would be displayed. To reverse the counting order a negative STEP is specified and the first and second expression are reversed thus:

FOR count=10 TO 1 STEP -1 PRINT count; NEXT count

would display the numbers 1 - 10 in reverse order.

Jumping into a FOR ... NEXT loop would generate an error at the corresponding NEXT statement if the loop has not already been executed at least once. Jumping out of a [FOR](FOR.htm) loop is allowed but should be avoided as it is bad programming practice. Terminating loops prematurely by branching out with [GOTO](GOTO.htm) or [GOSUB](GOSUB.htm) statements can cause stack overflow errors. If a program has to jump out of a loop then the reference variable should be set to the value specified by the expression immediately after the TO clause and the corresponding NEXT statement should be executed. Alternatively the [BREAK](BREAK.htm) statement could be used to exit the loop cleanly and continue with the statement immediately after the corresponding NEXT statement without changing the index variable, or the [CONTINUE](CONTINUE.htm) statement could be used to skip the remaining body of the loop and continue with the next iteration. For example:

FOR count = 1 TO 10 IF count == 5 THEN CONTINUE PRINT count IF count == 7 THEN BREAK NEXT count

would display the numbers 1, 2, 3, 4, 6 and 7.

If a FOR ... NEXT loop is halted with a [STOP](STOP.htm) or [TRAP](TRAP.htm) statement or by pressing the [HALT](TextTermHalt.htm) key, the current contents of the return stack can be displayed with the [LIST RETURN](LIST_RETURN.htm) statement. The [CONTINUE NEXT](CONTINUE_NEXT.htm) command can be used to restart the program and stop it again immediately before the last iteration which would complete the current FOR ... NEXT loop.

The [RETURN CLEAR](RETURN_CLEAR.htm) statement can be used to clear the return stack entry of the most recently executed subroutine call, along with any FOR ... NEXT information. Alternatively the [RETURN CLEAR](RETURN_CLEAR.htm) followed by the ALL clause will clear all subroutine and FOR ... NEXT information from the RETURN stack.

See also:

[BREAK](BREAK.htm), [FOR](FOR.htm), [CONTINUE](CONTINUE.htm), [CONTINUE NEXT](CONTINUE_NEXT.htm), [RETURN CLEAR](RETURN_CLEAR.htm)

REPEAT ... UNTIL loops and WHILE ... WEND loops

[REPEAT](REPEAT.htm) and [WHILE](WHILE.htm) loops perform the same function but in a different order. The expression can be expressed in the same fashion as with the IF ... THEN statement. A mixture of alpha and numeric conditions can be separated with the [OR](OR.htm) and [AND](AND.htm) logical operators, for example:

WHILE xpos \< xt OR ypos \< yt AND tmp\$ \<\> " " DO

is valid, the same condition could be used with the REPEAT ... UNTIL loop construct.

Both loop constructs evaluate the expression every time around the loop. The WHILE ... WEND loop evaluates the expression before the loop is started and therefore if the expression is false then the loop will not be executed and program execution would continue with the statement immediately after the corresponding WEND statement. The REPEAT ... UNTIL loop evaluates the expression at the end of the loop therefore guarantees at least one iteration. For example:

count = 0 REPEAT PRINT count count = count + 10 UNTIL count == 100

would display the numbers 0 to 90 in steps of 10. The same result could be obtained with the WHILE ... WEND loop thus

count = 0 WHILE count\<\>100 DO PRINT count count = count + 10 WEND

would also display the numbers 0 to 90 in steps of 10.

Though both constructs can extend across many lines each [REPEAT](REPEAT.htm) must be matched with the UNTIL statement, and each [WHILE](WHILE.htm) must be matched with the WEND statement. This is checked during the resolution process. The maximum number of nested loops may vary from machine to machine, though most machines allow up to 20. The [LIST](LIST.htm) statement will automatically indent the body of the loop.

Jumping in and out of loops again is permitted but is poor programming practice. Like FOR ... NEXT loops the variable could be set to meet the condition specified by the [WHILE](WHILE.htm) or UNTIL statement. Alternatively the [BREAK](BREAK.htm) statement could be used to abandon the loop completely or the [CONTINUE](CONTINUE.htm) statement could be used to skip the rest of the loop body, for example:

WHILE count\<\>tmp DO GOSUB 'update KEYIN char\$ IF char\$==exit_key\$ THEN BREAK GOSUB 'write_screen WEND . .

would keep looping until the variable *count* is equal to the variable *tmp*, unless the key pressed during the [KEYIN](KEYIN.htm) statement matches the contents of the variable *exit_key\$*.

It is also possible to write loops that execute forever by having a condition that is always true, and when the loop needs to be aborted the [BREAK](BREAK.htm) statement can be executed, e.g.

WHILE TRUE DO GOSUB 'get_next_record IF FLD(rec\$.accno\$)==search\$ THEN BREAK WEND

The same routine could be coded with a REPEAT ... UNTIL loop construct, although a normal expression that should never be met must be specified, thus,

REPEAT GOSUB 'get_next_record IF FLD(rec\$.accno\$)==search\$ THEN BREAK UNTIL junk_var = 1E30

See also:

[BREAK](BREAK.htm), [CONTINUE](CONTINUE.htm), [CONTINUE LOOP](CONTINUE_LOOP.htm), [REPEAT ... UNTIL](REPEAT.htm), [WHILE ... WEND](WHILE.htm)
