FLD

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

FLD fldname \[ = packspec\]\
FLD SKIP(numexpr)\
FLD AT(numexpr)

</div>

\
Where:\
\

<div class="indent">

packspec = a string expression or a field

</div>

</div>

------------------------------------------------------------------------

FLD statements may only appears inside a [DEFRECORD](DEFRECORD.htm)...END RECORD grouping that defines a record or structure. They define the size and format of the [fields](TutorialFields.htm) that make up the structure. Unlike other ways of initializing fields, records generate the start byte automatically with the first field of a record having an offset of one.


    DEFRECORD TestRec
       FLD a                             // Uses KCML internal numeric format
       FLD b$24                          // this starts at byte 9
       FLD c$(10)16                      // OCCURS(10)
       FLD d$<<9>>30                     // language occurs LANG(30,9)
    END RECORD

When used in a FLD statement a field name is not decorated with it characteristic leading dot though that dot is necessary if the field is referrred to in any other context. The names must also be unique across all records and two records cannot define the same field. It is an error to attempt to change the definition of a field originally defined in a record using some other field expression, thus in a program containing the above record, executing


    .a=(3,"UINT(4)")

will produce a runtime, recoverable, error. You can find the record that defines a field with [LIST R](LIST_R.htm).

The size and format of the field can be defined implicitly using the same notation as in DIM. So in the example above the variable *a* is a numeric field stored in KCML internal format and occupying 8 bytes in memory. The second field *b\$* is a string field occupying 24 bytes in memory and it will have a start offset of 9 as it follows the 8 byte .a field. Both numeric and string fields can repeat corresponding to the OCCURS clause in a database row. This is shown by using parentheses as exemplified by the .c\$ field in the example. This field will have a defined length of 16 but space for 10 instances, a total of 160 bytes, will be allocated in the record and the next field will start at byte 193. There is a special type of OCCURS for language specific fields whose runtime value depends on the language in use as specified by byte 20 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20). These use the chevron notation employed for field *.d\$* in the example. The length used in *.d\$* will be 30, the size of one element and the start offset will be calculated at runtime. If the value of the language byte is zero or is greater than the number of elements in the occurs, 9 in the example, then the start offset will be the start of the occurs.

You can specify particular packing formats using the optional packing expression. The string expression here must be one of the [\$FORMAT]($FORMAT.htm) strings e.g. CHAR(16) or NUM(9,2) defined in the [field specifier list](tmp/xp.htm). These override any implicit lengths which are then ignored. Occurs specifiers are honored except in the case of the LANG() and OCCURS() packing formats where the explicit values in the packing format take precedence. It is recommended that you use the new packing formats introduced with KCML 6.10 but older \$FORMAT/\$PACK strings are possible. As FLD is a resolve time statement, the packing expression must be a string literal or be a [COM](COM.htm) string inherited from a previous program. It is not case sensitive.


    DEFRECORD FmtRec
       FLD p     = "NUM(5,2)"
       FLD q$    = "CHAR(24)"
       FLD r(10) = "UINT(3)"
       FLD s$    = "LANG(30,9)"
       FLD t     = "NUM(5,2)"
    END RECORD

You can also define a field by reference to another field so for instance the previous example could have been written as


    DEFRECORD FmtRec
       FLD p     = "NUM(5,2)"
       FLD q$    = "CHAR(24)"
       FLD r(10) = "UINT(3)"
       FLD s$    = "LANG(30,9)"
       FLD t     = .p
    END RECORD

The initializing field does not have to have been defined in the same record though it must have been previously defined somewhere so that it has a value. The starting offset is ignored and only the packing format is copied.

It is not always necessary to account for every byte in a structure and it is helpful to be able to skip over bytes that are not relevant. This can be done with the SKIP(n) function which skips over n bytes. In the following example the .first\$ field will start at byte 2 of the structure.


    DEFRECORD FmtRec
       FLD SKIP(1)       // pad byte
       FLD first$
    END RECORD

There is no sanity check on this value so zero or even negative values are possible. This could be used to back up in the structure to alias more than one field onto the same address.

You can also control the offset used for a field by preceeding it with the AT(n) function which sets the offset (counted from 1) to use. You can alias two fields with something like


    DEFRECORD FmtRec2
       FLD first$
       FLD second$
       FLD AT(POS(.first$))
       FLD alias$        // this will alias .first$
    END RECORD

If a [REM](REM.htm) immediately follows a FLD then the editor will attempt to display it on the same line as the FLD approximately 40 characters in from the FLD. This indenting is not employed when SAVEing the program. As of KCML 6.20 this is deprecated and the // form of comment should be used instead.

The records in a program, together with their component fields, are shown in the KCML Workbench function browser window and also viewable with the [LIST R](LIST_R.htm) statement. When displaying variables in the debugger, the workbench will attempt to detect records and display optionally display the variable in a grid showing its component fields.

See also:

[DEFRECORD](DEFRECORD.htm), [LIST R](LIST_R.htm), [FLD()](FLD(.htm), [Field specifiers](tmp/xp.htm),
