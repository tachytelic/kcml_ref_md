\$PROG function

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

\$PROG\
\

</div>

</div>

------------------------------------------------------------------------

The \$PROG function is used to return the name of the last program [LOADed](LOAD.htm). The \$PROG function is valid wherever an alpha function is valid. The \$PROG statement is set to blank after a [CLEAR](CLEAR.htm) is executed.

The value of \$PROG is also displayed as part of the [LIST RETURN](LIST_RETURN.htm) output.

The \$PROG function is most useful when used in conjunction with the [RESAVE](RESAVE.htm) command.

Syntax examples:

RESAVE \$PROG 1000\
program\$(count) = \$PROG & comp_no\$\
mod\$ = STR(\$PROG,1,2)
