Parent (treeitem control property)

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

**Get parent index of this item**

This property returns the index of the parent node of a given tree node. The property can be used in conjunction with either an object reference to an existing tree node or the [Item()](PROP_TREE_ITEM.htm) method and the existing node's index. It returns an [index](PROP_GENERIC_DATAPTR.htm) which will be zero if the current node is the root node. The property allows a program to move up a given level in the tree. ParentIndex = .treeControl1.Item(ChildIndex).Parent

The [Level](PROP_TREEITEM_GETLEVEL.htm) property can be used to find the current level in a tree. The [Parent](PROP_TREEITEM_GETOPARENT.htm) property can also be used to return an object.

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
