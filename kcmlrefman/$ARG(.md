\$ARG() function

General Form:

\$ARG(param_num)

Where:

Param_num is a numeric expression\

------------------------------------------------------------------------

The \$ARG() function can be used to return the command line parameters passed to KCML when it was started. The argument paseed to the function is the ordinal of the parameter to be returned counted from zero thus in the example below \$ARG(0) is the program START and \$ARG(1) is the parameter string "DIR=/user1/pjc". The switches (parameters starting with a minus sign) before the first parameter are absorbed by KCML and are not included. See the [kcml utility](kcml.htm) reference for a list of legal command line switches. KCML will interpret the first parameter \$ARG(0) as a program to run initially. The other parameters are not examined by KCML and are left for the user to examine using this function.

kcml -g START 'DIR=/user1/pjc'

\$ARG() is valid wherever an alpha function is valid. Negative parameter numbers and numbers greater than the number supplied will return a blank string.

Syntax examples:

start_prog\$ = \$ARG(0)
