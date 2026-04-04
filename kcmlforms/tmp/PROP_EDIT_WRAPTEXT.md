WrapText (kcmledit control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Enable word wrapping**

Normally the text in a multiline edit box will not word wrap when the text typed by the user reaches the end of a line. This is often appropriate if, say, the box contains an address with a fixed number of lines.

However if the control will accept free text then setting this design time property in the forms designer the control will word wrap text to optimally fill the box.

Setting this property to TRUE will cause a vertical scroll bar to appear to make it clear that the text is not formatted.

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
