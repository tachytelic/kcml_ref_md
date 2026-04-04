LeftDblClk (tree control event)

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

**Left double click**

This event handler is called if the user left double clicks on a node or a leaf within the tree. The [Index](PROP_GENERIC_DATAPTR.htm) property is available within this event handler to determine which item the user double clicked on. For example, the following could be used to return the text associated with the item that the user selected: SelItem\$ = ..Item(..Index).Text\$

Note that if the [LeftClick()](PROP_TREE_LEFTCLICK.htm) event handler exists then it is called prior to *LeftDblClick().*

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
