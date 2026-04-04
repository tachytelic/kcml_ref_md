Changing the font type

The font type for a font set can be change by modifying the

*Name\$* property. When changing font names from the default font you should make sure that the new font exists on the target machine. The following would change the font name for the the *dlgfont1* font set:

.dlgfont1.name\$ = "New Times Roman"

This property can also be used to return the current font name for a font set, for example:

FontName\$ = .dlgfont1.name\$

Note that you cannot change the name of a stock font as it is based on the font used by the form.
