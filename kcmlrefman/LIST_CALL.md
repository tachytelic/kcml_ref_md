LIST CALL

------------------------------------------------------------------------

General Form:\
\
     \[@\]LIST \[title\] CALL \[\*\] \[callname\]\
\
Where:\
\
     callname      = is a user-written C routine\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST CALL statement finds all references to given [CALLs](CALL.htm) in a program. If no callname is specified then all [CALL](CALL.htm) references are listed. If the optional @ sign precedes the reserved word LIST, then the listing will be taken from the currently selected global partition, if any.

If an asterisk immediately follows the CALL then all statements containing the [CALL](CALL.htm) will be LISTed in full. Leading colons (:) are inserted to show the exact position of the [CALL](CALL.htm) statement within the line, for example:

LIST CALL \* KI_CLOSE\
KI_CLOSE - 00010 CALL KI_CLOSE handle TO ki_status\
            - 00900 ::CALL KI_CLOSE f_hndl TO ret

Without the asterisk the output would be as follows:

LIST CALL KI_CLOSE\
KI_CLOSE - 00010 00900

The output from the LIST CALL command can be redirected to a printer or to any Unix/DOS device or file with the [SELECT LIST](SELECT_LIST.htm) command.

Syntax examples:

LIST CALL\
@LIST CALL \*\
LIST CALL \* GETDATE\
@LIST CALL NEWSUB

See also:

[CALL](CALL.htm), [SELECT LIST](SELECT_LIST.htm), LIST U

 
