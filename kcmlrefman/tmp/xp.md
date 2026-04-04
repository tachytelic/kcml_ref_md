\$PACK and field specifiers

These formats are used in defining fields, in [\$FORMAT](../$FORMAT.htm), in the [FLD](../FLD.htm) elements of a [DEFRECORD](../DEFRECORD.htm) and as hex codes, directly in [\$PACK](../$PACK.htm) and [\$UNPACK](../$UNPACK.htm).

## Recommended formats for use in DEFRECORD fields

| Format | \$PACK code | Legacy | Purpose |
|----|----|----|----|
| [BOOL](../packspec.htm#BOOLEAN) |  |  | Numeric boolean with "1" for TRUE and "0" for FALSE |
| [CHAR(](../packspec.htm#CHAR) |  |  | Character field (presumed to be UTF-8 encoded) |
| [FP](../packspec.htm#FP) | FE08 |  | Internal representation of a KCML number |
| [HEX(](../packspec.htm#HEX) |  |  | Binary field |
| [INT(](../packspec.htm#INT) | Cd0y |  | Integer (signed) |
| [LANG(](../packspec.htm#LANG) |  |  | Multi-language string field |
| [NUM(](../packspec.htm#NUM) |  |  | Numeric (signed) |
| [TEXT(](../packspec.htm#TEXT) |  |  | Multiline text field |
| [TIME](../packspec.htm#TIME) | F703 |  | Time in seconds since midnight |
| [TIMESTAMP](../packspec.htm#TIMESTAMP) |  |  | TIMESTAMP conversion from TS6 to 0000-00-00 00:00:00.000Z format |
| [TS4](../packspec.htm#TS4) |  |  | Time stamp in seconds since 1970-01-01T0000Z held in 4 bytes |
| [TS6](../packspec.htm#TS6) |  |  | Time stamp in milliseconds since 0000-00-00 00:00:00.000Z held in 6 bytes |
| [UINT(](../packspec.htm#UINT) | Bd0y |  | Integer (unsigned) |
| [UNUM(](../packspec.htm#UNUM) |  |  | Numeric (unsigned) |

## Packing formats for numeric fields

| Format | \$PACK code | Legacy | Purpose |
|----|----|----|----|
| [B](../packspec.htm#BINARY) | Bd0y | Y | Unsigned binary format |
| [B+](../packspec.htm#SBINARY) | Cd0y | Y | Signed binary format |
| [BOOL](../packspec.htm#BOOLEAN) |  |  | Numeric boolean with "1" for TRUE and "0" for FALSE |
| [BR](../packspec.htm#BR) | Dd0y |  | Byte swapped (little-endian) unsigned binary format |
| [BR+](../packspec.htm#BRP) | Ed0y |  | Byte swapped (little-endian) signed binary format |
| [D](../packspec.htm#DISP) | 3dxx |  | IBM display format |
| [DATE](../packspec.htm#DATE) | F603 |  | Julian date |
| [F](../packspec.htm#FREE) | 10xx |  | ASCII free format |
| [FP](../packspec.htm#FP) | FE08 |  | Internal representation of a KCML number |
| [I](../packspec.htm#ASCIIINT) | 2dxx |  | Legacy ASCII integer format |
| [INT(](../packspec.htm#INT) | Cd0y |  | Integer (signed) |
| [M8](../packspec.htm#WANG) | F008 |  | BASIC-2 internal BCD format |
| [MD3](../packspec.htm#MD3) | FD03 |  | Three byte packed date of the form YYMMDD |
| [MD4](../packspec.htm#PACKDATE) | FD04 |  | Four byte packed date of the form CCYYMMDD |
| [MI4](../packspec.htm#IEEE4) | F304 |  | IEEE floating point L-H little-endian format |
| [MI8](../packspec.htm#IEEE) | F308 |  | IEEE floating point L-H little-endian format |
| [MJ](../packspec.htm#MJ) | F603 | Y | Julian date (replaced by DATE) |
| [MM4](../packspec.htm#MOTOROLA4) | F204 |  | IEEE floating point H-L big-endian format |
| [MM8](../packspec.htm#MOTOROLA) | F208 |  | IEEE floating point H-L big-endian format |
| [MT](../packspec.htm#MT) | F703 | Y | Time in seconds since midnight (replaced by TIME) |
| [MW8](../packspec.htm#WANG_A) | F008 | Y | BASIC-2 internal BCD format |
| [NUM(](../packspec.htm#NUM) |  |  | Numeric (signed) |
| [O+](../packspec.htm#OVERFLOW) | 7d0y |  | Packed decimal format with binary overflow |
| [P](../packspec.htm#USIGN) | 6dxx |  | Unsigned packed decimal format |
| [P+](../packspec.htm#PACK) | 5d0y |  | IBM packed decimal format |
| [SY8](../packspec.htm#SYM) | FE08 | Y | Internal representation of a KCML number (replaced by FP) |
| [TIME](../packspec.htm#TIME) | F703 |  | Time in seconds since midnight |
| [TS4](../packspec.htm#TS4) |  |  | Time stamp in seconds since 1970-01-01T0000Z held in 4 bytes |
| [U](../packspec.htm#IBM8) | 4dxx |  | IBM USASCII-8 format |
| [UINT(](../packspec.htm#UINT) | Bd0y |  | Integer (unsigned) |
| [UNUM(](../packspec.htm#UNUM) |  |  | Numeric (unsigned) |
| [W](../packspec.htm#SIGN) | 8d0y |  | Wang signed packed decimal format as in PACK |
| [WE](../packspec.htm#EVENSIGN) | 9d0y |  | Wang signed packed decimal format with even number of digits |
| [X](../packspec.htm#INFORMIX) |  |  | Informix money format |

Where:\
d = number of implied decimal places\
xx = field width in binary (xx \> 0)\
y = field width in binary (0 \< y \< +6)

## Packing formats for string fields

| Format | \$PACK code | Legacy | Purpose |
|----|----|----|----|
| [CHAR(](../packspec.htm#CHAR) |  |  | Character field (presumed to be UTF-8 encoded) |
| [HEX(](../packspec.htm#HEX) |  |  | Binary field |
| [LANG(](../packspec.htm#LANG) |  |  | Multi-language string field |
| [MB](../packspec.htm#MB) | FA01 | Y | Legacy boolean with "Y" for TRUE and "N" for FALSE |
| [TEXT(](../packspec.htm#TEXT) |  |  | Multiline text field |
| [TIMESTAMP](../packspec.htm#TIMESTAMP) |  |  | TIMESTAMP conversion from TS6 to 0000-00-00 00:00:00.000Z format |
| [TS6](../packspec.htm#TS6) |  |  | Time stamp in milliseconds since 0000-00-00 00:00:00.000Z held in 6 bytes |

Where:\
d = number of implied decimal places\
xx = field width in binary (xx \> 0)\
y = field width in binary (0 \< y \< +6)

## Extended string \$PACK(E) formats

These are not available for fields.

<span id="extended"></span>

| Format | \$PACK code | Legacy | Purpose |
|----|----|----|----|
| [BASE64](../packspec.htm#BASE64) |  |  | BASE64 encoding |
| [BITS(](../packspec.htm#BITS) |  |  | Count set bits in a string |
| [BOOL](../packspec.htm#BOOLEAN) |  |  | Numeric boolean with "1" for TRUE and "0" for FALSE |
| [CHAR(](../packspec.htm#CHAR) |  |  | Character field (presumed to be UTF-8 encoded) |
| [HEX(](../packspec.htm#HEX) |  |  | Binary field |
| [LANG(](../packspec.htm#LANG) |  |  | Multi-language string field |
| [META](../packspec.htm#METAPHONE) |  |  | METAPHONE phoneme encoding |
| [NUM(](../packspec.htm#NUM) |  |  | Numeric (signed) |
| [SNDX](../packspec.htm#SOUNDEX) |  |  | SOUNDEX encoding |
| [TEXT(](../packspec.htm#TEXT) |  |  | Multiline text field |
| [TIMESTAMP](../packspec.htm#TIMESTAMP) |  |  | TIMESTAMP conversion from TS6 to 0000-00-00 00:00:00.000Z format |
| [TS4](../packspec.htm#TS4) |  |  | Time stamp in seconds since 1970-01-01T0000Z held in 4 bytes |
| [TS6](../packspec.htm#TS6) |  |  | Time stamp in milliseconds since 0000-00-00 00:00:00.000Z held in 6 bytes |
| [UNUM(](../packspec.htm#UNUM) |  |  | Numeric (unsigned) |
| [URL](../packspec.htm#URL) |  |  | URL encoding |
| [UTF-16](../packspec.htm#UTF16) |  |  | UTF-16, UCS-2 or Unicode encoding |
| [UTF-16+](../packspec.htm#UTF16P) |  |  | UTF-16, UCS-2 or Unicode encoding |
| [UTF-16BE](../packspec.htm#UTF16BE) |  |  | UTF-16, UCS-2 or Unicode encoding, big-endian |
| [UTF-16BE+](../packspec.htm#UTF16BEP) |  |  | UTF-16, UCS-2 or Unicode encoding, big-endian, with XML encoding |
| [UTF-16LE](../packspec.htm#UTF16LE) |  |  | UTF-16, UCS-2 or Unicode encoding, little-endian |
| [UTF-16LE+](../packspec.htm#UTF16LEP) |  |  | UTF-16, UCS-2 or Unicode encoding, little-endian, with XML encoding |
| [UTF-32](../packspec.htm#UTF32) |  |  | UTF-32 or UCS-4 encoding |
| [UTF-32+](../packspec.htm#UTF32P) |  |  | UTF-32 or UCS-4 encoding with XML encoding |
| [UTF-32BE](../packspec.htm#UTF32BE) |  |  | UTF-32 or UCS-4 encoding, big-endian |
| [UTF-32BE+](../packspec.htm#UTF32BEP) |  |  | UTF-32 or UCS-4 encoding, big-endian, with XML encoding |
| [UTF-32LE](../packspec.htm#UTF32LE) |  |  | UTF-32 or UCS-4 encoding, little-endian |
| [UTF-32LE+](../packspec.htm#UTF32LEP) |  |  | UTF-32 or UCS-4 encoding, little-endian, with XML encoding |
| [UTF-8](../packspec.htm#UTF8) |  |  | UTF-8 encoding |
| [UTF-8+](../packspec.htm#UTF8PLUS) |  |  | UTF-8 and XML encoding |
| [X](../packspec.htm#INFORMIX) |  |  | Informix money format |
| [XML](../packspec.htm#XML) |  |  | XML entity encoding format |

## \$PACK(F) formats

<span id="field"></span>

| Format | \$PACK code | Legacy | Purpose |
|----|----|----|----|
| [A](../packspec.htm#ALPHA) | A000 | Y | Alphanumeric format |
| [A(](../packspec.htm#ALANG) | A000 | Y | Alphanumeric multi-language format |
| [B](../packspec.htm#BINARY) | Bd0y | Y | Unsigned binary format |
| [B+](../packspec.htm#SBINARY) | Cd0y | Y | Signed binary format |
| [BR](../packspec.htm#BR) | Dd0y |  | Byte swapped (little-endian) unsigned binary format |
| [BR+](../packspec.htm#BRP) | Ed0y |  | Byte swapped (little-endian) signed binary format |
| [C](../packspec.htm#COMP) | A100 |  | Compressed alphanumeric format |
| [D](../packspec.htm#DISP) | 3dxx |  | IBM display format |
| [DATE](../packspec.htm#DATE) | F603 |  | Julian date |
| [F](../packspec.htm#FREE) | 10xx |  | ASCII free format |
| [FP](../packspec.htm#FP) | FE08 |  | Internal representation of a KCML number |
| [I](../packspec.htm#ASCIIINT) | 2dxx |  | Legacy ASCII integer format |
| [INT(](../packspec.htm#INT) | Cd0y |  | Integer (signed) |
| [M8](../packspec.htm#WANG) | F008 |  | BASIC-2 internal BCD format |
| [MB](../packspec.htm#MB) | FA01 | Y | Legacy boolean with "Y" for TRUE and "N" for FALSE |
| [MD3](../packspec.htm#MD3) | FD03 |  | Three byte packed date of the form YYMMDD |
| [MD4](../packspec.htm#PACKDATE) | FD04 |  | Four byte packed date of the form CCYYMMDD |
| [MI4](../packspec.htm#IEEE4) | F304 |  | IEEE floating point L-H little-endian format |
| [MI8](../packspec.htm#IEEE) | F308 |  | IEEE floating point L-H little-endian format |
| [MJ](../packspec.htm#MJ) | F603 | Y | Julian date (replaced by DATE) |
| [MM4](../packspec.htm#MOTOROLA4) | F204 |  | IEEE floating point H-L big-endian format |
| [MM8](../packspec.htm#MOTOROLA) | F208 |  | IEEE floating point H-L big-endian format |
| [MT](../packspec.htm#MT) | F703 | Y | Time in seconds since midnight (replaced by TIME) |
| [MW8](../packspec.htm#WANG_A) | F008 | Y | BASIC-2 internal BCD format |
| [O+](../packspec.htm#OVERFLOW) | 7d0y |  | Packed decimal format with binary overflow |
| [P](../packspec.htm#USIGN) | 6dxx |  | Unsigned packed decimal format |
| [P+](../packspec.htm#PACK) | 5d0y |  | IBM packed decimal format |
| [SKIP](../packspec.htm#SKIP) | 00xx |  | Skip field |
| [SY8](../packspec.htm#SYM) | FE08 | Y | Internal representation of a KCML number (replaced by FP) |
| [TIME](../packspec.htm#TIME) | F703 |  | Time in seconds since midnight |
| [U](../packspec.htm#IBM8) | 4dxx |  | IBM USASCII-8 format |
| [UINT(](../packspec.htm#UINT) | Bd0y |  | Integer (unsigned) |
| [W](../packspec.htm#SIGN) | 8d0y |  | Wang signed packed decimal format as in PACK |
| [WE](../packspec.htm#EVENSIGN) | 9d0y |  | Wang signed packed decimal format with even number of digits |

Where:\
d = number of implied decimal places\
xx = field width in binary (xx \> 0)\
y = field width in binary (0 \< y \< +6)

## \$PACK(F) pack codes

| \$PACK spec | format | Deprecated | Purpose |
|----|----|----|----|
| 00xx | [SKIP](../packspec.htm#SKIP) |  | Skip field |
| 10xx | [F](../packspec.htm#FREE) |  | ASCII free format |
| 2dxx | [I](../packspec.htm#ASCIIINT) |  | Legacy ASCII integer format |
| 3dxx | [D](../packspec.htm#DISP) |  | IBM display format |
| 4dxx | [U](../packspec.htm#IBM8) |  | IBM USASCII-8 format |
| 5d0y | [P+](../packspec.htm#PACK) |  | IBM packed decimal format |
| 6dxx | [P](../packspec.htm#USIGN) |  | Unsigned packed decimal format |
| 7d0y | [O+](../packspec.htm#OVERFLOW) |  | Packed decimal format with binary overflow |
| 8d0y | [W](../packspec.htm#SIGN) |  | Wang signed packed decimal format as in PACK |
| 9d0y | [WE](../packspec.htm#EVENSIGN) |  | Wang signed packed decimal format with even number of digits |
| A000 | [A](../packspec.htm#ALPHA) | Y | Alphanumeric format |
| A000 | [A(](../packspec.htm#ALANG) | Y | Alphanumeric multi-language format |
| A100 | [C](../packspec.htm#COMP) |  | Compressed alphanumeric format |
| Bd0y | [B](../packspec.htm#BINARY) | Y | Unsigned binary format |
| Bd0y | [UINT(](../packspec.htm#UINT) |  | Integer (unsigned) |
| Cd0y | [B+](../packspec.htm#SBINARY) | Y | Signed binary format |
| Cd0y | [INT(](../packspec.htm#INT) |  | Integer (signed) |
| Dd0y | [BR](../packspec.htm#BR) |  | Byte swapped (little-endian) unsigned binary format |
| Ed0y | [BR+](../packspec.htm#BRP) |  | Byte swapped (little-endian) signed binary format |
| F008 | [M8](../packspec.htm#WANG) |  | BASIC-2 internal BCD format |
| F008 | [MW8](../packspec.htm#WANG_A) | Y | BASIC-2 internal BCD format |
| F108 | [MN](../packspec.htm#NIAKWA) |  | BASIC-2C internal format |
| F204 | [MM4](../packspec.htm#MOTOROLA4) |  | IEEE floating point H-L big-endian format |
| F208 | [MM8](../packspec.htm#MOTOROLA) |  | IEEE floating point H-L big-endian format |
| F304 | [MI4](../packspec.htm#IEEE4) |  | IEEE floating point L-H little-endian format |
| F308 | [MI8](../packspec.htm#IEEE) |  | IEEE floating point L-H little-endian format |
| F603 | [MJ](../packspec.htm#MJ) | Y | Julian date (replaced by DATE) |
| F603 | [DATE](../packspec.htm#DATE) |  | Julian date |
| F703 | [MT](../packspec.htm#MT) | Y | Time in seconds since midnight (replaced by TIME) |
| F703 | [TIME](../packspec.htm#TIME) |  | Time in seconds since midnight |
| FA01 | [MB](../packspec.htm#MB) | Y | Legacy boolean with "Y" for TRUE and "N" for FALSE |
| FD03 | [MD3](../packspec.htm#MD3) |  | Three byte packed date of the form YYMMDD |
| FD04 | [MD4](../packspec.htm#PACKDATE) |  | Four byte packed date of the form CCYYMMDD |
| FE08 | [SY8](../packspec.htm#SYM) | Y | Internal representation of a KCML number (replaced by FP) |
| FE08 | [FP](../packspec.htm#FP) |  | Internal representation of a KCML number |
