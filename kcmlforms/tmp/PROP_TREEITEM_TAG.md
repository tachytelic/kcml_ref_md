Tag\$ (treeitem control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Per item property for programmer use**

This string property can be use to assocaite an arbitrary string with a node in the tree. The string contents have no significance to the behaviour of the tree. Typically it is used by programmers to associate a database key or some other identifier with the the node so that it can be recalled if the user selects the node. The property can be applied to either an object reference to an existing tree node or the [Item()](PROP_TREE_ITEM.htm) method and the existing node's index. .treeControl1.Item(NodeIndex).Tag\$ = dbkey\$

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
