GOSUB'

------------------------------------------------------------------------

General Forms :\
\
1.      \[GOSUB\] ' label \[(\[BYREF \] argument \[, \[BYREF\] argument\] ...)\]\
\
2.      'label \[(\[BYREF\] argument \[, \[BYREF\] argument\] ...)\]\
\
Where:\
\
     label           = integer or a symbolic name\
\

------------------------------------------------------------------------

The GOSUB' statement is similar to the obsolete [GOSUB](GOSUB.htm) statement, except that instead of specifying a line number, a label is specified that relates to a label in a [DEFSUB'](DEFSUB.htm) or a [\$DECLARE']($DECLARE.htm) statement. The second form is used as a function valid wherever an alpha or numeric expression is valid. If used within an alpha expression the label must have a dollar sign appended to it, e.g.

name\$ = 'next_record\$() & initial\$

When a GOSUB' statement or function is executed KCML examines the symbol table for the [DEFSUB'](DEFSUB.htm) or [\$DECLARE']($DECLARE.htm) statement with the corresponding label, and execution of the program then continues after the [DEFSUB'](DEFSUB.htm) or [\$DECLARE']($DECLARE.htm) statement. Subroutines are terminated with a [RETURN](RETURN.htm) statement, which returns the program flow to the statement following the previous GOSUB' statement. If the function form is used the [RETURN](RETURN.htm) statement is used to return the value used within the alpha or numeric expression containing the function. The labels used with the GOSUB' statement and functions are a symbolic label consisting of up to 120 alphanumeric characters e.g. GOSUB 'get_next_record. The underscore character \`\_' can also be used to separate words as spaces cannot be used. The first character of a symbolic label must be a letter. If a subroutine is called by a regular GOSUB' statement that would normally return a value back to an alphanumeric expression, then the return value will be ignored.

Note that the reserved word GOSUB is optional and indeed now deprecated, therefore both of the following statements would perform the same task:

GOSUB 'ClearRecords(Rec_List\$(), Start_Pos, End_Pos)\
'ClearRecords(Rec_List\$(), Start_Pos, End_Pos)

The GOSUB' statement and function can also include an argument list to accept values and pass them to the [DEFSUB'](DEFSUB.htm) or [\$DECLARE']($DECLARE.htm) statements. The arguments should be enclosed in parentheses and separated with commas. The number of arguments in the GOSUB' statement and function should generally be the same as in the receiving [DEFSUB'](DEFSUB.htm) statement, they should also match in type (numeric to numeric, alpha to alpha etc.), otherwise an error will occur. Alpha and numeric arrays, field variables and symbols can be passed to the subroutine in this way. E.g.

'Route(ab\$, .nm, .size\$())

It is possible for the number of arguments in the GOSUB argument list to be less than the number of parameters in the DEFSUB list provided the extra parameters are at the end of the DEFSUB parameter list and were each initialized thus making them [optional parameters](DEFSUB.htm#Optional).

The [BYREF](BYREF.htm) qualifier may be specified against a numeric or simple string argument, and has to be matched by a BYREF qualifier in the [DEFSUB'](DEFSUB.htm) statement. This changes the behaviour so that instead of copying the value of the argument into a local copy used only in the routine, KCML will pass a reference to the original variable. Any changes made to the BYREF variable in the routine will be reflected back into the original argument as they both refer to the same object. This is very similar to passing the [SYM()](SYM(.htm) of the variable but the body of the routine does not then need any special constructs when referencing the variable. For example:

aValue = 10\
aString\$ = "Hello"\
'aRoutine(BYREF aValue, BYREF aString\$)

DEFSUB 'aRoutine(BYREF Total, BYREF Name\$)\
Total += 100\
Name\$ = & " World!"\
RETURN

would set the variable aValue to 110 and the variable aString\$ to "Hello World!".

If symbolic subroutine names are used then KCML will evaluate all the arguments of the [GOSUB'](DEFFNquote.htm) before passing any to the [DEFFN'](DEFFNquote.htm), whereas if integer subroutine names are used then KCML will evaluate each argument just before it is copied.

When executing a GOSUB' or when a routine is called from an alphanumeric function, KCML first searches the currently executing programs symbol table for the routine. If the routine is not found then the currently selected global partition, if any, is searched. Note that this means that if a partition calls a global routine which itself calls a subroutine then the original partition text is never searched unless the global routine specifically executes a [SELECT @PART](SELECT_@PART.htm) statement back to the parent text. This can be done because when KCML switches partitions to execute the global routine it remembers the global partition originally selected, and when it switches back to the original partition, on execution of a [RETURN](RETURN.htm) statement, it will re-select that global partition again.

If the environment variable KEEPSHARED is set KCML will not deselect the global partition on a [LOAD](LOAD.htm). Additionally it also changes the search algorithm so that the original parent text is searched first before the currently executing text. This allows the original partition to have routines which override those in the shared library text.

Example:

'GetNext(1)\
MAT SEARCH Section\$,=Check\$ TO locator()\
\
.      .\
\
DEFSUB 'GetNext(Stream)\
ret = READ \#Stream, Section\$\
RETURN

In the above the first two lines could be re-written to use the function form of the GOSUB' statement, thus

MAT SEARCH 'GetNext\$(1),=Check\$ TO locator()

the DEFFN statement would also need to be modified to change the subroutine name so that it can be used within a alpha expression, also the [RETURN](RETURN.htm) statement would need to be changed to return the contents of the variable section\$, thus

DEFSUB'GetNext\$(Stream)\
ret = READ \#stream, Section\$\
RETURN Section\$

Syntax examples:

'Label(1100,"type",HEX(1FFF))\
Record\$ = 'Name\$(.Fields\$()) & Address\$

See also:

[DEFFN'](DEFFNquote.htm), [DEFSUB'](DEFSUB.htm), [RENAME](RENAME.htm)
