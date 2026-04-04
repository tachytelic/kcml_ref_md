SELECT ERROR

------------------------------------------------------------------------

General Form:\
\
     SELECT ERROR \>error_code\
\
Where:\
\
     error_code           = a computational error 60-69.\
\

------------------------------------------------------------------------

The ERROR select parameter is used to suppress system error messages caused by computational errors.

Normally, when a computational error occurs the system displays the appropriate error message. If a computational error is detected after a SELECT ERROR statement, the error message is suppressed and the receiver variable is set to the default value.

| Error Code | Error Condition | Value Returned |
|----|----|----|
| 60 | Underflow | 0 |
| 61 | Overflow | \+ 9.999999999999E99 |
| 62 | Division by zero | \+ 9.999999999999E99 |
| 63 | Zero / or ^ zero | 0 |
| 64 | Zero raised to negative power | \+ 9.999999999999E99 |
| 65 | Negative number raised to non-integer power | ABS(A) ^ B |
| 66 | Square root of negative value | SQR(ABS(A)) |
| 67 | Log of zero | \- 9.999999999999E99 |
| 68 | Log of negative value | LOG(ABS(A)) |
| 69 | Argument too large | 0 |

Default SELECT ERROR values

The value of SELECT ERROR is reset to the default upon execution of a [CLEAR](CLEAR.htm), [LOAD RUN](LOAD_RUN.htm) command, or by entering SELECT ERROR \>60.

Syntax examples:

SELECT ERROR \> 65\
SELECT ERROR \> error_code, PRINT /005

See also:

[ERROR](ERROR.htm), [ON ... SELECT](ONSELECT.htm)
