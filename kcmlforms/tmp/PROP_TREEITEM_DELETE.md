Delete (treeitem control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Delete() Method

**Used to delete this item (and its children)**

This method deletes and frees a node and all its children. The method can be applied to either an object reference to an existing tree node or the [Item()](PROP_TREE_ITEM.htm) method and the existing node's index. .treeControl1.Item(NodeIndex).Delete()

or to prune a tree below the given level OBJECT node = node.Child WHILE (OBJECT node \<\> NULL) OBJECT nextnode = node.Next node.Delete() OBJECT node = nextnode WEND

It is polymorphic with the [Delete()](PROP_TREE_DELETE.htm) method which deletes whole trees when applied directly to a tree control.

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
