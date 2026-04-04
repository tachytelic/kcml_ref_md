Bold (treeitem control property)

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
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Set to indicate item has bold text**

This boolean property, if set TRUE, will render the text label for the node in a bold font. The property can be applied to either an object reference to an existing tree node or the [Item()](PROP_TREE_ITEM.htm) method and the existing node's index. .treeControl1.Item(NodeIndex).Bold = TRUE

or to set all the labels in the level below the current node to bold OBJECT node = node.Child WHILE (OBJECT node \<\> NULL) node.Bold = TRUE OBJECT node = node.Next WEND

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
