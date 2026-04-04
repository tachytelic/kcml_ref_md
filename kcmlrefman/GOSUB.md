GOSUB

------------------------------------------------------------------------

General Form:\
\
     GOSUB line_number\
\

------------------------------------------------------------------------

The GOSUB statement is used to execute a subroutine that begins at the specified line number. The subroutine is terminated with a [RETURN](RETURN.htm) statement.

Each time a subroutine is entered an entry is made into the [RETURN](RETURN.htm) stack. The stack entry is only removed when a [RETURN](RETURN.htm) statement is executed. All [RETURN](RETURN.htm) stack entries are removed when a [CLEAR](CLEAR.htm), [RETURN CLEAR](RETURN_CLEAR.htm) or a [LOAD](LOAD.htm) statement is executed. Jumping out of subroutines without executing a [RETURN](RETURN.htm) statement may eventually result in an A04 stack overflow error.

The [GOSUB 'label](GOSUBquote.htm) statement is to be preferred as it makes programs more readable.

Syntax examples:

GOSUB 1049\
IF act_1 \<\> test_1 THEN GOSUB 2020

See also:

[ON ... GOSUB](ONGOSUB.htm), [RETURN](RETURN.htm), [RETURN CLEAR](RETURN_CLEAR.htm), [GOSUB'](GOSUBquote.htm)

 
