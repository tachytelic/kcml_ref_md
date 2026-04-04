END

------------------------------------------------------------------------

General Form:\
\
     END\
\

------------------------------------------------------------------------

The END statement is used to indicate that the end of the current program has been reached. When the END statement is executed the END PROGRAM message is displayed. Executing the [CONTINUE](CONTINUE_command.htm) command after an END is not allowed. This statement should only be used while developing and debugging code, it should not be included in applications software as users will not want to be presented with the development environment.

The reserved word END can also be used as part of a conditional statement to test whether the end of the file was reached on a previous [READ \#](READhash.htm). Refer to the [IF ... THEN](IFTHEN.htm) statement for more information.

See also:

[\$END]($END.htm), [STOP](STOP.htm)

 
