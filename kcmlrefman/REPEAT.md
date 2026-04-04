REPEAT ... UNTIL

------------------------------------------------------------------------

General Form:\
\
     REPEAT\
          ...\
    \
<img src="bitmaps/repeat.gif" data-align="BOTTOM" data-border="0" alt="repeat.gif" />\
\
Where:\
     <img src="bitmaps/repeat1.gif" data-align="BOTTOM" data-border="0" alt="repeat1.gif" />\
     <img src="bitmaps/repeat2.gif" data-align="BOTTOM" data-border="0" alt="repeat2.gif" />\
\

------------------------------------------------------------------------

The REPEAT statement is used in conjunction with the UNTIL statement to form repetitive loops. This type of loop is the same as a [WHILE](WHILE.htm) loop in that the conditional expression is evaluated every time round the loop but unlike [WHILE](WHILE.htm) this form of loop only checks the condition at the end and therefore guarantees at least one iteration.

Though the body of the loop may extend across many lines, each REPEAT must be paired with an UNTIL statement. This is checked when the program is resolved. The editor will indent the body of a loop automatically. Generally REPEAT loops can be indented to a depth of 20.

The return stack is not used at execution time and [LIST RETURN](LIST_RETURN.htm) does not call attention to these loops.

Jumping in and out of loops is permitted but is very poor programming practice. KCML provides the [BREAK](BREAK.htm) statement to abandon a loop prematurely and [CONTINUE](CONTINUE.htm) to skip the rest of the loop body and resume the loop at the next iteration (re-evaluating the condition).

Example:

REPEAT\
     IF (count == temp)\
          BREAK\
     END IF\
     IF (MOD(count,5) == 0)\
          CONTINUE\
     END IF\
     'Adjust(count)\
UNTIL count++ \< 100

See also:

[BREAK](BREAK.htm), [CONTINUE](CONTINUE.htm), [WHILE](WHILE.htm), [CONTINUE LOOP](CONTINUE_LOOP.htm)
