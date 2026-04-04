Image (treeitem control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Indexed property

**Image shown when item is normal**

This property is used to specify the image used by items within a tree control. If no image is specified then the standard file and folder icons are used. Note that when an item is selected the image specified by the [*OpenImage* property is used. Therefore if you set *Image* you must also set](PROP_TREEITEM_OPENIMAGE.htm) [*OpenImage* otherwise the controls default images will be used when the user selects the item. .treeControl1.Item(Count).Image = &.CD .treeControl1.Item(Count).OpenImage = &.CD](PROP_TREEITEM_OPENIMAGE.htm)

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
