BREAK

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\
     BREAK\
\

</div>

------------------------------------------------------------------------

The BREAK statement provides an early exit from [FOR ... NEXT](FOR.htm) , [WHILE ... WEND](WHILE.htm) . or [REPEAT ... UNTIL](REPEAT.htm) loops. The BREAK must actually fall within the body of the loop and cannot be inside a subroutine called from within the loop. The pairing of BREAK with the [FOR](FOR.htm), [WHILE](WHILE.htm) or [REPEAT](REPEAT.htm) statements is checked at resolve time.

Example:

WHILE new_loop\<10 DO\
     IF (++new_loop = 5)\
          BREAK\
     END IF\
     'Update()\
WEND

See also:

[CONTINUE](CONTINUE.htm), [FOR ... TO](FOR.htm), [REPEAT ... UNTIL](REPEAT.htm), [WHILE ... WEND](WHILE.htm)
