Visible (tabbeditem control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Makes a tab page visible/invisible**

This property, when set to FALSE, is used to temporarily remove the specified tab page from a tab control. Tabs are initially visible unless set otherwise by the tab editor in the Forms Designer. Setting it to TRUE will restore it in its original position. If the target tab page is the current page when the property is set to FALSE then the next visible, enabled page in left to right order becomes the new current page . For example: .TabControl1.tab1.Visible = FALSE

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
