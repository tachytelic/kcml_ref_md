FLD(

------------------------------------------------------------------------

General Form:\
\
     FLD(alpha-variable.field-variable)\
\
From KCML6.20, multiple FLD( functions could be replaced by an extended FLD( function. The following are equivalent:\
\
     FLD(a\$.b\$.c)\
\
     FLD(FLD(a\$.b\$).c)\
\

------------------------------------------------------------------------

The FLD( function defines a substring within the alpha variable or array to which it is applied. The specifications of the substring, its start byte and length, are held in a special form of variable called a [field variable](TutorialFields.htm) which is distinguished by having a period as its first character.

Field variables can be initialised in records using [DEFRECORD](DEFRECORD.htm) and [FLD](FLD.htm), in [LET](LET.htm) statements or they can be [READ](READ.htm) from [DATA](DATA.htm) statements, for example:

DEFRECORD ExampleRec\
   FLD lockbyte\$1\
   FLD description\$\
END RECORD\
\
.description\$ = (2,16)\
\
READ .description\$\
DATA (2,16)

all define a string field *.description\$* which starts in byte 2 and is 16 bytes long. The parentheses are required. This field variable can then be applied to any alpha variable provided it is big enough to hold the substring. Thus for the field variable defined above

Result\$ = FLD(buffer\$.description\$)\
Result\$ = STR(buffer\$,2,16)

have the same effect. Using FLD( instead of [STR(](STR(.htm) not only improves the readability of programs, it will also execute faster in most circumstances.

Numeric field variables allow the substring to be considered as a number. The length parameter must give information about how the number is encoded in the string. This can be achieved by specifying a [\$FORMAT]($FORMAT.htm) numeric field specification. The length of the field is implied by the image. When used as a numeric expression FLD( will extract the substring and [\$UNPACK]($UNPACK.htm) the number. For backward compatibility, numeric fields can also be specified by supplying a [PACK](PACK.htm) image but this usage is now deprecated.

The starting position of a field and the size of a field may be found with the [POS(](POS(.htm) and [LEN(](LEN(.htm) functions respectively, i.e.

FieldStart = POS(.description\$)\
FieldLength = LEN(.description\$)

The packing format can be found using the [PACK(](PACKfn.htm) function.

Field variables cannot currently be used as a receiver variable in [CALL](CALL.htm) and DATA LOAD statements.

Note: Using postfix and prefix operators with a numeric field should be avoided as it will have an effect on performance as the field will need to be unpacked, changed and repacked.

See also:

[DATA](DATA.htm), [READ](READ.htm), [STR(](STR(.htm)
