Setting the text in an RTF control

------------------------------------------------------------------------

RTF formatted text can be placed into the control with the

*RichText\$* property. For example,

.rtfControl1.RichText\$ = "{\rtf1\ansi\ansicpg1252\deff0\deftab720{\fonttbl{\f0\fswiss MS Sans Serif;}{\f1\froman\fcharset2 Symbol;}{\f2\froman Times New Roman;}{\f3\froman Times New Roman;}}{\colortbl\red0\green0\blue0;\red0\green0\blue0;}\deflang2057\pard\plain\f2\fs20 \par }"

The previous does not actually place any text in the control it is simply used to default the font type and size etc.

Regular unformatted text can also be sent to the control with the

*Text\$* property.

The text can be retrieved from the control using these same properties.
