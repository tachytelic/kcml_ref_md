LOCAL DIM

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

LOCAL DIM dim_element \[,dim_element\] ...

</div>

\
Where:\
<img src="bitmaps/localdim.gif" data-align="BOTTOM" data-border="0" alt="LOCAL DIM" />\

<div class="indent">

|  |  |  |
|----|----|----|
| diml, dim2 | = | dimensions (numeric expressions) |
| length | = | numeric expression. If no length is specified then the default is 16. |

</div>

</div>

------------------------------------------------------------------------

The LOCAL DIM statement is used to define local variables within the scope of a subroutine defined with the [DEFSUB'](DEFSUB.htm) statement. Like [DIM](DIM.htm) and [COM](COM.htm), string and numeric scalar variables can be initialized by specifying an expression after an equals sign, for example

LOCAL DIM Value = 10\
LOCAL DIM AlphaValue\$ = "Hello!"

Note that the syntax only supports the initialization of numerics and basic strings. Arrays and field variables cannot be initialized in this way.

Variables defined with LOCAL DIM can be resized with the [MAT REDIM](MAT_REDIM.htm) statement and with the [REDIM](LET.htm#redim) qualifier in an assignment. Scalar string variables have their space allocation deferred until they are used in order to avoid unnecessary initialization if that first reference is a REDIM asignment as in the 'tagit() example below. The space requested there is an explicit zero to make it clear to the reader that the variable may not be used without REDIMing

Examples:


    DEFSUB 'new(number, size, data$())
       LOCAL DIM record$(number)size
        ... 
       RETURN size$
    END SUB

    DEFSUB 'tagit(tag$)
       LOCAL DIM x$0
       REDIM x$ = "<" & tag$ & ">"
       RETURN x$
    END SUB

See also:

[DEFSUB'](DEFSUB.htm)\
[REDIM](LET.htm#redim)
