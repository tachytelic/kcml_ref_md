KCML Datatypes

This table shows the mapping between SQL data types that can be used in a [CREATE TABLE](CREATE_TABLE.htm) statement and the old Rev7 .dd dictionary codes. Note that the data type specifies the TYPE, LENGTH, PIMAGE dictionary fields in combination with an optional SIGNED or UNSIGNED attributes. Packed numbers are to be assumed to be SIGNED however this can be overridden by the explicit attribute. Integers are assumed UNSIGNED unless the SIGNED attribute is used but note that signed integers are not used in Kerridge Rev7 or Rev8 applications and are not supported by KCML currently.

The precision *prec* defines the number of digits in total and the scale *scale* determines how many are after the decimal.

| Dictionary type | SQL type | Purpose |
|----|----|----|
| C | VARCHAR(len) | Strings of any size. NULL if first byte is 0xFF or 0x00 |
| P | NUMERIC(prec\[, scale\]) | KCML packed numbers. Considered to be NULL if first byte is 0xFF |
| B | INTEGER\[(size)\] | Integers 1-4 bytes. Cannot be NULL |
| N | INTEGER(4) | Internal representation of an integers 4 bytes. Cannot be NULL, not portable. |
| J | DATE | A date represented as a [Julian date](mk:@MSITStore:kcmlrefman.chm::/JulianDate.htm) in an unsigned integer of 3 bytes. A zero value is considered to be NULL |
| D | OLD_DATE | An old date representation. No longer used. |
| H | HEX(len) | A binary datatype which will be rendered as hex digits. Almost obsolete in Kerridge applications. |
| F | BIT | The logical type is a synthetic type generated whenever a column is of type VARCHAR, has width 1 and permits only the values Y, N or blank. A blank value is considered to be NULL. |
| G | BOOL | BOOLEAN 'Y', '1' or N' '0' held as a single byte |
| L | BCDDATE | A 3 byte YYMMDD packed date or a 4 byte CCYYMMDD packed date |
| K | DECIMAL(prec\[, scale\]) | IBM packed numbers |
| T | TIME | Time since midnight [local time](mk:@MSITStore:kcmlrefman.chm::/timezone.htm) in seconds as an unsigned integer in 3 bytes. |
| M | TIMESTAMP | Time in milliseconds since 00:00 GMT year 0000, as an unsigned integer in 6 bytes. |
| O | BLOB | BLOB - Binary Large OBject |
| Q | CBLOB | Character BLOB |
