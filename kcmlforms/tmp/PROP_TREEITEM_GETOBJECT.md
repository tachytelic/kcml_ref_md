GetObject (treeitem control method)

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
<td>Appears in<br />
browser</td>
<td>Advanced</td>
<td>KCML<br />
6.10+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> GetObject() Method

**Store an arbitrary object**

This method allows the programmer to retrieve an object previously associated a tree node. The object is stored using the [SetObject](PROP_TREEITEM_SETOBJECT.htm) method. The method can be applied to either an object reference to an existing tree node or the [Item()](PROP_TREE_ITEM.htm) method and the existing node's index. OBJECT DomNode = treeitem.GetObject()

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
