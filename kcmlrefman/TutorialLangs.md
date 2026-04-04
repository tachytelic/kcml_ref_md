International support

Client issues

The **KCML** client Kclient is language aware. It supports all the Left to Right Windows languages including the DBCS languages of the Far East. There is also a special version of the earlier Kerridge Windows terminal emulator available for Arabic and Hebrew languages with Right to Left input. This can be used only for text applications.

The Windows 2000 and Windows XP operating systems are also language aware with one core product that can be installed for various locales. Each locale involves installing specific fonts, translated menus and dialogs and defining the keyboard input method or IME. Thus a US version of Windows 2000 can also support both Japanese and Arabic operation by just switching Regional Settings in the control panel and installing the necessary resources from the operating system CD.

Kclient will detect the current default locale and, if supported, will use localized menus and dialogs. The client shipped with KCML 6.20 supports the following languages for menus and dialogs:

- English
- German
- French
- Spanish
- Dutch

There is also partial support for Japanese and Korean.

The default font used for application forms is also set by setting the default locale in the control panel.

[Local printing](LocalPrinters.htm) from the client is, by default, character oriented and sent directly to the selected device. To print DBCS and Arabic languages where the printer driver is responsible for forming the glyphs, the printer must be configured to use direct printing through a printer driver (DIR=Y in [\$DEVICE]($DEVICE.htm)) and the default font for the printer will be taken from the system default. This effectively means that local printing can only be done properly for the default locale though printing in English is supported in almost all locales.

To set a different locale in Windows use the Control Panel\|RegionalOptions dialog:

<img src="bitmaps/RegionalOptions.png" width="404" height="478" alt="Regional Options dialog in control panel" />

The list box at the top determines the locale to be used for this particular user. Setting this is sufficient to get the right default font for forms and for Kclient to pick up the right dialogs and menus. But for local printing to work you will need to set the system default for the machine which requires clicking the default button in the bottom left and setting the system locale.

<img src="bitmaps/SystemLocale.png" width="347" height="194" alt="System locale" />

This will require restarting Windows.

Finally you will want to set the keyboard input method using the Input Locales tab on the Regional Options dialog. This allows you to switch between installed input editors on the fly.

Multilingual strings

The programming language allows strings to be entered in several different languages to allow one set of software to be used in several different countries. These multilingual strings are distinguished from normal strings by being enclosed within chevrons and are valid wherever a quoted string is legal, for example:

color\$=\<\<"Black","Schwarz","Noir"\>\>

Byte 20 of the [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20) system variable is used to determine which string is to be used. This byte should be set before strings are assigned to a one byte binary number. Therefore, if the following was entered before the statement above:


        STR($OPTIONS,20,1)=BIN(3)
        PRINT color$

the French color "Noir" would be returned.

The first string in the chevrons, ("Black" in the example), must be present. There can be up to 254 other strings as alternatives for other languages. The first string is used as the default or if no string has been defined for the chosen language. Each time a statement containing a multilingual string definition is executed, byte 20 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20) is checked, thus allowing the user to change the language at any time. If a value of zero or a value greater that the number of strings actually specified, will result in the default string (string one) being used.

It is also possible to skip strings for a specified language, if they are not relevant, for example:


        PRINT <<"a", "b", , "d">>

would return "a" if the language was set to 3.

A list of the currently standardized language codes may be found [here](LanguageCodes.htm). Kclient will detect the locale of the version of Windows under which it is executing and will inform the server allowing the server to publish the suggested language code in byte 33 of [\$MACHINE]($MACHINE.htm#BYTE33). A multilingual program should use that suggestion to set the language or use it as the default of a prompt for the langauge. However this is not compulsory and a programmer is free to choose a private numbering scheme for byte 20 and the string index in the chevron.

PRINTUSING images

To allow the [PRINTUSING](PRINTUSING.htm) statement to specify a line containing multilingual image statements, the [\$IMAGE]($IMAGE.htm) statement is used instead of the % (image) statement. For example:


    PRINTUSING 9000,total
    $IMAGE<<"£###.##","DM####.##","FF#####.##">>

If byte 20 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20) was set to BIN(2) then the second (German) image would be used.

Miscellaneous

LIST

When a program containing multilingual strings is LISTed only the string matching the language currently selected is shown. By default, byte 20 of \$OPTIONS RUN is set to BIN(1), therefore only the first language string will be shown. All strings can be LISTed by setting this byte to BIN(0).

LIST \<\<

The [LIST \<\<](LISTchevron.htm) statement has been added to list only the program line numbers that contain multilingual strings. Adding an asterisk after the chevrons will list the line and the text containing the string, for example:


    LIST << *

    00030 :::tmp$=<<"Chein">>
    01000 :: IF cl$==<<"Noir"> THEN 9000

Notice that only one item is shown within the chevrons. By setting byte 20 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20) to BIN(0), LIST \<\< will then show all strings.

PRINTUSING separator and currency characters

The default separator characters used by image statements can be changed by setting bytes 5 and 6 of the [\$OPTIONS]($OPTIONS.htm) system variable. Byte 5 changes the replacement character for the comma, for example:


    08000 PRINTUSING 9000,1234567.123
    09000 % $###,###,###.###

would normally output the number as \$1,234,567.123, some countries like France use full stops to divide up the integer portion of the number and a comma to separate the integer portion from the numbers after the decimal point. By setting bytes 5 and 6 of the [\$OPTIONS]($OPTIONS.htm#BYTE5) system variable to HEX(2E) for the full stop and HEX(2C) for the comma respectively the number would be returned as \$1.234.567,123. The default currency symbol can also be changed by setting byte 4 of the [\$OPTIONS]($OPTIONS.htm#BYTE4) system variable.
