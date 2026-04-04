DEFFN' subroutine entry point

------------------------------------------------------------------------

General Form:

DEFFN 'label \[(variable \[, variable\] ...)\]

\
Where:

label = an integer value or a symbolic label.\
variable = an alpha, numeric, field, pointer or array variable

------------------------------------------------------------------------

This format of the DEFFN' statement is used as a subroutine entry point. The subroutine is called with the [GOSUB'](GOSUBquote.htm) statement/function or from the keyboard by pressing the appropriate function key. Once the subroutine has been called, the symbol table is scanned for the DEFFN' statement with the corresponding label, execution of the program then continues after the DEFFN' statement. Subroutines are terminated with a [RETURN](RETURN.htm) statement, which returns the program flow to the statement following the [GOSUB'](GOSUBquote.htm) statement.

DEFFN' has now been replaced by [DEFSUB'](DEFSUB.htm) and its use is now strongly discouraged.

The labels used with the DEFFN' statement can either be an integer value, or a symbolic label consisting of up to 120 alphanumeric characters. The underscore character \`\_' can also be used to separate words, but spaces cannot be used. The first character of a symbolic label must be a letter.

The DEFFN' statement can also include an argument list to accept values passed from the [GOSUB'](GOSUBquote.htm) statement. The arguments should be enclosed in brackets and separated with commas. All types of variables can be passed in this way, including alpha and numeric arrays, symbols (see [SYM(](SYM(.htm) ) and field variables (see [FLD(](FLD(.htm) ). The number of arguments in the DEFFN' statement should be the same as in the calling [GOSUB'](GOSUBquote.htm) statement, and should also match in type (numeric to numeric, alpha to alpha etc.), otherwise an error will occur. E.g.

'calc(first, second, name\$(),.balance)\
     .           .           .\
DEFFN'calc(a, b, tmp\$(),.newbal)\
     .           .           .\
RETURN

Only symbolic subroutine names can be called from within an alphanumeric expression.

If symbolic subroutine names are used KCML will evaluate all the arguments of the [GOSUB'](GOSUBquote.htm) before passing any to the DEFFN', whereas if integer subroutine names are used KCML will evaluate each argument just before it is copied.

Local variables may be defined for the subroutine with the [LOCAL DIM](LOCAL_DIM.htm) statement. For example:

DEFFN'new(abc,def\$)\
LOCAL DIM test\$16, other\$4096, temp\
.           .           .\
.           .           .\
RETURN

The variables test\$,other\$ and temp and their contents in the previous example would be lost after execution of the [RETURN](RETURN.htm) statement. See the Local variables chapter, (chapter 9) in Volume 1.

By default KCML always displays subroutine labels and variables in lowercase. However, setting the HEX(01) bit of byte 40 of [\$OPTIONS LIST]($OPTIONS_LIST.htm#BYTE40) instructs the editor to preserve the case of variables and sub-routine labels.

Syntax examples:

DEFFN'DrawScreen(Size, Length, Heading\$)\
DEFFN'Screen_window(row, column, depth, width, .FieldVar)\
DEFFN'testing\$(.FieldVar\$)

See also:

[DEFSUB'](DEFSUB.htm), [GOSUB'](GOSUBquote.htm), [LOCAL DIM](LOCAL_DIM.htm), [RETURN](RETURN.htm)
