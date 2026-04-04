CREATE TABLE

CREATE TABLE tablename (*coldesc* \[, *coldesc*\] ...) \[*tableparm* \[, *tableparm*\] ...\]

where *coldesc* describes an individual column and is

colname datatype \[ALIAS colname\] \[STARTBYTE integer\]\
\[DISPLAY 'image'\]\[SIGNED\|UNSIGNED\]\
\[OCCURS integer\]\[RANGE(from,to)\]\[TOTALLED\]\
\[PRIORITY(u,d,p)\]\[NAME 'string'\]\[SPECIAL 'string'\]\
\[PREVAL integer\]\[POSTVAL integer\]\
\[VALIDATE C\|R\|U\|V\|T 'string'\]\
\[SEQUENCE integer\]\[OVERLAPS colname \[BY integer\]\]\
\[\[NOT\] NULL\]\[DEFAULT number\|'string'\|NULL\|USER\]\

and the *tableparm* list describes properties of the table e.g.

\[NAME 'string'\]\
\[ROWS integer\]\
\[RECLEN integer \]\
\[EXTENT integer\]\
\[TYPE integer\]\
\[PACKING integer\]\
\[BLOCKLEN integer\]\
\[NOEDIT 'string'\]\
\[\[PATH 'string'\] \| \[TABLESPACE 'string'\]\]\
\[SERIAL mode \[colname\]\]\
\[DATESTAMP colname\]\
\[USERSTAMP colname\]\
\[IPREFIX 'string'\]\
\[EXCLUDE COLUMN colname 'string'\]\
\[CASE 'string'\]\
\[UPDATE 'string'\]\

Note that the optional NAME tableparm is needed to create the dictionary but the other tableparms are only required to create a table. Columns should be defined in the left to right order that the columns are laid out in the row buffer. The column attributes can occur in any order.

STARTBYTE

Used to define the 3 byte integer START field in the dictionary. The start byte field in the dictionary can be deduced from the sizes of previous fields, but to deal with overlaps and gap it can be fixed with this expression. When writing SQL from the dictionary *kconvdd* will only generate this clause if the currently calculated offset differs from the value in START.

DISPLAY

This defines the DIMAGE dictionary field. If not present then the field is set the same as the PIMAGE field. When *kconvdd* is converting from the dictionary it will check if the fields are the same and only generate this clause if different. It can be at most 20 chars, left justified.

ALIAS

Used to define optional ALIAS dictionary field. If not present this field will be blank.\
Max 8 characters

NAME

Used to define optional LNAME dictionary field. If not present leave this field blank. When generating SQL surround in single quotes as embedded blanks, parentheses and commas are allowed. Max 20 characters.

OCCURS

Defines the OCCURS dictionary field. If not present leave this field blank. Calculate the new start byte from the product of this value and the individual lengths. Set the dictionary field to blank if not specified. Use leading zeroes when generating a (three byte) dictionary field. Only generate in the SQL if dictionary field is non blank.

PRIORITY

Defines the UPFLAG, DSFLAG and RPFLAG dictionary fields. If not present in the SQL then these fields will be left blank. Sets minimum priorities for update, display and reporting. The priorities are single digit integers 0 to 9 or blank.

RANGE

Defines the RANGEFR and RANGETO dictionary fields. Field is expressed in the statement as an ascii number. If not present in the SQL leave these fields blank. Originally intended to set max and min numeric values for a column but as it was implemented using native doubles it is not portable between machines with different byte orders. Do not use.

TOTALLED

This defines the optional TOTALLED dictionary field which can only apply to number fields. The single character dictionary field can be blank (not applicable), Y if this clause present, or N if applicable and not present. The clause will be generated only if the dictionary entry is "Y".

SPECIAL

Defines the USER dictionary field for user defined text. If not present in the SQL this field will be blank.

PREVAL, POSTVAL

These are numbers corresponding to the validation routines to be called. If zero in the dictionary then *kconvdd* will not generate these clauses.

VALIDATE

Defines the VALTYPE and VALSTR fields in the dictionary. If not present then both fields in the dictionary will be set blank. If the datatype is BIT then this implies a VALTYPE of "C" and a VALSTR of "YN"

SEQUENCE

Defines the SEQNO field in the dictionary used to specify update order in table driven maintenance utilities like GB/EDIT. This is a two byte binary field so set to zero if not present and don't generate in SQL if zero in the dictionary.

OVERLAPS

Defines OVFIELD in the dictionary. The optional integer expression is used to define the OVOFFSET field. Some dictionary rows define fields that overlap others and such rows will have this OVERLAPS field set to the COLUMN that is overlapped. Only if this field is blank should the row be used in calculating start bytes and row lengths. The overlap amount is counted from one not zero so if the BY clause is missing then assume 1. When reading dictionary entries only inspect this field if the OVFIELD is no blanks as it appears to be set to 0x2020 as often as not.

NULL,\
NOT NULL

This defines if a NULL value is allowed. It is not currently enforced in Rev7 and there is no dictionary field so it will be accepted by the SQL parser and discarded but it may be implemented in future.

Table parameters

These define attributes of the actual table to be created. With the exception of NAME they are not used in the data dictionary specification. The optional NAME clause is used to create a \$NAME field in the dictionary whose LNAME field is the 20 character value of the string which is used to describe the purpose of the table. If not present in the ascii a \$NAME row will still be generated containing a blank field.

RECLEN

The required row length. If not given it will be deduced from the column specifiers but if given, it must be big enough to encompass all the columns so specified.

ROWS

The maximum number of rows required in the first extent (default 100).

EXTENT

A percentage figure from 0 to 155 defining the amount by which a table grows on auto-extension. For type 7 tables the calculation is based on the total number of pages already in the table, whilst for earlier table types the calculation is made on the maximum no of rows currently allowed in the table.

TYPE

This is one of the integers 3,4,5,6 or 7 and defines the type of KISAM table required for applications that require backward compatibility. If not specified then type 7 is assumed.

PACKING

A percentage figure from 50 to 100 indicating the packing factor for index blocks. If not supplied 50 (75 for type 7 tables) will be used which would be appropriate for a volatile file. Use 100 if you do not expect any inserts after the table has been loaded.

BLOCKLEN

An integer from the set of 2,4,or 8 indicating the size of an index block in units of 256 bytes.

SERIAL

Indicates which column, if any, is to be used to hold serial numbers for the table. The permissible modes are A, M and N, for automatic, manual and none respectively. Modes A and M require a valid column name, which must be of type INTEGER(4). Choosing automatic mode causes the database to insert consecutively increasing values, starting from 1, into the choosen column whenever a row is inserted into the table.

PATH

Allows the user to specify a file path to be used when the table is created. If a path is not supplied the table will be created in the current working directory, i.e. the directory in which the KCML executable is situated.

TABLESPACE

If a TABLESPACE is specified rather than a PATH the table will be created in the named TABLESPACE. If the TABLESPACE is a TREE tablespace the table name will be parsed to look for branch/company/module information and the table created in the appropriate directory, note, the tablename MUST conform to a specific format for the table to be created correctly in this case.

DATESTAMP

(Type 7 tables only) Allows a column to specified for datestamping rows, the column must be of type INTEGER(4). By default datestamping is turned off but can be turned on with a call to [KI_SET_DATESTAMP](tmp/KI_SET_DATESTAMP.htm).

USERSTAMP

(Type 7 tables only) Allows a column to specified for userstamping rows, the column must be of type VARCHAR and be less than 255 bytes long. By default userstamping is turned off but can be turned on with a call to [KI_SET_USERSTAMP](tmp/KI_SET_USERSTAMP.htm).

IPREFIX

(Type 7 tables only) Specifies the prefix that [KI_FLD](tmp/KI_FLD.htm) will use if its prefix parameter is blank.

EXCLUDE COLUMN

(Type 7 tables only) Allows a column to be specified which will allow rows to be excluded from word search indices. The column must be of type VARCHAR(1). The parameter *string* is a list of hex values (upto 16) that will be checked against when ascrtaining whether the column should be excluded, if the column contains one of the values in *string* then word search information will not be created for that row, so for example '0a10' would indicate that if the column contained either ascii decimal 10 or 16 then the row should be excluded from word search indices.

CASE

Specifies the column name style when the table is accessed from ODBC. Values include SHORT, SHORT_LOWER, SHORT_UPPER, LONG, LONG_LOWER and LONG_UPPER. The default is LONG, which uses the column ALIAS value.

UPDATE

Specifies the table accessed mode from ODBC. Values include Y and N. The default is Y, which means the table can be updated.

For type 7 tables the BLOCKLEN parameter is used to determine the pagesize of the table in Kbytes and should be in the range 8 - 64. The default value is 8 giving an 8K pagesize. Whilst it is currently possible to mix table pagesizes within a database it is not recomended and the ability to do so may be removed in the future.

Temporary files

Temporary files can be created with CREATE TABLE. For more information see [temporary files](mk:@MSITStore:kcmlrefman.chm::/temporary.htm).

Examples

CREATE TABLE SL00test (color VARCHAR(10), quantity NUMERIC(8))

See also:

[DROP TABLE](DROP_TABLE.htm), [CREATE INDEX](CREATE_INDEX.htm) [CREATE TABLESPACE](CREATE_TABLESPACE.htm),
