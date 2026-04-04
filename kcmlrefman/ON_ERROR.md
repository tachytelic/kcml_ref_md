ON ERROR

------------------------------------------------------------------------

<div class="Generalform">

General Form:\

<div class="indent">

ON ERROR alpha_receiver1, alpha_receiver2 GOTO line_number

</div>

\
Where:\

<div class="indent">

|  |  |  |
|----|----|----|
| alpha_receiver1 | = | used to return the error code. |
| alpha_receiver2 | = | used to return the number of the line which contains the erroneous statement. |

</div>

</div>

------------------------------------------------------------------------

The ON ERROR statement is used to capture recoverable errors. In general these are errors with numbers greater or equal to C60 though many errors below that (e.g. P48 or P37) are also recoverable. Non-recoverable errors always report an error and stop the program. Computational errors C60 to C69 can be suppressed entirely by using [SELECT ERROR](SELECT_ERROR.htm).

Once an error is detected by the ON ERROR statement the error code and line number are stored in respective variables and program execution then continues at the specified line.

Compatibility

Modern programs should use the structured [TRY/CATCH](TRY.htm) mechanism introduced with KCML 6.20. Structured error handling takes precedence over the ERROR and ON ERROR statements. The ON ERROR statement is not allowed at [\$COMPLIANCE]($COMPLIANCE.htm) level 3 and above.

Syntax examples:

ON ERROR error_no\$, line_no\$ GOTO 10000

See also:

[TRY](TRY.htm), [THROW](THROW.htm), [ERR](ERR.htm), [ERROR](ERROR.htm), [ERR\$(](ERR$(.htm)
