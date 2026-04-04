IsOnSelectedTab (generic control property)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
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
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**TRUE if on a tab page that is currently selected**

This read-only Boolean property returns TRUE if the control is on the selected tab page of a tab control. The selected page is the one whose controls are exposed.

If the control is not on a tab the value of the property is unpredictable and should not be used.

Note: This property was introduced under the name .TabVisible in KCML5.02 but was renamed .IsOnSelectedTab in KCML5.04.00.5374 as that name more accurately represented what the property means and it resolved an ambiguity with the tab page property of that name which was also renamed as [.IsSelectedTab](/tmp/PROP_TABBED_TABVISIBLE.htm).

##### Example:


     IF (.generic.IsOnSelectedTab)
       ...
     END IF

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
