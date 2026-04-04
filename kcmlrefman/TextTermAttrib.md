Text attributes

Programmers can give characters on the screen attributes of bold, blink and so on by first defining the current attribute with a HEX(0204) sequence and then enabling it with a HEX(0E). The attribute then stays in effect for all subsequent characters printed until a HEX(0F) character is printed, which disables the attribute and restores to the default characters. A carriage return for end of line will also disable the attribute. A later HEX(0E) will switch on the previous attribute.

Attributes are defined with the HEX(0204 *xx yy* 0F) sequence, where *xx* and *yy* are hex digits. This sequence disables any currently enabled attribute. The first digit controls dim, bright and blink attributes while the second controls reverse video and underline attributes. The two digits can be specified independently. Invalid digits are treated as 00.

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td width="8%"><em>xx</em></td>
<td width="8%">00<br />
02<br />
04<br />
08</td>
<td width="33%">Not bright, not blink.<br />
Bright.<br />
Blink.<br />
Bright and Blink.</td>
<td width="8%"><em>yy</em></td>
<td width="7%">00<br />
02<br />
04<br />
08</td>
<td width="36%">Off.<br />
Reverse video.<br />
Underline.<br />
Reverse video and underline.</td>
</tr>
</tbody>
</table>

The HEX(0204 *xx yy* 0F) sequence does not itself enable the newly defined attribute which requires a HEX(0E) however if the HEX(0204 *xx yy* 0E) sequence is used then the attribute is defined and enabled together. An attribute defined in this way is called permanent because it is not disabled at the end of a line but stays in force until an explicit HEX(0F).

Attributes are not affected by [HALT](TextTermHalt.htm) or HEX(03). They are disabled but not redefined by [RESET](TextTermHalt.htm). The [CLEAR](CLEAR.htm) command disables and redefines the current attribute back to the default.
