Field variables

Introduction

One of the most common operations in commercial programming is the manipulation of sub-strings. To simplify this operation **KCML** uses the concept of fields where a field is a symbol defining the offset and length of a sub-string which can then be applied to any string variable. This provides a real performance improvement over the [STR(](STR(.htm) function as well as substantially increasing the readability of the program, for example:

STR(paint\$,6,5) = "Blue"

would be replaced by

FLD(paint\$.color\$) = "Blue"

where *.color\$* is the field variable specifying the sub string.

Initializing field variables

The simplest way is to define them as part of a record using [DEFRECORD](DEFRECORD.htm) and [FLD](FLD.htm). This avoids having to calculate the offset for the start of the sub-string e.g.

DEFRECORD MyRec\
  FLD price\$5\
  FLD cost="-###.##"\
END RECORD

Other than in the special case of DEFRECORD definitions, field variables must start with a period. They can be explicitly initialized at resolve time in DIM or COM statements or at runtime with LET statements or by using [READ](READ.htm) from [DATA](DATA.htm) statements, for example:

DIM .part\$ = (1,5),.color\$ = (6,5)\
.price\$ = (11,5)\
.@types\$(1) = (16,10)

would be the same as

READ .part\$, .color\$, .price\$, .@type\$(1)\
DATA (1,5),(,5),(,5),(,10)

When using the [DATA](DATA.htm) statement to store the field, information the start of the field need not be specified as **KCML** will automatically calculate the start positions for each field.

If a field is not defined in the executing program, KCML will check the list of currently loaded [libraries](TutorialModules.htm) in turn to find it before reporting an error if it cannot be found. This mechanism is also supported for any [SELECT @PART](SELECT_@PART.htm) process global.

Numeric field variables allow the sub-string to be considered as a number. The length parameter must give information about how the number is to be encoded in the string. This can be achieved by specifying a [PACK](PACK.htm) image or by specifying a [\$FORMAT]($FORMAT.htm) numeric field specification. E.g.

.value = (1,"-####.###")\
.count = (start, "B4")

The length of the field is implied by the image. When used as a numeric expression [FLD(](FLD(.htm) will extract the sub string and either [UNPACK](UNPACK.htm) or \$[UNPACK](UNPACK.htm)d the number. The [PACK](PACK.htm) image or [\$FORMAT]($FORMAT.htm) field specifications can also be specified in [DATA](DATA.htm) statements, e.g.

READ .part\$, .color\$, .price, .quantity\
DATA (1,5),(,5),(,"B5.2"),(,"-#####.##")

Using field variables

Alpha fields can be used wherever an alpha expression is valid, and numeric fields can be used wherever a numeric expression is valid, for example:

total = FLD(record\$().count) \* discount

although a number can only be changed in a numeric field in LET statements, e.g.

FLD(record\$().count) = 0

All of the shorthand numeric operators that are described in chapter 15 can also be used with field variables although using post fix and prefix operators with numeric fields should be avoided as it will have an effect on performance as the field will need to be unpacked, changed and repacked.

Whole arrays can be packed and unpacked to a common field specification, e.g.

display() = FLD(record\$.form)

where the *.form* field specification is used repeatedly until the array *display()* has been filled, e.g.

DIM display(3)\
.form = (1,"P2")\
record\$ = HEX(0102 1234 9999)\
display() = FLD(record\$.form)\
PRINT display()\
\
102\
1234\
9999

Fields can also be packed from an array in a similar fashion:

FLD(record\$.form) = display()

where *.form* again specifies the first element of the array. The buffer must be big enough to hold all elements of the array. When arrays have been packed in this way the \`\<\>' operator can be used to extract individual elements, for example:

test = FLD(record\$.form\<2\>)

would extract the second element packed in the variable *record\$* according to the specification in *.form*.

Miscellaneous

LIST DIM, POS(, PACK( and LEN(

The [LIST DIM](LIST_DIM.htm) statement can be used to list field variables, and their field specifications.

Programmatically the [POS(](POS(.htm) and [LEN(](LEN(.htm) functions may be used to return the start position and length of the specified field. The [PACK(](PACKfn.htm) function can return the pack format for numeric fields. For example to return the start position and length of the field variable *.color\$* defined in the first example above, the following would be used:

PRINT POS(.color\$), LEN(.color\$)

which would return 6 and 5 respectively.

If arrays of fields are being used then the [DIM(](DIM(.htm) function can be used in the same way as with normal array variables to find the number of elements within each dimension, for example:

DIM .totals(15), .discounts(10,20)\
PRINT DIM(.totals(),1), DIM(.discounts(),2)\
15   20

Passing field variables into subroutines

Field variables can be passed into subroutines with the [GOSUB'](GOSUBquote.htm) statement. For example:

'qsort(.name\$, (2,"#.#"), (9,9), .ab())

would pass the field variables and parameters into the named subroutine. The parameters specified by the [DEFSUB](DEFSUB.htm) statements should match in type otherwise an error will occur. For example the following [DEFSUB](DEFSUB.htm) statement could be used to receive the field variables passed by the previous example:

DEFSUB 'qsort(.nm\$, .num, .type\$, .totals())

Note that the variables specified within the parentheses on a [DEFSUB](DEFSUB.htm) statement are declared as local variables.

IF ... THEN

The values of field variables can also be tested with the IF ... THEN statement as follows:

IF (.name\$ == .owner\$)\
...\
END IF\
IF (.legs\$ \<\> (5,9)) THEN ...

See also:

[DEFRECORD](DEFRECORD.htm), [FLD](FLD.htm), [DATA](DATA.htm), [FLD(](FLD(.htm), [LEN(](LEN(.htm), [POS(](POS(.htm), [READ](READ.htm), [STR(](STR(.htm)
