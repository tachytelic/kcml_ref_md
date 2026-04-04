Child (treeitem control property)

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
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Get index of first child item**

This property returns the first child for a given tree node. It can be used in conjunction with either an object reference to an existing tree node or the [Item()](PROP_TREE_ITEM.htm) method and an Index. It returns an [index](PROP_GENERIC_DATAPTR.htm) which will be zero if there are no children. ChildIndex = .treeControl1.Item(ItemIndex).Child

The [Child](PROP_TREEITEM_GETOCHILD.htm) property can also be used to return an object.

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
