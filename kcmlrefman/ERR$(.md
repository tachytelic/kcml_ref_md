ERR\$(

------------------------------------------------------------------------

General Form:\

ERR\$(error_code)

\
Where:

error_code = integer expression between 0 and 99

------------------------------------------------------------------------

The ERR\$( alphanumeric function is used to return a descriptive error message corresponding to the specified error code. This function is valid anywhere a string expression is legal though using it more than once in the same statement will give unexpected results.

The text of these messages are held in the text file *berror.d* which must be in a directory in the current path (conventionally it is in the kcml directory). The text of the messages may be altered in accordance with instructions that are to be found at the start of that file. Note that KCML often has more than one message for a given error code in order to be more specific about the nature of the problem. The ERR\$( function always returns the first entry in the file for the given code.

Prior to KCML 6.0 the function [\$ERR]($ERR.htm) was implemented as ERR\$(ERR). It now returns the last error message.

Syntax examples:

err_txt\$ = ERR\$(ERR)\
text\$ = ERR\$(97)

See also:

[ERR](ERR.htm), [\$ERR]($ERR.htm), [\$OSERR]($OSERR.htm), [ERROR](ERROR.htm)
