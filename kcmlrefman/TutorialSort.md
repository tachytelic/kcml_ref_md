Sorting methods

Introduction

An important feature of a commercial programming language is its ability to sort both alphanumeric and numeric data quickly and efficiently. **KCML** provides three statements to perform this task. The [SORT](SORT.htm) statement to sort whole arrays of data, and the [FSORT](FSORT_BU.htm) statement which sorts data files. The MAT SORT statement is also available for compatibility with other dialects of BASIC-2, and is not discussed in this section as it still retains many of the restrictions of BASIC-2.

The SORT statement

The [SORT](SORT.htm) statement is used to sort arrays of both alpha or numeric information. The sort is performed in place, and unlike the MAT SORTmatsort statement used by other BASIC-2 dialects, it requires no pointer or locator arrays.

Numeric arrays by default are sorted in ascending order, the order may be reversed by specifying a minus sign before the array name. E.g.

DIM abc(4) READ abc(): 4,6,1,9 SORT abc() MAT PRINT abc; SORT -abc() MAT PRINT abc;

1 4 6 9 9 6 4 1

The first [SORT](SORT.htm) statement sorts the array *abc* in ascending order while the second [SORT](SORT.htm) statement sorts the array in descending order.

Alphanumeric arrays are normally sorted on the whole of each array element, e.g.

DIM records\$(4)10 MAT READ record\$() DATA "Bill AB345","SteveAB535","Alan AB543","Fred AB135" SORT record\$() PRINT record\$()

Alan AB543Bill AB345Fred AB135SteveAB535

By specifying the start and length of a sub-field within each element the sort can be restricted to that sub-field. Sub fields are specified within the less than (\<) and greater than (\>) symbols after the alpha array variable. By default alphanumeric arrays are sorted in ascending order. By specifying a negative start position the array can be sorted in descending order. For example, to sort using the last five characters of the array specified in the previous example the following would be used:

DIM records\$(4)10 MAT READ record\$() DATA "Bill AB345","SteveAB535","Alan AB543","Fred AB135" SORT record\$()\<6,5\> PRINT record\$()

Fred AB135Bill AB345SteveAB535Alan AB543

to reverse the order of the sort the SORT statement would be changed to:

SORT record\$()\<-6,5\>

Field variables (see chapter 7) can also be used to specify a sub-field within each element with which the sort is to take place. For example the previous example has been re-written to replace the \`\<6,5\>' with the field variable *.code\$*, the field variable *.name\$* has also been initialized even though it is not used:

DIM record\$(4)10 .name\$ = (1,5) .code\$ = (6,5) MAT READ record\$() DATA "Bill AB345","SteveAB535","Alan AB543","Fred AB135" SORT record\$()\<.code\$\> PRINT record\$()

Fred AB135Bill AB345SteveAB535Alan AB543

To reverse the sort order a new field would have to be initialized specifying a negative start position, therefore the program could be modified thus,

.name\$ = (1,5) .code\$ = (6,5) .reverse\$ = (-6,5) SORT record\$()\<.reverse\$\> : PRINT record\$()

The FSORT statement

The [FSORT](FSORT_BU.htm) statement allows whole data files to be sorted, the file can be held either within an NPL platter image or within the UNIX or Windows file system. Two types of sort are available, a BU sort to sort information normally accessible with the DATA LOAD/SAVE BA, and the DATA LOAD/SAVE BU statements, and a DC sort to sort data file normally accessible with the DATA LOAD/SAVE DA and the DATA LOAD/SAVE DC statements.

Each type of sort statement allows the sort to be done either in place or an output file containing the sorted information may be specified after the optional TO clause. For example:

FSORT BU T#3, "SREC1" TO "TEMP", 256 \<16\>

would sort the file *SREC1* and place the sorted information into the file *TEMP*, leaving the source file unchanged. Sorts performed on platter images must be done in place.

FSORT BU

The FSORT BU statement is used to sort any file which has a fixed record length. The optional KEY clause allows the sort to be done on any selected segments of the record. Up to 10 segment specifies may be defined in a two dimensional array, which must have the dimensions (*N*, 3) where *N* is the number of segments making up the key. If no key clause is present the sort is performed in forward lexicographic order on the whole record. For each segment three numbers are specified:

|     |                                                |
|-----|------------------------------------------------|
| 1   | If negative sort backwards, else sort forwards |
| 2   | Start byte of the segment within the record    |
| 3   | Length of the segment                          |

An optional number of bytes to skip over the start of the file can be specified immediately after the second filename, if specified, otherwise after the first filename. These bytes will remain unchanged. If a destination file is specified they will be copied unchanged into the beginning of the destination file.

The less than (\<) and greater than (\>) signs are used to surround two extra parameters. The first specifies the record size in bytes, and the second specifies the number of records to sort, for example:

FSORT BU T#3, "SRECS1" TO "TEMP-1", 200 \<100,16\>

would sort the file SRECS1, the first 200 bytes are ignored and are copied across to the file *TEMP-1*. Each record is 100 bytes long, and only the first 16 bytes are to be sorted.

In the following example the file *SORTFILE* is created in the directory '/tmp', 200 records each of which contain 10 bytes of random data are then saved into the file. The file is then sorted according to the specified keys. Each element of the key is broken down as follows:

akey(1,1)=1 Sort key one in ascending order. akey(1,2)=1 Key one starts at position 1 within each record. akey(1,3)=3 Key one is 3 characters long. akey(2,1)=1 Sort key two in ascending order. akey(2,2)=5 Key two starts at position 2. akey(2,3)=3 Key two is 3 characters long. DIM sort1\$(20)10, akey(2,3) akey() = CON akey(1,3),akey(2,3) = 3 akey(2,2) = 5 SELECT \#1 "/tmp" DATA SAVE DC OPEN T#1,(80)"SORTFILE" ERROR DO DATA LOAD DC OPEN T#1,"SORTFILE" ENDDO REPEAT count = 1 REPEAT recchar = 1 REPEAT STR(sort1\$(count),recchar) = BIN(INT(RND(1)\*58)+65) UNTIL recchar++ ==10 UNTIL count++ ==20 DATA SAVE BU T#1,(byte,byte)sort1\$() UNTIL se++ ==98 FSORT BU T#1,\<10,200\> KEY akey()

FSORT DC

The FSORT DC statement is used to sort files or platter image files that are usually accessed with the obsolete DATA LOAD/SAVE DA or DATA LOAD/SAVE DC statements. DC files are no longer gererally used. This sort statement would generally be used to sort a locator file. The locator file would have been created by either taking information from a file index, or by sequentially reading each record of the file and copying the relevant information into the locator file. Once the locator file has been sorted, the index of the main file can then be rebuilt or the records could be copied from the source file into the new file in the order specified by the locator file.

Each 256 byte sector of the file should have been written as an alpha array and each element of the array is considered to be a record. As FSORT DCfsortdc calculates the record length by examining the header information at the start of the first sector, all sectors must be written in the same format. Multi sector DC records cannot be read.

An optional expression allows a number of 256 byte sectors to be skipped over at the beginning of the file, if a second filename is specified these sectors will be copied unchanged into the beginning of the second file. e.g.

FSORT DC T#12, "SRECS1" TO "TMP1", 10

would sort the file *SRECS1* copying the sorted data into the file *TMP1*, the first 10 sectors of the source file are copied across unchanged.

The optional KEY clause allows the sort to be done only on selected segments of the record. Up to 10 segment specifiers may be defined in a two dimensional key array which must have the dimensions (*N*,3), where *N* is the number of segments making up the key. If no KEY clause is present the sort is done in forward lexicographic order on the whole record. For each segment three numbers are specified:

|     |                                                |
|-----|------------------------------------------------|
| 1   | If negative sort backwards, else sort forwards |
| 2   | Start byte of segment in record (count from 1) |
| 3   | Length of segment                              |

Example:

DIM sort1\$(20)10, akey(2,3) akey(1,1) = CON akey(1,3),akey(2,3) = 3 akey(2,2) = 5 SELECT \#1 "/tmp" DATA SAVE DC OPEN T#1,(102)"SORTFILE" ERROR DO DATA LOAD DC OPEN T#1,"SORTFILE" ENDDO REPEAT count = 1 REPEAT recchar = 1 REPEAT STR(sort1\$(count),recchar) = BIN(INT(RND(1)\*58)+65) UNTIL recchar++ ==10 UNTIL count++ ==20 DATA SAVE DC \#1, sort1\$() UNTIL se++ ==98 FSORT DC T#1,"SORTFILE" TO "SORTOUT"KEY akey()

In the previous example the program first creates a DC file, it then fills each element of the array *sort1\$* with random characters. The array is then saved into the file *SORTFILE*. Once each sector of the file has had random information saved into it is then sorted according to the key specification. Each element of the key is broken down as follows:

|             |                                                  |
|-------------|--------------------------------------------------|
| akey(1,1)=1 | Sort key one in ascending order.                 |
| akey(1,2)=1 | Key one starts at position 1 within each record. |
| akey(1,3)=3 | Key one is 3 characters long.                    |
| akey(2,1)=1 | Sort key two in ascending order.                 |
| akey(2,2)=5 | Key two starts at position 2.                    |
| akey(2,3)=3 | Key two is 3 characters long.                    |

The WORKSPACE environment variable

When **KCML** is sorting information with the FSORT statement it will create a temporary work file which will be at least the same size as the file being sorted. By default these temporary work files will be created in the directory '/tmp' under Unix and in the system nominated sort directory (\$TMP or \$TEMP) under NT. If your machine only has limited space for files in the \`/tmp' directory then it may be advisable to set the [WORKSPACE](EnvVars.htm#WORKSPACE) environment variable. This variable specifies a directory in which FSORT will create any temporary files, for example:

WORKSPACE=/user1/tmp.fsort export WORKSPACE

if added into the *.profile* for each user would instruct FSORT to create all temporary work files in the directory '/user1/tmp.fsort'.
