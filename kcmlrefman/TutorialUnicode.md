Characters sets and Unicode

Versions of KCML prior to KCML 5.0 used a simple 7 bit character set derived from that used on the Wang 2200 where characters with the HEX(80) bit set were reserved for graphics. This was designed for US English and currency symbols and accented characters not in US-ASCII-7 such as £, é or ä were overloaded onto infrequently used punctuation characters like \|, \[ or { with different mapping for different European countries. The DW and WDW terminal emulators implemented these character sets with special fonts. This meant that data generated in France did not look right when viewed on a terminal setup for the German mapping. Furthermore many languages were not encodable this way and could not therefore be supported in KCML programs.

Starting with KCML5 in 1995, KCML switched to using standard Microsoft Windows 8 bit character sets in the Kclient GUI client though it was still possible to access the graphical character set in text mode programs and the older DW and WDW terminal emulators were still supported for backward compatibility. By using Windows character sets the number of languages supported was greatly extended to include all of Europe as well as Arabic and the MBCS characters sets of Chinese, Japanese and Korean. By default Kclient assumes the Latin-1 or ISO-8859-1 character set that covers most of Western Europe. KClient detects the locale of Windows on the users PC and reports this to the server where it is exposed as a language number in byte 33 of [\$MACHINE]($MACHINE.htm#BYTE33). While this system works well it has some drawbacks, namely

- the code page used for the data is not specified in the data but deduced
- it is not possible to mix two different character sets, e.g. Japanese and Korean or German and Greek on the same form though English is available in all code pages
- some languages are not supported in Windows code pages.

To resolve these issues KCML, starting with version 6.10, now assumes the default encoding for data is UTF-8 encoded Unicode.

Unicode

[Unicode](http://www.unicode.org) is a Industry Standard representation for characters that encompasses all the world languages in one code set. Currently the standard defines up to 65535 code points for this though there is provision for more. It can therefore be encoded in either 16 bit characters, called **UTF-16**, or in one or more 8 bit characters, called **UTF-8**. The first 256 code points align exactly with Latin-1 and thus provide a large degree of compatibility with existing applications.

Unicode is fully implemented in Microsoft Windows NT and partially supported in Windows 95, 98 and ME.

UTF-16 encoding

This is a trivial encoding where each character is represented by two bytes though there is an issue with defining the byte ordering. For English language applications this is a 100% overhead. Furthermore code that searches strings looking for HEX(00) characters will likely fail unless altered. KCML does not use UTF-16 though it provides a mechanism to translate in and out of it using [\$PACK]($PACK.htm)/[\$UNPACK]($UNPACK.htm).

UTF-8 encoding

This is a more complicated encoding where characters HEX(0000) to HEX(007F) are represented in one byte, characters HEX(0080) to HEX(07FF) are represented by two bytes and characters HEX(0800) to HEX(FFFF) are represented in 3 bytes.

|                        |                                  |
|------------------------|----------------------------------|
| HEX(0000) - HEX(007F): | 0*xxxxxxx*                       |
| HEX(0080) - HEX(07FF): | 110*xxxxx* 10*xxxxxx*            |
| HEX(0400) - HEX(FFFF): | 1110*xxxx* 10*xxxxxx* 10*xxxxxx* |

Thus the £ character which was HEX(A3) in Latin-1, and thus is HEX(00A3) in Unicode UTF-16, will be represented as HEX(C2A3) in UTF-8.

The scheme is carefully designed so that the ASCII characters below HEX(80) are represented by a single byte so programs searching for spaces or HEX(00) characters will unambiguously find them. In multibyte sequences all the bytes will have their HEX(80) bit set and the first byte is always in the range HEX(C0) to HEX(FD) indicating how many bytes follow thus allowing resynchronization in corrupt strings. The bytes HEX(FE) and HEX(FF) are never used which supports the traditional use of HEX(FF) in KCML as a padding character.

In English language applications there is no overhead for UTF-8 and applications and their data will be backward compatible. For the Latin alphabet languages used in most of Europe there will be a small overhead for the occasional accented character. However for Greek, encoded as HEX(0370) to HEX(03FF) in Unicode and for Cyrillic languages and Arabic, encoded as HEX(0400-04FF) and HEX(0600-06FF) respectfully, there will be a 100% overhead compared to the native codepages and in the Far East there will be a 50% overhead compared to the DBCS character sets used in KCML 5 though this is ameliorated by the fact that ideographic languages tend to have much shorter strings than alphabetic languages.

KCML support

If the **USING_UTF8** environment variable is set by the connection manager then KCML will consider all data in KDB tables to be UTF-8 encoded and all communications with the client will be in UTF-8.

The KCML 6.10 client will negotiate UTF-8 support with its server. It comes in two versions, one for NT4, Windows 2000 and Windows XP which supports Unicode fully because those operating systems support it, and another for use on Windows 9x and Windows Me which do not properly support Unicode where the client will try to convert UTF-8 strings received from the server into the local codepage of the client.

KCML 6.20 will assume UTF-8 encoding of data by default. There is a extended [\$PACK]($PACK.htm) format (E="UTF8") which allows the conversion of codepage strings in and out of UTF-8 strings and a number of other pack formats that convert between UTF-8 and UTF-16 and UTF-32 in various byte orders. The code page to use in UTF-8 conversions is set via a [language code](LanguageCodes.htm) in byte 61 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE61). This uses operating system locale tables and it may require specific language support to be installed on the server.

- The HEX(01) bit will be set in byte 59 of [\$MACHINE]($MACHINE.htm#BYTE59) if the server is using UTF-8 encoding
- The HEX(08) bit will be set in byte 53 of [\$MACHINE]($MACHINE.htm#BYTE53) if the client uses native Unicode, e.g. on NT4, Windows 2000 or Windows XP.
- To convert between UTF-8 and a native code page use the E="UTF-8" extended [\$PACK]($PACK.htm)/[\$UNPACK]($UNPACK.htm) specifying the code page with byte 61 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE61)
- The [VER](VER(.htm) and [POS](POS(.htm) functions have been extended to support Unicode
- [\$UPPER]($UPPER(.htm) and [\$LOWER]($LOWER(.htm) are also Unicode aware
- \$TRAN in R mode will error if the replacment would change the length of the string.
- The [ULEN8(](ULEN8(.htm)) function can be used to get the number of characters in a UTF-8 string and [LEN(](LEN(.htm) can be used to get the number of bytes.
- The [UNEXT8(](UNEXT8(.htm) and [UPREV8(](UPREV8(.htm) functions can be used to move one Unicode character forward or backward in a string. They return the byte offset of that character.

ULEN8(), UNEXT8() and UPREV8() will behave unpredictably if given data that is not proper UTF-8.

Miscellaneous

The Euro character € is defined as HEX(20AC) in UTF-16 and thus encoded as HEX(E282AC) in UTF-8. Some legacy data may encode this using the Microsoft proprietary encoding of HE(80) which is not a legal UTF-8 character. Note that this character is not implemented in many standard Windows fonts and in particular it is not implemented in the FixedSys font that is the default for the workbench.

Web resources

[Unicode FAQ](http://www.cl.cam.ac.uk/~mgk25/unicode.html) \[cam.ac.uk\]\
[Unicode standard](http://www.unicode.org/unicode/standard/standard.html) \[unicode.org\]
