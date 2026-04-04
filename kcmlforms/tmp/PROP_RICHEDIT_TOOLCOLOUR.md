ToolColor (richedit control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
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
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Set if colors should appear on the toolbar**

If this property is set to ***TRUE*** (the default) then the Color selection combo box option is added to the toolbar. If ***FALSE*** then it will not appear and if there are no other toolbar styles enabled ([ToolStyle](PROP_RICHEDIT_TOOLSTYLE.htm) and [ToolFont](PROP_RICHEDIT_TOOLFONT.htm)) then no editing toolbar will be displayed.

This property is a design time only property that has no effect if changed under program control.

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
