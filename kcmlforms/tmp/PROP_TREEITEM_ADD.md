Add (treeitem control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Add(string, int) Method

**Used to add items to a tree control**

|     |                          |
|-----|--------------------------|
| Str | Text of item to be added |
| Int | Flags                    |

This method is used to add items below the root of a tree control. It is applied to a tree node rather than the control itself. The first parameter specifies the label for the item and the second specifies the flags for the item. The valid flags, which may in some circumstances be combined, are as follows:

|  |  |  |
|----|----|----|
| \_TREE_UNSORTEDCHILD | 0x00 | Default - Unsorted child item |
| \_TREE_PARENT | 0x01 | Parent - The item will be displayed with a +/- button allowing expansion. This implies children will be added. |
| \_TREE_SORT | 0x02 | Sort - Add the item in the correct sorted place |
| \_TREE_SORTREVERSE | 0x04 | Sort reverse - Items are sorted in reverse order |
| \_TREE_FOLDERSFIRST | 0x08 | Folders first - Where some items have children and others do not, the items with children are listed first |

To reverse sort or sort folders-first the flag value must be combined with the \_TREE_SORT sort flag. Thus to reverse sort a flag value of \_TREE_SORT+\_TREE_SORTREVERSE is required. When sorting folders first the parent flag must be set when the parent item is added. The tree is not re-sorted if children are later added to an item created without the parent flag. So when adding items to be sorted folders-first the flag values should be \_TREE_SORT+\_TREE_FOLDERSFIRST or \_TREE_SORT+\_TREE_FOLDERSFIRST+\_TREE_PARENT depending on whether the items do or do not have children.

This method returns a unique [Index](PROP_GENERIC_DATAPTR.htm) which can later be used in conjunction with the [Item()](PROP_TREE_ITEM.htm) method to add child items to a parent level. For example, the following creates a top level parent entry with two second level or child entries. First = .treeControl1.Add("First",\_TREE_SORT+\_TREE_PARENT) .treeControl1.Item(First).Add("Second", \_TREE_SORT) .treeControl1.Item(First).Add("Third", \_TREE_SORT)

The [Expand()](PROP_TREE_EXPAND.htm) event handler is called when the user expands a new level. This allows the addition of items to lower level to be deferred until the user requests the information. This event handler should be used for populating a tree where possible as it is considerably more efficient than adding all the items to the tree in one go.

##### See also:

Other [treeitem](treeitem.htm) properties, methods and events, [tree](tree.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
