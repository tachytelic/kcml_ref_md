TRY and CATCH

<div class="Generalform">

General Form:\
\

<div class="indent">

TRY\
...\
\[CATCH ERR integer_expression \[, integer_expression ...\]\]\
...\
\[CATCH\]\
...\
END TRY

</div>

\
Where:\
\

<div class="indent">

integer_expression = any numeric expression reducing to an integer between 1 and 99

</div>

\

</div>

------------------------------------------------------------------------

The TRY/CATCH structured error handling statements allow centralized handling of run-time errors in the block of KCML code between the TRY and the first CATCH statement. There can be as many statements as necessary inside this block. There must be at least one CATCH ERR or CATCH statement between the TRY and the END TRY. A CATCH statement is either for a particular error code with an ERR clause specifying the particular error to be caught or it is a final CATCH statement which will handle any sort of error. There can be multiple CATCH ERR clauses but there can be only one final CATCH clause and, if present, it must be the last clause before the END TRY. Again each CATCH clause can have as many statements as are necessary to handle the applicable error.

TRY blocks can be nested. If an error cannot be handled in the executing block then KCML will search for an outer block and attempt to handle the error there. An error will also be promoted if it occurs during the execution of a CATCH clause. TRY blocks with a final CATCH clause will only invoke an outer handler if an error occurs in the statements within that clause.

TRY blocks can contain subroutine calls to any depth and errors in such routines will be handled unless the routines define their own handlers as TRY blocks can also nest in subroutines or WHILE/REPEAT loops provided all of the block is inside the loop or function.


    DEFSUB 'DoSums(a, b)
        LOCAL DIM r
        TRY
            r = 'divide(a, b)
        CATCH
            REM this will catch any other problem
            'log_error(ERR)
            r = 0
        END TRY
        RETURN r
    END SUB

    DEFSUB 'divide(quotient, divisor)
        REM this handles obvious problems locally
        LOCAL DIM dividend
        TRY
            dividend = quotient/divisor
        CATCH ERR 62
            REM division by zero results in infinity
            dividend = 9E99
        CATCH ERR 63
            REM however zero divided by zero is 0
            dividend = 0
        END TRY
        RETURN dividend
    END SUB

[THROW](THROW.htm) can be used to force a runtime error in KCML, commonly to rethrow an error caught in an inner TRY block so that a handler in an outer block can process it.

The error expressions referenced in a CATCH ERR are evaluated at resolve time following the same rules as expressions in DIM statements. They must reduce to either an integer between 1 and 99 inclusive, representing a regular KCML error code, or an integer between 1000 and 9999 representing a user defined error from a THROW. IF there is more than one expression on a CATCH ERR then the associated clause will be invoked if any of the expressions corresponds to the error that terminated the TRY block. Unlike the ERROR statement, all errors are considered recoverable. The special [KCML constant](TutorialConstants.htm) [\_KCML_USER_ERROR](tmp/UserErrHelp.htm)can be used for programmer defined errors thrown with a THROW statement.

If an error occurs in a program (or is explicitly thrown with THROW ERR) and there is no CATCH or CATCH ERR handler to catch it then a runtime error will occur which will either PANIC the program or force a development user into the KCML workbench.

When developing in the workbench if a runtime error occurs in a TRY block that could be caught by an outer CATCH outside the current subroutine then the error will be actioned by the workbench and execution will stop in the debugger at the point of the error. However if execution is resumed with CONTINUE or STEP then it will restart inside the CATCH. This gives the programmer a chance to see why and where the error occurred before switching to a completely different location. Errors produced by THROW are not treated this way and will be caught by an outer handler in the usual way.

Compatibility

TRY/CATCH/THROW was introduced in KCML 6.20 as a subset of a more general error handling mechanism that will debut with KCML 7. The TRY/CATCH statement is only allowed at [\$COMPLIANCE]($COMPLIANCE.htm) level 1 and above. Previous error handling mechanisms such as [ON ERROR](ON_ERROR.htm) and [ERROR DO](ERROR.htm) are now deprecated and are not allowed at \$COMPLIANCE level 3 and above.

See also:

[THROW](THROW.htm), [ON ERROR](ON_ERROR.htm), [SELECT ERROR](SELECT_ERROR.htm), [ERR](ERR.htm), [ERROR](ERROR.htm), [ERR\$(](ERR$(.htm)
