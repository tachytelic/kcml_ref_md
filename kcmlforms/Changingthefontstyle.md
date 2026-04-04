Changing the font style

The actual style of a font set can be changed by setting the [*Italic*,](tmp/PROP_FONT_ITALIC.htm) [*Bold, [Underline](tmp/PROP_FONT_UNDERLINE.htm)* and](tmp/PROP_FONT_BOLD.htm)

*Strikeout* properties. These styles are all activated if the property is set to *TRUE*, for example:

.dlgfont1.Italic = TRUE .dlgfont1.Bold = TRUE .dlgfont1.Underline = TRUE .dlgfont1.Strikeout = TRUE

These properties can also be used to test the current style being used by a font set, for example:

IF (.dlgfont1.bold) ... END IF

Note that you cannot change the style of stock fonts.
