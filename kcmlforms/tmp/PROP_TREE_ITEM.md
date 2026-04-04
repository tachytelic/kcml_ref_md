Item (tree control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Item(int) Method

**Used to access a tree item**

**Int**     The index of the item that is to be modified.

This method is used to provide access to the methods and properties of individual tree items. Items are referenced using the unique index value which is dynamically allocated as each item is added. The index value is returned by the [*Add()* method as each item is added to the tree. For example, the following uses the returns from the](PROP_TREE_ADD.htm) [*Add()* method to create a tree with two levels: First = .treeControl1.Add("First Folder",3) Second = .treeControl1.Item(First).Add("Second Folder", 3) Third = .treeControl1.Item(Second).Add("Item in Second folder",2)](PROP_TREE_ADD.htm)

The [Index](PROP_GENERIC_DATAPTR.htm) property can be used in conjunction with the *Item()* method to operate on the currently selected item. For example the following would change the text label of the currently selected item .treeControl1.Item(.treeControl1.Index).Text\$ = "New text"

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
