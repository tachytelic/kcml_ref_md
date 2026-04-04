\$MSG function

General Forms:\
\
1.      \$MSG = alpha_expression\
\
2.      alpha_variable = \$MSG\
\

------------------------------------------------------------------------

The \$MSG function is used to set a global system message which can be up to 80 bytes. The \$MSG function is legal anywhere an alpha variable is legal, including the left-hand side of an assignment statement.

The current value of \$MSG can be displayed, in a message box, on a KClient or WDW terminal using the **broadcast signal** via kservadm, [bkstat](bkstat.htm#table3) or the [WebServer](mk:@MSITStore:kwebserv.chm::/kcmlproc.htm).

Syntax examples:

STR(\$MSG,20,1) = new_message\$\
IF (\$MSG == system\$(2))

See also:

[bkstat](bkstat.htm), [WebServer](mk:@MSITStore:kwebserv.chm::/adminfns.htm).
