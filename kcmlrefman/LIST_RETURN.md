LIST RETURN

------------------------------------------------------------------------

General Form:

LIST \[title\] \[LOCAL\] RETURN

Where:

title = alpha_variable or a literal string

------------------------------------------------------------------------

The LIST RETURN statement lists information about the currently executing program. Information includes the currently executing line and statement, the last 10 programs loaded, the list of modules loaded, the name of the currently selected global partition, if any, and the contents of the return stack.

The return stack can also be displayed within the KCML workbench by selecting the LIST RETURN menu option.

If the reserved word LOCAL precedes the RETURN, then the output from the [LIST LOCAL](LIST_LOCAL.htm) statement will be inserted after any calls to a subroutine defined with the [DEFSUB'](DEFSUB.htm) statement. Also at the end of the stack listing any normal variables matching the local variables listed are listed with their sizes and contents.

See also:

[LIST LOCAL](LIST_LOCAL.htm), [\$PROG]($PROG.htm)
