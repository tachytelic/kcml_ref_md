DEFRECORD

------------------------------------------------------------------------

General Form:

- \[PRIVATE \| PUBLIC \| LOCAL\] DEFRECORD recordname
-    FLD fldname \[ = packspec\]
-    ...
- END RECORD

Where:

- packspec = string expression

------------------------------------------------------------------------

A DEFRECORD defines a record or structure by creating a number of field variables defined by the [FLD](FLD.htm) statements that fall between the DEFRECORD and the END RECORD. A record can then be created as a string variable with [DIM](DIM.htm) or [COM](COM.htm) to hold this structured information which can be accessed using the FLD() operator or with the data aware binding of a form. Structures are recommented as a way of storing state which can be passed as a single BYREF argument to functions reducing the number of arguments to function calls are avoiding any dependency on visibility of out of scope variables.

These two statements must be paired or a resolve time error will be signalled. They cannot nest. These statements are interpreted at resolve time and skipped at run time. Executable statements may appear inside the DEFRECORD structure, in particular REM statements, but they will not be executed. The DEFRECORD just defines the structure and it does not allocate any space.

If prefixed with PRIVATE then the record and the fields it defines will be visible only within the library where it is declared whereas if prefixed as PUBLIC then the record and fields can be directly referenced from the foreground or from other libraries. If neither PUBLIC nor PRIVATE is used, the record is presumed to be PUBLIC.

Normally a DEFRECORD must be placed outside of subroutines. However, if prefixed by LOCAL then it can be used inside a DEFSUB, so that the DEFRECORD will have local scope within the DEFSUB. Local scope means the fields, the defined length constant and helper functions are only accessible from within the subroutine and any subroutines nested inside. This means that two LOCAL DEFRECORD statements in separate subroutines can use the same names for fields without conflict.

For more about how the fields of a record are defined, see the [FLD](FLD.htm) statement.


    DEFRECORD TestRec
       FLD a
       FLD b$24
    END RECORD

The name of the record is represented internally in KCML with a leading underscore and it has a value of the size of the structure. This can be exploited when defining instances of a structure with DIM as they can be created to exactly the right size.


    DIM a$_TestRec
    FLD(a$.a)=1
    FLD(a$.b$)="Hello"

Records can be defined in [libraries](MODULE.htm) and referenced in the foreground or in other libraries using the usual rules for looking up field and constant definitions. They cannot be used in global partitions unless memory mapped (see [SELECT @PART](SELECT_@PART.htm)). If you unload a library that defines a record with fields then the link between the field reference in the executing program and their parent record is lost and the fields becomes regular fields which can be redefined.

The records in a program are shown in the KCML Workbench function browser window and also with the [LIST R](LIST_R.htm) statement.

DEFRECORD records can be used with [DataBind](mk:@MSITStore:kcmlforms.chm::/tmp/DataBind.htm) objects to make forms data aware through [Data Binding](mk:@MSITStore:kcmlforms.chm::/tmp/DataBind.htm).

Initializing the FLDs in a RECORD

When a record is resolved a pseudo-DEFSUB initializing routine is created which can then be used to initialize an instance of the record can be initialized according to the fields that make it up with numeric, DATE and TIME fields set to zero, characters fields set to spaces and boolean fields set to FALSE. The name of the DEFSUB is the name of the record with a **'\_Init\_** prefix. The string to be initialized is passed as a BYREF argument and must be at least as large as the defined size of the record. If bigger the extra space will be set to blanks.


    DIM TestRec$_TestRec
    '_Init_TestRec(BYREF TestRec$)

Enumerating the FLDs in a RECORD

Another pseudo-DEFSUB routine is created that allows a record's FLDs to be enumerated. The name of the DEFSUB is the name of the record with a **'\_Enum\_** prefix. It takes one BYREF argument in the form of a one dimensional string array and it returns a numeric result of the number of FLD elements in the named record. The string array argument is redimensioned in the call to have that number of elements and each element can be considered as an instance of this [KCML_DEFRECORD_Entry](tmp/kintfld.htm#KCML_DEFRECORD_Entry) record


    DIM trfmt$(1)1
    n = '_Enum_TestRec(BYREF trfmt$())
    FOR i = 1 TO n
        PRINT FLD(trfmt$(i).DEFRECORD_name$)
    NEXT i

The name returned for a string field will not have the trailing '\$'. This is to be compatible with the KCML7 convention and to be consistent with the names used in databinding on forms. Similarly the trailing parenthesis of an occurs field will not be shown.

Searching for FLDs in a RECORD

A pseudo-DEFSUB routine with a name formed by using the **'\_Find\_** with the record name. Given a string representing the name of a field, it returns BYREF a record as defined by the built in DEFRECORD [KCML_DEFRECORD_Entry](tmp/kintfld.htm#KCML_DEFRECORD_Entry). The record buffer is passed as the second parameter and it must be DIMed using the \_KCML_DEFRECORD_Entry record length and passed BYREF. The function returns TRUE if the field is found in the record and the structure was updated. Note that when searching for string FLDs, the '\$' suffix is ignored and need not be specified. This means that you ought not to have two fields, one numeric and one string, with the same name as they cannot be distinguished with this function.


    DIM TestRec$_TestRec, p$_KCML_DEFRECORD_Entry
    found = '_Find_TestRec("a", BYREF p$)
    PRINT found, RTRIM(FLD(p$.DEFRECORD_pack$))

Directly embedding secondary RECORDs in a RECORD

A secondary record or array of records can be embedded in a primary record as in this example


    DEFRECORD details
       FLD name$30
       FLD address$(5)30
    END RECORD

    DEFRECORD lines
       FLD partno$10
       FLD qty
       FLD price
    END RECORD

    DEFRECORD order
       FLD employee_no
       FLD bill$_details
       FLD delivery$_details
       FLD item_count
       FLD items$(_MAX_ITEMS)_lines
    END RECORD

    DIM _MAX_ITEMS=8, e$_order
    '_Init_order(BYREF e$)
    FLD(e$.bill$.name$)="Kerridge Computers"
    ...
    FLD(e$.items$<1>.partno$)="42634653"
    ...

Note the simplified grammar FLD(e\$.bill\$.name\$) that can replace FLD(FLD(a\$.bill\$).name\$). Also subscripting of arrays is through the \<\> operator as the array is defined as an occurrance.

Indirectly embedding secondary RECORDs in a RECORD

The direct approach shown [above](dirembed) has the advantage that you can instantiate all of the fields describing the order in one object but it has serveral serious disadvantages. The most significant problem is that arrays of secondary records are fixed in size. Furthermore it is not possible to have the secondary records sensibly initialized when the main record is initialized by the call to '\_Init_order(). Finally it is not possible to pass secondary objects embedded this way as BYREF parameters in subroutine calls. To address these problems KCML 6.20 also allows the secondary records to be specified by SYM as in this definition


    DEFRECORD order
       FLD employee_no
       FLD bill
       FLD delivery
       FLD items
    END RECORD

    DIM e$_order, bill$_details, delivery$_details, items$(1)_lines
    '_Init_order(BYREF e$)
    FLD(e$.bill) = SYM(bill$)
    FLD(e$.delivery) = SYM(delivery$)
    FLD(e$.items) = SYM(items$)

but now the secondary records must be instantiated separately in the DIM line and the linkage established by explicitly initializing the fields to the SYM of the corresponding record. Again there is a shorthand notation allowing access to the secondary records as FLD(e\$.bill.name\$) is the same as FLD(SYM(\*FLD(e\$.bill)\$.name\$). Subscripting of arrays is through the \<\> operator and not parentheses. The range of subscripts is checked against the linked array and the array must have only a single dimension.


    '_Init_details(BYREF bill$)
    '_Init_details(BYREF delivery$)
    FLD(e$.bill.name$)="Kerridge Computers"
    MAT REDIM items$(item_count)_lines
    FLD(e$.items<1>.partno$)="42634653"
    ...

Compatibility

DEF RECORD and FLD were introduced with KCML 6.10 and the complex FLD notation for accessing embedded secondary records arrived with KCML 6.20.

See also:

[LIST R](LIST_R.htm), [FLD()](FLD(.htm), [Internal structures](tmp/kintfld.htm),
