TabFirst (tabbed control property)

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

**Get first tab object**

The **TabFirst** property returns the first tab page of a tab control as an object. It may be used in conjunction with [TabNext](PROP_TABBED_GETNEXT.htm) to programmatically move through the tabs on a tab control. This method should be used with the tab control but it returns a tab page object. LOCAL DIM OBJECT t OBJECT t = .tabControl1.TabFirst

##### See also:

Other [tabbed](tabbed.htm) properties, methods and events, [tabbeditem](tabbeditem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
