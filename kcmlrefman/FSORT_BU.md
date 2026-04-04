FSORT BU

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\
 FSORT BU \#stream, \[file1 \[TO file2\]\] \[, expr1\] \<reclen \[,expr3\]\> \[KEY numeric_array\|string_expr\]\
\
Where:\
\

|               |                                                         |
|---------------|---------------------------------------------------------|
| file1, file2  | = Native operating system filename                      |
| expr1         | = number of bytes to skip over at the start of the file |
| reclen        | = recordlength                                          |
| expr3         | = number of records to sort                             |
| numeric-array | = array specifying sort keys                            |
| string-expr   | = key segment descriptors                               |

------------------------------------------------------------------------

</div>

The FSORT BU statement is used to sort the contents of a native file which has a fixed record length.

The sort may be done in place, or if two filenames are specified, each must be separated with the TO clause, the sorted information will be saved into the destination file, leaving the source file unchanged. Sorts for files held within platter images must be done in place.

A number of bytes at the start of the file may optionally be ignored. These bytes will be copied unchanged to the output file.

The length of each record must be specified. Optionally the number of records to sort can also be specified. The default is to assume the whole file.

If no platter address or stream is specified then FSORT will look in the current working directory for the specified file.

The optional KEY clause allows the sort to be done on only selected segments of the record. If no KEY clause is present the sort is done in forward lexicographic order on the whole record.

The KEY clause can specify a string expression in which case the expression will be considered to be a list of [sort key descriptors](sortdesc.htm). Alternatively if the clause refers to a numeric array then an alternative legacy representation is assumed in which up to 10 segment specifiers may be defined in a two dimensional numeric key array of dimensions (N,3) where N is the number of segments making up the key. For each segment three numbers are specified:

1.  if negative sort backwards, else sort forwards
2.  start byte of segment in record (count from 1)
3.  length of segment

Example:

<div class="listing">

FSORT BU \#3, "SRECS-1" TO "TEMP-1" ,1 \<16\>

</div>

In the example above the file \`SRECS-1' is sorted into the file \`TEMP-1'. The first 256 bytes are not sorted, they are copied into \`TEMP-1' and are left unchanged. The number 16 represents the record size.

The environment variable WORKSPACE determines the directory in which temporary work files are to be created.

Syntax examples:

<div class="listing">

FSORT BU \#7, "SORTFILE" ,skip_1 \<120,file_size\>\
FSORT BU \#33, "SORT-IN" TO "SORT-OUT",5 \<RecLen\>\
FSORT BU \#71, SORTFILE\$(2) \<RecLen\> KEY specification()

</div>
