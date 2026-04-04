\$PACK field specifiers

------------------------------------------------------------------------

The field and extended forms of [\$PACK]($PACK.htm) and [\$UNPACK]($UNPACK.htm) store data in the buffer in specified fields. Each specification contains two bytes, the first specifies the field type, the second specifies the field width. The alternative mnemonic form is used in [\$FORMAT]($FORMAT.htm) and [FLD()](FLD(.htm) definitions.

------------------------------------------------------------------------

Field specifiers

These new specifiers, introduced with KCML 6.10, can be used in field definitions, e.g. in [DEFRECORD](DEFRECORD.htm) [FLD](FLD.htm) statements or in the extended form of [\$PACK]($PACK.htm). The are to be preferred over the older BASIC-2 compatible codes.

CHAR(n)

A UTF-8 character string of length *n* bytes.

TEXT(x,y)

A UTF-8 character string representing a multiline object with *y* lines each of maximum length *x* bytes for a storage size of *x\*y* bytes. This type is interpreted by the forms data aware mechanism as requiring a multiline edit.

LANG(x,y)

A UTF-8 character string representing a multilanguage object with an array of *y* strings each of maximum length *x* bytes for a storage size of *x\*y* bytes. The string actually used as the value of the field is controlled by the current value of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20) byte 20. If this value is not in the range 1 to *y* then the first string is used.

INT(n)

Signed integer stored in *n* bytes where n can be up to 6 bytes though it is inefficiently packed if more than 4 bytes.

UINT(n)

Unsigned integer stored in *n* bytes where n can be up to 6 bytes though it is inefficiently packed if more than 4 bytes.

NUM(p,s)

This represents a signed packed BCD number with a precision of *p* and an optional scale of *s*. The maximum precision supported is currently 13 in KCML 6.10 though this may be increased in a future version of KCML.

UNUM(p,s)

This represents an unsigned packed BCD number with a precision of *p* and an optional scale of *s*. The maximum precision supported is currently 13 in KCML 6.10 though this may be increased in a future version of KCML.

FP

This represents a floating point number stored in the internal number format used by KCML. This format is independent of machine architecture and byte ordering currently and as such it is an efficient format for packing and unpacking however it should not be used in database rows as the format may change for future versions of KCML. Its best use is in DEFRECORD FLDs used only in programs and not saved to the database. This format was called SY8 in some versions of KCML 6.0 but that name is no longer supported.

DATE

This represents [Julian date](JulianDate.htm) stored in three bytes. It replaces the legacy [MD](#JDATE) format.

TIME

This represents a time counted in seconds since midnight. This replaces the legacy [MT](#MT) format.

TIMESTAMP

This represents a GMT time stamp stored in six bytes and giving the number of milliseconds since a fixed date in the past (the start of the Common Era 0000-01-01T00:00Z). It was introduced for KCML 6.10 and replaces the TS6 pack format which is now obsolete and the TS4 format which is less accurate.

BOOL

This represents a Boolean value stored in one byte as "0" for FALSE and "1" for TRUE though for compatibility with the legacy [MB](#MB) format, it will also unpack "Y" as TRUE and "N" and FALSE.

------------------------------------------------------------------------

Original pack formats

SKIP (00xx)

Skip xx characters.

ASCII Free Format (10xx)

ASCII free format is a displayable format equivalent to that produced by [PRINT](PRINT.htm)ing a numeric value. The format is made up of a sign byte, the mantissa and the optional exponent.

ASCII integer format (2dxx)

ASCII integer format is also a displayable format, all digits are stored as the ASCII representation of the number. Note there are no parentheses and this format can be easily confused with the more common [INT()](#INTEGER).

IBM display format (3dxx)

In IBM display format the digits are stored 1 digit per byte, in the form HEX(Fd) where \`d' is the digit to be stored (0 - 9). The sign is stored in the high order nibble of the last byte in the field, it is set to \`D' for a negative number and \`C' for a positive number.

IBM USASCII Format (4dxx)

In IBM USASCII format the digits are stored 1 digit per byte in the form HEX(5d) where \`d' is the digit to be stored (0 - 9). As with IBM display format, the sign is stored in the high order nibble of the last byte in the field. It is set to \`B' for a negative number and \`A' for a positive number.

IBM Packed decimal format (5dxx)

In IBM packed decimal format, digits are stores 2 digits per byte in the form hex(dd), where \`dd' are the digits to be packed. The sign is stored in the low order nibble of the last byte in the field and is set to \`D' for a negative number and \`C' for a positive number. The format will overflow into a special binary format if the number cannot be packed in BCD format. Widths of up to 6 bytes are allowed. The number to be packed must not exceed 9,999,999,999,999. The low order nibble of the last byte in the field identifies the value as being either packed decimal or binary. If the low order nibble is HEX(C - F), then the value is packed decimal (same as 5dxx). If the value is HEX(0 - B), the value is binary.

Unsigned Packed decimal (6dxx)

Unsigned packed decimal stores 2 digits per byte in the form HEX(dd), where \`dd' are the digits to be packed. No sign is stored.

Packed Decimal with Binary Overflow Format (7d0y)

The Packed Decimal with Binary Overflow Format is used to pack numeric values. The number is stored in packed decimal format if it fits into the specified field. The maximum field length allowed is 6. If the number is too large to be stored in packed decimal format, it is converted and stored in binary format. If the number is still too large for the field, an error (X71) results. The last hexdigit of the packed value identifies the type of format used to pack the number, HEX(C-F) the value is packed in decimal format, HEX(0-B) the value is packed in binary format.

Unsigned binary (Bd0y)

A field width of up to 6 bytes is supported though it is relatively inefficient above 4 bytes. Twos complement representation is used. This name is now deprecated in favor of UINT().

Signed binary (Cd0y)

A field width of up to 6 bytes is supported though it is relatively inefficient above 4 bytes. This name is now deprecated in favor of INT().

Byte swapped unsigned binary (Dd0y)

A field width of up to 6 bytes is supported though it is relatively inefficient above 4 bytes. Byte swapped means lowest byte first.

Byte swapped signed binary (Ed0y)

A field width of up to 6 bytes is supported though it is relatively inefficient above 4 bytes. Byte swapped means lowest byte first.

Signed Wang packed (8d0y)

This uses the same representation as the [PACK](PACK.htm) statement where the image contains an explicit sign and an odd number of \`#'s or no sign and an even number of \`#' characters, i.e all the nibbles are accounted for. E.g.

PACK(-#####.##) variable\$ FROM value\
\$PACK(F=HEX(8204)) variable\$ FROM value

are equivalent.

Signed Wang packed (9d0y)

This uses the same representation as the [PACK](PACK.htm) statement where the image contains an explicit sign and an even number of \`#'s or no sign and an odd number of \`#' characters. Because a nibble is unused the bit pattern is left justified and the last nibble is zero. E.g.

PACK(#####.##) a\$ FROM a\
\$PACK(F=HEX(9204)) a\$ FROM a

are equivalent.

Alphanumeric Format (A0xx)

The alphanumeric format field specifier provides a means to simply copy an alphanumeric string.

Compressed Alphanumeric Format (A1xx)

The compressed alphanumeric format field specifier provides a means to more compactly store characters with ASCII values of HEX(20) through to HEX(5F). These include uppercase characters, digits, space, and certain symbols. Other characters in the string to be packed, e.g. lower case characters 'a-z', will overflow and will not unpack correctly . The characters in the string are converted to 6-bit values as offsets from HEX(20) allowing 4 characters in 3 bytes.

<span id="WANG"></span><span id="NIAKWA"></span><span id="MOTOROLA"></span><span id="MOTOROLA4"></span><span id="IEEE"></span><span id="IEEE4"></span>

Floating point format (Ft04, Ft08)

The floating point format allows the internal format to be converted to formats used by external subroutines in other languages. The field width for Wang, BASIC-2C and VAX is always 8. For IEEE it can be 4 or 8 for the IEEE float and double formats. The actual format is determined by the \`t' digit.

|      |                                       |
|------|---------------------------------------|
| F008 | Wang internal numeric format          |
| F108 | BASIC-2C internal numeric format      |
| F204 | IEEE floating point H-L format float  |
| F208 | IEEE floating point H-L format double |
| F304 | IEEE floating point L-H format float  |
| F308 | IEEE floating point L-H format double |
| F408 | VAX floating point format             |

The H-L format of IEEE numbers is currently used with CPUs such as Motorola 680x0, 88000, SUN SPARC, and most other RISCs arhitectures. The byte reversed L-H format is used with Intel x86, DEC Alpha and the DEC version of the MIPs RISC. The VAX floating point format was used with Pyramid MIServer, CCI 6/32 and ICL DRS 700 as well as the VAX.

Count set bits in a string

This field format is available for the extended form of \$UNPACK only. It counts the number of bits set in the string whose length in bytes is given in the mnemonic e.g. BITS(256). The length can be up to 16MB. Prior to KCML 6.10 this format was represented by F=HEX(FBxxxxxx).

DEFSUB 'CountBits(BYREF a\$, len)\
LOCAL DIM a, f\$4\
\$UNPACK(E=\$PRINTF("BITS(%d)", len))a\$ TO a\
RETURN a

Informix money format

Informix money format allows a range of 1E-126 to 1E126, using 1 byte of the field for the exponent and signs, and packing two digits in each subsequent byte. In KCML pripr to 6.10 it was referenced with the HEX(FCxx) packing format so that for instance HEX(FC05), has 8 digits. For KCML6.10 it was replaced by the extended format E="Xnn". The leading digit may be zero so only 7 significant digits can be guaranteed. This format was used with Informix C-ISAM files.

Julian date

This format was used for packing Julian dates into 3 bytes binary. It has in turn been replaced by the mnemonic [DATE](#DATE) as this gives more information.

Time

This format was used for packing the time, specified as seconds since midnight, into 3 bytes binary. It has in turn been replaced by the mnemonic [TIME](#TIME).

Date format (FD03 and FD04)

This format is uses to pack and unpack a Julian date value into either a three or four byte BCD packed string. The FD03 format packs the information as YYMMDD whereas FD04 includes the century information by packing the value as CCYYMMDD.

Boolean

This format is used for packing the the boolean values TRUE and FALSE as "Y" or "N" respectively though this usage is meaningful only in English and is now deprecated. For compatibility with newer applications using the [BOOL](#BOOL) specifier it will also unpack "1" as TRUE and "0" as FALSE. When unpacking any value other than "Y" or "1" will be presumed to be FALSE.

------------------------------------------------------------------------

Extended pack formats

XML suitable format

Convert a string into a form suitable as an XML value, converting **&**, **\<**, **\>**, **"**, **'** and all characters below 0x20 and above 0x7F to **\&amp;**, **\&lt;**, **\&gt;**, **\&quot;**, **\&apos;** and **&#Xnn;** forms. For encoding and decoding trailing spaces are ignored.

URL encoding

Convert a string into a form suitable as a URL, converting all characters first to UTF-8 encoding, using [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE61) byte 61 to indicate the current language code page, and then convert all characters that are not ASCII letters or numbers to **%HH** form. This follows the convention of [RFC1738](http://www.w3.org/Addressing/rfc1738.txt) but is much stricter in that all characters other than A-Z, a-z and 0-9 will be encoded as hexidecimal digits. Note that there is no special handling of spaces or plus characters so if you are unpacking the body of a HTML form POST request then you will want to translate '+' to space with [\$TRAN]($TRAN.htm) e.g. `$TRAN(url$, " +")R`.

BASE64 encoding

Convert a string using base 64 encoding into a form suitable for email attachment etc. For encoding and decoding trailing spaces are ignored. To include trailing spaces use the [STR(](STR(.htm) function.

UTF-8 encoding

Convert a string using UTF-8 encoding and [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE61) byte 61 to indicate the current language code page. For encoding trailing spaces are ignored. To include trailing spaces use the [STR(](STR(.htm) function.

UTF-8+ encoding

This is a combination of UTF-8 and XML, to convert a string into a form suitable as an XML value, first converting to UTF-8, using [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE61) byte 61 to indicate the current language code page, and then converting **&**, **\<**, **\>**, **"**, **'** and all characters below 0x20 to **\&amp;**, **\&lt;**, **\&gt;**, **\&quot;**, **\&apos;** and **&#Xnn;** forms. For encoding and decoding trailing spaces are ignored. To include trailing spaces use the [STR(](STR(.htm) function.

<span id="UTF16"></span><span id="UTF16P"></span><span id="UTF16BE"></span><span id="UTF16LE"></span><span id="UTF16BEP"></span><span id="UTF16LEP"></span>

UTF-16, UTF-16BE, UTF-16LE encoding

These encodings are equivalent to UCS-2, UCS-2BE and UCS-2LE. They convert a UTF-8 string to UTF-16 Bigendian or Littleendian encoding. For UTF-16 the byte order defaults to the byte order of the machine. In order to allow the automatic detection of the byte order, it has become customary on some platforms (notably Win32) to start every Unicode string with the character U+FEFF (ZERO WIDTH NO-BREAK SPACE), also known as the Byte-Order Mark (BOM). Its byte-swapped equivalent U+FFFE is not a valid Unicode character, therefore it helps to unambiguously distinguish the Bigendian and Littleendian variants of UTF-16. To automatically add a BOM add the optional **+** to the specification. For encoding trailing spaces are ignored. To include trailing spaces use the [STR(](STR(.htm) function.

<span id="UTF32"></span><span id="UTF32P"></span><span id="UTF32BE"></span><span id="UTF32LE"></span><span id="UTF32BEP"></span><span id="UTF32LEP"></span>

UTF-32, UTF-32BE, UTF-32LE, encoding

These encodings are equivalent to UCS-4, UCS-4BE and UCS-4LE. They convert a UTF-8 string to UTF-32 Bigendian or Littleendian encoding. For UTF-32 the byte order defaults to the byte order of the machine. In order to allow the automatic detection of the byte order, it has become customary on some platforms (notably Win32) to start every Unicode string with the character U+0000FEFF (ZERO WIDTH NO-BREAK SPACE), also known as the Byte-Order Mark (BOM). Its byte-swapped equivalent U+FFFE0000 is not a valid Unicode character, therefore it helps to unambiguously distinguish the Bigendian and Littleendian variants of UTF-32. To automatically add a BOM add the optional **+** to the specification. For encoding trailing spaces are ignored. To include trailing spaces use the [STR(](STR(.htm) function.

SOUNDEX encoding

This produces a four byte SOUNDEX code representing the sound of the words in the source string. This can be used for fuzzy matching of English language surnames.

METAPHONE encoding

This has a similar purpose to the [SOUNDEX](#SOUNDEX) encoding, but produces a METAPHONE key representing the sound of the words in the source string. The resulting has is a variable sized string. This is likely to be more accurate than soundex as it has a better understanding of the pronunciation of the words used in English surnames. Metaphone was developed by Lawrence Philips and published in the December 1990 issue of Computer Language. It is described in \["Practical Algorithms for Programmers", Binstock & Rex, Addison Wesley, 1995\].
