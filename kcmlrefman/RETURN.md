RETURN

------------------------------------------------------------------------

General Form:\
\
     RETURN \[expr\]\
\
Where:\
     expr           = alpha or numeric expression\
\

------------------------------------------------------------------------

The RETURN statement is used to mark the end of a subroutine and to return program flow to the statement immediately following the most recent [GOSUB](GOSUB.htm) or [GOSUB'](GOSUBquote.htm) statement. RETURN can also be used to return alphanumeric values if the routine was called from within an alphanumeric expression (See [GOSUB'](GOSUBquote.htm)). The RETURN statement also terminates any open [FOR ... NEXT](FOR.htm) loops within the subroutine, and removes their entries from the RETURN stack. Any non-unique locally defined variables defined with either the [DEFSUB'](DEFSUB.htm) or [LOCAL DIM](LOCAL_DIM.htm) are also removed.

If RETURN is used to return a value back to an expression, the type of value returned must match the type of subroutine. E.g.

search\$ = 'Next_rec\$(stream)\
Total = 'Calculate(bal())\
     .           .           .\
DEFSUB 'Next_rec\$()\
     .           .           .\
RETURN Record\$\
DEFSUB 'Calculate(array())\
     .           .           .\
RETURN total_of_balances

If a RETURN statement is encountered in a routine called by a function key, RETURN returns control to immediate mode if the function key was pressed in immediate mode, or control is returned to the interrupted [LINPUT](LINPUT.htm) statement. If a [LINPUT](LINPUT.htm) statement is interrupted, RETURN returns control to the statement following the [LINPUT](LINPUT.htm) statement.

RETURN can also be used as a keyword prefixing arguments in [\$DECLARE]($DECLARE.htm#RETURN%20in%20$DECLARE) calls and object method calls.

'KCMLCORBACreate("myObject","Add",RETURN myhandle)\
worksheet.Range("A9").Value(RETURN t)\
worksheet.Range("A9").Value(RETURN NUM(t))\
worksheet.Range("A10:D11").Value(RETURN t())\

See also:

[DEFSUB'](DEFSUB.htm), [DEFFN'](DEFFNquote.htm), [GOSUB](GOSUB.htm), [GOSUB'](GOSUBquote.htm), [CONTINUE RETURN](CONTINUE_RETURN.htm)
