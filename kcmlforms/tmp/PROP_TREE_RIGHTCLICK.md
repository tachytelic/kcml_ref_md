RightClick (tree control event)

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

**Right click**

This event handler is called if the user right clicks on a node or a leaf within the tree. The [Index](PROP_GENERIC_DATAPTR.htm) property is available within this event handler to determine the item which was clicked by the the user. For example, the following could be used to return the text associated with the item that the user selected: SelItem\$ = ..Item(..Index).Text\$

Note that this event handler can also be used to display popup menus by calling the [*TrackPopup()* menu control method.](PROP_MENU_TRACKPOPUP.htm)

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
