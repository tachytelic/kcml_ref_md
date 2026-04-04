SelChange (tree control event)

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

**Occurs when a node is selected or deselected**

This event handler is called each time an item is selected within the tree. If the item is selected using the mouse and there is a [LeftClick()](PROP_TREE_LEFTCLICK.htm) event handler as well, then only the LeftClick() and not the SelChange() event will be generated. Using the cursor keys will still generate SelChange() events.

##### Example:


     DEFEVENT Form1.treeControl.SelChange()

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
