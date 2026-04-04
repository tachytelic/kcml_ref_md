DIM

<div class="Generalform">

General Form:

> \[PRIVATE\|PUBLIC\] DIM dim-element \[,dim-element\] ...

Where:

> <img src="bitmaps/dim.gif" data-align="bottom" data-border="0" alt="DIM" />
>
> |  |  |
> |----|----|
> | array_name | = an alpha or numeric array variable |
> | dim1, dim2 | = positive integer expressions specifying new dimensions. |
> | length | = positive integer expression specifying maximum length of each alpha array element. Defaults to 16. |

</div>

------------------------------------------------------------------------

The DIM statement statement in that it is used to declare, and optionally initialize, variables within a KCML program. It allows the initial dimensions of arrays and the lengths of strings to be defined. Variables defined in a DIM statement are marked as non-common and will be dropped on a [LOAD](LOAD.htm). They are reinitialized if the program is restarted by a [RUN](RUN.htm) command.

The DIM statement is a declaration used only during the resolve phase. At execution time it is skipped. Thus any expressions used in initialization must be capable of being evaluated at resolve time. Any variables used must be either constants or in common. A variable may be declared more than once but each declaration must be identical.

The dimensions and lengths of variables defined by DIM can be specified with a numeric scalar expressions that are evaluated at resolve time. String scalars are automatically assigned a length of 16 bytes if no length is specified.

Both common and non-common variables must previously be defined before they are referenced. When a DIM statement is executed during the resolve phase, the system notes the space required for each specified variable Arrays must always be declared before they are used but if a scalar variable is encountered within a program without a previous DIM, then the system will automatically declare it, thus scalar numerics and strings need not be explicitly DIMed. However this a a bad practice that can lead to bugs and it is not recommended (see comments [below](#forcedim)).

The space associated with arrays and scalar strings is not actually allocated at resolve time but on the first reference in an executing program. This minimizes the memory used in a program where some variables may not be used due to the direction of the flow of execution.

Specifying the length of alphanumeric variables and array dimensions

The dimensions of arrays and the lengths of alphanumeric variables or array elements are specified numeric expressions taht evaluate at resolve time to non-negative integer values. Numeric functions, such as [INT(](INT(.htm), [MAX(](MAX(.htm), [MIN(](MINfn.htm), [SGN(](SGN(.htm) etc. are valid within the numeric expression, although any variables used within the numeric expression must be constants or have been previously [COM](COM.htm)ed prior to the current program being [LOADed](LOAD.htm).

Changing the size of a variable or the dimensions of an array

Array dimensions may be changed explicitly during execution with [MAT REDIM](MAT_REDIM.htm), [LET REDIM](LET.htm) or by one of the following statements by specifying the new dimensions, enclosed in parentheses following the array name:

|                          |                            |                        |
|--------------------------|----------------------------|------------------------|
| [MAT CON](MAT_CON.htm)   | [MAT IDN](MAT_IDN.htm)     | [MAT ZER](MAT_ZER.htm) |
| [MAT READ](MAT_READ.htm) | [MAT REDIM](MAT_REDIM.htm) |                        |

If an array or string is DIMed with a size of zero, then no space is allocated during the resolve phase. Space can be allocated later when the size is known with any of the statements listed above. If the array is used before the space has been allocated then an error will result.

For example, the following would automatically resize each array to the dimensions specified within the parentheses.

DIM one(0), two(2,2)\
MAT REDIM one(20)\
MAT two = CON(32,33)

Initializing variables with the DIM statement

String and numeric scalar variables and [constants](TutorialConstants.htm) can be initialized at resolve time by specifying an expression after an equals sign. Numeric variables can be initialized using any numeric expression that can be evaluated at resolve time, although any variables used within the numeric must have previously been [COM](COM.htm)ed prior to the current program being LOADed.

String and numeric scalar variables can be initialized at resolve time by specifiying an expression after an equals sign. Numeric variables can be initialized using any numeric expression that can be evaluated at resolve time, although any variables used within the numeric must be constants or have previously been [COM](COM.htm)ed prior to the current program being [LOADed](LOAD.htm). String variables can only be initialized with a literal string or with the ALL function, e.g.

DIM test=100, news=10\*first\
DIM beta=INT(abc/2)

If no length is declared the string is then sized to match the number of characters in the initializing literal or HEX( function. To reserve more space than the specified literal a numeric length expression can be used to specify the required size.

DIM Test\$ = "ABCDE"\
DIM Letter\$1000 = HEX(FFFE FDFC)

Field variables can also be defined and initialized with DIM, for example:

DIM .Name\$=(1,35), Number=(35,"####")

PUBLIC and PRIVATE scope

If the PRIVATE keyword is used when declaring a constant or a field in a library then that constant or field will not be visible outside the library. This stops it clashing with another variable of the same name in another library and so enhances reliability in complex systems. It has no effect in foreground programs. You should use PRIVATE wherever possible.

Declaring a variable with PUBLIC DIM in a library defines it as a **library variable** that will be instantiated in the foreground program and persist in the foreground program across LOAD statements much like COM variables. If the defining library is unloaded then its public library variables revert to normal variables and they will no longer persist across program LOADs.

By default variables are DIMed in PUBLIC scope and the PUBLIC keyword is not required though if you have public library variables you are encouraged to use it to make your intentions plain.

Explicit declaration

Traditionally KCML has allowed scalar variables to be used without a previous declaration in a DIM or COM statement. However this is generally considered to be a bad practice as it can lead to bugs as a result of mispelling. Modern programming standards will mandate the explicit declaration of all variables. This is enforced in KCML through the use of one or more of several possible methods:

- Include a [\$COMPLIANCE]($COMPLIANCE.htm) 2 or greater statement in just those programs where all variables are declared. This has other effects.
- Set byte 38 of [\$OPTIONS]($OPTIONS.htm#BYTE38) is set to HEX(01). This will require all programs to declare their variables.
- The KCML Workbench editor will flag any undeclared variables by underlining them in red.

Note that the parameters of a [DEFSUB](DEFSUB.htm) are considered to be declared as local variables by the DEFSUB and they must not be included in a [LOCAL DIM](LOCAL_DIM.htm).

The case of variables

While KCML is not sensitive to the case of a variable, it does preserve the case as defined by the DIM statement that declared it. This can be overridden with by setting the HEX(01) bit of byte 40 of [\$OPTIONS LIST]($OPTIONS_LIST.htm#BYTE40). See [here](mk:@MSITStore:workbench.chm::/CaseRules.htm) for more about the case of variables in the Workbench.

Compatibility:

Prior to KCML 6.10 the dimensions of an array and the maximum length of a string array element were all limited to 65535. From 6.10 onwards this restriction is lifted and available memory becomes the only limitation.

Syntax examples:

DIM abc\$(20),files\$(100)10,as(9,2), .field1\$=(10,10)\
DIM old\$(new)new2, was\$(1),is(2), files(act)\
DIM .field1=(1, "-#####.###"), afield\$=(2,96), nline=SGN(abc)\
DIM abc=50, zyx=INT(90/def), newl\$(50)16

See also:

[COM CLEAR](COM_CLEAR.htm), [COM](COM.htm), [LOCAL DIM](LOCAL_DIM.htm), [DEFSUB'](DEFSUB.htm), [DIM(](DIM(.htm), [LIST DIM](LIST_DIM.htm), [\$OPTIONS]($OPTIONS.htm)
