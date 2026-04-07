# Character Sets and Unicode

> Explains how KCML handles character encoding — from legacy 7-bit and Windows code-page encodings through to full UTF-8 Unicode support introduced in KCML 6.10.

---

## Background

Versions of KCML prior to 5.0 used a 7-bit character set derived from the Wang 2200. Characters with the `HEX(80)` bit set were reserved for graphics. Accented and currency characters not in US-ASCII-7 (such as `£`, `é`, or `ä`) were overloaded onto infrequently used punctuation characters like `|`, `[`, or `{`, with different mappings for different European countries. This meant data generated in France did not display correctly on a German-configured terminal, and many languages could not be represented at all.

Starting with KCML 5 (1995), KCML switched to standard Microsoft Windows 8-bit code pages in the Kclient GUI client. This greatly extended language coverage to include all of Europe, Arabic, and the MBCS character sets for Chinese, Japanese, and Korean. By default Kclient uses Latin-1 (ISO-8859-1). Kclient detects the Windows locale and reports it to the server as a language number in byte 33 of `$MACHINE`.

The remaining limitations of code-page encoding are:
- The code page in use is deduced from context rather than stored with the data.
- It is not possible to mix two different character sets on the same form (e.g. Japanese and Korean together, or German and Greek together).
- Some languages are not supported by any Windows code page.

To resolve these issues, KCML 6.10 and later use **UTF-8 encoded Unicode** as the default encoding for all data.

---

## Unicode

[Unicode](http://www.unicode.org) is an industry-standard representation for characters covering all the world's languages in a single code set. The standard currently defines up to 65,535 code points. It can be encoded as 16-bit characters (UTF-16) or as sequences of 8-bit bytes (UTF-8). The first 256 Unicode code points correspond exactly to Latin-1, providing a high degree of backward compatibility.

Unicode is fully implemented in Windows NT; it is partially supported in Windows 95, 98, and ME.

---

## UTF-16 Encoding

Each character is represented by exactly two bytes. For English text this is a 100% storage overhead. Code that searches strings for `HEX(00)` characters will likely fail unless adapted. KCML does not use UTF-16 internally but provides translation via `$PACK` / `$UNPACK`.

---

## UTF-8 Encoding

UTF-8 is a variable-width encoding:

| Code point range | Byte pattern |
|-----------------|--------------|
| `HEX(0000)` – `HEX(007F)` | `0xxxxxxx` (1 byte) |
| `HEX(0080)` – `HEX(07FF)` | `110xxxxx 10xxxxxx` (2 bytes) |
| `HEX(0800)` – `HEX(FFFF)` | `1110xxxx 10xxxxxx 10xxxxxx` (3 bytes) |

**Example:** `£` is `HEX(00A3)` in Unicode (UTF-16) and `HEX(C2A3)` in UTF-8.

Key properties of UTF-8:
- ASCII characters below `HEX(80)` are single bytes, so code that searches for spaces or `HEX(00)` works without modification.
- In multi-byte sequences all bytes have the `HEX(80)` bit set; the first byte is always in the range `HEX(C0)`–`HEX(FD)` and indicates how many bytes follow, allowing resynchronisation in corrupt strings.
- `HEX(FE)` and `HEX(FF)` are never used, preserving the traditional KCML use of `HEX(FF)` as a padding character.

Storage overhead compared to native encodings:
- **English / US-ASCII:** zero overhead.
- **Latin-alphabet European languages:** small overhead for occasional accented characters.
- **Greek (`HEX(0370)`–`HEX(03FF)`), Cyrillic (`HEX(0400)`–`HEX(04FF)`), Arabic (`HEX(0600)`–`HEX(06FF)`):** 100% overhead versus native code pages.
- **Far East ideographic (CJK):** ~50% overhead versus DBCS, partially offset by shorter average string lengths in ideographic languages.

---

## KCML UTF-8 Support

If the `USING_UTF8` environment variable is set by the connection manager, KCML treats all data in KDB tables as UTF-8 encoded and all client communications use UTF-8.

**KCML 6.10** introduced the UTF-8 client, available in two variants:
- **NT4 / Windows 2000 / Windows XP** — full Unicode support, because those operating systems support it natively.
- **Windows 9x / Windows Me** — limited support; the client attempts to convert UTF-8 strings received from the server into the local code page.

**KCML 6.20** assumes UTF-8 encoding of all data by default.

### Key features

| Feature | Detail |
|---------|--------|
| `$PACK` / `$UNPACK` extended format `E="UTF8"` | Converts between code-page strings and UTF-8 strings |
| Byte 61 of `$OPTIONS RUN` | Code page to use in UTF-8 conversions, expressed as a language code |
| Byte 59 of `$MACHINE`, bit `HEX(01)` | Set when the server is using UTF-8 encoding |
| Byte 53 of `$MACHINE`, bit `HEX(08)` | Set when the client uses native Unicode (NT4, Windows 2000, Windows XP) |
| `VER(` and `POS(` | Extended to support Unicode character counting |
| `$UPPER(` and `$LOWER(` | Unicode-aware case conversion |
| `$TRAN` in R mode | Errors if the replacement would change the byte length of the string |
| `ULEN8(` | Returns the number of Unicode characters in a UTF-8 string |
| `LEN(` | Returns the number of bytes (not characters) in a string |
| `UNEXT8(` | Returns the byte offset of the next Unicode character forward in a UTF-8 string |
| `UPREV8(` | Returns the byte offset of the previous Unicode character in a UTF-8 string |

**Note:** `ULEN8()`, `UNEXT8()`, and `UPREV8()` behave unpredictably if passed data that is not valid UTF-8.

---

## The Euro Character

The Euro sign `€` is `HEX(20AC)` in Unicode and `HEX(E282AC)` in UTF-8. Some legacy data may use the Microsoft proprietary encoding `HEX(80)`, which is not valid UTF-8. The Euro character is absent from many standard Windows fonts and is not implemented in the FixedSys font used as the default in the KCML Workbench.

---

## See Also

- `$PACK` / `$UNPACK` — code-page and Unicode conversion
- `ULEN8(` — character count of a UTF-8 string
- `UNEXT8(` / `UPREV8(` — navigate by Unicode character in a UTF-8 string
- `$OPTIONS RUN` byte 61 — UTF-8 conversion code page
- `$MACHINE` bytes 53 and 59 — client/server Unicode capability flags
- [Unicode FAQ](http://www.cl.cam.ac.uk/~mgk25/unicode.html)
- [Unicode Standard](http://www.unicode.org/unicode/standard/standard.html)
