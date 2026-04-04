IsSelected (tabbeditem control property)

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
<td>Appears in<br />
browser</td>
<td>Advanced</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**TRUE if this tab page is selected**

This read-only Boolean property returns TRUE if the target tab page is the selected tab page of a tab control. The selected page is the one whose controls are exposed.

Note: This property was introduced under the name .TabVisible in KCML5.02 but was renamed .IsSelectedTab in KCML 5.04.00.5374 as that name more accurately represented what the property means and it resolved an ambiguity with the generic property of that name which was also renamed as [.IsOnSelectedTab](/tmp/PROPNUM_TABVISIBLE.htm). The old name is still supported for now but should not be used.

##### Example:


     IF (.tabbeditem.IsSelected)
       ...
     END IF

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
