NoItemRightClick (tree control event)

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
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Right click on a non-item area**

This event handler is called if the user right clicks on a tree control away on a node or a leaf within the tree. It supplements the [RightClick()](PROP_TREE_RIGHTCLICK.htm) event which is triggered by clicking on a tree node or leaf.

Note that this event handler can be used to display popup menus by calling the [*TrackPopup()* menu control method. Use the](PROP_MENU_TRACKPOPUP.htm) [MouseX](PROP_TREE_MOUSEX.htm) and [MouseY](PROP_TREE_MOUSEY.htm) properties to position the popup menu at the point on the control surface the click occurred.

##### Example:


     DEFEVENT Form1.treeControl.NoItemRightClick()

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
