COM

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

COM com-element \[,com-element\] ...

</div>

\
\
Where:

<div class="indent">

<img src="bitmaps/com.gif" data-align="BOTTOM" data-border="0" alt="com.gif" />

|  |  |
|----|----|
| array_name | = an alpha or numeric array variable |
| dim1, dim2 | = positive integer expressions specifying new dimensions. |
| length | = positive integer expression specifying maximum length of each alpha array element. Defaults to 16. |

</div>

</div>

------------------------------------------------------------------------

The COM statement is similar to the [DIM](DIM.htm) statement in that it is used to define variables within a KCML program. Variables defined with a COM statement are maintained when a new program is loaded into memory or when the current program is executed, unlike non-common variables (defined with the [DIM](DIM.htm) statement) which are cleared when a new program is loaded. Common variables can be very useful for passing data between multiple program loads.

Common variables can be defined after non-common variables. If common variables are to be used in a number of programs, then COM only needs to be executed by the first program, although if the same common variables are defined again in a later program, an error will not occur unless the dimensions differ from the previous. Variables defined by COM will only be cleared from memory on execution of a [CLEAR](CLEAR.htm), [CLEAR V](CLEAR.htm), or a [LOAD RUN](LOAD_RUN.htm) command.

Converting common variables to non-common variables

Common variables can be converted to non-common variables with the [COM CLEAR](COM_CLEAR.htm) statement. Executing [COM CLEAR](COM_CLEAR.htm) followed by a common variable will convert all variables defined after and including the specified variable to non-common variables.

Specifying the length of alphanumeric variables and array dimensions

The dimensions of arrays and the lengths of alphanumeric variables or array elements are specified either by positive numbers, or a numeric expression. Numeric functions, such as [INT(](INT(.htm), [MAX(](MAX(.htm), [MIN(](MINfn.htm), [SGN(](SGN(.htm) etc. are valid within the numeric expression, although any variables used within the numeric expression must have previously been COMed prior to the current program being [LOADed](LOAD.htm).

Changing the size of a variable or the dimensions of an array

Array dimensions may be changed explicitly during execution of the following statements by specifying the new dimensions, enclosed in parentheses following the array name:

|                          |                            |                        |
|--------------------------|----------------------------|------------------------|
| [MAT CON](MAT_CON.htm)   | [MAT IDN](MAT_IDN.htm)     | [MAT ZER](MAT_ZER.htm) |
| [MAT READ](MAT_READ.htm) | [MAT REDIM](MAT_REDIM.htm) |                        |

If an array or string is [COMed](COM.htm) with a size of zero, then no space is allocated during the resolve phase. Space can be allocated later when the size is known with any of the statements listed above. If the array is used before the space has been allocated then an error will result.

Initialising variables with the COM statement

Alpha and numeric scalar variables can be initialised at resolve time by specifying an expression after an equals sign. Numeric variables can be initialised using any numeric expression that can be evaluated at resolve time, although any variables used within the numeric must have previously been COMed prior to the current program being LOADed.

COM test=100, news=10\*first\
COM beta=INT(abc/2)

Alpha variables can only be initialised with the HEX( function or a literal string. The variable is then sized to match the number of characters in the literal or HEX( function. To reserve more space than the specified literal a numeric expression can be used to specify the required size.

COM Test\$ = "ABCDE"\
COM Letter\$1000 = HEX(FFFE FDFC)

Field variables can also be defined and initialised with the COM function, for example:

COM .Name\$=(1,35), Number=(35,"####")

Use of COM in KCML libraries

In KCM 6.01 and later, if a variable is defined as COM in a library, it will be copied to the foreground and added to the foreground common chain when the library is loaded with [LIBRARY ADD](MODULE.htm). These copies are unaffected if the library is unloaded at a later time.

Miscellaneous

If byte 38 of [\$OPTIONS]($OPTIONS.htm#BYTE38) is set to [HEX(01)](HEX(.htm), then [DIMing](DIM.htm) of all variables including numeric and field variables becomes mandatory. A resolve time error will result for any undimmed variable. This is an aid to debugging as it reduces the chance of a misspelled variable. In the case of [DEFSUB](DEFSUB.htm), the parameters specified do not need to be [DIMed](DIM.htm) elsewhere as they are local. ([DIMed](DIM.htm) means a variable declared with [DIM](DIM.htm), COM, or [LOCAL DIM](LOCAL_DIM.htm).)

By default KCML always displays variables and subroutine labels in lowercase. However, setting the HEX(01) bit of byte 40 of [\$OPTIONS LIST]($OPTIONS_LIST.htm#BYTE40) instructs the editor to preserve the case of variables and sub-routine labels.

Compatibility:

Prior to KCML 6.10 the dimensions of an array and the maximum length of a string array element were all limited to 65535. From 6.10 onwards this restriction is lifted and available memory becomes the only limitation.

Example:

First Program:

COM rows=20, columns=40\
LOAD "PROGRAM"\

Second Program:

COM table\$(rows+1,columns+1)20\
.      .\
.      .

The second program would define the variable table\$() as common with dimensions of 2, 4 and each element would be 20 bytes long.

Syntax examples:

COM sample(12,4), test(8), number_of_records, .name\$\
COM fred\$(from(1)\*2, from(2)\*2)length, .total\$=(start, "-#####.##")\
COM abc\$(20),files\$(100)10,as(9,2)\
COM old\$(new)new2, was\$(1),is(2), files(act)\
COM abc=50, zyx=INT(90/def), newl\$(50)16

See also:

[COM CLEAR](COM_CLEAR.htm), [DIM](DIM.htm), [DIM(](DIM(.htm), [LIST DIM](LIST_DIM.htm), [\$OPTIONS]($OPTIONS.htm)
