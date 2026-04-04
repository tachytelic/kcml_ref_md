Pointers

Introduction

Each **KCML** process has a symbol table containing references to variables, constants, line numbers and subroutine labels for the program currently held in memory. The [SYM(](SYM(.htm) function can be used to return the unique symbol index value as an integer of the specified variable or subroutine.

The integer can then be used to reference the variable or subroutine directly. This feature is particularly useful for writing generalised subroutines, as the programmer does not need to know what variable names are required by the subroutine, just the variable type. It is also useful when large variable or arrays need to be passed into a subroutine, as only the pointer to the variable or array needs to be passed, this saves memory and increases performance.

Using pointers to variables

The [SYM(](SYM(.htm) function allows the symbol of alpha, numeric, and field variables and arrays to be returned and used as a pointer. To obtain the symbol number of a variable, the variable name is specified within the parentheses following the [SYM(](SYM(.htm) function, for example:

alpha = SYM(abc\$)\
alpha_array = SYM(abc\$())

would return the symbol index of the variables *abc\$* and *abc\$()*.

To reference variables using the symbol number, the numeric variable containing the symbol number is specified after an asterisk within the parentheses following the [SYM(](SYM(.htm) function. The variable type is specified as normal, string variables require a \$ sign after the parentheses and array variables require parentheses, for example:

SYM(\*alpha)\$="Hello world!"\
SYM(\*alpha_array)\$()=ALL(HEX(FF))

would be used to change the contents of the variables *abc\$* and *abc\$()* from the previous example. Individual elements of array variables can also be referenced, e.g.

SYM(\*alpha_array)\$(10)="Nice day"

Numeric variables and arrays can be referenced in the same way, therefore:

numeric = SYM(abc)\
numeric_array = SYM(abc())

would store the symbol index values into the receiving variables, and

SYM(\*numeric) = total - discount\
SYM(\*numeric_array)() = ZER

would change the contents of the variables.

Field variables are referenced by placing a period before the [SYM(](SYM(.htm) function, for example:

numeric_field = SYM(.xyz)\
numeric_field_array = SYM(.xyz())

would place the symbol index values of the field variables into the receiving variables, and

.SYM(\*numeric_field)=(1,"######.##")\
.SYM(\*numeric_field_array)(1)=(40,"####.##")

would change the contents of the field variables.

The form of [SYM(](SYM(.htm) that allows the contents of variables to be modified can be used wherever the variable type is valid, for example the symbols returned by the previous examples could be used as follows:

SYM(\*alpha)\$="Hello world!"\
SYM(\*alpha_array)\$()=ALL(HEX(FF))\
PRINT SYM(\*alpha_array)\$(10)\
GOSUB 'sub1(SYM(numeric_field_array()))\
FLD(SYM(\*alpha)\$.SYM(\*numeric_field_array)(1))=100\
DATA LOAD BA T#1,(SYM(\*numeric))SYM(\*alpha_array)\$()

Using pointers to subroutines

The [SYM(](SYM(.htm) function can also be used to return the symbol index of a subroutine label. This allows the programmer to pass into a subroutine, for example a sort routine, the symbol index of a special routine that is to be called within the sort routine to compare items.

The [SYM(](SYM(.htm) function operates with subroutines in a similar way as is does with variables. When referencing the symbol index of a subroutine that returns a numeric value back to an expression, no additional information is required whereas a subroutine that returns a string value back to an alpha expression requires a dollar sign "\$" to immediately follow the parentheses. The optional parameter list that normally follows the subroutine label can be appended to the subroutine form of the [SYM(](SYM(.htm) function. For example:

numeric_sub=SYM('calculate_totals)\
alpha_sub=SYM('get_next_record\$)

would get the symbol index values for the two subroutines, and

GOSUB 'SYM(\*numeric_sub)(figures, discount)\
act_no = FLD('SYM(\*alpha_sub)\$(offset).account_no)

would reference the subroutines.

Miscellaneous

The symbol numbers themselves are allocated as each program is resolved. Therefore, depending on the number of previously [COM](COM.htm)ed variables, and the number of available global subroutines, etc. the symbol index of any one variable or subroutine may be different each time the program is executed.

The symbol number returned for a global variable will always be a negative integer, while the symbol number returned for all other variables and subroutines will always be a positive integer.

Note that if a global partition is deselected or if a different global partition is selected then the values of any pointers to global variables will be meaningless.

The [SYMNAME(](SYMNAME(.htm) function may be used to return the variable or subroutine name corresponding to the specified symbol index. E.g.

PRINT SYMNAME(alpha)\
var_name\$=SYMNAME(test)

See also:

[SYM(](SYM(.htm), [SYMNAME(](SYMNAME(.htm)
