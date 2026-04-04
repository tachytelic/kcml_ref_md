DEFSUB' subroutine entry point

------------------------------------------------------------------------

<div class="Generalform">

General Form:

<div class="indent">

\
\[PUBLIC\|PRIVATE\] DEFSUB 'label \[(\[BYREF\] dim_element \[, \[BYREF\] dim_element\] ...)\]\
...\
\[END SUB\]

</div>

\
Where:\
<img src="bitmaps/defsub.gif" data-align="BOTTOM" data-border="0" alt="defsub" />

<div class="indent">

diml, dim2 = dimensions (numeric expressions with a value \> 0 and \< 65536).\
length = numeric expression with a value \> 0 and \< 65536. If no length is specified then the default is 16.

</div>

</div>

------------------------------------------------------------------------

The DEFSUB' statement is similar to the obsolete [DEFFN'](DEFFNquote.htm) statement in that it defines a subroutine entry point, the difference being that DEFSUB' copies passed arguments into local variables. Additional local variables may be declared with the [LOCAL DIM](LOCAL_DIM.htm) statement. All local variables are lost when the [RETURN](RETURN.htm) statement is executed.

The arguments are defined as local variables with the same dimensions and contents as those being passed to the routine. These can either be numeric, string or field variables and arrays. Alternatively explicit dimensions may be specified in the same way as with a regular [DIM](DIM.htm) statement. If the dimensions of the arguments are explicitly defined within the DEFSUB' statement, then the dimensions must match those of the [GOSUB'](GOSUBquote.htm) statement or function otherwise an S24 error (Illegal expression or missing variable) will be reported. As the [DIM](DIM.htm) expressions are evaluated at execution time they can use arguments passed to the routine, for example:

DEFSUB'Get_Rec(Reclen, Another\$Reclen)

would DIMension the variable Another\$ to the size specified by Reclen. Strings passed into DEFSUB' have their receiving parameter variables DIMed to the same size as the number of bytes being passed. In the following example the local variable msg\$ will be created with a size of 5 bytes, the size of the string being passed into the subroutine.

'Greeting("hello")\
...\
DEFSUB'Greeting(msg\$)\
...\

Subroutine scope

As of KCML 6.0, the optional END SUB statement can be used to define subroutine scope. If present then KCML will consider all LOCAL DIM statements between the DEFSUB and the END SUB to be defining local variables for that routine. When displaying code in the Workbench the body of the subroutine between the two statments will be indented. If executed an END SUB will behave like a RETURN.

DEFSUB'Sum(a, b, BYREF c)\
    c = a+b\
END SUB

Programmers are strongly encouraged to use END SUB in every subroutine. They are required for [\$COMPLIANCE]($COMPLIANCE.htm) level 1, the basic level of compliance.

Passing by reference

The [BYREF](BYREF.htm) qualifier may be specified against a numeric, string or label argument, and has to be matched by a BYREF qualifier in the [GOSUB'](GOSUBquote.htm) statement. This changes the behaviour so that on exit from the subroutine, the value is copied back into the calling argument. The body of the routine does not then need any special constructs when referencing the variable. For example:

aValue = 10\
aString\$ = "Hello"\
'aRoutine(BYREF aValue, BYREF aString\$)

DEFSUB 'aRoutine(BYREF Total, BYREF Name\$)\
Total += 100\
Name\$ = & " World!"\
RETURN

DEFSUB 'fred(BYREF 'a)\
'a(1)\
RETURN

would set the variable aValue to 110 and the variable aString\$ to "Hello World!". Individual array values can also be referenced in this way, for example:

'anotherRoutine(BYREF MyArray\$(5), BYREF Totals(9))

BYREF can also be used to pass pointers to numbers into [\$DECLARE]($DECLARE.htm)d functions. This tells KCML to pass the address of the number rather than the value as would be the normal convention for numbers. Strings are always passed as pointers so BYREF is not needed for them. The keyword RETURN can also be used as an alternative to BYREF but its use for this purpose is now deprecated and BYREF is to be preferred.

\$DECLARE 'GetComputerName(RETURN STR(), TO RETURN INT())\
len = LEN(STR(name\$))\
'GetComputerName(name\$, BYREF len)\

To pass a function as an argument you can do something like

'fred(BYREF 'b)\
\
DEFSUB 'fred(BYREF 'a)\
'a(1)\
END SUB\
\
DEFSUB 'b(n)\
...\
END SUB

Optional arguments

The specified parameters can include optional arguments. This allows extra arguments to be added to a DEFSUB without affecting any GOSUB that calls it. If arguments are omitted from the call then the specified default value is used instead. For example:

DEFSUB 'aRoutine(First, Second, Third = 123, Fourth\$ = "Hello!")

may be called with:

'aRoutine(1, 2, 3, "Nice Day\$)\
'aRoutine(1, 2, 3)\
'aRoutine(1, 2)

Optional arguments may only be specified after normal arguments (if any). It is not possible to leave out intermediate arguments. Only simple numeric and string expressions are supported; arrays of all types and fields do not support optional arguments. In the current implementation the defaulting expression will always be executed even if the corresponding parameter is supplied. This will not be true in future implementations and must not be relied upon. Furthermore, to work with future implementations, the default values ought to be simple expressions that can be evaluated at resolve time. Complex defaulting expressions, such as function results, may be permitted by the KCML 6.x parser but their effect may not be predictable.

The syntax for optional string arguments was extended in KCML 6.0 to allow an explict length to be specifed and to allow BYREF on optional arguments. For example:

DEFSUB 'a(arg\$**16**="Default")

PUBLIC and PRIVATE

As of KCML 6.10, an optional PUBLIC or PRIVATE keyword can prefix the DEFSUB to indicate whether the function should be visible outside of any library it might be defined within. If no prefix is used then PUBLIC is implied.

Using the PRIVATE keyword ensures that there won't be a name clash with another library and that changes to the function will not affect programs or other libraries. It is good practice to use this keyword to inform other programmers that they can make these assumptions if they need to modify the function.

Nested subroutines

As of KCML 6.10, subroutines can be nested in order that they can properly share local variables declared in the outer routine. Nested subroutines must use END SUB and are only supported if the [\$COMPLIANCE]($COMPLIANCE.hrm) level is 1 or more. The inner routines of a nested group are presumed to be PRIVATE to the group and they cannot be called directly from outside the group or from outside the program or library.

See also:

[LOCAL DIM](LOCAL_DIM.htm), [RETURN](RETURN.htm), [GOSUB'](GOSUBquote.htm), [\$DECLARE]($DECLARE.htm)
