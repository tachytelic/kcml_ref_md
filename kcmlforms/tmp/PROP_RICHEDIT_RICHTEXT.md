RichText\$ (richedit control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**The text of the the control in rich text format**

This property is used to set or return the contents of the control in RTF format. The [*Text\$* property can be used to return the unformatted text.](PROPSTR_TITLE.htm)

For example, the following could be used to place some formatted text into the control: .rtfControl1.RichText\$ = "{\rtf1\ansi\ansicpg1252\deff0\deftab720{\fonttbl{\f0\fswiss MS Sans Serif;}{\f1\froman\fcharset2 Symbol;}{\f2\fswiss\fprq2 Arial;}}{\colortbl\red0\green0\blue0;\red255\green0\blue0;}\deflang2057\pard\plain\f2\fs72\cf1 Hello World!\plain\f0\fs17 \par }"

and the following would retrieve both the formatted and unformatted text from the control: Formatted\$ = .rtfControl1.RichText\$ Unformatted\$ = .rtfControl1.Text\$

**Note:** The Text\$ and RichText\$ properties are returned from the client. They will be correct and agree on entry to an event handler, but modifications to a rich text control within an event handler will not cause these properties to be updated until the event handler has completed.

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
