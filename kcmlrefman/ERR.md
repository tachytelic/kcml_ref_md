ERR

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

ERR

</div>

\

</div>

------------------------------------------------------------------------

The ERR function returns an error code representing the most recent error condition. ERR is valid wherever a numeric expression is legal.

Generally it will be a two digit code corresponding to the last KCML runtime recoverable error but [THROW ERR](THROW.htm) can be used to signal a user error with a code in the range 1000 to 9999 that can be caught in a [TRY/CATCH](TRY.htm) block and interrogated using this function.

Once a run-time error has been detected, ERR is set to the appropriate error code. After ERR is referenced it is set to zero, therefore subsequent references will return zero. Consequently you will generally want to copy it into a local variable as in


    TRY
        'OpenSomeFile()
    CATCH
        errcode = ERR
        IF (errcode == 82 OR errcode == 83)
            ...
        END IF
    END TRY 

Syntax examples:

result = ERR\
IF (ERR == 82)\
...\
END IF

See also:

[TRY](TRY.htm), [THROW](THROW.htm), [ERR\$(](ERR$(.htm), [\$OSERR]($OSERR.htm), [ERROR](ERROR.htm)
