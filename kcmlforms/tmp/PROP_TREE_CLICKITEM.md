ClickItem (tree control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Provided for 5.02 compatibility - used Index instead**

In KCML5.02 this property was used to indicate which tree node had been selected by clicking. In 5.03 and later it has been obsoleted and new programs must use the [Index](PROP_GENERIC_DATAPTR.htm) property instead to determine the selected node. This property will be removed from the next version of KCML

##### Example:


     n = .treeControl.ClickItem

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
