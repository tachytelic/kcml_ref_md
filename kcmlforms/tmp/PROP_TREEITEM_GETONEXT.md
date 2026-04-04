Next (treeitem control property)

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
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Object property

**Get next sibling as an object**

This property returns an object reference for the next sibling of a given tree node. A sibling is a node at the same level in the tree i.e. it shares the same parent node. The property can be used in conjunction with either an object reference to an existing tree node or the [Item()](PROP_TREE_ITEM.htm) method and an Index. It returns an object which will be NULL if there are no further siblings. The property allows a program to traverse across a given level in the tree. OBJECT c = c.Next

The [Level](PROP_TREEITEM_GETLEVEL.htm) property can be used to find the current level in a tree. All siblings share the same level.

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
