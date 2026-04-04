WHILE ... WEND

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/while.gif" data-align="BOTTOM" data-border="0" alt="while.gif" />\
          ....\
     WEND\
\
Where:\
     <img src="bitmaps/while1.gif" data-align="BOTTOM" data-border="0" alt="while1.gif" />\
     <img src="bitmaps/while2.gif" data-align="BOTTOM" data-border="0" alt="while2.gif" />\

------------------------------------------------------------------------

The WHILE statement is used in conjunction with the WEND statement to form repetitive loops. The the body of the loop may extend across many lines, each WHILE must be paired with a WEND. Pairing is checked when the program is resolved. [LIST](LIST.htm) will indent the body of a loop automatically. WHILE loops may be indented to a depth of a least 20. The return stack is not used at execution time, therefore [LIST RETURN](LIST_RETURN.htm) does not call attention to these loops.

Jumping in and out of loops is permitted but is very poor programming practice. KCML provides the [BREAK](BREAK.htm) statement to abandon a loop prematurely and [CONTINUE](CONTINUE.htm) to skip the rest of the loop body and resume the loop at the next iteration (re-evaluating the condition) e.g.

WHILE a \< 100 DO\
     IF (++a = b)\
          BREAK\
     END IF\
     IF (MOD(a,5)==0)\
          CONTINUE\
     END IF\
     'Calculate()\
WEND

It is possible to write loops that execute forever by having a condition that is always true e.g.

WHILE TRUE DO\
     'Read_keyboard\
     IF (char\$ == exit_key\$)\
          BREAK\
     END IF\
     'UpdateForm()\
WEND

Syntax examples:

WHILE NOT END DO\
WHILE x\<9 OR P\<\>6 AND Y\<\>100 DO\
WHILE 'counter\<\>45 AND a9\$="FN" DO

See also:

[BREAK](BREAK.htm), [CONTINUE](CONTINUE.htm), [REPEAT](REPEAT.htm), [CONTINUE LOOP](CONTINUE_LOOP.htm)
