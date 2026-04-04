Expand (treeitem control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Expand() Method

**Force expansion of tree item**

This method is used in conjunction with an object reference or the [Item()](PROP_TREE_ITEM.htm) method to expand levels within a tree control. If the level has never been expanded before then the [Expand()](PROP_TREE_EXPAND.htm) event handler is called if it exists. The [ExpandChange()](PROP_TREE_EXPANDCHANGE.htm) event is called each time a level is expanded and again when a level is collapsed. For example: .treeControl1.Item(ItemToExpand).Expand()

Tree levels can be collapsed again with the [Collapse()](PROP_TREEITEM_COLLAPSE.htm) method.

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
