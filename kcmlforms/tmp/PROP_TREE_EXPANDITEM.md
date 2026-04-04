ExpandItem (tree control property)

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

**Index of expanded item**

This property is used within the [Expand()](PROP_TREE_EXPAND.htm) event handler to determine which node the user is attempting to expand. It can then be used in conjunction with the [Item()](PROP_TREE_ITEM.htm) method to reference the properties of the node.

##### Example:


     n = .treeControl.ExpandItem

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
