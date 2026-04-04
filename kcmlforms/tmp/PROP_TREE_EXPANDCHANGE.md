ExpandChange (tree control event)

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

**Occurs when an item is expanded or collapsed (other than when an Expand event occurs)**

This event handler is called each time a tree control branch is expanded or collapsed. The [*Expanded* property can be used to determine if the branch is being expanded or collapsed, a value of ***TRUE*** means that the branch has been expanded. If the branch is being expanded for the first time then the](PROP_TREEITEM_EXPANDED.htm) [*Expand()* event is called instead. If the branch is then collapsed and later re-expanded then only the *ExpandChange()* event is called.](PROP_TREE_EXPAND.htm)

Tree branches are either expanded and collapsed by the user or they can be expanded and collapsed under program control using the [*Expand()* and](PROP_TREEITEM_EXPAND.htm) [*Collapse()* methods.](PROP_TREEITEM_COLLAPSE.htm)

##### Example:


     DEFEVENT Form1.treeControl.ExpandChange()

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
