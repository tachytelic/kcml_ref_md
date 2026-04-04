HasButtons (tree control property)

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
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Set if the tree display images against each item**

A tree that has this style property set to TRUE adds a button to the left side of each parent item. The user can click the button once instead of double-clicking the parent item to expand or collapse the child.

Note that this style does not add buttons to items at the root of the hierarchy. To do so, you must also set [HasLines](PROP_TREE_HASLINES.htm) and [LinesAtRoot](PROP_TREE_LINESATROOT.htm) properties.

This property is a design time only property and can therefore only be set within the KCML forms designer. Changing it or inspecting it will have no effect at runtime.

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
