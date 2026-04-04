Index (generic property)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Index of the currently selected item**

This is a read-only integer property whose value will be the index number of the currently selected item in a listbox, combo listbox or tree. Index numbers are assigned by the control when an entry is added to it. They count from 1. If nothing is selected then the value will be zero.

In a multi-select list box the value of the property will be zero.

##### Example:


     n = .treeControl.Index

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
