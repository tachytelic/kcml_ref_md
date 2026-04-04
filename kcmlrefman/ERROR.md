ERROR

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
<img src="bitmaps/error.gif" data-align="BOTTOM" data-border="0" alt="ERROR general form" />\
Where:\

<div class="indent">

statement = any KCML statement

</div>

\

</div>

------------------------------------------------------------------------

The ERROR statement provides a means of handling recoverable program execution errors, by suppressing the normal error response and passing control to the program.

When an error is detected in a statement that is immediately followed by an ERROR statement, the normal error response is suppressed, and program execution continues with the statement immediately following the ERROR statement. All of the statements on the line after the ERROR statement are executed if an error occurred. If no error occurred then execution continues with the next line of the program, unless the ERROR statement is followed by a [DO group](DO.htm), then execution continues with the statement following the [DO group](DO.htm).

The ERROR statement can only be used to detect a recoverable error which (generally) has a code of 48 or is within the range of 65 to 99. The recovery status of an error (RECOVerable or FATAL) may be found in the file berror.d. Errors which have been suppressed with the [SELECT ERROR](SELECT_ERROR.htm) statement will not be detected with the ERROR statement.

Compatibility

Modern programs should use the structured [TRY/CATCH](TRY.htm) mechanism introduced with KCML 6.20. Structured error handling takes precedence over the ERROR and ON ERROR statements. The ERROR statement is not allowed at [\$COMPLIANCE]($COMPLIANCE.htm) level 3 and above.

Example:

LOAD program\$: ERROR DO\
     action = junk\
     'DisplayError()\
ENDDO

See also:

[TRY](TRY.htm), [THROW](THROW.htm), [ON ERROR](ON_ERROR.htm), [SELECT ERROR](SELECT_ERROR.htm), [DO group](DO.htm), [ERR](ERR.htm), [ERROR](ERROR.htm), [ERR\$(](ERR$(.htm)
