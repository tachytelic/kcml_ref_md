THROW

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

THROW ERR \[integer_expression\]

</div>

\
Where:\

<div class="indent">

integer_expression = an optional numeric expression

</div>

\

</div>

------------------------------------------------------------------------

THROW can be used to force a runtime error in KCML. Generally this will be done in the context of a [TRY/CATCH](TRY.htm) block which can catch the error and handle it. Another common requirement is to rethrow an error caught in an inner TRY block so that a handler in an outer block can process it.


    TRY
        ...
    CATCH
        errcode = ERR
        IF (errcode == 82)
            REM handle here
            ...
        ELSE
            REM handle in some outer handler
            THROW ERR errcode
        END IF
    END IF

The error number thrown must be either a KCML error between 1 and 99 inclusive or a user error between 1000 and 9999 inclusive. If no error code is supplied then the current error will be rethrown, including any minor error code information, provided the statement is executed in a CATCH block. All errors thrown with THROW ERR are considered as recoverable and can be caught in an outer TRY block. The special [KCML constant](TutorialConstants.htm) [\_KCML_USER_ERROR](tmp/UserErrHelp.htm)can be used for programmer defined errors.

If an error is thrown with THROW ERR and there is no CATCH or CATCH ERR handler to catch it then a runtime error will occur which will either PANIC the program or force a development user into the KCML workbench.

Compatibility

THROW ERR was introduced in KCML 6.20 as part of the TRY/CATCH structured error facility. It is a subset of a more general error handling mechanism that will debut with KCML 7. The TRY/CATCH statement is only allowed at [\$COMPLIANCE]($COMPLIANCE.htm) level 2 and above.

Example:

THROW ERR \_KCML_USER_ERROR

See also:

[TRY](TRY.htm), [THROW](THROW.htm), [ON ERROR](ON_ERROR.htm), [SELECT ERROR](SELECT_ERROR.htm), [DO group](DO.htm), [ERR](ERR.htm), [ERROR](ERROR.htm), [ERR\$(](ERR$(.htm)
