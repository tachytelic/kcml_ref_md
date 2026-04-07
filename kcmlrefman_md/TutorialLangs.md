# International Support

> Covers multilingual string handling, locale configuration, PRINTUSING image localization, and character set settings for building internationalized KCML applications.

## Description

The KCML client (Kclient) is language-aware and supports all left-to-right Windows languages including the DBCS (double-byte character set) languages of the Far East. A special version of the older Kerridge Windows terminal emulator supports Arabic and Hebrew right-to-left text input for text-mode applications.

Windows 2000 and Windows XP ship as a single core product that can be configured for any locale by installing fonts, translated menus and dialogs, and an appropriate keyboard input method (IME). A US installation of Windows can support Japanese or Arabic operation simply by changing Regional Settings in Control Panel.

Kclient detects the current default locale and uses localized menus and dialogs where available. Kclient shipped with KCML 6.20 supports the following languages for menus and dialogs:

- English
- German
- French
- Spanish
- Dutch

There is also partial support for Japanese and Korean.

The default font used for application forms is set by the default locale in Control Panel.

Local printing from Kclient is by default character-oriented and sent directly to the selected device. To print DBCS or Arabic text where the printer driver is responsible for forming glyphs, the printer must be configured for direct printing through a printer driver (`DIR=Y` in `$DEVICE`). The default font for the printer is taken from the system default, which means local printing works correctly only for the active locale — though English printing is supported in almost all locales.

---

## Multilingual Strings

The KCML programming language allows strings to be entered in multiple languages within a single program. Multilingual strings are enclosed in double chevrons (`<<` ... `>>`) and are valid wherever a quoted string is legal.

### Syntax

```
variable$ = <<"string1","string2","string3",...>>
```

Byte 20 of `$OPTIONS RUN` selects which string is active. Set this byte to a one-byte binary number before using multilingual strings.

### Parameters

| Element | Description |
|---------|-------------|
| `string1` | The default (first/English) string. Always required. |
| `string2` ... `string254` | Alternative language strings. Up to 254 alternatives. |
| `$OPTIONS RUN` byte 20 | Selects the active language: `BIN(1)` = first string, `BIN(2)` = second, etc. `BIN(0)` or a value beyond the number of strings defined returns the default. |

Strings for particular language positions can be omitted (left empty) if they are not relevant:

```kcml
PRINT <<"a", "b", , "d">>
```

With byte 20 set to `BIN(3)`, this returns `"a"` because the third position is empty and the default is used.

### Examples

```kcml
STR($OPTIONS,20,1)=BIN(1)
color$=<<"Black","Schwarz","Noir">>
PRINT color$
```

**Output:**
```
Black
```

```kcml
STR($OPTIONS,20,1)=BIN(3)
color$=<<"Black","Schwarz","Noir">>
PRINT color$
```

**Output:**
```
Noir
```

---

## PRINTUSING Images

To use localized format images with `PRINTUSING`, use the `$IMAGE` statement in place of the `%` image statement:

```kcml
PRINTUSING 9000,total
$IMAGE <<"$###.##","DM####.##","FF#####.##">>
```

If byte 20 of `$OPTIONS RUN` is set to `BIN(2)`, the second (German) image `DM####.##` is used.

---

## Miscellaneous

### LIST

When a program containing multilingual strings is `LIST`ed, only the string matching the currently selected language is shown. By default, byte 20 of `$OPTIONS RUN` is `BIN(1)`, so only the first language string is displayed. Setting byte 20 to `BIN(0)` causes all strings to be shown.

### LIST <<

The `LIST <<` statement lists only the program line numbers that contain multilingual strings. Appending `*` also displays the line text:

```
LIST << *

00030 :::tmp$=<<"Chein">>
01000 :: IF cl$==<<"Noir"> THEN 9000
```

Setting byte 20 to `BIN(0)` before `LIST <<` shows all strings in each chevron.

### PRINTUSING Separator and Currency Characters

The default separator characters used by image statements can be overridden using `$OPTIONS`:

| `$OPTIONS` byte | Default | Purpose |
|----------------|---------|---------|
| Byte 4 | `$` | Default currency symbol |
| Byte 5 | `,` | Thousands separator character |
| Byte 6 | `.` | Decimal separator character |

**Example — French number formatting:**

```
08000 PRINTUSING 9000,1234567.123
09000 % $###,###,###.###
```

Default output: `$1,234,567.123`

With bytes 5 and 6 of `$OPTIONS` set to `HEX(2E)` (`.`) and `HEX(2C)` (`,`) respectively:

Output: `$1.234.567,123`

---

## Setting the Locale in Windows

Use **Control Panel → Regional Options** to configure the locale for the current user. This determines the default font for forms and causes Kclient to pick up the correct dialogs and menus.

For local printing to work correctly, the **system default locale** must also be set (via the Default button in Regional Options). This requires a Windows restart.

Keyboard input methods are configured on the **Input Locales** tab of Regional Options.

---

## Language Code Detection

Kclient detects the locale of the Windows installation and reports a suggested language code in byte 33 of `$MACHINE`. A multilingual program should use this suggestion to set byte 20 of `$OPTIONS RUN`, or use it as the default for a language prompt. Using the `$MACHINE` suggestion is not compulsory; a programmer may use any private numbering scheme.

A list of standardized language codes is in the separate `LanguageCodes` reference.

---

## See Also

- `$OPTIONS RUN` (byte 20 — language selector, byte 4/5/6 — formatting characters)
- `$MACHINE` (byte 33 — client-reported language code)
- `$IMAGE` — multilingual PRINTUSING image statement
- `PRINTUSING`
- `LIST <<`
- `LanguageCodes`
