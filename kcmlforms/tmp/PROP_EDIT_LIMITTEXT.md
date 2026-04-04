LimitText (edit control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Used to restrict the amount of text entered into the control**

This property allows the maximum length of a string entered into an edit box to be restricted. For example: .EditControl1.LimitText = 40

The [*MaxText()* text event handler is called, if it exists, when the text limit set by *LimitText* is reached.](PROP_EDIT_MAXTEXT.htm)

##### See also:

Other [edit](edit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
