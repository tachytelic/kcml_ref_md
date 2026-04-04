TabNext (tabbeditem control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Read<br />
only</td>
<td>Advanced</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Object property

**Get next tab object**

Given a tab page, this property will return, as an object, the next tab on a tab control (or NULL if at the end). The first tab on a tab control is retrieved with [TabFirst](PROP_TABBED_GETFIRST.htm). LOCAL DIM OBJECT t OBJECT t = .tabControl1.TabFirst WHILE OBJECT t \<\> NULL DO REM A tab operation on t. e.g. t.Enabled = TRUE OBJECT t = t.TabNext WEND

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
