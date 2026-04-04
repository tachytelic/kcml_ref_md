Local variables in subroutines

Introduction

Local variables allow subroutines to use variable names that are already in use outside the subroutine. Upon exit from the subroutine all variables defined within the routine are discarded, the memory is freed and the original values of any non-unique variables are restored. Local variables are defined either within the [DEFSUB](DEFSUB.htm) statement or with the [LOCAL DIM](LOCAL_DIM.htm) statement.

The DEFSUB' statement

The [DEFSUB](DEFSUB.htm) statement is used in a similar way to the [DEFFN](DEFFNquote.htm) statement in that it defines the start of the specified named subroutine. [DEFSUB](DEFSUB.htm) routines like [DEFFN](DEFFNquote.htm) routines, can be called either with [GOSUB'](GOSUBquote.htm) statements or from wherever an alphanumeric expression is valid. The difference being that [DEFSUB](DEFSUB.htm) also defines the scope for local variables, meaning that any variables defined within the subroutine, and subsequent subroutines will be discarded and the original values of any non-unique variables are restored upon execution of the [RETURN](RETURN.htm) statement. Any variable previously defined outside the subroutine can be referenced in the normal way.

Subroutine names must start with an alpha character followed by up to 127 alphanumeric characters. Whole words may be divided by underscores, i.e. *get_next_record* would be a valid subroutine name. Integer subroutine labels are not allowed, whereas they can be used with [DEFFN](DEFFNquote.htm). If the subroutine is to return an alpha value then a dollar sign should be appended to the label name.

The variables specified as parameters within the [DEFSUB](DEFSUB.htm) statement are automatically defined as local variables taking the same dimensions as the variables specified by the calling statement, the contents of any existing variables that have the same name are backed up. The dimensions of these variables may also be explicitly defined following the same rules as a regular [DIM](DIM.htm) statement. The dimensions of array variables passed into the subroutine must match those specified by the [DEFSUB](DEFSUB.htm) statement otherwise an error will result, this is designed to prevent any unplanned array re-sizing which could later cause a more serious problem. Only the length of alpha scalar variables can be changed. E.g.

00000 DIM tmp\$1000, .name\$, .zyx\$(10)4, abc . . . 00010 name\$ = FLD('get_record\$(1,tmp\$,zyx\$()).name\$) 00090 DEFSUB 'get_record\$(abc,def\$256, ghi\$(10)4) . . . 00500 RETURN result\$

In the previous example by specifying the array dimensions in both the [DIM](DIM.htm) and [DEFSUB](DEFSUB.htm) statements prevents any possible problems that may be caused if for some reason the array *zyx\$()* had been explicitly re-dimensioned elsewhere in the program.

The variables defined within the [DEFSUB](DEFSUB.htm) statement are evaluated at execution time and can therefore be used as arguments passed to the routine. For example:

DEFSUB 'get_next_record\$(n,def\$n) . . . RETURN result\$

would define the variable *def\$* to *n* bytes long.

A subroutine defined with the [DEFSUB](DEFSUB.htm) statement may also call itself recursively, thus defining a new set of variables each time. However, recursion is limited by the size of the return stack which is currently 42. For example:

DEFSUB'factorial(n) RETURN (n == 1 ? 1 : n \* 'factorial(n-1))

The LOCAL DIM statement

Additional local variables may be defined with the [LOCAL DIM](LOCAL_DIM.htm) statement which follows the same rules at the [DIM](DIM.htm) statement except that explicit initialization of scalar variables is not allowed. [LOCAL DIM](LOCAL_DIM.htm) can also be used to define local variables within normal [DEFFN](DEFFNquote.htm) subroutines. In both cases if a variable declared with [LOCAL DIM](LOCAL_DIM.htm) already exists its contents are backed-up and are restored upon execution of the [RETURN](RETURN.htm) statement. In the following example [LOCAL DIM](LOCAL_DIM.htm) is used to redefine the variable *zyx\$* as a local variable within the subroutine *'abc*.

|                      |                    |
|----------------------|--------------------|
| DIM zyx\$ = "AABBCC" | zyx\$6="AABBCC"    |
| GOSUB 'abc()         | zyx\$6="AABBCC"    |
| DEFFN 'abc()         | zyx\$6="AABBCC"    |
| LOCAL DIM zyx\$9     | zyx\$9=" "         |
| zyx\$ = "ZZZYYYXXX"  | zyx\$9="ZZZYYYXXX" |
| RETURN               | zyx\$9="ZZZYYYXXX" |
| STOP                 | zyx\$6="AABBCC"    |

Jumping out of a routine is allowed but is considered to be poor programming practice. Executing a [RETURN CLEAR](RETURN_CLEAR.htm) or a [RETURN CLEAR ALL](RETURN_CLEAR.htm) will restore the contents of any non-unique global variables to their original values. Jumping into the middle of a [DEFSUB](DEFSUB.htm) subroutine of into a subroutine containing local variables defined with [LOCAL DIM](LOCAL_DIM.htm) is allowed but all variables will be considered as normal variables. An error is reported if [LOCAL DIM](LOCAL_DIM.htm) is executed outside a [DEFSUB](DEFSUB.htm) or a [DEFFN](DEFFNquote.htm) subroutine, or executed after a jump into the middle of a subroutine. [LOCAL DIM](LOCAL_DIM.htm) can be used anywhere within a subroutine though it is recommended that it is used immediately after the [DEFFN](DEFFNquote.htm) or [DEFSUB](DEFSUB.htm) statement.

Note that it is not possible to return locally dimensioned string variables. It is also not possible to MAT REDIM a locally dimensioned variable to a larger size.

LIST DIM and LIST LOCAL

The [LIST DIM](LIST_DIM.htm) statement, if executed within a subroutine containing local variables, will also show the variable name, dimensions and contents of any local variables. The variable type shown in the first column of the [LIST DIM](LIST_DIM.htm) output is set to L for local variables. Only information about the local form is shown for any non-unique local variables. [LIST DIM](LIST_DIM.htm) outputs variables in the order in which they were declared, therefore local variables will always appear at the end of the output. For example:

LIST DIM C type\$1 "." C new_var\$16 " " D status\$(5)1 "A","A","A","A","B" D .name\$ D .total\$ (1,0x6002) L table\$(2)10 " "," " L count 45 L .balance (0,0000)

Alternatively the [LIST LOCAL](LIST_LOCAL.htm) command may be used to list only the currently defined local variables. The output from list local is the same as with [LIST DIM](LIST_DIM.htm), showing the variable name, dimensions and contents. [LIST LOCAL](LIST_LOCAL.htm) is really only useful if executed within a subroutine containing local variables, outside such a subroutine [LIST LOCAL](LIST_LOCAL.htm) will return nothing.

LIST LOCAL RETURN

The [LIST LOCAL RETURN](LIST_RETURN.htm) statement inserts the output from the [LIST LOCAL](LIST_LOCAL.htm) statement after a call to a subroutine containing local variables into the return stack section of the [LIST RETURN](LIST_RETURN.htm) statement. At the end of the output the original dimensions and contents of any locally defined non-unique variables is also shown, for example:

:list local return Program at line 30, statement 6 Global partition 248 'LIBRARY ' now selected Last 3 programs loaded: \$prog MENU1 - GENMENU oldest LOGIN Return stack contents Top 00030 :::FOR d = 1 TO n , varying D now 1, by 1, until 10 - 00010 ::GOSUB 'get(10) L N 10 L AB\$16 "................" L BA\$16 "................" - 00010 :FOR b = 1 TO 10 , varying B now 1, by 1, until 10 Bottom 00010 FOR a = 0 TO 9 STEP 2, varying A now 0, by 2, until 9 Original values of local variables C N 0 C AB\$40 "TEST1 " D BA\$25 "TEST2 "

The previous example shows that the subroutine *'get* had three local variables defined, these may have been defined either within a [DEFSUB](DEFSUB.htm) statement or with the [LOCAL DIM](LOCAL_DIM.htm) statement. The dimensions and contents of the local variables are shown after the subroutine was called. At the end of the output the original type, dimension and contents of the variables is also shown.

See also:

[DEFSUB](DEFSUB.htm), [DEFFN](DEFFNquote.htm), [GOSUB'](GOSUBquote.htm), [LIST LOCAL](LIST_LOCAL.htm), [LIST RETURN](LIST_RETURN.htm), [LOCAL DIM](LOCAL_DIM.htm)
