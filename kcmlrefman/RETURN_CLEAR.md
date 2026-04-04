RETURN CLEAR

------------------------------------------------------------------------

General Form:

RETURN CLEAR \[ALL\]

------------------------------------------------------------------------

The RETURN CLEAR statement clears the return stack entry of the most recently executed subroutine call. Any [FOR ... NEXT](FOR.htm) information from the subroutine is also cleared. Once the stack information is cleared program flow continues with the statement immediately following the RETURN CLEAR statement.

RETURN CLEAR followed by the ALL parameter will clear all subroutine, local variable and [FOR ... NEXT](FOR.htm) information from the return stack.

In KCML 4.0 it was permitted to use RETURN CLEAR to exit from a function that returns a value used in an arithmetic expression, e.g. a = 2 + 'sub()

However doing this would leave data on KCML's internal arithmetic stack and if done enough times in a loop the stack would eventually overflow, so starting with KCML 5.0 KCML will detect this and error the RETURN CLEAR with a P41.6 error. The previous KCML 4 behaviour can be restored by setting the [COMPAT40](EnvVars.htm#COMPAT40) environment variable or setting byte 38 of [\$OPTIONS RUN]($OPTIONS_RUN.htm).

Syntax examples:

RETURN CLEAR\
RETURN CLEAR ALL

See also:

[FOR ... NEXT](FOR.htm), [GOSUB](GOSUB.htm), [GOSUB'](GOSUBquote.htm), [RETURN](RETURN.htm)
