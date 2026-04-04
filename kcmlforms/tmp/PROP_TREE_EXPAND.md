Expand (tree control event)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Occurs when an item is expanded for the first time**

This event handler is called when the user attempts to expand a new tree branch. It will also be called when the [Expand()](PROP_TREEITEM_EXPAND.htm) method is called. It is only called once for each unique branch and therefore will not be called if the user later collapses and re-expands the branch. This makes this a suitable place to populate tree nodes on demand. If the branch is never expanded then the population will not take place.

The [ExpandItem](PROP_TREE_EXPANDITEM.htm) property is used to determine the unique index of the branch. This property can then be used with the [Item()](PROP_TREE_ITEM.htm) and [Add()](PROP_TREE_ADD.htm) methods to add items to the branch before it is displayed, for example: DEFEVENT Form1.tree1.Expand() LOCAL DIM a a = ..ExpandItem ..Item(a).Add("New node", 0) END EVENT

The [ExpandChange()](PROP_TREE_EXPANDCHANGE.htm) event is generated whenever a node is expanded or collapsed, except when an Expand() event is generated first.

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
